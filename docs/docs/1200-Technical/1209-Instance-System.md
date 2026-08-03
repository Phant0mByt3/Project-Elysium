# 1209 — Instance System

**Project:** Elysium MMORPG
**Category:** Technical
**Status:** Design Complete — Implementation Pending
**Related Systems:** [1202-Network.md](1202-Network.md) · [1203-Server-Structure.md](1203-Server-Structure.md) · [1208-Performance.md](1208-Performance.md) · [1210-World-Management.md](1210-World-Management.md) · [1211-Server-Synchronisation.md](1211-Server-Synchronisation.md)

---

## 1. Instance Architecture

Elysium does **not** run as a single massive shared world. Instead, the world is decomposed into independently running **instances**, each a self-contained Minecraft server process managing one region of the game.

| World Element | Instanced? |
|---|---|
| Continents | Yes — each continent is its own instance |
| Dungeons | Yes — one instance per active dungeon run |
| Raids | Yes — one instance per active raid group |
| Floating islands | Yes — separate instance per island cluster |
| Underground worlds | Yes — separate instance per underground region |
| Cities/hub areas | Yes — typically instanced as part of their parent continent, with high player-count scaling (see §11) |

All instances sit behind a single **Proxy** layer that players connect to first, which then routes them to the correct backend instance.

---

## 2. Why Instances Are Used

| Reason | Explanation |
|---|---|
| **Performance** | A single world server has a hard ceiling on entity count, chunk load, and tick rate. Splitting the world lets each instance run at full performance for its player count. |
| **Isolation** | A crash or slowdown in one dungeon instance cannot affect players on the open continent. |
| **Scalability** | Instances can be spun up and down on demand, matching player population instead of over-provisioning a single giant server. |
| **Security** | Instance-local state (loot rolls, boss health, exploit attempts) is isolated, reducing the blast radius of any single compromised session. |
| **Content control** | Raid and dungeon instances can be reset, versioned, and patched independently of the always-on open world. |

---

## 3. Instance Types

| Type | Lifetime | Player Cap | Example |
|---|---|---|---|
| **Open World Instance** | Persistent, always running | High (soft-capped, see §11) | Valoria continent |
| **Dungeon Instance** | Created on entry, destroyed after completion/timeout | Small group (5–8) | Frostheim ice caverns |
| **Raid Instance** | Created on entry, destroyed after completion/timeout | Raid-sized (10–30) | Ashlands world-boss lair |
| **Event Instance** | Created for scheduled/triggered events, destroyed after event ends | Variable | Seasonal world event (see [../0800-Multiplayer/0807-Seasons.md](../0800-Multiplayer/0807-Seasons.md)) |

### 3.1 Open World Instances

Persistent instances that map to continents and their sub-regions (see [1210-World-Management.md](1210-World-Management.md) §Continent Sizes). These run continuously and are the default destination on login.

### 3.2 Dungeon Instances

Created the moment a party enters a dungeon portal, using a **template snapshot** of the dungeon's base layout (see [1210-World-Management.md](1210-World-Management.md) §Dungeon Worlds). Destroyed automatically on party wipe-timeout, completion, or extended inactivity.

### 3.3 Raid Instances

Function identically to Dungeon Instances but sized for larger groups, with additional systems for boss phase tracking and loot distribution (see [../0800-Multiplayer/0802-Raiding.md](../0800-Multiplayer/0802-Raiding.md)).

### 3.4 Event Instances

Spun up by the Instance Manager (§4) on a schedule or trigger condition (see [../0100-World/0109-World-Events.md](../0100-World/0109-World-Events.md)), and torn down once the event concludes, freeing resources immediately rather than persisting empty event space.

---

## 4. Player Transfer System

Moving a player between instances (e.g. entering a dungeon, or crossing from one continent instance to another) follows a consistent handoff sequence:

1. Client requests transfer (e.g. walks into a dungeon portal, or a fast-travel action from [../0100-World/0111-Fast-Travel.md](../0100-World/0111-Fast-Travel.md)).
2. Proxy notifies the **Instance Manager** of the transfer request.
3. Instance Manager confirms the target instance exists (or creates it, §5) and reserves a player slot.
4. Player's session data (character state, inventory, buffs) is synced via [1211-Server-Synchronisation.md](1211-Server-Synchronisation.md) to the target instance.
5. Proxy re-routes the player's connection to the target instance.
6. Source instance releases the player's slot and unloads their entity after a short grace period (in case of transfer failure/retry).

```text
Player Client
     │
     ▼
   Proxy
     │
     ▼
Instance Manager ── confirms/creates target instance
     │
     ▼
Target World Server ── receives synced player state
```

---

## 5. Data Loading

On instance entry, only the data required for that instance is loaded:

