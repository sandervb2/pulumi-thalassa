# CLAUDE.md

Guidance for AI agents working in this repository.

## What this repo is

`pulumi-thalassa` is a **bridged Pulumi provider**. It is not hand-written: it
wraps the upstream Terraform provider
[`thalassa-cloud/terraform-provider-thalassa`](https://github.com/thalassa-cloud/terraform-provider-thalassa)
via the [`pulumi-terraform-bridge`](https://github.com/pulumi/pulumi-terraform-bridge)
(v3, SDKv2 shim) and emits multi-language SDKs (Python, Node.js, Go, .NET).

The upstream provider is a **go.mod dependency** in `provider/go.mod` — *not* a
git submodule. There is no `patches/` directory and no `.gitmodules`. Updating
the provider's feature set = bumping that dependency and regenerating.

## The single most important rule: never hand-edit generated files

Most of this repo is generated. Editing generated output is the #1 way to break
a bridged provider. **Treat these as read-only** — change the source, then
regenerate:

| Generated (do NOT edit by hand)                     | Source of truth                          | Regenerate with        |
| --------------------------------------------------- | ---------------------------------------- | ---------------------- |
| `sdk/**` (python, nodejs, go, dotnet)               | upstream schema + `provider/resources.go`| `make generate`        |
| `provider/cmd/pulumi-resource-thalassa/schema.json` | upstream schema + `provider/resources.go`| `make tfgen` (`schema`)|
| `provider/cmd/.../bridge-metadata.json`             | upstream schema + `provider/resources.go`| `make tfgen`           |
| `Makefile`, `mise.toml`, `.golangci.yml`             | `.ci-mgmt.yaml`                          | `make ci-mgmt`         |

**Human-editable surface is small** — in practice only:
- `provider/resources.go` — bridge config, token/naming overrides, doc edits
- `provider/go.mod` — the upstream version pin
- `.ci-mgmt.yaml` — Makefile/tooling config (then `make ci-mgmt`)
- `.github/workflows/**`, `renovate.json` — hand-written CI (not ci-mgmt)
- `examples/`, `README.md`, `CHANGELOG.md`

If you think you need to edit anything else, you're probably solving it in the
wrong place. Stop and reconsider.

## Primary task: sync with new upstream Thalassa features

Thalassa ships features in the Terraform provider first. Pulling them in is a
**version bump + regenerate**, not new code. Token mapping is fully automatic
(`MustComputeTokens(tokens.SingleModule("thalassa_", "index", tokens.MakeStandard("thalassa")))`),
so new upstream resources/datasources map into Pulumi automatically.

### Preferred path: Pulumi's `upgrade-provider` tool

This is how Pulumi maintains bridged providers. It bumps the upstream provider,
the bridge, and the matching `pulumi/pulumi` version, then regenerates SDKs.

```bash
go install github.com/pulumi/upgrade-provider@latest
# Target the latest upstream release:
upgrade-provider sandervb2/pulumi-thalassa --kind=all --upstream-provider-name=terraform-provider-thalassa
# Or pin a specific upstream version:
upgrade-provider sandervb2/pulumi-thalassa --kind=all --target-version=<x.y.z> --upstream-provider-name=terraform-provider-thalassa
```

Note: `upgrade-provider` only manages Pulumi-related dependencies (bridge,
pulumi/pulumi, plugin-sdk fork, java-gen). It does **not** bump unrelated
libraries — leave those to Renovate. **Major** upstream bumps (e.g. a `vN`
module-path change) are not handled automatically and need manual steps.

### Manual path (if the tool can't run or you want fine control)

```bash
cd provider
go get github.com/thalassa-cloud/terraform-provider-thalassa@<version>   # e.g. @v0.22.0
go mod tidy
cd ..
make tfgen        # regenerate schema.json + bridge-metadata.json
make build        # regenerate + build all SDKs and the provider plugin
```

Do **not** manually bump `github.com/pulumi/pulumi/pkg/v3` or `.../sdk/v3` in
`provider/go.mod`. The bridge pulls the version it needs; let it. Forcing a
newer `pkg`/`sdk` than the bridge was built against breaks compilation of the
bridge's transitive deps (e.g. `pulumi-hcl`). Renovate is configured not to
bump them in `provider/` for this reason. If you bump the bridge, keep the
`replace` directive for `terraform-plugin-sdk/v2` in sync with the bridge's own
`go.mod` (the fork is intentionally unreleased and must match).

### Renovate and automatic regeneration

Renovate bumps `provider/go.mod` (upstream provider, bridge) but cannot run
`make`. Two pieces keep those PRs correct:

- **`Verify` fails on stale generated files.** After `make tfgen` and
  `make generate_<lang>`, it fails if `provider/cmd/pulumi-resource-thalassa/`
  or `sdk/<lang>/` differ from what's committed. Fix by regenerating and
  committing — never by editing the generated files.
- **`Regenerate` workflow** (`.github/workflows/regenerate.yml`) runs on
  Renovate PRs that touch `provider/go.mod`/`go.sum`, runs `make tfgen` +
  `make generate_sdks`, and pushes a `chore(deps): regenerate schema and sdks`
  commit as the `pulumi-thalassa-regen[bot]` GitHub App. Renovate ignores that
  author (`gitIgnoredAuthors`), so it keeps rebasing the PR.

  It pushes with a GitHub App token because pushes made with `GITHUB_TOKEN`
  don't trigger new workflow runs, so `Verify` would never report on the
  regenerated commit. Setup:
  - GitHub App named **`pulumi-thalassa-regen`** (the name must match
    `renovate.json`), Repository permissions → **Contents: Read and write**,
    no webhook, installed on this repository only.
  - Repository **variable** `REGEN_APP_CLIENT_ID` = the App's Client ID.
  - Repository **secret** `REGEN_APP_PRIVATE_KEY` = the App's private key.

### After any sync — always

1. **Review the schema diff.** `git diff provider/cmd/pulumi-resource-thalassa/schema.json`
   is the source of truth for what changed. Confirm new resources appear, check
   for unexpected removals (a removed resource is a breaking change), and watch
   for type/required changes on existing fields.
2. **Sanity-check tokens.** New upstream resources should produce sensible
   Pulumi names. If `thalassa_some_thing` maps to an awkward token, add an
   explicit override in `provider/resources.go` (see below) — don't edit the
   generated SDK.
3. **Build all SDKs:** `make build` must pass.
4. **Run tests:** `make test_provider`, then `make test` (examples; requires a
   prior `make build`).
5. **Lint:** `make lint_provider` (or `make lint_provider.fix`).
6. **Update examples** in `examples/basic-ts` and `examples/basic-py` if you're
   showcasing a notable new resource.

## Token / naming overrides

Only needed when the automatic mapping produces a poor name or you want a
nicer module layout. Add targeted overrides in `provider/resources.go`, e.g.:

```go
Resources: map[string]*tfbridge.ResourceInfo{
    "thalassa_some_resource": {Tok: tfbridge.MakeResource(mainPkg, mainMod, "NicerName")},
},
```

Keep overrides minimal and intentional — every manual override is something a
future you has to maintain across regenerations. Prefer the automatic mapping.

## Build & tooling

- Tool versions are pinned in `mise.toml` (Go, Node, Python, .NET, pulumi,
  pulumictl). Run `mise install` first. Do not edit `mise.toml` by hand — it's
  generated from `.ci-mgmt.yaml`. Note: its Go pin (1.21) is older than what
  `provider/go.mod` requires; CI uses Go 1.27.x, so build with that.
  If `GOROOT` is set by mise to the old Go, override it.
- `make help` lists targets. Common ones: `build`, `generate`, `tfgen`/`schema`,
  `test_provider`, `test`, `lint_provider`, `clean`, `ci-mgmt`.
- Makefile/tooling config: edit `.ci-mgmt.yaml`, then `make ci-mgmt`. Commit
  the regenerated output together. GitHub workflows under `.github/workflows/`
  are hand-written and edited directly. `make ci-mgmt` runs ci-mgmt's
  generator, which may (re)write files under `.github/` — review its diff and
  discard anything that clobbers the hand-written workflows.

## Contribution conventions (enforced — match them)

**Conventional Commits**, enforced by `.conform.yaml` (the `Conform` job in
`verify.yml`, a required check on `main`). Every commit in a PR is checked:
- Format: `type(scope): description` — scope is optional.
- Allowed types: `fix`, `refactor`, `perf`, `chore`, `test`, `docs`, `no_type`.
  (`feat` is **not** in the configured list — for upstream feature syncs use
  `chore(deps):` or `fix:` as appropriate, matching existing history.)
- Allowed scopes: `release`, `deps`, `ci`. Any other scope fails.
- Header ≤200 chars; description ≤100 chars; no trailing `.`.
- Description must be **lowercase and start with a lowercase letter** — a
  leading digit or capital fails the case check (`chore(release): 0.5.0` fails,
  `chore(release): release 0.5.0` passes).
- Description must start with a verb in **imperative mood** (`add`, `fix`,
  `upgrade` — not `added`, `fixes`, `upgrading`).
- Spellchecked against US English (`color`, not `colour`).
- Body is optional; no DCO sign-off or GPG signature required.
- Examples: `chore(deps): upgrade upstream provider to v0.22.0`,
  `fix(ci): correct release workflow`, `docs: document new loadbalancer fields`.

**Releases** are automated via release-please (`CHANGELOG.md` is generated from
commit history — don't edit it manually). Versioning is currently pre-1.0; the
module path has no `/vN` suffix, so avoid changes that would force a major
version unless that's the explicit goal.

**One logical change per PR.** A dependency bump + regenerated SDKs is one
coherent PR. Don't mix an upstream sync with unrelated refactors.

## Definition of done for a sync PR

- [ ] `provider/go.mod` points at the intended upstream version; `go mod tidy` clean
- [ ] `schema.json` diff reviewed; new resources present, no surprise removals
- [ ] `make build` passes (all four SDKs regenerated and committed)
- [ ] `make test_provider` and `make test` pass
- [ ] `make lint_provider` clean
- [ ] No hand-edits to generated files
- [ ] Commit messages follow `.conform.yaml`
- [ ] Examples/README updated if a notable resource was added

## Quick reference

- Upstream provider: `github.com/thalassa-cloud/terraform-provider-thalassa` (in `provider/go.mod`)
- Bridge config: `provider/resources.go`
- Package name / module: `thalassa` / `index`
- Auth: `thalassa:organisationId`, `thalassa:token` (or `THALASSA_ORGANISATION_ID` / `THALASSA_TOKEN`)
- Upstream docs: https://registry.terraform.io/providers/thalassa-cloud/thalassa/latest
