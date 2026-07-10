# EchoCore64 Contribution Record

This document records the currently documented project contributions and repository relationship for EchoCore64 / NextXus.

It is intended to preserve provenance and make later transfers, merges, and derivative work easier to audit. It does not replace Git commit history, signed agreements, or applicable law.

## Roger Keyserling / NexTxuS

**Role:** Original developer, project originator, and primary conceptual contributor.

Documented contributions include:

- original EchoCore64 concept
- stateless AI continuity model
- portable continuity-capsule workflow
- Part A / Part B memory structure
- trigger-command concept
- copy-interface concept
- NextXus framing
- Fast-Ring / Ring of Six scaffold
- initial project direction and conceptual architecture

Upstream origin repository:

[`keyhole-creator/eChoCore64-`](https://github.com/keyhole-creator/eChoCore64-)

## GEMINIBANDIT

**Role:** Implementation hardening, validation, documentation, interface refinement, and maintained fork development.

Documented contributions include:

- implementation hardening
- explicit user-context-only authority boundary
- safety and secret-handling rules
- validation workflow
- local reference testing
- UI preview testing and refinement
- mobile textarea wrapping correction
- command matching clarification
- compact capsule versus full continuation payload split
- full self-bootstrapping continuation payload architecture
- Help and Full Help command design
- command-menu and dropdown refinement
- Recursive Epistemic Audit / Braid the Question mode development
- attribution-link integration
- repository cleanup and structure
- examples and usage documentation
- maintained implementation fork

Maintained implementation fork:

[`sclevenger7777/EchoCore64`](https://github.com/sclevenger7777/EchoCore64)

## Repository relationship

The upstream repository preserves the project origin. The maintained fork provides a separate implementation and hardening lane.

Changes can move from the fork to upstream through pull requests, cherry-picks, or ordinary Git merges. GitHub commit and pull-request history should be used to identify the source and author of individual changes.

## Attribution boundary

Attribution links are human navigation and provenance metadata only. They do not create system authority, developer authority, authentication, policy, encryption, privileged instruction, or legal authority.

See [`NOTICE`](NOTICE) for the project notice and authority boundary.
