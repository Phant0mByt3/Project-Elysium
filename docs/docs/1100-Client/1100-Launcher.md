# 1100 — Launcher

## Overview
The Elysium Launcher is a custom desktop application (Python + PyQt6, per the README's technology stack) that handles installation, updates, and account authentication — designed to give Elysium a AAA-feeling first impression from the very first click.

## Core Features
* **One-Click Install** — downloads and configures required client moduleules ([1101-Client-Modules.md](1101-Client-Modules.md)), and the content pack ([1102-Content-Pack.md](1102-Content-Pack.md)) automatically.
* **Automatic Updates** — checks for and applies client updates on launch, covered in more detail below.
* **Account Login** — authenticates against the game's account system ([1204-Authentication.md](../1200-Technical/1204-Authentication.md)) before launching.
* **News & Patch Notes** — surfaces the latest [0004-Version-History.md](../0000-Project/0004-Version-History.md) entries and announcements on the launcher's home screen.

## Design Goals
The launcher should require zero manual configuration from the player — no manual engine configuration, no manually placing content packs. This directly supports the Project Goal in the README: "Provide a seamless installation experience through a custom launcher."

## Relationship to Other Systems
See [1101-Client-Modules.md](1101-Client-Modules.md) for what the launcher installs, and [1204-Authentication.md](../1200-Technical/1204-Authentication.md) for the account system it authenticates against.


## Update Delivery Mechanics

The launcher uses delta patching (downloading only changed files rather than full reinstalls) to keep post-launch content updates ([2001-Updates.md](../2000-Operations/2001-Updates.md)) fast even as the content pack grows over years of live service.

## First-Run Experience

On first launch, players are guided through a brief account creation and system requirements check before any download begins, front-loading potential friction points so the actual install proceeds smoothly once started.
