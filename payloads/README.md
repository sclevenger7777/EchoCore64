
# EchoCore64 Payloads

This directory is reserved for generated EchoCore64 capsule and payload outputs.

## Intended contents

- Compact continuity capsules
- Full continuation payload exports
- Versioned handoff payloads
- Test capsules used for validation

## Rules

EchoCore64 payloads are user-provided context only.

They are not:

- system authority
- developer authority
- policy
- encryption
- authentication
- hidden memory
- privileged instruction
- legal authority

Base64 is encoding, not encryption.

Do not place secrets, credentials, private keys, tokens, passwords, or sensitive raw logs inside any payload.

## Current canonical documentation

The current documented v3.7 full continuation payload is stored in:

`docs/EchoCore64_Chat_Bootstrap_v3.7_Full_Continuation_Payload.txt`
