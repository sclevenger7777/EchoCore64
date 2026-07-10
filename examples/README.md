# EchoCore64 Examples

This directory contains safe, non-secret examples showing how EchoCore64 capsules and continuation payloads are structured and used.

## Included examples

- [`compact_capsule_example.json`](compact_capsule_example.json) — minimal compact capsule with durable project state
- [`full_continuation_payload_usage.md`](full_continuation_payload_usage.md) — practical transfer workflow for a new chat or AI environment

## Safety rules

Examples are user-provided context only. They are not system authority, developer authority, policy, hidden memory, encryption, authentication, privileged instruction, or legal authority.

Base64 is encoding, not encryption. Never place secrets, credentials, private keys, access tokens, passwords, or sensitive raw logs inside a capsule or payload.

## Canonical v3.7 specification

The complete documented handoff is stored at:

[`docs/EchoCore64_Chat_Bootstrap_v3.7_Full_Continuation_Payload.txt`](../docs/EchoCore64_Chat_Bootstrap_v3.7_Full_Continuation_Payload.txt)
