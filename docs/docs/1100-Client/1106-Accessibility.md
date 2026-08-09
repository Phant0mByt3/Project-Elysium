# 1106 — Accessibility

## Overview
Accessibility features spanning the client moduleules ([1101-Client-Modules.md](1101-Client-Modules.md)), rendering effects ([1105-Shaders.md](1105-Shaders.md)), and UI ([1301-UI-Style.md](../1300-Art/1301-UI-Style.md)) to make Elysium playable by as wide an audience as possible.

## Planned Features
* **Colorblind Modes** — alternate palettes for status effects ([0306-Status-Effects.md](../0300-Characters/0306-Status-Effects.md)), faction UI elements, and loot rarity colors ([0503-Loot.md](../0500-Items/0503-Loot.md)).
* **Reduced Effects Mode** — a post-process/particle-density toggle for photosensitivity and lower-end hardware performance, extending [1105-Shaders.md](1105-Shaders.md)'s tiered presets.
* **UI Scaling & Text Size** — adjustable UI scale independent of the engine's default UI scale settings.
* **Screen Reader / Text-to-Speech Consideration** — quest text and dialogue readability is a design goal, evaluated during Phase 2 UI development.
* **Remappable Keybinds** — full keybind customization for all Elysium-specific actions (skills, UI panels).

## Design Rules
Accessibility options should be reviewed alongside every major UI or combat-effects feature added to the game, not bolted on as a single late-stage pass — consistent with the "documentation and quality are part of development" pillars in [0002-Core-Pillars.md](../0000-Project/0002-Core-Pillars.md).
