# 54 — Loot Tables

## Overview
This document defines the framework for how specific drop tables are built per encounter (quest, dungeon boss, raid boss, world boss). Actual per-boss tables are populated as each encounter is designed ([016-Dungeons.md](016-Dungeons.md), [017-Raids.md](017-Raids.md), [018-World-Bosses.md](018-World-Bosses.md)).

## Table Structure
Each boss/encounter loot table should define:
* **Guaranteed drops** — currency ([101-Currency.md](101-Currency.md)), crafting materials.
* **Rare-or-higher item pool** — a curated list of items that can drop, sized to the group size and difficulty tier.
* **Drop chance per difficulty** — Normal/Heroic/Mythic tiers increase both item level and drop chance slightly, per [016-Dungeons.md](016-Dungeons.md)/[017-Raids.md](017-Raids.md) difficulty standards.
* **Set piece tagging** — which armor set ([051-Armour.md](051-Armour.md)) a drop belongs to, if any.

## Design Rules
* Item pools should cover every role (tank/healer/damage) roughly evenly per boss, avoiding "this boss only drops caster gear" problems.
* Legendary items ([055-Legendary-Items.md](055-Legendary-Items.md)) use bespoke, lower-probability tables layered on top of the standard tier table, sometimes requiring a quest chain rather than a pure drop chance.
* Loot tables should be reviewed alongside balance passes ([049-Balance.md](049-Balance.md)) since itemization directly affects class power.
