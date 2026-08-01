# 1109 — Settings

**Project:** Elysium MMORPG
**Category:** Client
**Status:** Design Complete — Implementation Pending
**Related Systems:** [1107-Controls.md](1107-Controls.md) · [1108-UI-Systems.md](1108-UI-Systems.md) · [1106-Accessibility.md](1106-Accessibility.md) · [../1200-Technical/1201-Database.md](../1200-Technical/1201-Database.md) · [../1200-Technical/1211-Server-Synchronisation.md](../1200-Technical/1211-Server-Synchronisation.md)

---

## 1. Settings Overview

The Settings system is the single persistence layer for every player-configurable option in Elysium — controls, graphics, audio, UI, gameplay, accessibility, account, privacy, and performance. It is designed around one rule: **any option a player can change should be saved automatically, synced across servers, and restorable to default at any time.**

Settings are grouped into categories, each covered below, and are stored both locally (for fast startup) and remotely (for cross-server/cross-device consistency — see §12).

---

## 2. Controls Settings

Covers everything defined as *default* in [1107-Controls.md](1107-Controls.md), made fully configurable here:

| Option | Description |
|---|---|
| Key rebinding | Remap any action ID to any physical key (see [1107-Controls.md](1107-Controls.md) §11) |
| Controller support | Enable/disable controller input, choose controller profile |
| Custom profiles | Save multiple named keybind profiles (e.g. "PvE", "PvP") and hot-switch between them |
| Mouse sensitivity | Camera look sensitivity, separate sliders for X/Y axis |
| Invert Y-axis | Toggle |
| Hold vs. Toggle | Per-action choice for holdable inputs (e.g. Sprint, Walk) |

---

## 3. Graphics Settings

| Option | Range/Values | Notes |
|---|---|---|
| Render distance | 4–32 chunks | Higher values increase server-side load estimation; see [../1200-Technical/1208-Performance.md](../1200-Technical/1208-Performance.md) |
| Shadows | Off / Low / Medium / High | Affects both terrain and dynamic entity shadows |
| Particles | Off / Reduced / Full | Reduced mode caps concurrent ability VFX particles |
| Effects | Off / Reduced / Full | Governs screen-space effects (bloom, chromatic aberration) |
| Texture quality | Low / Medium / High | Tied to resource pack resolution, see [1102-Resource-Pack.md](1102-Resource-Pack.md) |
| VSync | On / Off | |
| Field of View | 60°–110° | |

---

## 4. Shader Settings

Elysium ships with a first-party shader pack (see [1105-Shaders.md](1105-Shaders.md)); the settings interface exposes:

| Option | Description |
|---|---|
| Shader profile | None / Performance / Balanced / Cinematic |
| Custom shader upload | Advanced users may load a compatible third-party shader pack |
| Dynamic weather effects | Toggle (rain, fog, god rays) |
| Water reflections | Off / Low / High |

---

## 5. Audio Settings

| Option | Description |
|---|---|
| Master volume | Global multiplier |
| Music volume | Includes the soundtrack (see [1104-Soundtrack.md](1104-Soundtrack.md)) |
| SFX volume | Combat, ability, and environment sounds |
| Ambient volume | World ambience (wind, crowds, wildlife) |
| Voice/UI volume | NPC voice lines and UI feedback sounds |
| Mute on unfocus | Toggle |

---

## 6. UI Settings

| Option | Description |
|---|---|
| HUD scaling | Global and per-element scale (see [1108-UI-Systems.md](1108-UI-Systems.md) §18) |
| Interface movement | Enable/lock dragging of HUD elements |
| Notifications | Toggle categories: loot, achievement, guild, system |
| UI theme | Default / High Contrast / Colourblind-safe |
| Chat window opacity | Slider |

---

## 7. Gameplay Settings

| Option | Description |
|---|---|
| Auto-loot | Toggle |
| Combat text | Toggle floating damage/healing numbers |
| Tooltip detail level | Basic / Advanced (advanced shows raw formulas) |
| Auto-target nearest enemy | Toggle |
| Quest auto-track new quests | Toggle |

---

## 8. Accessibility Settings

Full scope owned by [1106-Accessibility.md](1106-Accessibility.md); Settings exposes the toggles directly:

| Option | Description |
|---|---|
| Colourblind mode | Protanopia / Deuteranopia / Tritanopia / Off |
| Reduced motion | Disables non-essential animation |
| Subtitles | On/Off, size, background opacity |
| Screen reader support | Toggle for UI narration |
| Hold-to-toggle conversion | Converts all hold-inputs to toggle-inputs |

---

## 9. Account Settings

