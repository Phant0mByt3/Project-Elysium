# 1222 — Load Balancing

**Project:** Elysium MMORPG  
**Category:** Technical  
**Status:** Design Complete — Implementation Pending  
**Related:** [1203-Server-Structure.md](1203-Server-Structure.md) · [1209-Instance-System.md](1209-Instance-System.md) · [1223-Server-Scaling.md](1223-Server-Scaling.md) · [1208-Performance.md](1208-Performance.md)

---

## 1. Overview

Load Balancing distributes player connections and instance workload across available hardware so that no single process becomes a bottleneck and so that capacity can grow with population.

---

## 2. Responsibilities

- Route new connections through the proxy to healthy backends
- Place new open-world layers and dungeon/raid instances on suitable hosts
- Avoid overloading individual game processes beyond their designed player and entity budgets
- Support draining and maintenance of individual nodes without full outages

---

## 3. Design Rules

1. Balancing decisions prefer player experience (low latency, stable instances) over pure evenness of hardware utilisation.
2. Existing groups and friends are kept together where possible when creating or assigning instances.
3. Health checks remove unhealthy nodes from rotation automatically.


---

## Additional Detail: Player Routing

The login/proxy layer described in [1203-Server-Structure.md](1203-Server-Structure.md) routes players to the least-loaded appropriate overworld shard or instance server, using real-time load metrics from [1216-Monitoring.md](1216-Monitoring.md) rather than static assignment.

## Graceful Degradation

Under unexpectedly high load, non-critical systems (certain analytics collection, cosmetic-only features) can be temporarily throttled to preserve core gameplay responsiveness, a deliberate degradation strategy rather than allowing the entire server to become unresponsive.
