# 141 — Coding Standards

## Language & Tooling
Java, built with Gradle, targeting the Paper server API, per the README's technology stack. All server-side code lives within the modular plugin architecture described in [120-Plugin-Architecture.md](120-Plugin-Architecture.md).

## Standards
* **Style** — consistent formatting (a shared `.editorconfig`/formatter config), enforced via CI before merge.
* **Modularity** — new features should be added to the appropriate existing plugin module or a clearly scoped new one, never bolted onto an unrelated module for convenience.
* **Server Authority** — no gameplay-affecting logic should trust client-reported state; see [127-Anti-Cheat.md](127-Anti-Cheat.md) for why this is a hard requirement, not a style preference.
* **Database Access** — all persistence goes through the shared data access layer described in [121-Database.md](121-Database.md); no plugin should open its own raw database connections.

## Documentation
Every public plugin API method should have a doc comment; every new system should have a corresponding entry or update in this `docs/` directory, per [140-Development-Standards.md](140-Development-Standards.md).

## Review
All code changes require review before merge; testing expectations are covered in [146-Testing.md](146-Testing.md).
