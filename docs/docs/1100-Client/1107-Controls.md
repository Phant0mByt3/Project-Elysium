# Controls

**Project:** Elysium MMORPG
**Category:** Client
**Status:** Design Complete — Implementation Pending
**Related Systems:** [../0400-Gameplay/0400-Game-Mechanics.md](../0400-Gameplay/0400-Game-Mechanics.md) · [../0400-Gameplay/0401-Combat.md](../0400-Gameplay/0401-Combat.md) · [1108-UI-Systems.md](1108-UI-Systems.md) · [1109-Settings.md](1109-Settings.md) · [1106-Accessibility.md](1106-Accessibility.md)

---

## 1. Overview

Elysium replaces vanilla Minecraft's control scheme entirely with a **custom MMORPG control layout**, built to support ability-bar combat, class identity, and full UI navigation without relying on Minecraft's native item-use and hotbar systems.

This document is the technical reference for every default keybind in the game, how those binds route into gameplay systems, and how the rebinding layer works underneath them.

### 1.1 Design Principles

- **Ability-bar first** — combat inputs (`Q E R T`) are always in the same physical position regardless of class, so muscle memory transfers between characters.
- **One key, one purpose** — no context-sensitive overloading of the same key for unrelated systems (a longstanding source of MMORPG player frustration).
- **Left-hand combat, right-hand camera** — matches the genre-standard WASD + mouse layout so players from other MMORPGs feel at home immediately.
- **Everything rebindable** — every bind in this document is a *default*, not a fixed rule; see §14.

---

## 2. Movement Controls

| Key | Action |
|---|---|
| `W` | Move forward |
| `A` | Strafe left |
| `S` | Move backward |
| `D` | Strafe right |
| `Space` | Jump |
| `Left Shift` (hold) | Sprint |
| `Left Ctrl` (hold) | Walk / auto-run toggle (configurable, see [1109-Settings.md](1109-Settings.md)) |
| `Mouse Move` | Camera look |
| `Scroll Wheel` | Camera zoom (first ↔ third person) |

Movement is grounded in standard WASD, deliberately overriding Minecraft's default sneak/fly-adjacent bindings so that all remaining keys are free for ability and UI use.

---

## 3. Combat Controls

Combat input is built around a fixed four-slot core ability bar plus a special and ultimate row, as introduced in [0308-Class-Progression.md](../0300-Characters/0308-Class-Progression.md) §4.

| Key | Action | System |
|---|---|---|
| `Q` | Ability slot 1 | [0302-Skills.md](../0300-Characters/0302-Skills.md) |
| `E` | Ability slot 2 | [0302-Skills.md](../0300-Characters/0302-Skills.md) |
| `R` | Ability slot 3 | [0302-Skills.md](../0300-Characters/0302-Skills.md) |
| `T` | Ability slot 4 | [0302-Skills.md](../0300-Characters/0302-Skills.md) |
| `TAB` | Special ability (class-defining utility, e.g. interrupt, dispel) | [../0400-Gameplay/0401-Combat.md](../0400-Gameplay/0401-Combat.md) |
| `Left Click` | Basic/auto attack | [../0400-Gameplay/0401-Combat.md](../0400-Gameplay/0401-Combat.md) |
| `Right Click` | Secondary interact / block (class-dependent) | [../0400-Gameplay/0401-Combat.md](../0400-Gameplay/0401-Combat.md) |

### 3.1 Ability Hotkeys — Extended Bar

Beyond the core four, players unlock additional ability slots through leveling (see [0305-Leveling.md](../0300-Characters/0305-Leveling.md)):

| Key | Action | Unlock Reference |
|---|---|---|
| `F` | Ability slot 5 | Unlocked mid-progression |
| `G` | Ability slot 6 | Unlocked mid-progression |
| `1` | Ultimate ability 1 | [0308-Class-Progression.md](../0300-Characters/0308-Class-Progression.md) §11 |
| `2` | Ultimate ability 2 | Advanced Class Path exclusive |

### 3.2 Ultimate Abilities

Ultimates are the highest-impact abilities in a class's kit, gated behind long cooldowns or resource thresholds.

| Key | Slot | Notes |
|---|---|---|
| `1` | Primary Ultimate | Available from base class kit |
| `2` | Secondary Ultimate | Unlocked via Advanced Class Path (see [0308-Class-Progression.md](../0300-Characters/0308-Class-Progression.md) §10) |

---

## 4. Class Movement Abilities

Every class has one dedicated movement-oriented ability bound to `ALT`, reinforcing class fantasy at the input level rather than burying it in the general ability bar.

| Class | `ALT` Ability | Effect |
|---|---|---|
| Mage | Arcane Teleport | Short-range blink through obstacles |
| Druid | Wild Sprint | Temporary burst movement speed, breaks roots |
| Warrior | Charge | Gap-closer with a brief stun on impact |
| Rogue | Shadowstep | Teleport behind target |
| Ranger | Disengage | Backward leap, briefly grants evasion |

> **Developer Note:** `ALT` is reserved *exclusively* for class movement — no other system may bind to it by default, since consistent muscle memory here is core to combat readability, especially in PvP (see [../0800-Multiplayer/0804-PvP.md](../0800-Multiplayer/0804-PvP.md)).

---

## 5. Inventory Shortcuts

| Key | Action |
|---|---|
| `I` | Open Character / Inventory interface (see [1108-UI-Systems.md](1108-UI-Systems.md) §Inventory Design) |
| `B` | Open Bag-only quick view (compact inventory) |
| `Shift + Left Click` | Quick-move item between bag and equipment/storage |
| `Ctrl + Left Click` | Split item stack |

