# 0403 — Boss Mechanics

**Project:** Elysium MMORPG  
**Category:** Gameplay  
**Status:** Design Complete — Implementation Pending  
**Related:** [0401-Combat.md](0401-Combat.md) · [0402-Enemy-Design.md](0402-Enemy-Design.md) · [0106-Dungeons.md](../0100-World/0106-Dungeons.md) · [0107-Raids.md](../0100-World/0107-Raids.md) · [0306-Status-Effects.md](../0300-Characters/0306-Status-Effects.md)

---

## 1. Overview

Boss encounters are the highlight of group content. Every boss must have a clear **mechanic identity** — a phrase players can use to describe it in one sentence (e.g. “the boss that splits into three”, “the one that forces you to spread then stack”).

---

## 2. Design Requirements

Every boss (dungeon or raid) must include:

- At least one unique, non-generic mechanic beyond “hits hard”.
- Clear visual and audio telegraphs for every high-damage or lethal ability.
- A framing narrative that ties the encounter to the region or main story.
- Distinct phases or escalating behaviour so the fight changes over time.
- Loot table tuned to the content tier ([0504-Loot-Tables.md](../0500-Items/0504-Loot-Tables.md)).

---

## 3. Difficulty Tiers

| Tier | Tuning Philosophy | Audience |
|------|-------------------|----------|
| **Normal** | Learn the fight; forgiving mistakes | Leveling / first clear |
| **Heroic** | Requires coordination and correct execution | Max-level group finder |
| **Mythic** | Precise execution, limited margin for error | Organised guild groups |

Mythic may include additional mechanics or stricter enrage timers that do not appear on lower difficulties.

---

## 4. Common Mechanic Families

- Positioning (spread, stack, safe zones, dance floors)
- Adds / prioritisation
- Resource management (boss energy, player debuffs that must be cleansed or passed)
- Phase transitions triggered by health or time
- Soft enrages that escalate pressure rather than hard wipe timers (preferred where possible)

---

## 5. Telegraphs & Fairness

All lethal or near-lethal abilities must be telegraphed with enough time for a reasonably attentive player to react. “Gotcha” one-shots with no warning are forbidden. Visual clarity takes priority over spectacle when the two conflict (see [1300-Art-Style.md](../1300-Art/1300-Art-Style.md) and combat readability goals).

---

## 6. Technical Notes

Boss state machines and mechanic scripts are owned by the combat/encounter plugin. All critical timing and damage is server-authoritative. Client effects are cosmetic only.
