# 0711 — Quest Rewards

**Project:** Elysium MMORPG  
**Category:** Quests  
**Status:** Design Complete — Implementation Pending  
**Related:** [0700-Quests.md](0700-Quests.md) · [0503-Loot.md](../0500-Items/0503-Loot.md) · [1001-Currency.md](../1000-Economy/1001-Currency.md) · [0706-Reputation.md](0706-Reputation.md)

---

## 1. Overview

Quest rewards are the primary early- and mid-game source of experience, currency, and gear. They are tuned so that a player following the available quests in a region arrives at the next region at an appropriate level and with competitive equipment.

---

## 2. Reward Types

| Type | Notes |
|------|-------|
| **Experience** | Primary leveling driver through the 1–30 range |
| **Aurum** | Soft currency; steady income for repairs, training, and small purchases |
| **Gear** | Often a choice of items appropriate to the player’s level and armour type |
| **Reputation** | Toward relevant factions or organisations |
| **Items / Consumables** | Potions, food, reagents, or unique quest items |
| **Cosmetics / Unlocks** | Occasional appearances, emotes, or titles |
| **Recipes / Knowledge** | Profession or lore unlocks |

---

## 3. Design Rules

1. Rewards should feel commensurate with the effort and narrative weight of the quest.
2. Gear rewards offer meaningful choices rather than a single “best” item for every class.
3. Main Quest rewards are slightly stronger or more iconic than average side-quest rewards at the same level.
4. Repeatable content (dailies, weeklies) uses different reward profiles focused on reputation, currency, and endgame resources rather than pure experience.

---

## 4. Technical Notes

Reward packages are defined in quest data. Granting is transactional and server-authoritative; the client only displays the offer and confirmation.


## 5. Reward Choice Presentation

When a quest offers a choice of item rewards, options are filtered to the player's class and, where reasonably inferable, their current specialization, reducing the historical MMORPG friction of choosing between four items only one of which is remotely usable.

## 6. Catch-Up Rewards

Quests completed significantly below a player's current level (via twinking or backtracking) scale down experience appropriately but retain full currency and reputation value, discouraging power-leveling exploits without punishing players revisiting old content for completionist reasons.
