# 0916 — Player Milestones

**Project:** Elysium MMORPG  
**Category:** Player Systems  
**Status:** Design Complete — Implementation Pending  
**Related:** [0305-Leveling.md](../0300-Characters/0305-Leveling.md) · [0905-Player-Progression.md](0905-Player-Progression.md) · [0704-Achievements.md](../0700-Quests/0704-Achievements.md) · [0917-Account-Progression.md](0917-Account-Progression.md)

---

## 1. Overview

Player Milestones are significant, one-time (or rarely repeated) achievements in a character’s or account’s life: first max level, first raid clear, first legendary, major story chapter completions, and similar moments. They are used for celebration, rewards, and long-term progression tracking.

---

## 2. Examples

- Reaching level 10 / 25 / 50
- Completing each Main Story act
- First dungeon / first Heroic / first Mythic clear
- Obtaining a Legendary or Artifact item
- Founding or joining a guild
- Major exploration thresholds

---

## 3. Design Rules

1. Milestones should feel special without interrupting flow excessively.
2. Associated rewards are modest and flavourful (titles, small cosmetics, celebration effects).
3. Milestones feed into Account Progression and achievement systems where appropriate.
4. The game acknowledges the milestone clearly (toast, journal entry, or short fanfare).

---

## 4. Technical Notes

Milestone flags are stored persistently. Unlock events can trigger UI celebrations, mail, or other systems.


---

## Additional Detail: Milestone Categories

Milestones mark significant one-time moments in a character's journey — first level cap reached, first dungeon cleared, first raid boss defeated, first Exalted reputation — each accompanied by a small in-client celebration moment (visual effect, announcement) distinct from the broader achievement system's more exhaustive tracking.

## Account-Wide Milestone History

A chronological account-wide milestone timeline lets players (and, with permission, their friends) look back on their journey through Elysium, reinforcing the sense of a personal story well told rather than just a checklist of completed tasks.
