# 102 — Vendors

## Overview
NPC vendors provide a baseline, always-available marketplace independent of player supply — selling reagents, basic gear, repair services, and recipes.

## Vendor Types
* **General Goods Vendors** — basic consumables, repair services, found in every city and village ([0103-Cities.md](../0100-World/0103-Cities.md), [0104-Villages.md](../0100-World/0104-Villages.md)).
* **Class Trainers** — teach new skills as characters level ([0302-Skills.md](../0300-Characters/0302-Skills.md)); functionally vendors of ability unlocks rather than items.
* **Profession Trainers & Recipe Vendors** — teach profession recipes ([0600-Professions.md](../0600-Professions/0600-Professions.md)).
* **Reputation Quartermasters** — faction/reputation-gated vendors selling tier-exclusive rewards ([0706-Reputation.md](../0700-Quests/0706-Reputation.md), [0707-Factions-Reputation.md](../0700-Quests/0707-Factions-Reputation.md)).
* **Sundered Shard Vendors** — endgame catch-up gear and cosmetics ([1001-Currency.md](1001-Currency.md)).

## Design Rules
Vendor stock and prices should never directly undercut the player economy's Auction House ([1003-Auction-House.md](1003-Auction-House.md)) for tradeable goods — vendors exist as a reliability floor, not a replacement for player trading.
