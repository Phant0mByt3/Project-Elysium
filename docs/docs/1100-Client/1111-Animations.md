# 1111 — Animations

**Project:** Elysium MMORPG  
**Category:** Client  
**Status:** Design Complete — Implementation Pending  
**Related:** [0312-Character-Animations.md](../0300-Characters/0312-Character-Animations.md) · [1307-Animation-Style.md](../1300-Art/1307-Animation-Style.md) · [1103-Custom-Models.md](1103-Custom-Models.md) · [0401-Combat.md](../0400-Gameplay/0401-Combat.md)

---

## 1. Overview

This document covers the client-side presentation and technical handling of animations: how animation data is packaged, played, blended, and prioritised on the player’s machine. Design intent for character and combat animation lives primarily in the Characters and Art documents; this file focuses on client implementation concerns.

---

## 2. Responsibilities

- Playback of locomotion, combat, emote, and cinematic animations
- Blending and layering (upper body vs lower body, additive hits, etc.)
- LOD and simplification for distant or numerous entities
- Synchronisation with server-authoritative state (attack moments, ability releases)

---

## 3. Design Rules

1. Combat readability takes priority over pure spectacle when the two conflict.
2. Animation budgets respect the performance targets in [1113-Client-Optimisation.md](1113-Client-Optimisation.md) and [1208-Performance.md](../1200-Technical/1208-Performance.md).
3. Client prediction is used for responsiveness, but final authority on combat outcomes remains with the server.

---

## 4. Technical Notes

Animation assets are delivered via the content pack and custom model pipeline. The client animation system integrates with native gameplay module hooks and any custom rendering layers required for Elysium’s visual identity.
