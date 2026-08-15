# 1221 — Caching System

**Project:** Elysium MMORPG  
**Category:** Technical  
**Status:** Design Complete — Implementation Pending  
**Related:** [1201-Database.md](1201-Database.md) · [1219-Data-Storage.md](1219-Data-Storage.md) · [1208-Performance.md](1208-Performance.md) · [1211-Server-Synchronisation.md](1211-Server-Synchronisation.md)

---

## 1. Overview

The Caching System reduces database and service load by holding frequently read, slowly changing, or expensive-to-compute data in memory or a distributed cache.

---

## 2. Use Cases

- Character and account lookups
- Item and recipe definitions
- Auction House listings and price summaries
- Guild roster and permission snapshots
- Session and rate-limit state

---

## 3. Design Rules

1. Cache is never the source of truth for durable player state.
2. Invalidation or short TTLs keep cached data sufficiently fresh.
3. Cache stampedes and thundering herds are considered in design.
4. Critical writes still go through the authoritative path with appropriate consistency guarantees.


---

## Additional Detail: Cache Invalidation Strategy

Cached data (item templates, quest definitions, static world data) uses a clear invalidation strategy tied to content versioning, ensuring a content update reliably propagates to all cached copies rather than risking stale data serving outdated definitions.

## Cache Layer Placement

Caching occurs both at the plugin layer (in-memory, per-server-process) and at a shared distributed cache layer for data that must remain consistent across multiple server processes, balancing raw speed against consistency requirements per data type.
