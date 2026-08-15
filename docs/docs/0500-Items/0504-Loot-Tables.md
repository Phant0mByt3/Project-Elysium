# 0504 — Loot Tables

## Overview
This document defines the framework for how specific drop tables are built per encounter (quest, dungeon boss, raid boss, world boss). Actual per-boss tables are populated as each encounter is designed ([0106-Dungeons.md](../0100-World/0106-Dungeons.md), [0107-Raids.md](../0100-World/0107-Raids.md), [0108-World-Bosses.md](../0100-World/0108-World-Bosses.md)).

## Table Structure
Each boss/encounter loot table should define:
* **Guaranteed drops** — currency ([1001-Currency.md](../1000-Economy/1001-Currency.md)), crafting materials.
* **Rare-or-higher item pool** — a curated list of items that can drop, sized to the group size and difficulty tier.
* **Drop chance per difficulty** — Normal/Heroic/Mythic tiers increase both item level and drop chance slightly, per [0106-Dungeons.md](../0100-World/0106-Dungeons.md)/[0107-Raids.md](../0100-World/0107-Raids.md) difficulty standards.
* **Set piece tagging** — which armor set ([0501-Armour.md](0501-Armour.md)) a drop belongs to, if any.

## Design Rules
* Item pools should cover every role (tank/healer/damage) roughly evenly per boss, avoiding "this boss only drops caster gear" problems.
* Legendary items ([0505-Legendary-Items.md](0505-Legendary-Items.md)) use bespoke, lower-probability tables layered on top of the standard tier table, sometimes requiring a quest chain rather than a pure drop chance.
* Loot tables should be reviewed alongside balance passes ([0309-Balance.md](../0300-Characters/0309-Balance.md)) since itemization directly affects class power.


---

## Loot Table Weighting

Item pools use weighted-random selection rather than flat equal chance, allowing designers to make certain slots (e.g. weapons, tier-set pieces) rarer than generic accessories within the same encounter, while still guaranteeing role coverage per kill over a reasonable number of attempts.

## Bonus Loot Mechanics

Weekly bonus rolls (a limited number of extra loot chances per lockout) give players additional agency over their itemization pace without breaking the lockout structure described in [0107-Raids.md](../0100-World/0107-Raids.md).

## Currency and Material Drops

Every encounter also drops a baseline of currency and crafting materials scaled to its tier, feeding both the economy sinks/sources model in [1010-Currency-Sinks.md](../1000-Economy/1010-Currency-Sinks.md) and the crafting loop in [0508-Crafting.md](0508-Crafting.md).

## Table Review Cadence

Loot tables are reviewed every balance pass alongside class tuning ([0309-Balance.md](../0300-Characters/0309-Balance.md)), since a table that over- or under-serves a given role can distort perceived class balance even when the underlying class math is correct.
