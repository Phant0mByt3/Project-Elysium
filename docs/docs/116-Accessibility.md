# 116 — Accessibility

## Overview
Accessibility features spanning the client mods ([111-Client-Mods.md](111-Client-Mods.md)), shaders ([115-Shaders.md](115-Shaders.md)), and UI ([131-UI-Style.md](131-UI-Style.md)) to make Elysium playable by as wide an audience as possible.

## Planned Features
* **Colorblind Modes** — alternate palettes for status effects ([047-Status-Effects.md](047-Status-Effects.md)), faction UI elements, and loot rarity colors ([053-Loot.md](053-Loot.md)).
* **Reduced Effects Mode** — a shader/particle-density toggle for photosensitivity and lower-end hardware performance, extending [115-Shaders.md](115-Shaders.md)'s tiered presets.
* **UI Scaling & Text Size** — adjustable UI scale independent of Minecraft's native GUI scale settings.
* **Screen Reader / Text-to-Speech Consideration** — quest text and dialogue readability is a design goal, evaluated during Phase 2 UI development.
* **Remappable Keybinds** — full keybind customization for all Elysium-specific actions (skills, UI panels).

## Design Rules
Accessibility options should be reviewed alongside every major UI or combat-effects feature added to the game, not bolted on as a single late-stage pass — consistent with the "documentation and quality are part of development" pillars in [002-Core-Pillars.md](002-Core-Pillars.md).