| Data | Loaded From | Notes |
|---|---|---|
| Character state | Central database (see [1201-Database.md](1201-Database.md)) | Always loaded fresh at instance entry |
| Instance terrain | Pre-built world template (see [1210-World-Management.md](1210-World-Management.md)) | Cached on disk per instance type |
| Instance-local state (boss HP, loot tables rolled) | Instance memory only | Never persisted beyond instance lifetime, except final results (e.g. loot awarded) |

---

## 6. Instance Creation

| Step | Description |
|---|---|
| 1. Trigger | Player/party requests entry, or a scheduled event fires |
| 2. Template selection | Instance Manager selects the correct world template |
| 3. Process allocation | A backend world server process is allocated (from a warm pool where possible, to reduce cold-start time) |
| 4. World load | Template is loaded into the allocated process |
| 5. Registration | Instance is registered with the Instance Manager and made available for player transfer |

> **Developer Note:** Dungeon and raid instances should draw from a **warm pool** of pre-initialized processes wherever infrastructure allows, to minimize the load-in delay a party experiences when entering content — this directly affects perceived performance even though it is a backend concern (see [1208-Performance.md](1208-Performance.md)).

---

## 7. Instance Shutdown

Instances are torn down when:

- All players have left and a grace timeout has elapsed (prevents instant destroy/recreate churn from brief disconnects).
- A raid/dungeon is completed and the completion timeout expires.
- A scheduled event's end time is reached.
- An administrative shutdown is issued (e.g. for a content patch).

On shutdown, any data that must persist (loot awarded, quest completion, achievement progress) has already been written back via [1211-Server-Synchronisation.md](1211-Server-Synchronisation.md) at the moment it occurred — shutdown itself performs no additional save, only resource cleanup.

---

## 8. Scaling

| Scaling Lever | Description |
|---|---|
| Horizontal instance scaling | Additional Open World Instances of the same continent can be spun up if a single instance approaches its player cap |
| On-demand dungeon/raid scaling | Each party/raid gets its own instance automatically — no manual scaling needed |
| Instance Manager load balancing | New instance creation requests are distributed across available backend hardware based on current load |

---

## 9. Performance Advantages

- Per-instance tick rate stays stable because entity/chunk load is bounded by that instance's design cap, not the whole game world.
- Instances failing to meet performance targets can be flagged and investigated in isolation (see [1208-Performance.md](1208-Performance.md)) without needing to reproduce the issue on a live shared world.
- Dungeon/raid instances can be aggressively optimized (e.g. reduced simulation distance) since their scope is small and known in advance.

---

## 10. Security Advantages

- Exploits or cheating attempts within a single instance cannot directly affect players in other instances.
- Loot rolls, boss mechanics validation, and anti-cheat checks (see [1207-Anti-Cheat.md](1207-Anti-Cheat.md)) run within the isolated instance, reducing the attack surface exposed to the wider player base.
- Instance-local state is discarded on shutdown, limiting the value of any state-manipulation exploit to a single, short-lived session.

---

## 11. Open World Player Caps and Scaling

| Continent Instance | Soft Cap (before new instance spins up) |
|---|---|
| Valoria | High-population threshold, monitored by Instance Manager |
| Frostheim | Medium-population threshold |
| Ashlands | Medium-population threshold |
| Celestia | Lower-population threshold (smaller continent, see [1210-World-Management.md](1210-World-Management.md)) |

When a continent instance approaches its soft cap, the Instance Manager creates a parallel instance ("layer") of the same continent and begins routing new arrivals to it, keeping existing players on their current layer to avoid disrupting group content in progress.

---

## 12. System Rules Summary

1. No world instance may hold more than its designed player cap; the Instance Manager creates new layers rather than overloading an existing one.
2. Dungeon and raid instances are always created per-party/per-raid — instances are never shared across unrelated groups.
3. Instance-local state is never persisted beyond instance lifetime except through explicit synchronisation events (loot, quest completion, achievements).
4. Every instance transfer goes through the Proxy → Instance Manager → Target Instance sequence; direct client-to-instance connections are not permitted.
5. Instance shutdown performs cleanup only — all meaningful state changes must already be synchronised before shutdown begins.

---

## 13. Story Phasing

Players are placed into different world instances depending on:

* quest completion
* story progression
* expansion state

Example:
```
Aurelia_PreCollision
Aurelia_Collision_Event
Aurelia_PostCollision
```
Players in different phases cannot normally interact until they synchronize their timeline.

---

## 13. Connections to Other Systems

| System | Relationship |
|---|---|
| [1202-Network.md](1202-Network.md) | Defines the low-level connection and routing protocol the Proxy and Instance Manager use |
| [1203-Server-Structure.md](1203-Server-Structure.md) | Defines how the Proxy, Instance Manager, and World Servers are physically/logically organised |
| [1208-Performance.md](1208-Performance.md) | Defines the performance budgets each instance type must meet |
| [1210-World-Management.md](1210-World-Management.md) | Source of the world templates each instance is created from |
| [1211-Server-Synchronisation.md](1211-Server-Synchronisation.md) | Defines how player and world data moves between instances and the central database |
