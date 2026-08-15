# 0500 — Weapons

**Category:** Items
**Status:** Living Document
**Related:** [0300-Classes.md](../0300-Characters/0300-Classes.md) · [0504-Loot-Tables.md](0504-Loot-Tables.md) · [0509-Enchanting.md](0509-Enchanting.md)

---

## 1. Overview

Weapons are the primary determinant of a character's damage output and combat identity, tuned to reflect each class's fantasy as defined in [0300-Classes.md](../0300-Characters/0300-Classes.md).

## 2. Weapon Types

| Type | Description | Primary Classes |
| --- | --- | --- |
| One-Handed Swords / Axes / Maces | Usable by most melee classes, often paired with a shield or off-hand | Vanguard, Oathkeeper |
| Two-Handed Swords / Axes / Maces / Polearms | Higher base damage, slower attack pace | Vanguard |
| Daggers | Finesse-based, enable specific Shade abilities | Shade |
| Bows / Crossbows | Primary ranged weapon type | Wayfarer |
| Staves / Wands | Primary caster weapon type | Arcanist, Warden (caster form) |
| Shields | Off-hand, tank-focused, contributes heavily to Armor ([0304-Stats.md](../0300-Characters/0304-Stats.md)) | Vanguard, Oathkeeper |

## 3. Design Rules

* Weapon type restricts which classes can equip it, but not which specialization — a Vanguard tank and a Vanguard damage specialization use the same weapon pool.
* Weapon damage and stat budget scale with item level per the loot table framework in [0504-Loot-Tables.md](0504-Loot-Tables.md).
* Visually, weapons should escalate in silhouette and effect flourish as item level increases, giving players a readable sense of gear progression at a glance — see [1300-Art-Style.md](../1300-Art/1300-Art-Style.md).

## 4. Weapon Damage Scaling

Weapon base damage scales primarily with item level, with rarity ([0510-Item-Rarity.md](0510-Item-Rarity.md)) determining the secondary stat budget layered on top. This keeps the relationship between "better weapon" and "bigger numbers" intuitive while still rewarding chasing higher rarity for build-defining secondary stats.

## 5. Class-Specific Weapon Fantasy

* **Vanguard** — heavy, impactful weapons with weighty animations and strong hit-stop feedback.
* **Arcanist** — staves and wands with distinct elemental particle trails matching the caster's spell school ([0307-Elements.md](../0300-Characters/0307-Elements.md)).
* **Shade** — dual daggers with fast, precise animations emphasizing speed over weight.
* **Warden** — staves or fist weapons depending on specialization, with nature-themed visual effects.
* **Oathkeeper** — one-handed weapon and shield combinations with radiant visual accents.
* **Wayfarer** — bows and crossbows with distinct draw and release animations per weapon subtype.

## 6. Acquisition

Weapons drop from quests, dungeons, raids, and vendors, and can be player-crafted via Blacksmithing ([0606-Blacksmithing.md](../0600-Professions/0606-Blacksmithing.md)) or Woodworking for bows. Legendary-tier weapons are tracked separately in [0505-Legendary-Items.md](0505-Legendary-Items.md).

## 7. Enchanting

Weapons can be enhanced with enchantments — see [0509-Enchanting.md](0509-Enchanting.md) for the full system, including weapon-specific enchant slots and on-hit proc effects.

## 8. Transmogrification

Weapon appearances can be changed independently of their underlying stats through the transmog system — see [0513-Transmog-System.md](0513-Transmog-System.md) — letting players maintain a preferred visual identity as they upgrade.
