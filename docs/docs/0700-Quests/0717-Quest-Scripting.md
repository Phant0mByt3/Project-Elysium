# 0717 — Quest Scripting

**Project:** Elysium MMORPG  
**Category:** Quests  
**Status:** Design Complete — Implementation Pending  
**Related:** [0700-Quests.md](0700-Quests.md) · [0210-Dialogue-System.md](../0200-Lore/0210-Dialogue-System.md) · [1200-Plugin-Architecture.md](../1200-Technical/1200-Plugin-Architecture.md) · [1403-Quest-Writing-Guide.md](../1400-Development/1403-Quest-Writing-Guide.md)

---

## 1. Overview

Quest scripting is the technical layer that turns quest design documents into runnable content: objective tracking, dialogue triggers, branching logic, cinematic starts, reward grants, and world-state changes.

---

## 2. Goals

- Allow content designers to implement the majority of quests without writing low-level Java code.
- Keep quest logic data-driven and hot-reloadable where possible.
- Ensure all critical outcomes (progress, rewards, flags) are server-authoritative.
- Support the dialogue, branch, and cinematic systems already defined.

---

## 3. Script Responsibilities

- Accept / decline / complete / abandon handling
- Objective progress (kills, collects, interacts, location reaches)
- Conditional visibility and availability (level, quest flags, reputation, faction)
- Dialogue tree triggers and branch recording
- Spawning / despawning of temporary NPCs or objects
- Starting cinematics or scripted sequences
- Granting rewards and setting persistent flags

---

## 4. Design Rules

1. Scripts should be readable and maintainable by the narrative and design teams with support from engineering.
2. Side effects that alter the permanent world (beyond temporary event props) require explicit design approval.
3. Error handling must prevent quests from becoming permanently stuck; recovery paths or GM tools exist for edge cases.

---

## 5. Technical Notes

The quest scripting runtime lives inside the modular plugin architecture. Quest definitions and scripts are versioned assets loaded by the server. See [1200-Plugin-Architecture.md](../1200-Technical/1200-Plugin-Architecture.md) for ownership boundaries.
