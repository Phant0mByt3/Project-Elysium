# 18 — World Bosses

World bosses are powerful, open-world enemies that spawn on a timer or by trigger, encouraging spontaneous large-group cooperation outside of instanced content — supporting Pillar 4 in [02-Core-Pillars.md](02-Core-Pillars.md).

## Design Rules
* Tuned for 10–40 players depending on level range; scale down gracefully for smaller raids.
* Always tied to regional lore, never a generic "big monster."
* Drop guaranteed region-appropriate loot plus a chance at a unique cosmetic or mount (see [91-Mounts.md](91-Mounts.md)).
* Compete for tagging fairly across factions — see [84-PvP.md](84-PvP.md) for contested-tag rules where Concord and Pact players meet at the same spawn.

## Launch World Bosses

**Grothmar, the Root-Warden** *(Wildwood Reach, Level 14)* — the corrupted forest spirit behind [16-Dungeons.md](16-Dungeons.md)'s Hollow Root dungeon has an open-world counterpart that occasionally breaks free of the dungeon's seal.

**The Ashen Colossus** *(Ashenclaw Tundra, Level 40)* — an animated construct from the pre-Sundering era, awoken by orc clan excavation efforts. Central to a regional questline about whether to destroy or study it.

**Maelith's Herald** *(coastal Aurelia, Level 22)* — a storm elemental tied to the goddess Maelithir ([32-Gods.md](32-Gods.md)), spawning during in-game storms.

## Spawn & Notification
World boss spawn windows and notifications are a server plugin responsibility — see [120-Plugin-Architecture.md](120-Plugin-Architecture.md) for the event-scheduling system these depend on.
