# 1100 — Launcher

## Overview
The Elysium Launcher is a custom desktop application (Python + PyQt6, per the README's technology stack) that handles installation, updates, and account authentication — designed to give Elysium a AAA-feeling first impression before the player even opens Minecraft.

## Core Features
* **One-Click Install** — downloads and configures Fabric, required client mods ([1101-Client-Mods.md](1101-Client-Mods.md)), and the resource pack ([1102-Resource-Pack.md](1102-Resource-Pack.md)) automatically.
* **Automatic Updates** — checks for and applies client updates on launch, covered in more detail below.
* **Account Login** — authenticates against the game's account system ([1204-Authentication.md](../1200-Technical/1204-Authentication.md)) before launching.
* **News & Patch Notes** — surfaces the latest [0004-Version-History.md](../0000-Project/0004-Version-History.md) entries and announcements on the launcher's home screen.

## Design Goals
The launcher should require zero manual configuration from the player — no manually installing Fabric, no manually placing resource packs. This directly supports the Project Goal in the README: "Provide a seamless installation experience through a custom launcher."

## Relationship to Other Systems
See [1101-Client-Mods.md](1101-Client-Mods.md) for what the launcher installs, and [1204-Authentication.md](../1200-Technical/1204-Authentication.md) for the account system it authenticates against.
