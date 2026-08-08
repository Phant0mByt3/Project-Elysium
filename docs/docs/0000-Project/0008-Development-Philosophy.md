# 0008 — Development Philosophy

**Project:** Elysium MMORPG  
**Category:** Project  
**Status:** Living Document  
**Related:** [0001-Vision.md](0001-Vision.md) · [0002-Core-Pillars.md](0002-Core-Pillars.md) · [1400-Development-Standards.md](../1400-Development/1400-Development-Standards.md)

---

## 1. Core Belief

Elysium is not a mod or reskin of another game with RPG features bolted on.  
It is an MMORPG built natively on Unreal Engine.

Every decision is measured against one question:

> Does this make the player feel they are living in Elysium, rather than playing a game built in an engine?

If the answer is no, the feature is redesigned or discarded.

---

## 2. Documentation-First Development

No system is considered complete until it is documented in this GDD.

- Design documents are written **before** implementation begins.
- Implementation must match the document; if reality diverges, the document is updated first.
- Undocumented features are treated as unfinished features (Pillar 6).

This practice prevents tribal knowledge, reduces design drift, and makes onboarding new contributors straightforward.

---

## 3. Quality Over Quantity

A smaller, fully realised continent is preferable to a larger, empty one.  
A polished 5-player dungeon with three memorable bosses is preferable to ten forgettable ones.

Content is not shipped until it meets the bar defined in [1400-Development-Standards.md](../1400-Development/1400-Development-Standards.md) and the relevant discipline standards (building, writing, coding, art).

---

## 4. Handcrafted World Priority

The world is authored, never generated at runtime.

- Terrain, cities, dungeons, and landmarks exist because a designer placed them with purpose.
- Default engine/template systems that threaten world integrity (unrestricted free-building, unbounded flight, unrestricted terrain destruction) are removed or heavily restricted — see [1210-World-Management.md](../1200-Technical/1210-World-Management.md).
- Exploration is rewarded because every region contains intentional secrets (Pillar 1).

---

## 5. Player Experience Hierarchy

When conflicts arise, resolve them in this order:

1. Immersion and world integrity
2. Meaningful progression and choice
3. Multiplayer cooperation and social systems
4. Technical performance and stability
5. Convenience and quality-of-life

Convenience never overrides immersion or progression design.

---

## 6. Iterative but Disciplined

Prototypes and playtests are essential, especially for combat feel and talent trees.  
However, iteration happens inside a clear design frame:

- Core pillars and vision are not renegotiated every sprint.
- Balance changes are logged and justified in [0309-Balance.md](../0300-Characters/0309-Balance.md).
- Scope is controlled by the Roadmap ([0003-Roadmap.md](0003-Roadmap.md)); “nice-to-have” ideas go into [9999-Ideas.md](../9000-Future/9999-Ideas.md) or [0005-Future-Plans.md](0005-Future-Plans.md).

---

## 7. Long-Term Thinking

Elysium is designed to grow for years.

- Systems are built with expansion in mind (new continents, new classes, new professions).
- Lore seeds future content years in advance (see [9000-Future/](../9000-Future/)).
- Technical architecture supports horizontal scaling and independent instance updates ([1209-Instance-System.md](../1200-Technical/1209-Instance-System.md)).

Short-term shipping pressure never justifies architectural decisions that would make future expansions painful.

---

## 8. The Final Test

The highest praise Elysium can receive is not:

> “This is an amazing Unreal Engine server.”

It is:

> “I forgot I was playing Unreal Engine.”

Every design choice, every block placed, every line of dialogue, and every talent node should serve that outcome.
