# 1224 — Region Servers

**Project:** Elysium MMORPG  
**Category:** Technical  
**Status:** Design Complete — Implementation Pending  
**Related:** [1209-Instance-System.md](1209-Instance-System.md) · [0101-Continents.md](../0100-World/0101-Continents.md) · [1210-World-Management.md](1210-World-Management.md) · [1223-Server-Scaling.md](1223-Server-Scaling.md)

---

## 1. Overview

Region Servers (or continent / open-world instances) host the persistent shared world for a given continent or major region. They are the always-on counterparts to the ephemeral dungeon and raid instances.

---

## 2. Characteristics

- Long-lived processes with persistent world state
- Higher player soft-caps than dungeon instances
- Host cities, overworld questing, world events, and world bosses
- May be layered (multiple parallel instances of the same continent) when population demands it

---

## 3. Design Rules

1. A crash or restart of one region server does not take down other continents or instances.
2. Player transfer between region servers (and into content instances) follows the synchronisation and proxy rules already defined.
3. World protection and building restrictions are enforced here as the primary open-world authority.


---

## Additional Detail: Regional Deployment Plan

Post-launch, server infrastructure is planned to expand from an initial single-region deployment to multiple geographic regions based on observed player distribution, prioritized by where the largest underserved latency-sensitive populations are concentrated.

## Cross-Region Play

Where multiple regions exist, cross-region play (grouping with a friend on a different regional server) is supported for social features at the cost of higher latency, with clear in-client latency indicators so players can make informed grouping decisions.
