# 1414 — Asset Management

**Project:** Elysium MMORPG  
**Category:** Development  
**Status:** Design Complete — Implementation Pending  
**Related:** [1319-Art-Asset-Pipeline.md](../1300-Art/1319-Art-Asset-Pipeline.md) · [1102-Content-Pack.md](../1100-Client/1102-Content-Pack.md) · [1405-Naming-Conventions.md](1405-Naming-Conventions.md)

---

## 1. Overview

Asset Management covers naming, storage, versioning, and ownership of art, audio, and data assets from source to runtime packs.

---

## 2. Rules

- Consistent naming and folder layout  
- Source vs runtime separation  
- Clear ownership per discipline  
- No orphaned or undocumented large binaries in primary repos without process  


---

## Additional Detail: Asset Lifecycle Tracking

Each art and audio asset is tracked through its lifecycle (concept, in-progress, in-review, approved, in-content-pack) using the same tooling that manages the broader content pipeline ([1409-Content-Pipeline.md](1409-Content-Pipeline.md)), giving the art team clear visibility into production status across hundreds of concurrent assets.

## Deprecation and Cleanup

Assets superseded by newer versions or removed from the game are formally deprecated rather than silently deleted, preserving a clean audit trail and preventing accidental breakage of any content still referencing an older asset during the transition period.
