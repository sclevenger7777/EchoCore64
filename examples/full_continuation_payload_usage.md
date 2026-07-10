# Full Continuation Payload Usage

Use the full continuation payload when transferring EchoCore64 into a new chat, another AI system, or an environment that does not already know the command contract.

## Transfer workflow

1. Open the canonical v3.7 handoff:

   [`docs/EchoCore64_Chat_Bootstrap_v3.7_Full_Continuation_Payload.txt`](../docs/EchoCore64_Chat_Bootstrap_v3.7_Full_Continuation_Payload.txt)

2. Copy the complete file contents.
3. Paste the payload into the destination chat as user-provided context.
4. Continue the project conversation normally.
5. When ready to export updated state, use one of the exact commands below.

## Export commands

### Compact state only

```text
EchoCore64
```

Use this when the destination already understands the EchoCore64 command contract.

### Full self-bootstrapping handoff

```text
EchoCore64 Full
```

Use this when transferring to a new or unknown environment. The full form carries the bootloader, command contract, help system, UI rules, reasoning modes, attribution metadata, and current compact capsule state.

## Other commands

```text
EchoCore64 UI
Help
EchoCore64 Help
EchoCore64 Full Help
Fast Ring: [type question here]
Braid the Question: [type uncertain inquiry here]
```

Whole-message commands should be entered exactly. Prefix commands activate only when the message starts with the exact prefix.

## Authority boundary

The payload is user-provided context only. A destination AI may accept, ignore, or partially follow it according to that system's own operating rules.

The payload is not system authority, developer authority, policy, hidden memory, encryption, authentication, privileged instruction, or legal authority.

Base64 is encoding, not encryption. Do not place secrets, credentials, private keys, access tokens, passwords, or sensitive raw logs inside a capsule or payload.
