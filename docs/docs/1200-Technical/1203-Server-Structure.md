# 1203 — Server Structure

## Overview
Describes how Elysium's server infrastructure is organized at a deployment level, distinct from the plugin/code architecture in [1200-Plugin-Architecture.md](1200-Plugin-Architecture.md).

## Server Types
* **Overworld Server(s)** — hosts the persistent, shared open world (all continents, [0101-Continents.md](../0100-World/0101-Continents.md)); may eventually be sharded per-continent as population grows.
* **Instance Servers** — dynamically spun-up servers/processes hosting dungeon and raid instances ([0106-Dungeons.md](../0100-World/0106-Dungeons.md), [0107-Raids.md](../0100-World/0107-Raids.md)), torn down when empty.
* **Arena/PvP Servers** — dedicated lightweight instances for Arena matches ([0805-Arenas.md](../0800-Multiplayer/0805-Arenas.md)).
* **Login/Proxy Layer** — handles player connection routing between the overworld and instance servers, giving the illusion of a single seamless world.

## Cross-Version Update Support
Per the README's technical goals, the server structure should support rolling out client updates without forcing a hard disconnect of the entire playerbase where possible — a proxy layer capable of managing mixed-version compatibility windows during patch rollout.

## Relationship to Other Docs
See [1201-Database.md](1201-Database.md) for shared data access across all server types, and [1208-Performance.md](1208-Performance.md) for performance targets per server type.


## Instance Lifecycle

Instance servers are provisioned on-demand when a group enters a dungeon or raid, and torn down automatically after a period of inactivity or when the group fully disbands, keeping server resource usage proportional to actual demand rather than statically over-provisioned — see [1209-Instance-System.md](1209-Instance-System.md) for the detailed instance management architecture.

## Load Distribution

The overworld server layer is designed to eventually shard by continent or region as concurrent population grows, coordinated with the load balancing strategy in [1222-Load-Balancing.md](1222-Load-Balancing.md).
