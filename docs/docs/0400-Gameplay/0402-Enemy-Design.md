# 0402 — Enemy Design

**Project:** Elysium MMORPG  
**Category:** Gameplay  
**Status:** Design Complete — Implementation Pending  
**Related:** [0401-Combat.md](0401-Combat.md) · [0403-Boss-Mechanics.md](0403-Boss-Mechanics.md) · [0404-AI-Behaviour.md](0404-AI-Behaviour.md) · [0102-Regions.md](../0100-World/0102-Regions.md) · [0307-Elements.md](../0300-Characters/0307-Elements.md)

---

## 1. Overview

Enemies in Elysium are designed to feel native to their region and to teach players the language of combat. Every enemy type should communicate its threat profile through silhouette, animation, and telegraphing before the player has read a single tooltip.

---

## 2. Enemy Categories

| Category | Role | Examples |
|----------|------|----------|
| **Trash / Pack** | Fill combat space, teach basic mechanics | Bandits, wolves, lesser undead |
| **Elite** | Stronger single targets or small groups with one signature ability | Named lieutenants, corrupted beasts |
| **Mini-Boss** | Dungeon or open-world focal points short of full bosses | Dungeon mid-bosses, world-event champions |
| **Boss** | Full encounter design with phases and mechanics | See [0403-Boss-Mechanics.md](0403-Boss-Mechanics.md) |
| **World Boss** | Large-scale open-world encounters | See [0108-World-Bosses.md](../0100-World/0108-World-Bosses.md) |

---

## 3. Design Principles

1. **Readable identity** — a player should know within the first second whether an enemy is melee, ranged, caster, or special.
2. **Regional flavour** — enemy types and visual language match the biome and local conflict of the region ([0102-Regions.md](../0100-World/0102-Regions.md)).
3. **One signature mechanic** — even trash packs should have a small, learnable behaviour (e.g. a charging attack, a short-range fear, a heal on low health).
4. **Elemental & status consistency** — resistances and status applications follow the rules in [0307-Elements.md](../0300-Characters/0307-Elements.md) and [0306-Status-Effects.md](../0300-Characters/0306-Status-Effects.md).
5. **No pure sponge** — high health without interesting behaviour is avoided; difficulty comes from mechanics and positioning, not raw numbers alone.

---

## 4. Loot & Progression Tie-in

Enemy difficulty and rarity of drops are tuned against the regional level band and the loot tables in [0504-Loot-Tables.md](../0500-Items/0504-Loot-Tables.md). Named elites and mini-bosses are the primary sources of Uncommon and Rare gear while leveling.

---

## 5. Technical Notes

Enemy templates live in data files owned by the combat plugin. AI behaviour trees are defined in [0404-AI-Behaviour.md](0404-AI-Behaviour.md). All damage, threat, and status application is server-authoritative.
