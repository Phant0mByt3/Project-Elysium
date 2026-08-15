# 0910 — Player Statistics

**Project:** Elysium MMORPG  
**Category:** Player Systems  
**Status:** Design Complete — Implementation Pending  
**Related:** [0911-Character-Profile.md](0911-Character-Profile.md) · [0909-Achievement-Tracking.md](0909-Achievement-Tracking.md) · [0401-Combat.md](../0400-Gameplay/0401-Combat.md) · [1205-API.md](../1200-Technical/1205-API.md)

---

## 1. Overview

Player Statistics are the recorded metrics of a character’s (and sometimes account’s) activity: kills, deaths, damage, healing, exploration, crafting counts, and similar numbers. They feed the character profile, certain achievements, and optional external tools.

---

## 2. Categories

| Category | Examples |
|----------|----------|
| **Combat** | Enemies slain, deaths, damage dealt/taken, healing done |
| **PvP** | Honorable kills, arena matches, rating highs |
| **Exploration** | Zones discovered, landmarks found, distance traveled |
| **Crafting / Gathering** | Items crafted, nodes gathered |
| **Social / Misc** | Emotes used, friends made, guild tenure |

---

## 3. Design Rules

1. Statistics are primarily for personal interest and achievement criteria; they are not a competitive ranking system by themselves.
2. Players can view their own stats easily; public visibility is controlled by privacy settings.
3. Tracking is efficient and does not impact combat performance.

---

## 4. Technical Notes

Stats are incremented via server-side events and stored in a form suitable for both real-time display and periodic aggregation. Sensitive or high-frequency combat stats may be sampled or summarised rather than stored in full detail indefinitely.


---

## Additional Detail: Statistic Categories

Tracked statistics span combat (total damage dealt, bosses defeated), exploration (distance traveled, landmarks found), economy (Aurum earned, items crafted), and social (dungeons run with friends, guild events attended), giving players a rich personal history of their time in Elysium.

## Privacy and Display

Players control which statistics are visible to others via their profile privacy settings ([0911-Character-Profile.md](0911-Character-Profile.md)), ensuring statistics tracking feels like a personal record-keeping tool rather than an exposed surveillance feature.
