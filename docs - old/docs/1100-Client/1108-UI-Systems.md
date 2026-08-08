# 1108 — UI Systems

**Project:** Elysium MMORPG
**Category:** Client
**Status:** Design Complete — Implementation Pending
**Related Systems:** [1107-Controls.md](1107-Controls.md) · [1109-Settings.md](1109-Settings.md) · [../1300-Art/1301-UI-Style.md](../1300-Art/1301-UI-Style.md) · [../1300-Art/1304-Icons.md](../1300-Art/1304-Icons.md) · [../0300-Characters/0300-Classes.md](../0300-Characters/0300-Classes.md) · [../0400-Gameplay/0400-Game-Mechanics.md](../0400-Gameplay/0400-Game-Mechanics.md)

---

## 1. UI Philosophy

Elysium is built as a **standalone MMORPG experience**. Every interface is custom-built and replaces the vanilla Minecraft HUD and menus entirely — no survival hunger bar, no vanilla inventory grid, no experience bar in the Minecraft style.

### 1.1 Core Principles

- **Information density without clutter** — a raiding player needs cooldowns, buffs, and party health at a glance; a leveling player needs quest and minimap focus. The UI must serve both without redesign.
- **Consistent visual language** — every interface shares the same frame style, iconography, and colour rules from [../1300-Art/1301-UI-Style.md](../1300-Art/1301-UI-Style.md).
- **Diegetic minimalism** — the HUD stays out of the way during exploration and expands only when combat or menus demand it.
- **Class-aware by default** — UI elements (ability bar layout, resource bar colour/shape) adapt automatically based on the equipped class (see [../0300-Characters/0300-Classes.md](../0300-Characters/0300-Classes.md)).

---

## 2. Main HUD

The default HUD, visible during normal gameplay, is composed of independently toggleable modules:

| HUD Element | Default Position | Notes |
|---|---|---|
| Health/Mana/Resource bars | Bottom-centre | See §3 |
| Ability bar | Bottom-centre, above resource bars | See §4 |
| Buff/debuff tray | Top-right | See §6 |
| Minimap | Top-right corner | See §12 |
| Quest tracker | Right edge | See §11 |
| Target frame | Top-centre (appears on target select) | Mirrors player resource bar layout |
| Party frames | Left edge | Appears only when in a party (see §15) |

All positions are drag-repositionable; see §17 for custom positioning rules.

---

## 3. Health/Mana/Resource Displays

| Bar | Description |
|---|---|
| Health | Universal across all classes; red gradient by default, recolourable in §17 |
| Mana / Resource | Class-dependent — Mage uses Mana, Warrior uses Rage, Rogue uses Energy, Druid uses a hybrid resource |
| Secondary resource (where applicable) | Combo points, stacks, or charges rendered as pips beneath the main resource bar |

Resource bar colour and shape are pulled automatically from class data (see [../0300-Characters/0300-Classes.md](../0300-Characters/0300-Classes.md)) so no manual per-class UI work is needed when new classes are added.

---

## 4. Ability Bar

The ability bar mirrors the control scheme in [1107-Controls.md](1107-Controls.md) exactly — slot position, key label, and bound action are always in sync.

| Slot | Bound Key | Source |
|---|---|---|
| 1–4 | `Q E R T` | Core abilities |
| 5 | `TAB` | Special ability |
| 6–7 | `F G` | Extended slots |
| 8–9 | `1 2` | Ultimates |
| 10 | `ALT` | Class movement ability |

Each slot renders: ability icon (see [../1300-Art/1304-Icons.md](../1300-Art/1304-Icons.md)), keybind label, cooldown overlay, and a charge counter for abilities with multiple charges.

---

## 5. Cooldown Displays

- **Radial sweep** overlay on the ability icon, darkening clockwise as the ability is used and clearing counterclockwise as it becomes available.
- **Numeric countdown** for cooldowns over 3 seconds; sub-3-second cooldowns show sweep only, to reduce visual noise during fast rotations.
- **Global cooldown (GCD)** renders as a thin shared border pulse across all ability slots simultaneously, distinguishing "everything is on GCD" from "this specific ability is on cooldown."

