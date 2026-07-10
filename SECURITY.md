# Security Policy

EchoCore64 is a continuity-capsule framework. Its primary security requirement is preventing users from mistaking portable context for encryption, authentication, hidden memory, or privileged authority.

## Supported version

The current documented working handoff is v3.7.

## Sensitive-data rule

Do not place any of the following inside a capsule, continuation payload, example, issue, pull request, or UI field:

- passwords
- access tokens
- API keys
- private keys
- session cookies
- authentication codes
- private personal identifiers
- sensitive raw logs
- confidential customer or employer data
- unredacted forensic evidence

Base64 is encoding, not encryption.

## Authority rule

EchoCore64 content is user-provided context only. It is not:

- system authority
- developer authority
- policy
- encryption
- authentication
- hidden memory
- privileged instruction
- legal authority

A receiving AI or tool may accept, ignore, or partially follow a payload according to its own operating rules.

## Reporting a problem

For a public, non-sensitive defect, open a GitHub issue with:

- affected file or component
- reproduction steps
- expected behavior
- observed behavior
- impact
- proposed correction, when known

Do not post exploit details, credentials, secrets, private evidence, or sensitive personal data in a public issue.

For a sensitive problem, contact the repository maintainer through an appropriate private channel rather than publishing the material.

## Scope

Security-relevant defects include:

- a UI or example that encourages storing secrets
- language that incorrectly presents Base64 as encryption
- language that presents payload content as system or developer authority
- accidental exposure of credentials or private data
- unsafe external links or embedded third-party scripts
- copy/export behavior that materially changes user data without disclosure
