# 1123 — Client Configuration

**Project:** Elysium MMORPG  
**Category:** Client  
**Status:** Design Complete — Implementation Pending  
**Related:** [1109-Settings.md](1109-Settings.md) · [1113-Client-Optimisation.md](1113-Client-Optimisation.md) · [1106-Accessibility.md](1106-Accessibility.md) · [1101-Client-Mods.md](1101-Client-Mods.md)

---

## 1. Overview

Client Configuration covers the storage, application, and exposure of all user-configurable options: graphics, audio, controls, UI scale, accessibility, and gameplay preferences.

---

## 2. Categories

- Graphics and performance presets
- Audio volumes and device selection
- Keybinds and input options
- UI scale, layout, and visibility toggles
- Accessibility (colourblind modes, text size, motion reduction, etc.)
- Gameplay toggles (auto-loot, camera behaviour, combat text, etc.)

---

## 3. Design Rules

1. Defaults are sensible for a first-time player on typical hardware.
2. Every option has a clear label and, where needed, a short description.
3. Changes that require a restart are minimised and clearly marked.
4. Configuration is stored locally and, where appropriate, can be synced or reset easily.

---

## 4. Technical Notes

Settings are read and written by the client mod stack. Some options affect only the local client; others (e.g. certain gameplay preferences) may be stored on the character or account record for consistency across machines.
