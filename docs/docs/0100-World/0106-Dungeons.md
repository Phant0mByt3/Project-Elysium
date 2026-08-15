# 0106 — Dungeons

**Category:** World
**Status:** Living Document
**Related:** [0107-Raids.md](0107-Raids.md) · [0803-Dungeon-Finder.md](../0800-Multiplayer/0803-Dungeon-Finder.md) · [0504-Loot-Tables.md](../0500-Items/0504-Loot-Tables.md)

---

## 1. Overview

Dungeons are instanced, 5-player group content forming the primary mid-level progression loop between questing and raiding ([0107-Raids.md](0107-Raids.md)). Each dungeon is entered via a hand-built portal or entrance in the open world and queued into via the Dungeon Finder ([0803-Dungeon-Finder.md](../0800-Multiplayer/0803-Dungeon-Finder.md)).

## 2. Structure

Every dungeon should contain:

* **2–4 bosses**, each with at least one unique mechanic beyond "high damage."
* **A short framing narrative** connecting it to the region's local conflict or main story.
* **Trash pulls** with intentional pull paths, not open-field mob soup.
* **A loot table** tuned to the dungeon's level range ([0504-Loot-Tables.md](../0500-Items/0504-Loot-Tables.md)).
* **An estimated clear time** of 25–45 minutes at intended gear level.

## 3. Difficulty Modes

* **Normal** — tuned for the dungeon's intended level range while leveling.
* **Heroic** — max-level, group-finder-eligible, higher difficulty and better loot.
* **Mythic** — small guild/premade-only, hardest tuning, best pre-raid gear.

## 4. Launch Dungeon List (Aurelia & Vethmoor)

| Dungeon | Region | Level Range | Theme |
| --- | --- | --- | --- |
| The Hollow Root | Wildwood Reach | 12–16 | Corrupted forest spirit |
| The Drowned Chapel | Greywater Fens | 18–22 | Undead cult |
| The Ember Foundry | Ember Deeps | 30–36 | Rogue forge-construct uprising |
| Ashenclaw Den | Ashenclaw Tundra | 38–44 | Orc warband trial |

## 5. Dungeon Design Detail

### The Hollow Root
A corrupted grove beneath Wildwood Reach where a once-benevolent forest spirit has been twisted by lingering Sundering energy. Three bosses culminate in the corrupted spirit itself, whose fight alternates between a ranged "corruption bloom" phase and a melee "root lash" phase, teaching players to react to visual telegraphs early.

### The Drowned Chapel
A sunken chapel beneath the Greywater Fens, overrun by a cult attempting to resurrect a pre-Sundering saint as an undead thrall. Bosses include cult acolytes, a possessed choir encounter with sound-based mechanics, and the cult leader as the final boss.

### The Ember Foundry
Dwarven forge-constructs, originally built for mining, have gone rogue under Ember Deeps' unstable heat conditions. Mechanical bosses emphasize positioning around environmental hazards (lava vents, heat zones — see [0117-Environmental-Hazards.md](0117-Environmental-Hazards.md)).

### Ashenclaw Den
A trial ground used by orc warbands to test new warriors; players fight through escalating trial encounters culminating in a warband champion duel, reinforcing Duskward Pact combat culture.

## 6. Post-Launch Dungeon Expansion

New dungeons ship with each region added post-launch (see [0101-Continents.md](0101-Continents.md)), maintaining roughly one dungeon per two regions to keep the leveling path populated with group content options.

## 7. Design Ownership

Dungeon encounters are jointly owned by the World Director (layout, theme) and Lead Game Designer (boss mechanics, balance) per [0007-Team-Structure.md](../0000-Project/0007-Team-Structure.md), and must pass a dedicated encounter-design review before entering the loot table balance pass.
