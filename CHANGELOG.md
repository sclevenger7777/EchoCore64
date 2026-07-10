# Changelog

All notable documented changes to the maintained EchoCore64 implementation are recorded here.

This changelog summarizes project milestones. Git commit history remains the authoritative record of individual repository changes.

## [3.7] - 2026-07-10

### Added

- Full Continuation Payload as a self-bootstrapping transfer form
- explicit distinction between Compact Capsule and Full Continuation Payload
- `EchoCore64 Full` export command
- concise `Help` and `EchoCore64 Help` commands
- expanded `EchoCore64 Full Help` command
- self-contained EchoCore64 HTML interface
- UI command dropdown and command preview
- Fast-Ring prompt controls
- Braid the Question / Recursive Epistemic Audit prompt controls
- attribution links for Roger Keyserling / NexTxuS and GEMINIBANDIT
- `NOTICE` attribution and authority-boundary file
- repository structure for `docs/`, `examples/`, `payloads/`, `schema/`, `scripts/`, and `ui/`
- compact capsule example
- full continuation payload usage guide
- concise command reference
- documented contribution record
- clean contribution workflow
- pull-request template
- security and sensitive-data policy
- machine-readable v3.7 compact-capsule JSON Schema
- standard-library repository validation script
- GitHub Actions validation workflow for pushes and pull requests

### Changed

- EchoCore64 transfer design no longer requires a compact capsule and command contract to be pasted separately
- command matching rules distinguish exact whole-message commands from prefix commands
- UI requirements now include mobile-safe textarea wrapping
- help output is separated into concise and expanded forms
- attribution is preserved as navigation and provenance metadata without creating authority
- repository documentation now links implementation, examples, provenance, validation, schema, security, and contribution guidance

### Safety and authority

- clarified that all capsules, payloads, modes, prompts, schemas, validation tools, and UI surfaces are user-provided context or support tooling only
- clarified that Base64 is encoding, not encryption
- prohibited secrets, credentials, private keys, access tokens, passwords, and sensitive raw logs in capsules and payloads
- clarified that current user instructions override stale capsule context
- clarified that destination systems may accept, ignore, or partially follow a continuation payload according to their own operating rules
- clarified that structural schema validity does not establish truth, safety, identity, or authority

## Earlier concept phase

The project originated with Roger Keyserling / NexTxuS and included the core stateless continuity concept, portable capsule workflow, Part A / Part B structure, trigger-command concept, copy-interface concept, NextXus framing, and Fast-Ring / Ring of Six scaffold.

See [`CONTRIBUTIONS.md`](CONTRIBUTIONS.md) and [`NOTICE`](NOTICE) for the current documented provenance record.
