# 0510 — Item Rarity

**Project:** Elysium MMORPG  
**Category:** Items  
**Status:** Design Complete — Implementation Pending  
**Related:** [0503-Loot.md](0503-Loot.md) · [0504-Loot-Tables.md](0504-Loot-Tables.md) · [0505-Legendary-Items.md](0505-Legendary-Items.md) · [1302-Colour-Palette.md](../1300-Art/1302-Colour-Palette.md)

---

## 1. Overview

Item rarity communicates power, exclusivity, and visual prestige. The colour language is consistent across tooltips, nameplates, loot streams, and the Auction House.

---

## 2. Rarity Tiers

| Rarity | Colour | Typical Sources | Notes |
|--------|--------|-----------------|-------|
| **Common** | White | Vendors, early quests, basic drops | Functional but unremarkable |
| **Uncommon** | Green | Quest rewards, trash & elite drops | First meaningful upgrades |
| **Rare** | Blue | Dungeon bosses, higher elites, profession crafts | Solid mid-game gear |
| **Epic** | Purple | Heroic dungeon / raid bosses, high-end crafts | Strong endgame baseline |
| **Legendary** | Orange | Specific raid encounters, long quest chains, rare world drops | Named items with unique effects — see [0505-Legendary-Items.md](0505-Legendary-Items.md) |
| **Relic** | Gold | Extremely rare, often tied to gods or ancient history | See [0506-Relics.md](0506-Relics.md) |

---

## 3. Design Rules

1. Higher rarity must feel meaningfully better, not just statistically denser.
2. Legendary and Relic items carry unique mechanics or strong fantasy; they are never pure stat sticks.
3. Colour coding must remain colourblind-safe (additional icons or patterns where necessary — see Accessibility).
4. Rarity is fixed on the item; it does not change through upgrading (upgrading improves power within the same rarity or moves the item to a higher tier only through specific systems).

---

## 4. Visual & UI Impact

Rarity determines border colour, tooltip header treatment, loot toast styling, and name colour in chat and the Auction House. The palette is defined in [1302-Colour-Palette.md](../1300-Art/1302-Colour-Palette.md).


---

## 5. Rarity and the Leveling Curve

Uncommon and Rare items dominate the leveling experience, with Epic items becoming common only at max-level dungeon and raid content. This keeps rarity feeling special throughout the leveling journey rather than being trivialized by level 20.

## 6. Rarity Across Content Types

| Content | Typical Rarity Ceiling |
| --- | --- |
| Leveling quests | Uncommon, occasional Rare |
| Normal dungeons | Rare |
| Heroic dungeons | Rare to Epic |
| Raids (Normal/Heroic) | Epic |
| Raids (Mythic) | Epic, with Legendary/Relic chance |

## 7. Cross-System Consistency

Rarity colour and naming conventions are shared across items, mounts, pets, and titles ([0900-Player-Systems/](../0900-Player-Systems/)) so players learn the color language once and can apply it across every collection system in the game.
