# 1223 — Server Scaling

**Project:** Elysium MMORPG  
**Category:** Technical  
**Status:** Design Complete — Implementation Pending  
**Related:** [1222-Load-Balancing.md](1222-Load-Balancing.md) · [1209-Instance-System.md](1209-Instance-System.md) · [1217-Server-Architecture.md](1217-Server-Architecture.md) · [0003-Roadmap.md](../0000-Project/0003-Roadmap.md)

---

## 1. Overview

Server Scaling describes how the Elysium backend grows (and shrinks) with player population and content demand, from early alpha through live service and expansions.

---

## 2. Scaling Dimensions

| Dimension | Approach |
|-----------|----------|
| **Open-world capacity** | Additional continent layers / instances |
| **Dungeon & raid capacity** | On-demand instance spin-up |
| **Shared services** | Horizontal scaling of auth, economy, social, etc. |
| **Database** | Read replicas, sharding only if proven necessary |
| **Geographic** | Future consideration for latency-sensitive regions |

---

## 3. Design Rules

1. Prefer horizontal scaling of stateless or lightly stateful services.
2. Instance-based content is naturally parallelisable and should remain so.
3. Capacity planning uses monitoring data and load-test results, not guesswork alone.
4. Scaling procedures are documented and automatable where practical.
