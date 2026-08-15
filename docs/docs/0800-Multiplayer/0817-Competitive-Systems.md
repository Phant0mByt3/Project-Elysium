# 0817 — Competitive Systems

**Project:** Elysium MMORPG  
**Category:** Multiplayer  
**Status:** Design Complete — Implementation Pending  
**Related:** [0804-PvP.md](0804-PvP.md) · [0805-Arenas.md](0805-Arenas.md) · [0808-Leaderboards.md](0808-Leaderboards.md) · [0807-Seasons.md](0807-Seasons.md) · [0802-Raiding.md](0802-Raiding.md)

---

## 1. Overview

Competitive Systems are the formal structures that turn skill expression into ranked progression, seasonal rewards, and public recognition. They cover both PvP (arenas, rated battlegrounds if added) and high-end PvE (Mythic raid racing, optional speed clears).

---

## 2. Pillars

| Pillar | Description |
|--------|-------------|
| **Rated Matchmaking** | Skill-based brackets with visible rating |
| **Seasonal Structure** | Clear start/end, reward tracks, title distribution |
| **Leaderboards & Prestige** | Public rankings and exclusive cosmetics/titles |
| **Fairness & Integrity** | Anti-cheat, decay, and smurf/boost detection |

---

## 3. Design Rules

1. Competitive play is opt-in; the rest of the game remains fully playable and rewarding without it.
2. Seasons give returning and new players regular fresh starts.
3. Rewards emphasise cosmetics, titles, and prestige over raw power that would create permanent pay-or-win gaps.
4. Balance and tuning for competitive brackets are tracked separately where necessary (see [0309-Balance.md](../0300-Characters/0309-Balance.md)).

---

## 4. Technical Notes

Rating calculations, matchmaking queues, and seasonal reward grants are handled by dedicated services that sit alongside the core gameplay servers. All outcomes that affect rating or rewards are server-authoritative.


## 5. Mythic Raid Racing

At the start of each new raid tier, a brief "race" period sees top guilds compete for world-first clears, tracked publicly through the leaderboard system ([0808-Leaderboards.md](0808-Leaderboards.md)) and celebrated through community-facing recognition, without affecting the raid's accessibility for the broader playerbase once the race period ends.

## 6. Integrity Systems

Rating decay for inactive players, smurf-account detection, and boosting-service detection are all handled through dedicated backend monitoring, ensuring competitive rankings remain a meaningful signal of actual skill over time.
