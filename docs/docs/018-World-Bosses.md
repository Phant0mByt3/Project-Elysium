# 18 — World Bosses

World bosses are powerful, open-world enemies that spawn on a timer or by trigger, encouraging spontaneous large-group cooperation outside of instanced content — supporting Pillar 4 in [002-Core-Pillars.md](002-Core-Pillars.md).

## Design Rules
* Tuned for 10–40 players depending on level range; scale down gracefully for smaller raids.
* Always tied to regional lore, never a generic "big monster."
* Drop guaranteed region-appropriate loot plus a chance at a unique cosmetic or mount (see [091-Mounts.md](091-Mounts.md)).
* Compete for tagging fairly across factions — see [084-PvP.md](084-PvP.md) for contested-tag rules where Concord and Pact players meet at the same spawn.

## Launch World Bosses

**Grothmar, the Root-Warden** *(Wildwood Reach, Level 14)* — the corrupted forest spirit behind [016-Dungeons.md](016-Dungeons.md)'s Hollow Root dungeon has an open-world counterpart that occasionally breaks free of the dungeon's seal.

**The Ashen Colossus** *(Ashenclaw Tundra, Level 40)* — an animated construct from the pre-Sundering era, awoken by orc clan excavation efforts. Central to a regional questline about whether to destroy or study it.

**Maelith's Herald** *(coastal Aurelia, Level 22)* — a storm elemental tied to the goddess Maelithir ([032-Gods.md](032-Gods.md)), spawning during in-game storms.

## Spawn & Notification
World boss spawn windows and notifications are a server plugin responsibility — see [120-Plugin-Architecture.md](120-Plugin-Architecture.md) for the event-scheduling system these depend on.
