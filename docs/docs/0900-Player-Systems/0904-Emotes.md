# 0904 — Emotes

**Category:** Player Systems
**Status:** Living Document
**Related:** [0903-Cosmetics.md](0903-Cosmetics.md) · [0204-Races.md](../0200-Lore/0204-Races.md)

---

## 1. Overview

Emotes are player-triggered animations and (where applicable) sound effects used for social expression and roleplay, reinforcing the game's identity as a persistent social world (Pillar 4, [0002-Core-Pillars.md](../0000-Project/0002-Core-Pillars.md)).

## 2. Categories

* **Basic Emotes** — available to all characters from the start (wave, sit, dance, bow, laugh).
* **Racial Emotes** — unique to each playable race ([0204-Races.md](../0200-Lore/0204-Races.md)), reinforcing racial identity and culture.
* **Class Emotes** — flavor animations tied to a character's class identity ([0300-Classes.md](../0300-Characters/0300-Classes.md)), such as an Arcanist's idle spell-weaving animation.
* **Unlockable Emotes** — earned through achievements ([0704-Achievements.md](../0700-Quests/0704-Achievements.md)), seasonal events ([0807-Seasons.md](../0800-Multiplayer/0807-Seasons.md)), or rare drops.

## 3. Design Rules

* Emotes should never be usable in a way that disrupts combat or grants any gameplay advantage.
* Racial emotes should be written and animated with input from the lore team to stay consistent with each race's culture as described in [0204-Races.md](../0200-Lore/0204-Races.md).

## 4. Text and Chat Bubble Integration

Emotes generate an appropriate chat bubble and system message (e.g. "[Name] waves at [Target]"), giving them social legibility even for players who may have muted animation effects for performance reasons.

## 5. Group Emotes

A small set of emotes support a second participant (a handshake, a duel bow), triggering a synchronized animation between two consenting players, adding a light roleplay and social bonding tool.

## 6. Technical Notes

Emote definitions (animation, sound, chat bubble text) are a client-side responsibility — see [1101-Client-Modules.md](../1100-Client/1101-Client-Modules.md).
