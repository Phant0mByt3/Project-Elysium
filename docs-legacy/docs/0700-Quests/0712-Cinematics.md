# 0712 — Cinematics

**Project:** Elysium MMORPG  
**Category:** Quests  
**Status:** Design Complete — Implementation Pending  
**Related:** [0207-Main-Story.md](../0200-Lore/0207-Main-Story.md) · [0708-Main-Quest.md](0708-Main-Quest.md) · [1112-Cutscenes.md](../1100-Client/1112-Cutscenes.md) · [1309-Cinematics.md](../1300-Art/1309-Cinematics.md)

---

## 1. Overview

Cinematics (in-engine cutscenes and scripted sequences) are used sparingly to highlight major story moments, introduce key NPCs or locations, and give emotional punctuation to the Main Quest and important side stories.

---

## 2. Usage Guidelines

- Reserved for chapter openings/closings, major revelations, and the lead-in to significant encounters (e.g. the approach to the Sunken Concord).
- Length is kept short so that players remain in control of pacing.
- Players can usually skip a cinematic after the first viewing (or always, depending on final accessibility settings).
- Cinematics never contain critical mechanical information that is not also available through quest text or NPC dialogue.

---

## 3. Production

Cinematics are authored using the client’s cutscene tools and custom animations/cameras. They are triggered by quest scripts ([0717-Quest-Scripting.md](0717-Quest-Scripting.md)) and play for the relevant players in the instance.

---

## 4. Design Rules

1. Spectacle serves story, not the other way around.
2. Every cinematic should leave the player with a clearer sense of character, place, or stakes.
3. Technical performance targets still apply; cinematics must not tank frame rate on minimum-spec hardware.
