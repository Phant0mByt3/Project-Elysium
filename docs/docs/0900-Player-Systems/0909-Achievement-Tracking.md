# 0909 — Achievement Tracking

**Project:** Elysium MMORPG  
**Category:** Player Systems  
**Status:** Design Complete — Implementation Pending  
**Related:** [0704-Achievements.md](../0700-Quests/0704-Achievements.md) · [0907-Collections.md](0907-Collections.md) · [0808-Leaderboards.md](../0800-Multiplayer/0808-Leaderboards.md) · [0910-Player-Statistics.md](0910-Player-Statistics.md)

---

## 1. Overview

Achievement Tracking is the system that records progress toward and completion of achievements, displays them to the player, and grants associated rewards (titles, cosmetics, points).

---

## 2. Responsibilities

- Listen for relevant gameplay events (kills, quests, exploration, social actions, etc.)
- Update progress counters and criteria
- Grant completion rewards and fire notifications
- Expose data to the Achievement UI, character profile, and leaderboards where applicable

---

## 3. Design Rules

1. Progress should be visible and understandable; hidden criteria are used sparingly and intentionally.
2. Achievements celebrate a wide range of playstyles (combat, exploration, social, collection, mastery).
3. Point totals and rare achievements feed prestige without becoming a pure score chase that dominates the game.
4. Account-wide vs character-specific achievements are clearly marked.

---

## 4. Technical Notes

Achievement state is stored authoritatively on the server. Criteria evaluation is event-driven and efficient enough to run at scale. Client receives progress updates and completion events for UI and toasts.
