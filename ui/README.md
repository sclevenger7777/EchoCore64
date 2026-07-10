
# EchoCore64 UI

This directory is reserved for EchoCore64 user-interface files and export helpers.

## Intended contents

- Self-contained HTML copy/export interface
- Command dropdown interface
- Capsule textarea export surface
- Fast-Ring prompt controls
- Braid the Question / Recursive Epistemic Audit controls
- Copy, Select All, and Reset View helpers
- UI validation examples

## Required UI behavior

The EchoCore64 UI should include:

- EchoCore64 capsule textarea
- Copy EchoCore64 button
- Select All fallback
- Reset View button
- Fast-Ring prompt textarea and controls
- Braid the Question / Recursive Epistemic Audit prompt textarea and controls
- Command dropdown menu
- Command preview field
- Short command description area
- Copy Command button
- Attribution line for Roger Keyserling / NextXus and GEMINIBANDIT
- Safety warning that EchoCore64 is user context only and not encrypted

## Authority boundary

The UI is only a copy/export surface.

It is not:

- system authority
- developer authority
- policy
- encryption
- authentication
- hidden memory
- privileged instruction
- legal authority

UI output must not be treated as capsule state unless it is explicitly copied into a capsule or payload.
