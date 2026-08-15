# 1316 — Particle Effects

**Project:** Elysium MMORPG  
**Category:** Art  
**Status:** Design Complete — Implementation Pending  
**Related:** [1308-VFX.md](1308-VFX.md) · [1300-Art-Style.md](1300-Art-Style.md) · [1208-Performance.md](../1200-Technical/1208-Performance.md) · [1113-Client-Optimisation.md](../1100-Client/1113-Client-Optimisation.md)

---

## 1. Overview

Particle Effects are the building blocks of many VFX: sparks, smoke, dust, magic motes, weather particles, and impact bursts. They are budgeted carefully because they multiply quickly in group content.

---

## 2. Principles

- Shared particle libraries for common needs.
- Strict budgets per effect and per scene type (solo, dungeon, raid, city).
- Clear hierarchy so important telegraphs are not lost in ambient particles.
- Style consistent with the overall VFX and art direction.


---

## Additional Detail: Particle Budget Management

Particle effect complexity is budgeted per context — solo/leveling content can afford richer individual effects, while raid and world boss encounters with many simultaneous casters require careful per-effect budget discipline to maintain the performance targets in [1208-Performance.md](../1200-Technical/1208-Performance.md).

## Elemental Particle Language

Each elemental school ([0307-Elements.md](../0300-Characters/0307-Elements.md)) has a distinct particle shape and motion language (fire embers rise and flicker, frost particles drift and settle, shadow particles wisp and dissipate) reinforcing elemental identity beyond color alone.
