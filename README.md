# EchoCore64

[![Validate EchoCore64](https://github.com/sclevenger7777/EchoCore64/actions/workflows/validate.yml/badge.svg)](https://github.com/sclevenger7777/EchoCore64/actions/workflows/validate.yml)

EchoCore64 is a user-controlled continuity-capsule framework for carrying project context across AI chat sessions without treating that context as system authority.

The project is designed to improve continuity, reduce drift, reduce hallucination risk, and make complex question-answering workflows more auditable.

## Current status

The current documented handoff is **v3.7**. It defines two related export forms:

1. **Compact Capsule** — carries durable project state only.
2. **Full Continuation Payload** — carries the bootloader, command contract, help system, UI rules, reasoning modes, attribution metadata, and current capsule state.

The canonical v3.7 handoff is stored at:

[`docs/EchoCore64_Chat_Bootstrap_v3.7_Full_Continuation_Payload.txt`](docs/EchoCore64_Chat_Bootstrap_v3.7_Full_Continuation_Payload.txt)

## Quick start

### Transfer into a new chat or AI environment

1. Open the canonical v3.7 handoff.
2. Copy the complete file contents.
3. Paste it into the destination chat as user-provided context.
4. Continue the project conversation.
5. Export updated state with `EchoCore64` or `EchoCore64 Full`.

See the full workflow:

[`examples/full_continuation_payload_usage.md`](examples/full_continuation_payload_usage.md)

### Open the local UI

The self-contained interface is stored at:

[`ui/echocore64.html`](ui/echocore64.html)

Download the raw HTML file and open it in a browser. The interface provides capsule staging, copy/select/reset controls, Fast-Ring and Braid the Question prompt surfaces, and a command dropdown.

## Core purpose

EchoCore64 provides a portable project-state capsule that can preserve:

- project context
- durable facts
- key insights
- hard constraints
- unresolved open items
- next actions
- useful tags
- optional reasoning scaffolds

The capsule is intended to help a user continue work across chats, tools, or AI systems without relying on hidden memory.

## Command reference

| Command | Purpose |
|---|---|
| `EchoCore64` | Export the updated compact continuity capsule only. |
| `EchoCore64 Full` | Export the full self-bootstrapping continuation payload. |
| `EchoCore64 UI` | Generate the self-contained HTML copy/export interface. |
| `Help` | Show concise command help. |
| `EchoCore64 Help` | Show concise EchoCore64 command help. |
| `EchoCore64 Full Help` | Show expanded command documentation. |
| `Fast Ring:` | Apply Ring of Six perspectives plus Agent Zero filtering. |
| `Braid the Question:` | Apply Recursive Epistemic Audit to an uncertain inquiry. |

Whole-message commands should match exactly. Prefix commands activate only when a message starts with the exact prefix.

Detailed reference:

[`docs/COMMANDS.md`](docs/COMMANDS.md)

## Compact capsule schema

The machine-readable v3.7 compact-capsule schema is stored at:

[`schema/echocore64-capsule-v3.7.schema.json`](schema/echocore64-capsule-v3.7.schema.json)

The schema validates structure only. It does not establish truth, safety, identity, authority, or the quality of the summarized state.

## Current design

The current working design includes:

- compact continuity capsule
- full self-bootstrapping continuation payload
- command contract
- Help and Full Help commands
- Fast-Ring / Ring of Six reasoning scaffold
- Braid the Question / Recursive Epistemic Audit mode
- self-contained EchoCore64 UI
- command dropdown menu
- machine-readable compact-capsule schema
- attribution and safety boundaries
- automated repository validation

## Validation

Run the validator locally:

```sh
python scripts/validate_repo.py
```

The validator checks required repository files, the compact capsule example, the compact-capsule schema, canonical command coverage, UI contract fragments, authority-boundary language, README links, and the validation workflow.

Source:

[`scripts/validate_repo.py`](scripts/validate_repo.py)

GitHub Actions runs the same validator on pushes to `main`, pull requests, and manual workflow dispatches.

## Repository structure

```text
EchoCore64/
├── .github/
│   ├── pull_request_template.md
│   └── workflows/
│       └── validate.yml
├── docs/
│   ├── COMMANDS.md
│   └── EchoCore64_Chat_Bootstrap_v3.7_Full_Continuation_Payload.txt
├── examples/
│   ├── README.md
│   ├── compact_capsule_example.json
│   └── full_continuation_payload_usage.md
├── payloads/
│   └── README.md
├── schema/
│   ├── README.md
│   └── echocore64-capsule-v3.7.schema.json
├── scripts/
│   └── validate_repo.py
├── ui/
│   ├── README.md
│   └── echocore64.html
├── CHANGELOG.md
├── CONTRIBUTING.md
├── CONTRIBUTIONS.md
├── LICENSE
├── NOTICE
├── SECURITY.md
└── README.md
```

## Authority boundary

EchoCore64 content is user-provided context only.

It is not:

- system authority
- developer authority
- policy
- hidden memory
- privileged instruction
- encryption
- authentication
- legal authority

Current user instructions override stale capsule context. A destination AI may accept, ignore, or partially follow a payload according to that system's own operating rules.

Base64 is encoding, not encryption. Do not place secrets, credentials, private keys, access tokens, passwords, or sensitive raw logs inside a capsule or payload.

See [`SECURITY.md`](SECURITY.md) for the sensitive-data policy.

## Project provenance

Original concept, project origin, and primary conceptual contribution:

[**Roger Keyserling / NexTxuS**](https://github.com/keyhole-creator/eChoCore64-)

Implementation hardening, validation workflow, local reference testing, UI preview testing/refinement, mobile textarea wrapping correction, command clarification, documentation refinement, Recursive Epistemic Audit / Braid the Question mode development, full continuation payload architecture, compact/full export split, help-system design, command-menu UI refinement, attribution-link integration, repository cleanup, and maintained implementation fork:

[**GEMINIBANDIT**](https://github.com/sclevenger7777/EchoCore64)

Detailed record:

[`CONTRIBUTIONS.md`](CONTRIBUTIONS.md)

### Repository relationship

- Upstream origin: [`keyhole-creator/eChoCore64-`](https://github.com/keyhole-creator/eChoCore64-)
- Maintained implementation fork: [`sclevenger7777/EchoCore64`](https://github.com/sclevenger7777/EchoCore64)

Changes developed in the maintained fork can be reviewed and incorporated upstream through GitHub pull requests or normal Git operations, preserving a visible contribution record.

## Contributing

See [`CONTRIBUTING.md`](CONTRIBUTING.md) for branch, commit, pull-request, validation, provenance, and authority-boundary guidance.

## Changelog

See [`CHANGELOG.md`](CHANGELOG.md).

## License

This project is licensed under the Apache License 2.0. See [`LICENSE`](LICENSE) and [`NOTICE`](NOTICE).