---

## 6. UI Shortcuts

| Key | Action |
|---|---|
| `M` | Open Map interface |
| `J` | Open Quest Log |
| `K` | Open Skill / Talent interface |
| `O` | Open Guild interface |
| `N` | Open Social / Friends interface |
| `Escape` | Close active window / open Settings menu if no window is open |

Full interface behavior for each of these is documented in [1108-UI-Systems.md](1108-UI-Systems.md).

---

## 7. Interaction Controls

| Key | Action |
|---|---|
| `F` (contextual, hold) | Interact with NPC, object, or resource node — overridden by ability slot 5 only outside interact range |
| `Left Click` (on NPC) | Talk / open vendor / quest dialogue |
| `X` | Dismount |
| `V` | Sheath/unsheathe weapon (cosmetic, no gameplay effect) |

> **Developer Note:** `F` is context-sensitive *only* between interaction and Ability Slot 5 — this is the single deliberate exception to the "one key, one purpose" rule in §1.1, resolved by proximity: interaction takes priority within interact range, ability use otherwise.

---

## 8. Mount Controls

| Key | Action |
|---|---|
| `Y` (hold) | Summon/dismiss last-used mount |
| `Space` | Mount jump (where applicable) |
| `X` | Dismount |
| `Shift` | Mount sprint (where applicable) |

See [../0900-Player-Systems/0901-Mounts.md](../0900-Player-Systems/0901-Mounts.md) for mount-specific ability binds (flying mounts, combat mounts, etc.), which layer on top of this base scheme.

---

## 9. Map Controls

| Key | Action |
|---|---|
| `M` | Toggle full map |
| `Scroll Wheel` (in map) | Zoom map |
| `Left Click` (in map) | Set waypoint / travel marker |
| `Right Click` (in map) | Clear waypoint |

---

## 10. Party and Social Controls

| Key | Action |
|---|---|
| `P` | Open Party interface |
| `Enter` | Open chat |
| `Enter` then `/p` | Party chat |
| `Enter` then `/g` | Guild chat |
| `Ctrl + Click` (on player) | Invite to party |

---

## 11. Key Rebinding System

All binds in this document are stored as **default profiles**, not hardcoded values. The rebinding system works as follows:

1. Every bindable action has a unique internal action ID (e.g. `ability.slot.1`, `ui.inventory.toggle`).
2. Keybinds map `physical key → action ID`, stored per-profile in [1109-Settings.md](1109-Settings.md).
3. Conflicts are detected at bind-time: assigning a key already in use prompts the player to confirm the swap.
4. Profiles can be saved, named, and switched (e.g. a "PvP" profile vs. a "Leveling" profile).
5. Rebinding does **not** require a client restart; changes apply immediately.

| Rule | Description |
|---|---|
| Reserved keys | `Escape`, `Enter` cannot be unbound (safety requirement) |
| Per-class overrides | A player may bind ability slots differently per class if desired |
| Reset to default | One-click revert to the table values in this document |

---

## 12. Controller Support

Elysium supports a full controller layout mapped from the keyboard scheme above, using radial ability selection to fit the reduced button count.

| Controller Input | Maps To |
|---|---|
| Left Stick | Movement (WASD) |
| Right Stick | Camera |
| Face Buttons (A/B/X/Y or ×/○/□/△) | Ability slots `Q E R T` |
| Triggers | `TAB` special / basic attack |
| Bumpers | Ultimate 1 / Ultimate 2 |
| D-Pad | UI shortcuts (Map, Inventory, Quest Log, Social) via radial menu |
| Right Stick Click | Class movement ability (`ALT` equivalent) |

Controller rebinding follows the same profile system described in §11, with controller-specific profiles stored separately from keyboard/mouse profiles.

---

## 13. Future VR Compatibility

Controls are designed with a future VR mode in mind, without requiring a rework of the underlying action-ID system described in §11:

- All actions are already abstracted behind action IDs rather than raw key codes, so a VR controller mapping is a new *profile*, not a new *system*.
- Ability slots `Q E R T` map conceptually to a VR gesture/wrist-menu system (one gesture per core ability).
- Class movement abilities (`ALT`) map to a dedicated VR controller button to preserve the "always available, always the same input" rule from §4.
- Full VR-specific control documentation will be added as its own file once VR moves from consideration to active development; this document will be updated to link to it.

---

## 14. System Rules Summary

1. All default binds are listed in this document; no system may silently claim an unbound key.
2. `ALT` is reserved exclusively for class movement abilities.
3. `Q E R T` are reserved exclusively for the four core ability slots across all classes.
4. Rebinding is always available, changes apply live, and reserved safety keys (`Escape`, `Enter`) cannot be removed.
5. Controller and future VR support must map onto the same underlying action-ID system, not a parallel one.

---

## 15. Connections to Other Systems

| System | Relationship |
|---|---|
| [../0400-Gameplay/0400-Game-Mechanics.md](../0400-Gameplay/0400-Game-Mechanics.md) | Defines the mechanics that control inputs trigger |
| [../0400-Gameplay/0401-Combat.md](../0400-Gameplay/0401-Combat.md) | Defines resource costs, cooldowns, and effects behind combat binds |
| [1108-UI-Systems.md](1108-UI-Systems.md) | Defines the interfaces opened by UI shortcut keys |
| [1109-Settings.md](1109-Settings.md) | Stores and persists all keybind profiles |
| [1106-Accessibility.md](1106-Accessibility.md) | Defines alternative input accommodations (hold-vs-toggle, remapping aids, colourblind-safe prompts) |
