# 0714 — Quest Branches

**Project:** Elysium MMORPG  
**Category:** Quests  
**Status:** Design Complete — Implementation Pending  
**Related:** [0700-Quests.md](0700-Quests.md) · [0210-Dialogue-System.md](../0200-Lore/0210-Dialogue-System.md) · [0208-Side-Stories.md](../0200-Lore/0208-Side-Stories.md) · [0707-Factions-Reputation.md](0707-Factions-Reputation.md)

---

## 1. Overview

Quest branches are points where player choice (dialogue, faction, previous actions, or explicit decisions) changes the subsequent steps, rewards, or narrative outcome of a quest or chain. Branches add replay value and roleplaying weight without exploding content production costs.

---

## 2. Branch Types

| Type | Description |
|------|-------------|
| **Dialogue Choice** | Immediate different response or small outcome difference |
| **Faction Branch** | Different quest givers, framing, or rewards based on Concord vs Pact |
| **Reputation / Prior Choice** | Access or tone changes based on earlier decisions or rep level |
| **Ending Branch** | Distinct conclusions to a side story (e.g. peaceful vs confrontational resolution) |

---

## 3. Design Rules

1. Branches must be meaningful enough to notice but not so divergent that they require entirely separate content pipelines for every path.
2. The Main Quest uses light branching (flavour and framing) rather than mutually exclusive critical paths.
3. Side stories are the primary home for more significant branches and alternate endings.
4. Players should be able to understand the consequences of a choice at the moment they make it, or shortly afterward.

---

## 4. Technical Notes

Branch state is stored on the character’s quest progress record. Subsequent quest availability and dialogue options query this state. See [0717-Quest-Scripting.md](0717-Quest-Scripting.md).
