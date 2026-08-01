# 141 — Coding Standards

## Language & Tooling
Java, built with Gradle, targeting the Paper server API, per the README's technology stack. All server-side code lives within the modular plugin architecture described in [1200-Plugin-Architecture.md](../1200-Technical/1200-Plugin-Architecture.md).

## Standards
* **Style** — consistent formatting (a shared `.editorconfig`/formatter config), enforced via CI before merge.
* **Modularity** — new features should be added to the appropriate existing plugin module or a clearly scoped new one, never bolted onto an unrelated module for convenience.
* **Server Authority** — no gameplay-affecting logic should trust client-reported state; see [1207-Anti-Cheat.md](../1200-Technical/1207-Anti-Cheat.md) for why this is a hard requirement, not a style preference.
* **Database Access** — all persistence goes through the shared data access layer described in [1201-Database.md](../1200-Technical/1201-Database.md); no plugin should open its own raw database connections.

## Documentation
Every public plugin API method should have a doc comment; every new system should have a corresponding entry or update in this `docs/` directory, per [1400-Development-Standards.md](1400-Development-Standards.md).

## Review
All code changes require review before merge; testing expectations are covered in [1406-Testing.md](1406-Testing.md).
