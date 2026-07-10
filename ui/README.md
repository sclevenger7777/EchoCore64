# EchoCore64 UI

This directory contains the self-contained EchoCore64 browser interface and its implementation notes.

## Current interface

[`echocore64.html`](echocore64.html)

The HTML file is self-contained and has no external runtime dependencies. Download the raw file and open it in a modern browser.

## Included functions

- EchoCore64 capsule staging textarea
- Copy EchoCore64 button
- Select All fallback
- Reset View button
- Fast-Ring prompt textarea and controls
- Braid the Question / Recursive Epistemic Audit prompt textarea and controls
- Command dropdown menu
- Command preview field
- Short description for each selected command
- Copy Command button
- Insert Template button
- Clickable project attribution
- User-context-only and Base64 safety warnings

## Command menu

The dropdown includes:

- `EchoCore64`
- `EchoCore64 Full`
- `EchoCore64 UI`
- `Fast Ring:`
- `Braid the Question:`
- `Help`
- `EchoCore64 Help`
- `EchoCore64 Full Help`

## Running locally

1. Download [`echocore64.html`](echocore64.html).
2. Open the file with a browser.
3. Paste or edit capsule content in the capsule textarea.
4. Use the command menu or reasoning-mode prompt fields.
5. Use **Copy** where clipboard access is available, or **Select All** as a fallback.

The reusable source is the HTML file itself. A rendered preview is not a substitute for the source document.

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

UI content does not become capsule state unless the user explicitly copies or incorporates it into a capsule or continuation payload.

Base64 is encoding, not encryption. Do not place secrets, credentials, private keys, access tokens, passwords, or sensitive raw logs inside the UI fields.
