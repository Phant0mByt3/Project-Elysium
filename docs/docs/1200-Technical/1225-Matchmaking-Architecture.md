# 1225 — Matchmaking Architecture

**Project:** Elysium MMORPG  
**Category:** Technical  
**Status:** Design Complete — Implementation Pending  
**Related:** [0803-Dungeon-Finder.md](../0800-Multiplayer/0803-Dungeon-Finder.md) · [0805-Arenas.md](../0800-Multiplayer/0805-Arenas.md) · [0811-Party-Finder.md](../0800-Multiplayer/0811-Party-Finder.md) · [1209-Instance-System.md](1209-Instance-System.md)

---

## 1. Overview

Matchmaking Architecture covers the services and logic that form groups for dungeons, raids, arenas, and other queued content, then hand those groups to the Instance Manager for instance creation and player transfer.

---

## 2. Responsibilities

- Accept queue requests with role and rating information
- Form balanced groups according to content rules
- Estimate and communicate wait times
- Create or assign instances and transfer players
- Handle deserters, requeues, and partial group recovery

---

## 3. Design Rules

1. Role balance and basic power checks prevent obviously incomplete groups from entering content.
2. Cross-faction rules are applied according to the design of each activity.
3. Matchmaking is fair and resistant to simple queue manipulation.
4. Failure modes degrade gracefully (clear errors, return to queue or world).


---

## Additional Detail: Matchmaking Fairness

The matchmaking service balances group formation speed against composition quality (role balance, approximate item level), using configurable weighting so that, for example, Dungeon Finder ([0803-Dungeon-Finder.md](../0800-Multiplayer/0803-Dungeon-Finder.md)) can prioritize speed while Arena ranked matchmaking ([0805-Arenas.md](../0800-Multiplayer/0805-Arenas.md)) prioritizes rating-appropriate fairness.

## Queue Health Monitoring

Queue wait times per role and bracket are actively monitored, with alerts triggering design review if a specific role or bracket's queue times grow unreasonably long, indicating a potential balance or population issue worth investigating.
