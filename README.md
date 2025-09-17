# Thalassa Cloud Resource Provider

The Thalassa Cloud Resource Provider for [Pulumi](https://www.pulumi.com) lets you manage [Thalassa](https://www.thalassa.cloud/) resources.

The provider is built on [the upstream Terraform provider](https://github.com/thalassa-cloud/terraform-provider-thalassa).

## Installing using the SDK (recommended)

This provider can be used either via the language SDKs (**recommended**). When you run `pulumi up`, the Pulumi CLI will automatically download the matching provider plugin
from the [GitHub Releases](https://github.com/sandervb2/pulumi-thalassa/releases) page. or by manually installing the plugin.

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

### Go (not yet available)

```bash
go get github.com/sandervb2/pulumi-thalassa/sdk/go/...
```

### .NET (not yet available)

```bash
dotnet add package Pulumi.Thalassa
```

## Manual Plugin Installation (optional)

If you want to install the plugin manually:

1. Download the appropriate archive version for your OS/arch:

   ```bash
   wget https://github.com/sandervb2/pulumi-thalassa/releases/download/vX.Y.Z/pulumi-resource-thalassa-vX.Y.Z-OPERATING_SYSTEM-ARCH.tar.gz
   ```

2. Install it into Pulumi:

   ```bash
   pulumi plugin install resource thalassa X.Y.Z \
     -f ./pulumi-resource-thalassa-vX.Y.Z-OPERATING_SYSTEM-ARCH.tar.gz
   ```

## Configuration

The provider can be configured via Pulumi config values or via environment variables.

### Using Pulumi Config

```bash
pulumi config set thalassa:organisationId <organisation-id>
pulumi config set thalassa:token <secret-token> --secret
```

Example (*TypeScript*):

```typescript
import * as thalassa from "@sandervb2/pulumi-thalassa";

const vpc = new thalassa.Vpc("example", {
  name: "my-vpc",
});
```
### Using Environment Variables

```typescript
import * as thalassa from "@sandervb2/pulumi-thalassa";

const provider = new thalassa.Provider("custom", {
  organisationId: process.env.THALASSA_ORGANISATION_ID,
  token: process.env.THALASSA_TOKEN,
});

const vpc = new thalassa.Vpc("example", {
  name: "my-vpc",
}, { provider });
```

## Reference

For detailed reference documentation, please visit the upstream Terraform provider's documentation at:
👉 [https://registry.terraform.io/providers](https://registry.terraform.io/providers/thalassa-cloud/thalassa/latest)
