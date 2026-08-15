# 1307 — Animation Style

**Project:** Elysium MMORPG  
**Category:** Art  
**Status:** Design Complete — Implementation Pending  
**Related:** [1300-Art-Style.md](1300-Art-Style.md) · [0312-Character-Animations.md](../0300-Characters/0312-Character-Animations.md) · [1318-Animation-Guidelines.md](1318-Animation-Guidelines.md) · [0401-Combat.md](../0400-Gameplay/0401-Combat.md)

---

## 1. Overview

Animation Style defines the motion language of Elysium: weight, timing, exaggeration, and readability. It ensures that characters, creatures, and effects feel cohesive and that combat telegraphs remain clear.

---

## 2. Principles

- **Readable first** — combat animations prioritise clear wind-ups and impacts over pure realism.
- **Weight and material** — heavy armour and large creatures move with appropriate inertia; light and agile characters feel quicker.
- **Class identity** — each class has a recognisable motion signature.
- **Grounded fantasy** — motion supports the high-fantasy tone without sliding into pure cartoon or pure simulation.

---

## 3. Application

Applies to player characters, NPCs, creatures, environmental motion, and cinematic performances. Detailed production rules live in [1318-Animation-Guidelines.md](1318-Animation-Guidelines.md).


---

## 4. Combat Telegraph Timing

Wind-up animations for dangerous abilities are timed to give players a consistent, learnable reaction window across all enemy types, directly supporting the "readable, learnable patterns" goal in [0404-AI-Behaviour.md](../0400-Gameplay/0404-AI-Behaviour.md).

## 5. Idle and Traversal Variety

Beyond combat, each race and class has distinct idle fidget and traversal animations (walk, run, jump) reinforcing personality and identity even outside of combat, avoiding the "generic humanoid" feeling common when animation budgets are stretched thin across many character types.
