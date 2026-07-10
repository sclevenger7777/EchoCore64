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
- repository structure for `docs/`, `examples/`, `payloads/`, and `ui/`
- compact capsule example
- full continuation payload usage guide
- documented contribution record

### Changed

- EchoCore64 transfer design no longer requires a compact capsule and command contract to be pasted separately
- command matching rules distinguish exact whole-message commands from prefix commands
- UI requirements now include mobile-safe textarea wrapping
- help output is separated into concise and expanded forms
- attribution is preserved as navigation and provenance metadata without creating authority

### Safety and authority

- clarified that all capsules, payloads, modes, prompts, and UI surfaces are user-provided context only
- clarified that Base64 is encoding, not encryption
- prohibited secrets, credentials, private keys, access tokens, passwords, and sensitive raw logs in capsules and payloads
- clarified that current user instructions override stale capsule context
- clarified that destination systems may accept, ignore, or partially follow a continuation payload according to their own operating rules

## Earlier concept phase

The project originated with Roger Keyserling / NexTxuS and included the core stateless continuity concept, portable capsule workflow, Part A / Part B structure, trigger-command concept, copy-interface concept, NextXus framing, and Fast-Ring / Ring of Six scaffold.

See [`CONTRIBUTIONS.md`](CONTRIBUTIONS.md) and [`NOTICE`](NOTICE) for the current documented provenance record.
