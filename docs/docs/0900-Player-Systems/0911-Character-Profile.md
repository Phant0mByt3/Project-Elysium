# 0911 — Character Profile

**Project:** Elysium MMORPG  
**Category:** Player Systems  
**Status:** Design Complete — Implementation Pending  
**Related:** [0910-Player-Statistics.md](0910-Player-Statistics.md) · [0705-Titles.md](../0700-Quests/0705-Titles.md) · [0903-Cosmetics.md](0903-Cosmetics.md) · [0800-Guilds.md](../0800-Multiplayer/0800-Guilds.md)

---

## 1. Overview

The Character Profile is the inspectable summary of a player character: appearance, equipment, titles, selected statistics, guild, and optional bio or status. It is the primary way players learn about each other at a glance.

---

## 2. Displayed Information

- Character name, title, level, class, specialisation
- Race and faction
- Guild name and rank (if any)
- Currently equipped gear (with item levels and key stats)
- Selected achievements or showcase items
- Optional short status / roleplay text
- Privacy-controlled statistics

---

## 3. Design Rules

1. Profile should be readable in a few seconds.
2. Players control how much personal or statistical detail is public.
3. Gear and title display respect transmog and cosmetic choices.
4. Profile data is consistent whether viewed in-game or (later) via external API / companion tools.

---

## 4. Technical Notes

Profile payloads are assembled on demand from character, guild, and collection data. Caching is used for frequently inspected popular characters to reduce load.


---

## Additional Detail: Profile Customization

Players can select a profile banner, background, and featured achievements/titles to display on their public character profile, giving the profile screen a light self-expression dimension similar to a personal résumé of their Elysium journey.

## Cross-Character Account Summary

The profile system also supports an account-level summary view showing all characters on the account side by side, useful for guild recruiters or friends deciding which of a player's characters to invite for a given activity.
