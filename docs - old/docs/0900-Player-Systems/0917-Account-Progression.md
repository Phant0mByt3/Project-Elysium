# 0917 — Account Progression

**Project:** Elysium MMORPG  
**Category:** Player Systems  
**Status:** Design Complete — Implementation Pending  
**Related:** [0905-Player-Progression.md](0905-Player-Progression.md) · [0907-Collections.md](0907-Collections.md) · [0916-Player-Milestones.md](0916-Player-Milestones.md) · [0807-Seasons.md](../0800-Multiplayer/0807-Seasons.md)

---

## 1. Overview

Account Progression captures long-term, cross-character growth: collection unlocks, certain achievements, seasonal reward tracks, and other benefits that persist regardless of which character the player is currently playing. It rewards the player for investing time in Elysium as a whole.

---

## 2. Components

| Component | Description |
|-----------|-------------|
| **Collections** | Mounts, pets, appearances, toys, etc. |
| **Account Achievements** | Selected achievements that count once per account |
| **Seasonal Tracks** | Battle-pass style or simple reward tracks that reset periodically |
| **Shared Unlocks** | Heirlooms, certain convenience items, or account-wide perks |
| **Milestone Record** | Major firsts and lifetime statistics |

---

## 3. Design Rules

1. Account Progression never replaces character progression; both exist in parallel.
2. Power tied to account progression is carefully limited so that new characters still have a meaningful journey.
3. Collection and cosmetic rewards are the primary long-term currency of account progression.
4. Players can see their account-wide progress from any character.

---

## 4. Technical Notes

Account-level data is stored against the account record and is available to every character on that account. Systems that grant account unlocks emit events that the collection and achievement services consume.
