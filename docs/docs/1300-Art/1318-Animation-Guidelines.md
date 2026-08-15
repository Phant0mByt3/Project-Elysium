# 1318 — Animation Guidelines

**Project:** Elysium MMORPG  
**Category:** Art  
**Status:** Design Complete — Implementation Pending  
**Related:** [1307-Animation-Style.md](1307-Animation-Style.md) · [0312-Character-Animations.md](../0300-Characters/0312-Character-Animations.md) · [1306-Models.md](1306-Models.md) · [1400-Development-Standards.md](../1400-Development/1400-Development-Standards.md)

---

## 1. Overview

Animation Guidelines are the practical production rules for animators and technical artists: naming, frame rates, looping standards, export settings, and review criteria that keep motion consistent and pipeline-friendly.

---

## 2. Topics

- Naming and folder conventions
- Loop and one-shot standards
- Root motion vs in-place expectations
- Hit-frame and event tagging for combat
- LOD and compression guidelines
- Review checklist against readability and style

---

## 3. Design Rules

1. Guidelines exist to reduce rework and protect combat clarity.
2. Exceptions are documented when a specific creature or cinematic requires them.
3. Pipeline changes are coordinated with Engineering and Client teams.


---

## Additional Detail: Production Standards

Animation production follows documented frame-rate, rig compatibility, and file-naming conventions to ensure consistency across a growing roster of characters and creatures produced by multiple animators over the course of a multi-year live service project.

## Motion Capture vs Hand-Keyed

Core combat and traversal animations for playable classes prioritize hand-keyed animation for maximum stylistic control and telegraph clarity, while crowd/ambient NPC animations may use motion capture or simplified procedural techniques where full bespoke animation isn't cost-effective at scale.
