# 0808 — Leaderboards

**Project:** Elysium MMORPG  
**Category:** Multiplayer  
**Status:** Design Complete — Implementation Pending  
**Related:** [0805-Arenas.md](0805-Arenas.md) · [0807-Seasons.md](0807-Seasons.md) · [0802-Raiding.md](0802-Raiding.md) · [0704-Achievements.md](../0700-Quests/0704-Achievements.md)

---

## 1. Overview

Leaderboards surface competitive and prestige rankings across PvP, PvE, and selected progression metrics. They exist to give high-performing players visibility and to give the wider community targets and heroes to follow, without making every system a pure ranking treadmill.

---

## 2. Leaderboard Categories

| Category | Examples | Reset |
|----------|----------|-------|
| **Arena / Rated PvP** | 2v2, 3v3, Solo Shuffle-style ratings | Seasonal |
| **Raid Progression** | First kills, speed clears (optional) | Per tier / seasonal |
| **World / Region** | World boss participation, exploration metrics | Soft / ongoing |
| **Profession / Economic** | Optional craft or market rankings | Seasonal or none |
| **Achievement / Collection** | Points, rare unlocks | Ongoing |

---

## 3. Design Rules

1. Leaderboards should celebrate skill and dedication without shaming the majority of players who will never appear on them.
2. Rankings that affect rewards are seasonal so that new players and returning players have a fair window.
3. Exploits or boost-style ranking inflation are actively monitored and corrected (see Anti-Cheat and economy monitoring).
4. Players can opt out of public display where privacy is a concern.

---

## 4. Technical Notes

Leaderboard data is aggregated from authoritative server events and stored in a queryable form for the client UI and any external API. Updates are near-real-time for active brackets and batched for less critical boards.