---

## 6. Buff and Debuff System

| Element | Behavior |
|---|---|
| Buff tray | Top-right, positive effects, sorted by duration remaining |
| Debuff tray | Directly beneath buff tray, negative effects, sorted by severity then duration |
| Stack counter | Rendered as a numeral badge on the icon for stacking effects |
| Expiry warning | Icon border flashes amber under 3 seconds remaining |

Buff/debuff data is sourced from [../0300-Characters/0306-Status-Effects.md](../0300-Characters/0306-Status-Effects.md).

---

## 7. Quest Tracker

- Docked to the right edge by default; collapsible per-quest.
- Displays active quest name, current objective, and progress (e.g. `3/5`).
- Colour-coded by quest type (main story, side, daily, weekly — matching categories in [../0700-Quests/0700-Quests.md](../0700-Quests/0700-Quests.md)).
- Clicking an objective pings its location on the minimap and full map.

---

## 8. Minimap

| Feature | Behavior |
|---|---|
| Rotation mode | Player-facing rotation by default, north-locked optional |
| Zoom | Scroll wheel while hovered |
| Icons | NPCs, quest markers, points of interest, party members |
| Ping system | `Shift + Click` on minimap broadcasts a ping to party |

---

## 9. Character Interface

Opened via `I` (see [1107-Controls.md](1107-Controls.md) §5). Displays:

- **Character model** — real-time render of equipped gear and cosmetics
- **Equipment slots** — arranged around the character model
- **Statistics** — derived combat stats (crit chance, haste, etc.)
- **Attributes** — base stats from [../0300-Characters/0304-Stats.md](../0300-Characters/0304-Stats.md)
- **Progression summary** — current level, specialisation, and Advanced Class Path (see [../0300-Characters/0308-Class-Progression.md](../0300-Characters/0308-Class-Progression.md))

---

## 10. Inventory Interface

Shares the same window frame as the Character Interface (tabbed), opened via the same `I` key.

| Element | Description |
|---|---|
| Bag grid | Sortable, stackable item grid |
| Item tooltip | Hover reveals stats, rarity colour, and set bonus text |
| Quick-equip | Double-click to auto-equip to the correct slot |
| Currency tray | Fixed header row showing gold and other currencies (see [../1000-Economy/1001-Currency.md](../1000-Economy/1001-Currency.md)) |

---

## 11. Equipment Interface

Integrated into the Character Interface (§9) rather than a separate window — equipment slots surround the character model directly, with drag-and-drop from the Inventory grid.

| Slot Group | Slots |
|---|---|
| Armour | Head, Shoulders, Chest, Hands, Legs, Feet |
| Weapon | Main-hand, Off-hand |
| Accessories | Rings ×2, Necklace, Trinket ×2 |

---

## 12. Skill Interface

Opened via `K`. Displays the Skill and Talent Trees side by side:

- **Skill panel** — active/passive skills, ranking controls, Skill Point counter (see [../0300-Characters/0302-Skills.md](../0300-Characters/0302-Skills.md))
- **Talent panel** — node-based tree, Talent Point counter (see [../0300-Characters/0303-Talent-Trees.md](../0300-Characters/0303-Talent-Trees.md))
- **Preview mode** — lets players plan a build without spending points, useful before a respec

---

## 13. Map Interface

Full-screen version of the minimap (§8), opened via `M`:

- Continent-level and region-level zoom tiers
- Fast travel node markers (see [../0100-World/0111-Fast-Travel.md](../0100-World/0111-Fast-Travel.md))
- Waypoint setting, shared with party members if grouped

---

## 14. Social Interfaces