| Option | Description |
|---|---|
| Display name | Subject to naming rules (see [../1400-Development/1405-Naming-Conventions.md](../1400-Development/1405-Naming-Conventions.md)) |
| Linked email | For account recovery |
| Two-factor authentication | On/Off (see [../1200-Technical/1204-Authentication.md](../1200-Technical/1204-Authentication.md)) |
| Session management | View/revoke active logins |

---

## 10. Privacy Settings

| Option | Description |
|---|---|
| Online status visibility | Everyone / Friends Only / Invisible |
| Whisper permissions | Everyone / Friends Only / Guild Only / Off |
| Party invite permissions | Everyone / Friends Only / Off |
| Data sharing preferences | Analytics opt-in/out, where legally applicable |

---

## 11. Performance Settings

| Option | Description |
|---|---|
| Frame rate cap | Uncapped / 30 / 60 / 120 / 144 |
| Background process throttling | Reduce client resource use when window unfocused |
| Network bandwidth mode | Standard / Low-bandwidth (reduces update frequency for cosmetic effects) |
| Preload distant instances | Toggle, trades memory for reduced load-in stutter (see [../1200-Technical/1209-Instance-System.md](../1200-Technical/1209-Instance-System.md)) |

---

## 12. Advanced Settings

Hidden behind an "Advanced" toggle for players who want raw control:

| Option | Description |
|---|---|
| Custom config file access | Read-only export of the underlying settings JSON |
| Debug overlay | FPS, ping, memory usage |
| Experimental features | Opt-in toggles for features in active testing |

---

## 13. Saving Settings

- Every setting change is applied **immediately** in the client and queued for persistence.
- A local cache is written on every change (debounced to avoid excessive disk writes) so settings survive a crash.
- The queued change is pushed to the account's settings record in the database (§14) within a few seconds, subject to normal network conditions.

---

## 14. Database Storage

Settings are stored per-account (not per-character), except for keybind profiles, which may optionally be scoped per-character if a player enables per-character overrides (see [1107-Controls.md](1107-Controls.md) §11).

| Data | Storage Location | Notes |
|---|---|---|
| Account-wide settings | Central account database (see [../1200-Technical/1201-Database.md](../1200-Technical/1201-Database.md)) | Graphics, audio, accessibility, privacy |
| Per-character overrides | Character record | Keybind profile selection, UI layout if customised per-class |
| Local cache | Client-side file | Fast startup, offline fallback |

---

## 15. Synchronisation Between Servers

Because Elysium runs on a multi-instance server architecture (see [../1200-Technical/1209-Instance-System.md](../1200-Technical/1209-Instance-System.md)), settings must remain consistent regardless of which world instance or continent a player is currently connected to.

This is handled by the account-level settings service described in [../1200-Technical/1211-Server-Synchronisation.md](../1200-Technical/1211-Server-Synchronisation.md):

1. On login, the Settings service fetches the account's settings record once, before any world instance connection is established.
2. Settings are passed to whichever instance the player connects to as part of session handoff.
3. Any in-session setting change is written back to the central account record, not to the instance itself, so a later transfer to a different instance (e.g. entering a dungeon) carries the same settings without re-fetching.

---

## 16. Default Profiles

New accounts start from a **Default Profile**, tuned for a mid-range system and a first-time player:

| Category | Default |
|---|---|
| Graphics | Medium preset |
| Audio | All channels at 80% |
| UI theme | Default |
| Controls | Base layout from [1107-Controls.md](1107-Controls.md) |
| Accessibility | All off (opt-in model) |

Default profiles are versioned; a future balance or UX pass may ship a new default profile version without retroactively altering existing players' saved settings.

---

## 17. System Rules Summary

1. All settings are account-scoped by default; only keybind profiles may be character-scoped.
2. Every change is saved locally immediately and remotely within seconds.
3. Settings must be available before instance connection completes at login (§15).
4. Accessibility toggles (§8) are opt-in and never auto-enabled based on inferred player behavior.
5. Advanced/debug settings (§12) must never affect gameplay balance — display and diagnostics only.

---

## 18. Connections to Other Systems

| System | Relationship |
|---|---|
| [1107-Controls.md](1107-Controls.md) | Source of all keybind defaults; this document stores and persists player overrides |
| [1108-UI-Systems.md](1108-UI-Systems.md) | Source of all UI modules; this document stores scale/position/theme preferences |
| [1106-Accessibility.md](1106-Accessibility.md) | Defines accessibility feature scope; this document exposes the toggles |
| [../1200-Technical/1201-Database.md](../1200-Technical/1201-Database.md) | Physical storage layer for account and character settings records |
| [../1200-Technical/1211-Server-Synchronisation.md](../1200-Technical/1211-Server-Synchronisation.md) | Ensures settings are consistent across all instances a player connects to |
