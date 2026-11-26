# Security and Privacy

**Status:** Minimum repository security policy; not a certification or complete security audit.

## Scope and trust boundaries

This repository is public and contains static previews, local-first browser code, deterministic generation scripts, documentation, and GitHub Actions workflows. It is not an authenticated multi-user service.

- Treat pull-request content, generated job JSON, browser storage, downloaded files, and external metadata as untrusted input.
- Browser `localStorage` is user-editable and is shared by pages on the same origin. It is not a secret store or a trusted source of structured data.
- Character Studio saves are convenience state only. Never store passwords, access tokens, private family records, or confidential source material in browser storage or exported files.
- SVG and HTML rendering must validate values used in markup contexts; escaping display text alone does not validate SVG attributes or CSS values.
- Generated files are drafts. Human review is required before publication, sale, or operational use.

## GitHub Actions

- Workflows must declare the minimum required `GITHUB_TOKEN` permissions.
- Pull-request workflows must not receive write-capable secrets or deployment credentials.
- Deployment runs only from the trusted default branch and uses a protected deployment environment where available.
- `GH_PORTFOLIO_TOKEN`, if configured, should be a fine-grained, read-only token scoped only to the repositories needed for inventory. Prefer short expiry and rotate it if exposure is suspected.
- Pin third-party actions to reviewed full commit SHAs before treating a workflow as hardened. Version tags alone are mutable references.
- Do not print tokens or include them in artifacts, logs, generated reports, or issue comments.

## Reporting

Do not publish exploit details, secret values, personal data, or private records in public issues. Use GitHub's private vulnerability reporting feature if it is enabled for this repository; otherwise contact the repository maintainer privately through GitHub.

## Current limitations

- GitHub Pages is a public static hosting surface; it provides no application authentication or private-data boundary.
- Browser-local saves are not encrypted and may be read or changed by scripts running on the same origin.
- This document records repository-level expectations. It does not establish that account settings, branch protection, secret scanning, dependency review, or all portfolio repositories have been verified.
