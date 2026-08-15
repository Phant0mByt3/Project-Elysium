# 0908 — Journals

**Project:** Elysium MMORPG  
**Category:** Player Systems  
**Status:** Design Complete — Implementation Pending  
**Related:** [0200-Lore.md](../0200-Lore/0200-Lore.md) · [0105-Landmarks.md](../0100-World/0105-Landmarks.md) · [0704-Achievements.md](../0700-Quests/0704-Achievements.md) · [0907-Collections.md](0907-Collections.md)

---

## 1. Overview

Journals are in-game codex-style records that collect discovered lore, bestiary entries, region descriptions, and personal adventure notes. They reward exploration and curiosity and give players a readable history of what they have learned about Elysium.

---

## 2. Journal Sections

| Section | Content |
|---------|---------|
| **Lore & History** | Fragments from landmarks, books, and quests |
| **Bestiary** | Defeated or observed creature types |
| **Regions & Places** | Discovered zones, cities, and notable locations |
| **Characters** | Important NPCs the player has met |
| **Personal Log** | Optional player-facing summary of major story beats completed |

---

## 3. Design Rules

1. Entries are unlocked by gameplay (exploration, combat, quests), not purchased.
2. Journals never gate critical progression; they are pure enrichment.
3. Writing stays consistent with the tone and canon of the lore documents.
4. The UI supports reading at the player’s own pace and revisiting old entries.

---

## 4. Technical Notes

Unlock flags are stored on the character or account. Content text is data-driven and can be updated without client patches where appropriate.


---

## Additional Detail: Lore Journal Integration

Journals surface discovered lore items (books, murals, inscriptions found via [0105-Landmarks.md](../0100-World/0105-Landmarks.md)) in a readable, searchable in-client library, letting lore-focused players revisit discovered content without needing external wikis.

## Chronological Organization

Entries are automatically sorted along the world's timeline ([0201-Timeline.md](../0200-Lore/0201-Timeline.md)), helping players build a coherent mental model of Elysium's history as they piece together fragments discovered in different regions and in a non-linear order.
