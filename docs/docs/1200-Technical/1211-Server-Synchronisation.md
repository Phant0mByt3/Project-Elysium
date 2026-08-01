# Server Synchronisation

**Project:** Elysium MMORPG
**Category:** Technical
**Status:** Design Complete — Implementation Pending
**Related Systems:** [1201-Database.md](1201-Database.md) · [1202-Network.md](1202-Network.md) · [1203-Server-Structure.md](1203-Server-Structure.md) · [1204-Authentication.md](1204-Authentication.md) · [1205-API.md](1205-API.md) · [1206-Security.md](1206-Security.md) · [1209-Instance-System.md](1209-Instance-System.md)

---

## 1. Synchronisation Overview

Because Elysium's world is split across many independent instances (see [1209-Instance-System.md](1209-Instance-System.md)), no single server process holds the full picture of a player's account, guild, or economy state. **Server Synchronisation** is the backend layer responsible for keeping every instance, the database, and the player's client in agreement about what is currently true.

```text
                 Proxy
                   │
           Authentication
                   │
          ┌────────┴────────┐
          │  Server Instances │  (Open World, Dungeon, Raid, Event)
          └────────┬────────┘
                   │
               Database
```

Every instance communicates with the Database exclusively through the Synchronisation layer's defined events and API calls (§9, §10) — instances never write directly to another instance's memory or state.

---

## 2. Player Data Syncing

| Data | Sync Trigger | Frequency |
|---|---|---|
| Position/appearance | Continuous while in an instance | Real-time (streamed) |
| Level/experience | On change (level-up, quest completion) | Event-driven |
| Currency | On transaction | Event-driven |
| Settings | On change, see [../1100-Client/1109-Settings.md](../1100-Client/1109-Settings.md) | Event-driven |

Player data syncing ensures that if a player disconnects mid-session or transfers instances (see [1209-Instance-System.md](1209-Instance-System.md) §4), no progress made before the last successful sync is lost.

---

## 3. Character Syncing

Character state (stats, equipped gear, active buffs, specialisation, Advanced Class Path — see [../0300-Characters/0308-Class-Progression.md](../0300-Characters/0308-Class-Progression.md)) is synced at two points:

1. **On instance entry** — full character state is loaded fresh from the Database into the target instance.
2. **On meaningful change** — incremental updates are pushed back to the Database (e.g. gear swap, talent respec) without waiting for instance exit.

This "load-fresh, push-incremental" model avoids both stale data on entry and expensive full-state writes on every minor change.

---

## 4. Inventory Syncing

| Concern | Handling |
|---|---|
| Item pickup/drop | Synced immediately to prevent item duplication across instances |
| Cross-instance trade | Routed through the central Database via [1205-API.md](1205-API.md) rather than direct instance-to-instance transfer |
| Bank/storage access | Reads and writes go directly through the Database, since Banking (see [../1000-Economy/1006-Banking.md](../1000-Economy/1006-Banking.md)) must be consistent regardless of which instance a player is in |

> **Developer Note:** Inventory syncing is the single highest-risk area for duplication exploits. All inventory-affecting operations must be idempotent and acknowledge-gated — an instance must receive Database confirmation before showing an item as successfully moved, not optimistically before confirmation.

---

## 5. Quest Syncing

Quest progress (see [../0700-Quests/0700-Quests.md](../0700-Quests/0700-Quests.md)) is synced per-objective, not per-quest, so that partial progress made in one instance (e.g. a kill objective in an open-world instance) is immediately visible if the player transfers into a dungeon instance to complete the next objective.

---

## 6. Economy Syncing

| System | Sync Behavior |
|---|---|
| Auction House (see [../1000-Economy/1003-Auction-House.md](../1000-Economy/1003-Auction-House.md)) | Fully centralized — not instance-local at all; all instances query the same live Database records |
| Vendors | Instance-local stock (if any) syncs restock timers back to the Database on a schedule |
| Currency balance | Synced on every transaction, with Database as the single source of truth |

---

## 7. Guild Syncing

Guild roster, ranks, guild bank (see [../0800-Multiplayer/0800-Guilds.md](../0800-Multiplayer/0800-Guilds.md)), and guild chat state are stored centrally and synced to any instance containing an online guild member, so guild-wide notifications (member joined, bank withdrawal) reach all online members regardless of which instance they occupy.

---

## 8. Party Syncing

Party membership, roles, and loot rules (see [../0800-Multiplayer/0801-Parties.md](../0800-Multiplayer/0801-Parties.md)) are synced in real time between party members even when they are split across different instances briefly (e.g. one member finishing a solo objective while others wait in a hub instance), so the party frame UI (see [../1100-Client/1108-UI-Systems.md](../1100-Client/1108-UI-Systems.md) §15) stays accurate for everyone.

---

## 9. Achievement Syncing

Achievement progress (see [../0700-Quests/0704-Achievements.md](../0700-Quests/0704-Achievements.md)) is synced on every qualifying event and validated against the Database's authoritative record before being confirmed to the client, preventing a client-side-only achievement unlock from being trusted without server confirmation.

---

## 10. Reputation Syncing

Faction reputation (see [../0700-Quests/0707-Factions-Reputation.md](../0700-Quests/0707-Factions-Reputation.md)) is synced identically to quest progress — incremental, event-driven updates pushed to the Database immediately upon a reputation-granting action, so reputation-gated content (vendors, quests) is consistently available regardless of instance.

---

## 11. Instance Transfers

Instance transfer synchronisation is the most latency-sensitive sync operation in the system, since the player is actively waiting on it. The sequence (expanded from [1209-Instance-System.md](1209-Instance-System.md) §4) is:

