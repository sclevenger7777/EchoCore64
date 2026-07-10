# EchoCore64 Schema

This directory contains machine-readable structure definitions for EchoCore64 capsule formats.

## Current schema

[`echocore64-capsule-v3.7.schema.json`](echocore64-capsule-v3.7.schema.json)

The v3.7 schema describes the compact capsule structure, including:

- fixed EchoCore64 type marker
- v3.7 version marker
- user-context-only authority marker
- project and founding metadata
- attribution metadata
- Fast-Ring and Recursive Epistemic Audit mode references
- durable session-state arrays

## Scope

The schema validates structure, not truth, safety, identity, authority, or the quality of the summarized project state.

A structurally valid capsule may still contain stale, incomplete, incorrect, unsafe, or irrelevant content. Current user instructions and the receiving system's actual operating rules remain controlling.

Base64 is encoding, not encryption. Do not place secrets, credentials, private keys, access tokens, passwords, or sensitive raw logs inside a capsule.

## Example

See:

[`examples/compact_capsule_example.json`](../examples/compact_capsule_example.json)
