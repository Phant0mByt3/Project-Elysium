# 1201 — Database

## Overview
PostgreSQL serves as Elysium's persistent data store, accessed exclusively through the shared core plugin's data access layer ([1200-Plugin-Architecture.md](1200-Plugin-Architecture.md)) rather than direct queries from feature plugins.

## Core Schema Areas
* **Accounts & Characters** — authentication-linked account records and per-character data ([1204-Authentication.md](1204-Authentication.md)).
* **Inventory & Items** — item instances, bank storage ([1006-Banking.md](../1000-Economy/1006-Banking.md)), mail attachments ([1005-Mail.md](../1000-Economy/1005-Mail.md)).
* **Progression** — level, talents, reputation, achievements, titles ([0305-Leveling.md](../0300-Characters/0305-Leveling.md), [0303-Talent-Trees.md](../0300-Characters/0303-Talent-Trees.md), [0706-Reputation.md](../0700-Quests/0706-Reputation.md), [0704-Achievements.md](../0700-Quests/0704-Achievements.md)).
* **Social** — guilds, guild banks, party history ([0800-Guilds.md](../0800-Multiplayer/0800-Guilds.md)).
* **Economy** — auction house listings, transaction logs ([1003-Auction-House.md](../1000-Economy/1003-Auction-House.md)).
* **Raid/Dungeon Lockouts** — per-character weekly lockout state ([0802-Raiding.md](../0800-Multiplayer/0802-Raiding.md)).

## Design Principles
* Schema migrations are versioned and applied through managed migration scripts (run via the build pipeline), never manual production edits.
* Read-heavy data (item templates, quest definitions) should be cached in-memory at the plugin layer, with the database as the source of truth rather than the hot path for every read.
* Backups and replication strategy to be finalized alongside [1206-Security.md](1206-Security.md) ahead of Closed Beta.


## Scaling Strategy

As player population grows, read replicas are used to offload reporting and analytics queries ([2006-Analytics.md](../2000-Operations/2006-Analytics.md)) from the primary transactional database, keeping gameplay-critical write performance stable under load.

## Data Integrity Guarantees

All economy-affecting operations (trades, auction house transactions, mail) use database transactions with appropriate isolation levels to prevent race conditions that could enable item duplication, directly supporting the anti-cheat goals in [1207-Anti-Cheat.md](1207-Anti-Cheat.md).