1. Source instance flushes any pending unsaved state changes to the Database.
2. Synchronisation layer confirms the flush succeeded.
3. Target instance requests the player's current state from the Database.
4. Target instance loads the state and confirms readiness to the Proxy.
5. Proxy completes the connection handoff.

If step 2 fails (Database unavailable or write conflict), the transfer is aborted and the player remains on the source instance rather than risking a load into an instance with stale data.

---

## 12. Database Communication

All synchronisation ultimately reads and writes through the central Database described in [1201-Database.md](1201-Database.md). Communication follows:

| Pattern | Use Case |
|---|---|
| Read-through cache | High-frequency reads (e.g. Auction House listings) |
| Write-behind queue | Non-critical, high-frequency writes (e.g. position updates) batched before persisting |
| Synchronous write | Critical writes (e.g. currency transactions, item transfers) that must confirm before the client sees success |

---

## 13. API Communication

Cross-instance and instance-to-database operations that aren't raw database reads/writes go through the internal API described in [1205-API.md](1205-API.md) — for example, guild bank withdrawal requests, auction house bid placement, and party invite routing across instances.

---

## 14. Network Events

The Synchronisation layer relies on the event/messaging infrastructure defined in [1202-Network.md](1202-Network.md) to broadcast state changes to interested instances without requiring every instance to poll the Database constantly:

| Event Type | Example | Subscribers |
|---|---|---|
| Player state change | Level-up, gear change | The player's current instance only |
| Guild event | Member online, bank change | All instances hosting online guild members |
| Economy event | Auction sold, price update | Any instance with the Auction House UI open |
| Party event | Member joined/left, loot roll | All instances hosting party members |

---

## 15. Real-Time Updates

Real-time sync (position, combat state, party frames) uses a low-latency streamed connection per [1202-Network.md](1202-Network.md), separate from the higher-latency-tolerant Database write path, so combat responsiveness is never bottlenecked by persistence operations.

---

## 16. Persistent Data

| Data Class | Persistence Behavior |
|---|---|
| Character progression, inventory, currency | Always persisted, synchronous critical writes |
| Guild/party membership | Persisted, synchronous |
| Instance-local combat state (boss HP mid-fight) | Not persisted — see [1209-Instance-System.md](1209-Instance-System.md) §5 |
| Settings | Persisted, see [../1100-Client/1109-Settings.md](../1100-Client/1109-Settings.md) §14 |

---

## 17. Failure Handling

| Failure | Handling |
|---|---|
| Database temporarily unavailable | Write-behind queue buffers non-critical writes; critical writes (currency, items) block and retry rather than silently failing |
| Instance crash mid-transfer | Player remains connected to the last confirmed instance; transfer is retried or the player is returned to a safe hub instance |
| Network partition between instance and Database | Instance enters a degraded read-only mode for affected systems until connectivity is restored |

---

## 18. Recovery Systems

- Failed critical writes are retried with exponential backoff before surfacing an error to the player.
- A player whose last transfer failed mid-flight is placed in a recovery queue that re-attempts state restoration on next login, rather than risking a corrupted mid-transfer state.
- Instance crashes trigger an automatic Instance Manager restart (see [1209-Instance-System.md](1209-Instance-System.md) §6) using the last confirmed-synced player states.

---

## 19. Data Consistency

| Guarantee | Scope |
|---|---|
| Strong consistency | Currency, item ownership, quest completion — no instance may show a state the Database hasn't confirmed |
| Eventual consistency | Guild online-status display, minor cosmetic state — acceptable to lag by a small margin for performance |

This split mirrors the general MMORPG principle of treating anything with real player value (items, currency, progression) as strongly consistent, while treating purely informational/display state as eventually consistent to preserve performance.

---

## 20. Security

- All instance-to-Database and instance-to-instance synchronisation traffic is authenticated using the credentials established at login (see [1204-Authentication.md](1204-Authentication.md)) — no instance can act on behalf of a player without a valid, current session token.
- Synchronisation events are validated server-side against expected state transitions (e.g. an item transfer event is rejected if the source instance's last confirmed state doesn't actually contain that item), coordinating with [1206-Security.md](1206-Security.md) and [1207-Anti-Cheat.md](1207-Anti-Cheat.md).
- All synchronisation channels are internal-network only and are not exposed to the public-facing Proxy layer.

---

## 21. System Rules Summary

1. No instance is ever the sole source of truth for account-level data — the Database always is.
2. Critical data (currency, items, progression) uses strong, synchronous consistency; informational data may be eventually consistent.
3. Instance transfers must confirm a successful state flush before allowing the destination instance to load, per §11.
4. All synchronisation traffic is authenticated and validated against expected state transitions.
5. Failures on critical writes must retry and surface clearly rather than silently dropping data.

---

## 22. Connections to Other Systems

| System | Relationship |
|---|---|
| [1201-Database.md](1201-Database.md) | The authoritative persistence layer this document synchronises against |
| [1202-Network.md](1202-Network.md) | Provides the transport and event/messaging infrastructure used for synchronisation |
| [1203-Server-Structure.md](1203-Server-Structure.md) | Defines the physical/logical layout of the Proxy, Authentication, and Instance layers shown in §1 |
| [1204-Authentication.md](1204-Authentication.md) | Supplies the session credentials that authorise all sync operations |
| [1205-API.md](1205-API.md) | Carries cross-instance operations that aren't raw database reads/writes |
| [1206-Security.md](1206-Security.md) | Defines the broader security model that synchronisation validation supports |
| [1209-Instance-System.md](1209-Instance-System.md) | Consumes this document's transfer and syncing behavior to move players between instances |
