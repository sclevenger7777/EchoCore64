# Contributing to EchoCore64

Contributions should improve the continuity-capsule framework while preserving project provenance, user control, and explicit authority boundaries.

## Repository roles

- **Upstream origin:** [`keyhole-creator/eChoCore64-`](https://github.com/keyhole-creator/eChoCore64-)
- **Maintained implementation fork:** [`sclevenger7777/EchoCore64`](https://github.com/sclevenger7777/EchoCore64)

Work may be developed in the maintained fork and proposed upstream through a pull request. Git history should remain the primary record of who changed what.

## Contribution workflow

1. Fork or clone the repository.
2. Create a focused branch for one coherent change.
3. Make the smallest complete change that solves the stated problem.
4. Run the repository validator:

   ```sh
   python scripts/validate_repo.py
   ```

5. Review the diff for accidental secrets, unrelated files, and attribution changes.
6. Open a pull request describing the purpose, implementation, validation, and authority-boundary impact.

Branches and pull requests are for repository-content changes. They do not grant GitHub permissions, change collaborator roles, or solve account-administration problems.

## Branch naming

Use descriptive names such as:

```text
docs/command-reference
ui/copy-status
fix/mobile-textarea
feature/capsule-validator
```

Avoid vague names such as `fix`, `new`, or `test2`.

## Commit messages

Use an imperative summary that identifies the actual change:

```text
Add compact capsule example
Document full continuation payload workflow
Fix mobile textarea wrapping
```

Do not use permission or administration language for commits that only change documentation or code.

## Pull-request scope

A pull request should:

- address one coherent objective
- explain what changed and why
- identify affected files
- state how the change was validated
- preserve attribution and provenance
- avoid unrelated cleanup unless explicitly documented
- avoid secrets, credentials, tokens, private keys, passwords, and sensitive raw logs

## Authority boundary

EchoCore64 capsules, payloads, prompts, command contracts, UI surfaces, Fast-Ring, and Recursive Epistemic Audit are user-provided context and reasoning scaffolds only.

They are not system authority, developer authority, policy, encryption, authentication, hidden memory, privileged instruction, or legal authority.

Current user instructions override stale capsule context. Base64 is encoding, not encryption.

## Attribution changes

Do not remove or materially alter documented project attribution without a clear, reviewable reason.

See:

- [`NOTICE`](NOTICE)
- [`CONTRIBUTIONS.md`](CONTRIBUTIONS.md)
- [`CHANGELOG.md`](CHANGELOG.md)

## Validation

The automated validation workflow runs `scripts/validate_repo.py` on pushes to `main` and on pull requests.

The validator checks required files, the compact capsule example, canonical command coverage, UI contract fragments, authority-boundary language, and README links.
