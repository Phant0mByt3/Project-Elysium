# 1401 — Coding Standards

## Language & Tooling
C++, built with Unreal Build Tool, targeting the Unreal Engine dedicated server API, per the README's technology stack. All server-side code lives within the modular plugin architecture described in [1200-Plugin-Architecture.md](../1200-Technical/1200-Plugin-Architecture.md).

## Standards
* **Style** — consistent formatting (a shared `.editorconfig`/formatter config), enforced via CI before merge.
* **Modularity** — new features should be added to the appropriate existing plugin module or a clearly scoped new one, never bolted onto an unrelated module for convenience.
* **Server Authority** — no gameplay-affecting logic should trust client-reported state; see [1207-Anti-Cheat.md](../1200-Technical/1207-Anti-Cheat.md) for why this is a hard requirement, not a style preference.
* **Database Access** — all persistence goes through the shared data access layer described in [1201-Database.md](../1200-Technical/1201-Database.md); no plugin should open its own raw database connections.

## Documentation
Every public plugin API method should have a doc comment; every new system should have a corresponding entry or update in this `docs/` directory, per [1400-Development-Standards.md](1400-Development-Standards.md).

## Review
All code changes require review before merge; testing expectations are covered in [1406-Testing.md](1406-Testing.md).


## Error Handling Philosophy

Server code fails safely and loudly — errors are logged with sufficient context for debugging ([1212-Logging.md](../1200-Technical/1212-Logging.md)) rather than silently swallowed, and any error affecting player-facing state (a failed transaction, a failed quest update) triggers a clear rollback rather than leaving data in an inconsistent state.

## Performance-Conscious Code

Given the real-time, many-concurrent-player nature of an MMORPG server, code handling frequently-called paths (combat tick processing, movement updates) undergoes additional performance review against the budgets described in [1208-Performance.md](../1200-Technical/1208-Performance.md), while less frequently called code (one-time quest completion logic) is optimized for clarity and maintainability first.
