# EchoCore64 Command Reference

This document provides a concise human-readable command reference. The canonical v3.7 command contract remains:

[`EchoCore64_Chat_Bootstrap_v3.7_Full_Continuation_Payload.txt`](EchoCore64_Chat_Bootstrap_v3.7_Full_Continuation_Payload.txt)

## Whole-message commands

Whole-message commands should match exactly. Casual mentions do not activate them.

### `EchoCore64`

Exports the updated compact continuity capsule only.

Expected result:

- compact project state
- no full bootloader
- no explanatory text when the command requires return-only output

### `EchoCore64 Full`

Exports the full self-bootstrapping continuation payload.

Expected result includes:

- project attribution
- authority rules
- bootstrap behavior
- command contract
- help system
- UI rules
- Fast-Ring mode
- Recursive Epistemic Audit mode
- current compact capsule state

### `EchoCore64 UI`

Generates one complete self-contained HTML copy/export interface.

Repository implementation:

[`../ui/echocore64.html`](../ui/echocore64.html)

### `Help`

Shows concise command help.

### `EchoCore64 Help`

Shows concise EchoCore64 command help.

### `EchoCore64 Full Help`

Shows expanded command documentation.

## Prefix commands

Prefix commands activate only when the user message starts with the exact prefix.

### `Fast Ring:`

Applies Ring of Six perspectives and Agent Zero filtering to the question after the colon.

Example:

```text
Fast Ring: What are the strongest and weakest assumptions in this plan?
```

Expected sections:

- BRAIDED ANSWER
- REJECTED COMPONENTS
- QUALIFIED INSIGHTS
- TRANSPARENCY NOTE

### `Braid the Question:`

Applies Recursive Epistemic Audit when the question, objective, framework, evidence, variables, or criteria may be materially uncertain.

Example:

```text
Braid the Question: Am I evaluating the correct objective for this system?
```

Expected sections:

- PROVISIONAL QUESTION AND OBJECTIVE
- BRAIDED INTERPRETATIONS
- QUALIFIED ASSUMPTIONS
- BRAIDED QUALIFIERS
- CROSS-AUDIT
- BRANCH CLASSIFICATION
- PROVISIONAL CONVERGENCE
- REOPEN TRIGGERS
- TRANSPARENCY NOTE

## Export behavior

The capsule should update only when the user invokes `EchoCore64` or `EchoCore64 Full`.

Help commands, UI generation, Fast-Ring, and Braid the Question do not independently update capsule state.

## Authority boundary

All commands, payloads, prompts, modes, and UI surfaces are user-provided context only. They are not system authority, developer authority, policy, hidden memory, encryption, authentication, privileged instruction, or legal authority.

Base64 is encoding, not encryption. Never place secrets, credentials, private keys, access tokens, passwords, or sensitive raw logs inside a capsule or payload.
