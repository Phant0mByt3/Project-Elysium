# 0408 — Physics Systems

**Project:** Elysium MMORPG
**Category:** Gameplay
**Status:** Living Document
**Related:** [0400-Game-Mechanics.md](0400-Game-Mechanics.md) · [0117-Environmental-Hazards.md](../0100-World/0117-Environmental-Hazards.md)

---

## 1. Overview

Elysium uses Unreal Engine's physics systems for movement, fall damage, ragdoll death effects, and environmental interactions, tuned to support MMORPG-style combat rather than default engine physics behaviour.

## 2. Movement Physics

Player movement uses a custom character movement component tuned for responsive, server-authoritative movement that still feels smooth on the client through prediction and reconciliation (see [1202-Network.md](../1200-Technical/1202-Network.md)).

## 3. Fall Damage

Fall damage scales with fall distance beyond a safe threshold, consistent with the falling hazards described in [0117-Environmental-Hazards.md](../0100-World/0117-Environmental-Hazards.md). Certain class movement abilities (see [0400-Game-Mechanics.md](0400-Game-Mechanics.md)) grant fall damage immunity or reduction as part of their kit.

## 4. Ragdoll and Death Effects

Enemy death uses ragdoll physics for a satisfying "kill feel" on appropriate enemy types, while boss encounters use scripted death animations to preserve narrative weight rather than defaulting to ragdoll.

## 5. Environmental Physics

Destructible or physics-reactive props (breakable crates, swinging chandeliers used as environmental hazards in dungeons) are used sparingly and intentionally, primarily as boss mechanic set pieces rather than generic world clutter.

## 6. Performance Considerations

Physics simulation is budgeted per scene to avoid frame rate impact during large group fights (world bosses, raid encounters with many simultaneous players), with less critical physics effects (loose debris, cloth simulation) reduced in high player-count scenarios automatically.

## 7. Technical Ownership

Physics tuning is jointly owned by the Technical Lead and Lead Game Designer, reviewed whenever new movement abilities or environmental hazards are introduced — see [0007-Team-Structure.md](../0000-Project/0007-Team-Structure.md).
