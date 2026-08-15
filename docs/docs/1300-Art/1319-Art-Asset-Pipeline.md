# 1319 — Art Asset Pipeline

**Project:** Elysium MMORPG  
**Category:** Art  
**Status:** Design Complete — Implementation Pending  
**Related:** [1300-Art-Style.md](1300-Art-Style.md) · [1102-Content-Pack.md](../1100-Client/1102-Content-Pack.md) · [1414-Asset-Management.md](../1400-Development/1414-Asset-Management.md) · [1400-Development-Standards.md](../1400-Development/1400-Development-Standards.md)

---

## 1. Overview

The Art Asset Pipeline describes how concept becomes in-game asset: briefing, production, review, export, packaging into the content pack, and live update.

---

## 2. Stages

1. Brief / reference against style and design docs  
2. Concept / blockout  
3. High production (model, texture, animation, VFX as needed)  
4. Technical pass (LODs, budgets, naming)  
5. Art and design review  
6. Export and pack integration  
7. In-game verification  

---

## 3. Design Rules

1. No asset ships without a style and budget review.
2. Naming and folder structure follow project conventions so packs stay maintainable.
3. Source files are archived; runtime assets are optimised.
4. Hotfix and patch updates follow the same quality gates at appropriate speed.


---

## Additional Detail: Pipeline Stages

The asset pipeline moves through concept approval, blockout/greybox review, final asset production, technical integration (rigging, LOD, texture assignment), and a final style-consistency review before an asset is merged into the content pack ([1102-Content-Pack.md](../1100-Client/1102-Content-Pack.md)).

## Version Control and Asset Tracking

All art assets are tracked through a version-controlled asset management system, allowing the team to roll back problematic changes and maintain a clear history of iteration on any given asset throughout its production lifecycle.
