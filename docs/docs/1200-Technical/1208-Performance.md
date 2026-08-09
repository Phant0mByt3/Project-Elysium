# 1208 — Performance

## Overview
Performance targets and optimization strategy spanning both server (Unreal Engine dedicated server / PostgreSQL) and client (native client moduleules, content pack, rendering effects) — essential given the scale of raids, world events, and territory control PvP ([0107-Raids.md](../0100-World/0107-Raids.md), [0109-World-Events.md](../0100-World/0109-World-Events.md), [0806-Territory-Control.md](../0800-Multiplayer/0806-Territory-Control.md)).

## Server-Side
* Instance-based architecture ([1203-Server-Structure.md](1203-Server-Structure.md)) keeps dungeon/raid load isolated from the shared overworld server.
* Database query optimization and caching at the plugin layer ([1201-Database.md](1201-Database.md)) to avoid hot-path database calls during combat.
* Regular load testing planned during Closed Beta ([0003-Roadmap.md](../0000-Project/0003-Roadmap.md)) to validate world-event and territory-control scale.

## Client-Side
* Tiered graphics quality presets ([1105-Shaders.md](../1100-Client/1105-Shaders.md)) and performance-optimization client moduleules ([1101-Client-Modules.md](../1100-Client/1101-Client-Modules.md)) to support a wide range of hardware.
* Model and texture budgets for custom assets ([1103-Custom-Models.md](../1100-Client/1103-Custom-Models.md)) reviewed against target minimum-spec hardware.

## Cross-Version Update Support
Performance work should account for the README's cross-version update support goal — new content should not silently regress performance on already-supported hardware configurations.
