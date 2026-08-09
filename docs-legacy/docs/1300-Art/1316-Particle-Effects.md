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
