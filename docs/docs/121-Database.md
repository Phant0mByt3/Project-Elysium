# 121 — Database

## Overview
PostgreSQL serves as Elysium's persistent data store, accessed exclusively through the shared core plugin's data access layer ([120-Plugin-Architecture.md](120-Plugin-Architecture.md)) rather than direct queries from feature plugins.

## Core Schema Areas
* **Accounts & Characters** — authentication-linked account records and per-character data ([124-Authentication.md](124-Authentication.md)).
* **Inventory & Items** — item instances, bank storage ([106-Banking.md](106-Banking.md)), mail attachments ([105-Mail.md](105-Mail.md)).
* **Progression** — level, talents, reputation, achievements, titles ([046-Leveling.md](046-Leveling.md), [043-Talent-Trees.md](043-Talent-Trees.md), [076-Reputation.md](076-Reputation.md), [074-Achievements.md](074-Achievements.md)).
* **Social** — guilds, guild banks, party history ([080-Guilds.md](080-Guilds.md)).
* **Economy** — auction house listings, transaction logs ([103-Auction-House.md](103-Auction-House.md)).
* **Raid/Dungeon Lockouts** — per-character weekly lockout state ([082-Raiding.md](082-Raiding.md)).

## Design Principles
* Schema migrations are versioned and applied through Gradle-managed migration scripts, never manual production edits.
* Read-heavy data (item templates, quest definitions) should be cached in-memory at the plugin layer, with the database as the source of truth rather than the hot path for every read.
* Backups and replication strategy to be finalized alongside [126-Security.md](126-Security.md) ahead of Closed Beta.