| Interface | Key | Contents |
|---|---|---|
| Friends List | `N` | Online status, quick invite/whisper |
| Guild Roster | `O` | See §16 |
| Chat Window | `Enter` | Channel tabs (Say, Party, Guild, World) |

---

## 15. Party Interface

Appears automatically on the left edge of the HUD when grouped (also accessible full-screen via `P`):

- Party member frames with health/resource bars
- Role icons (Tank/Healer/DPS) *(reserved, future content)*
- Ready-check and loot-role indicators

---

## 16. Guild Interface

Opened via `O`:

- Member roster with rank, last-online, and note fields
- Guild bank interface (see [../1000-Economy/1006-Banking.md](../1000-Economy/1006-Banking.md))
- Guild perks/progression panel (see [../0800-Multiplayer/0800-Guilds.md](../0800-Multiplayer/0800-Guilds.md))

---

## 17. Settings Interface

Opened via `Escape` when no other window is active, or directly from any menu's settings icon. Full option breakdown lives in [1109-Settings.md](1109-Settings.md); the UI-specific tab covers:

- HUD element toggles (show/hide per module from §2)
- **UI scaling** — global scale slider (75%–150%) plus per-element override
- **Custom positioning** — drag-and-drop repositioning of every HUD module listed in §2, with a "lock UI" toggle to prevent accidental drags mid-combat
- **UI themes** — palette variants built on [../1300-Art/1301-UI-Style.md](../1300-Art/1301-UI-Style.md) (Default, High Contrast, Colourblind-safe — see §19)

---

## 18. UI Scaling and Custom Positioning

| Feature | Behavior |
|---|---|
| Global scale | Multiplies all HUD element sizes uniformly |
| Per-element scale | Overrides global scale for a single module (e.g. larger buff tray, smaller minimap) |
| Snap-to-grid | Optional, aids aligning multiple HUD elements neatly |
| Profile save | Positioning/scaling saved per settings profile, synced via [1109-Settings.md](1109-Settings.md) |

---

## 19. Accessibility Options

Full accessibility scope is owned by [1106-Accessibility.md](../1100-Client/1106-Accessibility.md); the UI system exposes the following hooks to support it:

- Colourblind-safe theme variants (§17)
- Scalable text independent of overall UI scale
- Screen-reader-friendly tooltip structure
- Reduced-motion mode (disables non-essential UI animation, e.g. cooldown sweep easing)

---

## 20. Performance Considerations

| Concern | Mitigation |
|---|---|
| Party frames in large raids | Frames beyond 5 members switch to a compact renderer with reduced update frequency |
| Buff/debuff tray overflow | Caps visible icons at 12, overflow collapses into a "+N more" indicator |
| Minimap rendering cost | Minimap terrain snapshot refreshes on a timer, not every frame, to avoid redundant redraws |
| UI animation load | Reduced-motion mode (§19) also serves as a performance option on low-end hardware |

Performance budgets for UI rendering are tracked alongside general client performance in [../1200-Technical/1208-Performance.md](../1200-Technical/1208-Performance.md).

---

## 21. Connections to Other Systems

| System | Relationship |
|---|---|
| [1107-Controls.md](1107-Controls.md) | Every UI shortcut key and ability bar slot is defined there; this document renders what those keys open |
| [1109-Settings.md](1109-Settings.md) | Stores UI scale, positioning, and theme preferences persistently |
| [../1300-Art/1301-UI-Style.md](../1300-Art/1301-UI-Style.md) | Defines the visual language (frames, colours) used across every interface in this document |
| [../1300-Art/1304-Icons.md](../1300-Art/1304-Icons.md) | Source of all ability, item, and UI iconography |
| [../0300-Characters/0300-Classes.md](../0300-Characters/0300-Classes.md) | Drives class-specific resource bar colour/shape and ability bar defaults |
| [../0400-Gameplay/0400-Game-Mechanics.md](../0400-Gameplay/0400-Game-Mechanics.md) | Defines the underlying systems (cooldowns, resources, status effects) that the UI visualises |
