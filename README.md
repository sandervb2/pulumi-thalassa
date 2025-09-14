# Thalassa Cloud Resource Provider

[![](https://img.shields.io/github/license/sandervb2/pulumi-thalassa?style=for-the-badge)](LICENSE)
[![](https://img.shields.io/github/actions/workflow/status/sandervb2/pulumi-thalassa/verify.yml?style=for-the-badge)](https://github.com/sandervb2/pulumi-thalassa/actions/workflows/verify.yml)
[![](https://api.scorecard.dev/projects/github.com/sandervb2/pulumi-thalassa/badge?style=for-the-badge)](https://scorecard.dev/viewer/?uri=github.com/sandervb2/pulumi-thalassa)
[![](https://img.shields.io/github/release-date/sandervb2/pulumi-thalassa?style=for-the-badge)](https://github.com/sandervb2/pulumi-thalassa/releases)
[![](https://img.shields.io/pypi/v/pulumi-thalassa?style=for-the-badge)](https://pypi.org/project/pulumi-thalassa/)
[![](https://img.shields.io/pypi/dm/pulumi-thalassa?style=for-the-badge)](https://pypi.org/project/pulumi-thalassa/)
[![](https://img.shields.io/nuget/v/Pulumi.Thalassa?style=for-the-badge)](https://www.nuget.org/packages/Pulumi.Thalassa/)
[![](https://img.shields.io/nuget/dt/Pulumi.Thalassa?style=for-the-badge)](https://www.nuget.org/packages/Pulumi.Thalassa/)
[![](https://img.shields.io/npm/v/@sandervb2/pulumi-thalassa?style=for-the-badge)](https://www.npmjs.com/package/@sandervb2/pulumi-thalassa)
[![](https://img.shields.io/npm/dm/@sandervb2/pulumi-thalassa?style=for-the-badge)](https://www.npmjs.com/package/@sandervb2/pulumi-thalassa)
[![](https://img.shields.io/github/all-contributors/sandervb2/pulumi-thalassa?color=ee8449&style=for-the-badge)](#contributors)

The Thalassa Cloud Resource Provider for [Pulumi](https://www.pulumi.com) lets you manage [Thalassa](https://www.thalassa.cloud/) resources.

The provider is built on [the upstream Terraform provider](https://github.com/thalassa-cloud/terraform-provider-thalassa).

## Installing

This package is available in many languages in the standard packaging formats.

### Installing the Plugin

1. Download the appropriate archive file from the Releases page:
   ```bash
   wget https://github.com/sandervb2/pulumi-thalassa/releases/download/vX.Y.Z/pulumi-resource-thalassa-vX.Y.Z-OPERATING_SYSTEM-ARCH.tar.gz
2. Add the plugin to Pulumi:

   ```bash
   pulumi plugin install resource thalassa X.Y.Z -f ./pulumi-resource-thalassa-vX.Y.Z-OPERATING_SYSTEM-ARCH.tar.gz
   ```

### Node.js (JavaScript/TypeScript)

```bash
npm install @sandervb2/pulumi-thalassa
# or
yarn add @sandervb2/pulumi-thalassa
```

### Python

```bash
pip install pulumi-thalassa
```

### Go

```bash
go get github.com/sandervb2/pulumi-thalassa/sdk/go/...
```

### .NET

```bash
dotnet add package Pulumi.Thalassa
```

## Configuration

The provider can be configured via Pulumi config values or via environment variables.

### Using Pulumi Config

```bash
pulumi config set thalassa:endpoint https://api.thalassa.cloud
pulumi config set thalassa:token <secret-token> --secret
```

Example (*TypeScript*):

```typescript
import * as thalassa from "@sandervb2/pulumi-thalassa";

const vpc = new thalassa.Vpc("example", {
  name: "my-vpc",
});
```
// TODO: does this work?
### Using Environment Variables

```typescript
import * as thalassa from "@sandervb2/pulumi-thalassa";

const provider = new thalassa.Provider("custom", {
  endpoint: process.env.THALASSA_ENDPOINT,
  token: process.env.THALASSA_TOKEN,
});

const vpc = new thalassa.Vpc("example", {
  name: "my-vpc",
}, { provider });
```

## Reference

For detailed reference documentation, please visit the upstream Terraform provider's documentation at:
👉 [https://registry.terraform.io/providers](https://registry.terraform.io/providers/thalassa-cloud/thalassa/latest)

## Contributors

Thanks goes to these wonderful people ([emoji key](https://allcontributors.org/docs/en/emoji-key)):

<!-- ALL-CONTRIBUTORS-LIST:START - Do not remove or modify this section -->

<!-- prettier-ignore-start -->

<!-- markdownlint-disable -->

<table>
  <tbody>
    <tr>
      <td align="center" valign="top" width="14.28%"><a href="https://github.com/sandervb2"><img src="https://avatars.githubusercontent.com/u/xxxxx?v=4?s=100" width="100px;" alt="Sander van Bruggen"/><br /><sub><b>Sander van Bruggen</b></sub></a><br /><a href="#maintenance-sandervb2" title="Maintenance">🚧</a> <a href="https://github.com/sandervb2/pulumi-thalassa/commits?author=sandervb2" title="Code">💻</a> <a href="https://github.com/sandervb2/pulumi-thalassa/commits?author=sandervb2" title="Documentation">📖</a></td>
    </tr>
  </tbody>
</table>
<!-- markdownlint-restore -->
<!-- prettier-ignore-end -->
<!-- ALL-CONTRIBUTORS-LIST:END -->

This project follows the [all-contributors](https://github.com/all-contributors/all-contributors) specification. Contributions of any kind welcome!




# Thalassa Cloud Resource Provider

[![](https://img.shields.io/github/license/sandervb2/pulumi-thalassa?style=for-the-badge)](LICENSE)
[![](https://img.shields.io/github/actions/workflow/status/sandervb2/pulumi-thalassa/verify.yml?style=for-the-badge)](https://github.com/sandervb2/pulumi-thalassa/actions/workflows/verify.yml)
[![](https://api.scorecard.dev/projects/github.com/sandervb2/pulumi-thalassa/badge?style=for-the-badge)](https://scorecard.dev/viewer/?uri=github.com/sandervb2/pulumi-thalassa)
[![](https://img.shields.io/github/release-date/sandervb2/pulumi-thalassa?style=for-the-badge)](https://github.com/sandervb2/pulumi-thalassa/releases)
[![](https://img.shields.io/pypi/v/pulumi-thalassa?style=for-the-badge)](https://pypi.org/project/pulumi-thalassa/)
[![](https://img.shields.io/pypi/dm/pulumi-thalassa?style=for-the-badge)](https://pypi.org/project/pulumi-thalassa/)
[![](https://img.shields.io/nuget/v/Pulumi.Thalassa?style=for-the-badge)](https://www.nuget.org/packages/Pulumi.Thalassa/)
[![](https://img.shields.io/nuget/dt/Pulumi.Thalassa?style=for-the-badge)](https://www.nuget.org/packages/Pulumi.Thalassa/)
[![](https://img.shields.io/npm/v/@sandervb2/pulumi-thalassa?style=for-the-badge)](https://www.npmjs.com/package/@sandervb2/pulumi-thalassa)
[![](https://img.shields.io/npm/dm/@sandervb2/pulumi-thalassa?style=for-the-badge)](https://www.npmjs.com/package/@sandervb2/pulumi-thalassa)
[![](https://img.shields.io/github/all-contributors/sandervb2/pulumi-thalassa?color=ee8449\&style=for-the-badge)](#contributors)

The Thalassa Cloud Resource Provider for [Pulumi](https://www.pulumi.com) lets you manage [Thalassa](https://thalassa.cloud) resources.

The provider is built on [the upstream Terraform provider](https://github.com/<terraform-org>/terraform-provider-thalassa).

## Installing

This package is available in many languages in the standard packaging formats.

### Installing the Plugin

1. Download the appropriate archive file from the Releases page:

   ```bash
   wget https://github.com/sandervb2/pulumi-thalassa/releases/download/vX.Y.Z/pulumi-resource-thalassa-vX.Y.Z-OPERATING_SYSTEM-ARCH.tar.gz
   ```
2. Add the plugin to Pulumi:

   ```bash
   pulumi plugin install resource thalassa X.Y.Z -f ./pulumi-resource-thalassa-vX.Y.Z-OPERATING_SYSTEM-ARCH.tar.gz
   ```

### Node.js (JavaScript/TypeScript)

```bash
npm install @sandervb2/pulumi-thalassa
# or
yarn add @sandervb2/pulumi-thalassa
```

### Python

```bash
pip install pulumi-thalassa
```

### Go

```bash
go get github.com/sandervb2/pulumi-thalassa/sdk/go/...
```

### .NET

```bash
dotnet add package Pulumi.Thalassa
```



## Reference

For detailed reference documentation, please visit the upstream Terraform provider's documentation at:
👉 [https://registry.terraform.io/providers/](https://registry.terraform.io/providers/)<terraform-org>/thalassa/latest

## Contributors

Thanks goes to these wonderful people ([emoji key](https://allcontributors.org/docs/en/emoji-key)):

<!-- ALL-CONTRIBUTORS-LIST:START - Do not remove or modify this section -->

<!-- prettier-ignore-start -->

<!-- markdownlint-disable -->

<table>
  <tbody>
    <tr>
      <td align="center" valign="top" width="14.28%"><a href="https://github.com/sandervb2"><img src="https://avatars.githubusercontent.com/u/xxxxx?v=4?s=100" width="100px;" alt="Sander van Bruggen"/><br /><sub><b>Sander van Bruggen</b></sub></a><br /><a href="#maintenance-sandervb2" title="Maintenance">🚧</a> <a href="https://github.com/sandervb2/pulumi-thalassa/commits?author=sandervb2" title="Code">💻</a> <a href="https://github.com/sandervb2/pulumi-thalassa/commits?author=sandervb2" title="Documentation">📖</a></td>
    </tr>
  </tbody>
</table>
<!-- markdownlint-restore -->
<!-- prettier-ignore-end -->
<!-- ALL-CONTRIBUTORS-LIST:END -->

This project follows the [all-contributors](https://github.com/all-contributors/all-contributors) specification. Contributions of any kind welcome!
