# 0405 — Aggro System

**Project:** Elysium MMORPG
**Category:** Gameplay
**Status:** Living Document
**Related:** [0404-AI-Behaviour.md](0404-AI-Behaviour.md) · [0401-Combat.md](0401-Combat.md)

---

## 1. Overview

The aggro (threat) system determines which player an enemy targets during combat, forming the mechanical foundation of the tank role described in [0401-Combat.md](0401-Combat.md).

## 2. Threat Generation

* Damage dealt generates threat proportional to the damage amount.
* Healing generates threat split among the healed targets' current threat standing.
* Tank-specific abilities generate bonus threat beyond their raw damage/healing value, allowing tanks to establish and hold aggro efficiently.

## 3. Threat Tables

Each enemy maintains a threat table tracking accumulated threat per player. The enemy targets whichever player holds the highest threat value, switching targets if another player's threat exceeds the current target's by a defined margin (a "threat leash"), preventing erratic target-switching from minor threat fluctuations.

## 4. Tank Tools

Tank classes (Vanguard, Oathkeeper, Warden in tank specialization) have access to taunt abilities that force an immediate threat table update, useful for picking up loose adds or correcting a mispull.

## 5. Non-Combat and Solo Play

Outside of group content, threat mechanics still apply but are largely invisible to a solo player, since there's only one possible target. The system's complexity becomes relevant primarily in dungeons, raids, and world boss encounters with multiple participants.

## 6. Design Rationale

An explicit threat system (rather than pure "last hit" or "closest player" targeting) gives group content structure and a clear tank role, directly supporting the cooperative multiplayer pillar in [0002-Core-Pillars.md](../0000-Project/0002-Core-Pillars.md).

## 7. Tuning and Iteration

Threat generation values are tuned alongside general combat balance, reviewed under the same cadence described in [0309-Balance.md](../0300-Characters/0309-Balance.md).
