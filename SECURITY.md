# Security Policy

## Reporting a vulnerability

Please do not publish exploitable vulnerability details, credentials, access tokens, or private data in a public issue.

Report security concerns privately through GitHub's repository security reporting feature if it is enabled for this repository. If private reporting is unavailable, contact the repository owner through a trusted private channel and provide only the minimum details needed to investigate.

Include the affected file or component, impact, reproduction steps, and any suggested mitigation. Do not include live credentials or personal data.

## Credential handling

- Never commit passwords, API keys, access tokens, private keys, or production credentials.
- Store required CI credentials in GitHub Actions secrets or an appropriate secret manager.
- Revoke and rotate any credential suspected of exposure; deleting it from a file or commit is not sufficient.
- Use least-privilege permissions for tokens, workflows, and integrations.

## Changes and releases

Security-sensitive changes should be proposed through pull requests and reviewed before merge where repository settings permit. Automated checks are defense in depth and do not replace human review or operational backups.
