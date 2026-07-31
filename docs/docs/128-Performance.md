# 128 — Performance

## Overview
Performance targets and optimization strategy spanning both server (Paper/PostgreSQL) and client (Fabric mods, resource pack, shaders) — essential given the scale of raids, world events, and territory control PvP ([17-Raids.md](17-Raids.md), [19-World-Events.md](19-World-Events.md), [86-Territory-Control.md](86-Territory-Control.md)).

## Server-Side
* Instance-based architecture ([123-Server-Structure.md](123-Server-Structure.md)) keeps dungeon/raid load isolated from the shared overworld server.
* Database query optimization and caching at the plugin layer ([121-Database.md](121-Database.md)) to avoid hot-path database calls during combat.
* Regular load testing planned during Closed Beta ([03-Roadmap.md](03-Roadmap.md)) to validate world-event and territory-control scale.

## Client-Side
* Tiered shader presets ([115-Shaders.md](115-Shaders.md)) and performance-optimization client mods ([111-Client-Mods.md](111-Client-Mods.md)) to support a wide range of hardware.
* Model and texture budgets for custom assets ([113-Custom-Models.md](113-Custom-Models.md)) reviewed against target minimum-spec hardware.

## Cross-Version Update Support
Performance work should account for the README's cross-version update support goal — new content should not silently regress performance on already-supported hardware configurations.
