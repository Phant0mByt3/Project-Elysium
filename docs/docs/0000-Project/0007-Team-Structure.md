# 0007 — Team Structure

**Project:** Elysium MMORPG  
**Category:** Project  
**Status:** Living Document  
**Related:** [0001-Vision.md](0001-Vision.md) · [0002-Core-Pillars.md](0002-Core-Pillars.md) · [0003-Roadmap.md](0003-Roadmap.md) · [1400-Development-Standards.md](../1400-Development/1400-Development-Standards.md)

---

## 1. Overview

Project Elysium is built by a multidisciplinary team organised around the six Core Pillars and the documentation-first workflow. Roles are defined by responsibility rather than hierarchy; every contributor is expected to treat documentation as part of the deliverable (Pillar 6).

The structure is intentionally lean during Pre-Production and expands as the project moves into Phase 1–3.

---

## 2. Core Roles

| Role | Primary Ownership | Key Documents |
|------|-------------------|---------------|
| **Creative Director** | Overall vision, lore consistency, final design sign-off | [0001-Vision.md](0001-Vision.md), [0200-Lore.md](../0200-Lore/0200-Lore.md) |
| **Lead Game Designer** | Systems design, combat, progression, economy balance | [0300-Characters/](../0300-Characters/), [0400-Gameplay/](../0400-Gameplay/), [1000-Economy/](../1000-Economy/) |
| **World Director** | Continent & region design, landmarks, dungeons, raids | [0100-World/](../0100-World/), [1402-Building-Standards.md](../1400-Development/1402-Building-Standards.md) |
| **Narrative Lead** | Main story, side stories, NPC voice, quest writing standards | [0207-Main-Story.md](../0200-Lore/0207-Main-Story.md), [1403-Quest-Writing-Guide.md](../1400-Development/1403-Quest-Writing-Guide.md), [1404-NPC-Writing-Guide.md](../1400-Development/1404-NPC-Writing-Guide.md) |
| **Technical Lead** | Plugin architecture, server topology, database, anti-cheat | [1200-Technical/](../1200-Technical/), [1401-Coding-Standards.md](../1400-Development/1401-Coding-Standards.md) |
| **Art Director** | Visual identity, content pack, UI style, model/texture standards | [1300-Art/](../1300-Art/), [1102-Content-Pack.md](../1100-Client/1102-Content-Pack.md) |
| **Client Lead** | Launcher, native client moduleules, HUD, accessibility | [1100-Client/](../1100-Client/) |
| **QA Lead** | Test plans, bug triage, playtest coordination | [1406-Testing.md](../1400-Development/1406-Testing.md), [1407-Bug-Tracking.md](../1400-Development/1407-Bug-Tracking.md) |

---

## 3. Discipline Teams

### World Building Team
Builders, terrain artists, and dungeon designers. Responsible for every handcrafted block of Aurelia, Vethmoor, and future continents. Follows [1402-Building-Standards.md](../1400-Development/1402-Building-Standards.md) and the region templates in [0102-Regions.md](../0100-World/0102-Regions.md).

### Systems Design Team
Combat math, talent trees, itemization, profession progression, economy sinks/sources. Owns the balance process documented in [0309-Balance.md](../0300-Characters/0309-Balance.md).

### Narrative & Quest Team
Writers who produce quest text, dialogue trees, lore books, and cinematic scripts. All content must pass consistency checks against [0200-Lore.md](../0200-Lore/0200-Lore.md) and the writing guides.

### Engineering Team
Unreal Engine (C++) server developers, database engineers, networking specialists, and anti-cheat implementers. Organised into modular plugin owners per [1200-Plugin-Architecture.md](../1200-Technical/1200-Plugin-Architecture.md).

### Art & Client Team
Texture artists, modelers, UI designers, and client moduleders. Produces the content pack and custom models that make players forget they are looking at reused engine assets.

### Live Operations (post-launch)
Community managers, moderators, support staff, and analytics. Detailed in the [2000-Operations/](../2000-Operations/) series once the project reaches Closed Beta.

---

## 4. Decision-Making

- **Design decisions** that affect player experience require sign-off from the relevant Lead + Creative Director.
- **Technical architecture** changes require Technical Lead + at least one systems designer review.
- **Art direction** changes require Art Director approval against [1300-Art-Style.md](../1300-Art/1300-Art-Style.md).
- All decisions that alter a documented system must update the corresponding Markdown file before the change is considered complete.

---

## 5. Onboarding & Contribution

New contributors receive:
1. The Vision and Core Pillars documents.
2. The Documentation Guide ([0006-Documentation-Guide.md](0006-Documentation-Guide.md)).
3. The relevant discipline standards (coding, building, writing, or art).
4. Access to the current region/system they will work on.

No feature or asset is merged until its documentation is updated.

---

## 6. Scaling Notes

During Pre-Production the team is small and multi-hatted. As Phase 3 (World Building) and Phase 4 (Closed Alpha) begin, the World Building and QA teams expand first. Live Operations roles are added only when public testing starts.

This document is updated whenever a new permanent role is created or ownership of a major system changes.
