# 123 — Server Structure

## Overview
Describes how Elysium's server infrastructure is organized at a deployment level, distinct from the plugin/code architecture in [120-Plugin-Architecture.md](120-Plugin-Architecture.md).

## Server Types
* **Overworld Server(s)** — hosts the persistent, shared open world (all continents, [011-Continents.md](011-Continents.md)); may eventually be sharded per-continent as population grows.
* **Instance Servers** — dynamically spun-up servers/processes hosting dungeon and raid instances ([016-Dungeons.md](016-Dungeons.md), [017-Raids.md](017-Raids.md)), torn down when empty.
* **Arena/PvP Servers** — dedicated lightweight instances for Arena matches ([085-Arenas.md](085-Arenas.md)).
* **Login/Proxy Layer** — handles player connection routing between the overworld and instance servers, giving the illusion of a single seamless world.

## Cross-Version Update Support
Per the README's technical goals, the server structure should support rolling out client updates without forcing a hard disconnect of the entire playerbase where possible — a proxy layer capable of managing mixed-version compatibility windows during patch rollout.

## Relationship to Other Docs
See [121-Database.md](121-Database.md) for shared data access across all server types, and [128-Performance.md](128-Performance.md) for performance targets per server type.
