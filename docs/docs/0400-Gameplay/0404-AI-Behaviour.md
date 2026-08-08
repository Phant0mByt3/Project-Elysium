# 0404 — AI Behaviour

**Project:** Elysium MMORPG  
**Category:** Gameplay  
**Status:** Design Complete — Implementation Pending  
**Related:** [0402-Enemy-Design.md](0402-Enemy-Design.md) · [0405-Aggro-System.md](0405-Aggro-System.md) · [0401-Combat.md](0401-Combat.md) · [1200-Plugin-Architecture.md](../1200-Technical/1200-Plugin-Architecture.md)

---

## 1. Overview

Enemy AI in Elysium is built from reusable behaviour modules rather than one-off scripts for every creature. This keeps implementation consistent and makes it easier to tune packs and bosses across regions.

---

## 2. Core Behaviour Modules

| Module | Description |
|--------|-------------|
| **Idle / Patrol** | Default non-combat movement and ambient actions |
| **Acquire Target** | How the AI selects its first and subsequent targets (see Aggro) |
| **Melee Attack Loop** | Basic weapon or claw attacks with optional specials on cooldown |
| **Ranged / Caster Loop** | Projectile or spell casts with positioning preferences |
| **Special Ability** | Signature mechanic with telegraph and cooldown |
| **Flee / Reset** | Leash and reset behaviour when players leave the engagement zone |
| **Call for Help** | Optional social aggro that pulls nearby allies |

Bosses extend these modules with phase-specific overrides and custom state machines.

---

## 3. Design Rules

1. AI should feel purposeful, not random. Every action should have a readable reason.
2. Pathing must respect the handcrafted geometry of dungeons and open-world spaces; AI should not clip through intentional barriers.
3. Group AI (packs) should create interesting decision points for players (interrupt priority, kill order, positioning) without requiring perfect play on Normal difficulty.
4. AI never cheats on information the player could not reasonably have; telegraphs exist for a reason.

---

## 4. Performance Considerations

AI server tick rate and pathfinding complexity are budgeted against the performance targets in [1208-Performance.md](../1200-Technical/1208-Performance.md). Large open-world packs use simplified logic compared with dungeon and raid encounters.

---

## 5. Technical Notes

Behaviour trees / state machines live in the combat plugin data layer. All targeting, movement, and ability decisions are evaluated server-side. Clients only receive the resulting animation and effect packets.
