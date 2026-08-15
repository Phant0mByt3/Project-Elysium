# 1218 — Plugin Communication

**Project:** Elysium MMORPG  
**Category:** Technical  
**Status:** Design Complete — Implementation Pending  
**Related:** [1200-Plugin-Architecture.md](1200-Plugin-Architecture.md) · [1202-Network.md](1202-Network.md) · [1211-Server-Synchronisation.md](1211-Server-Synchronisation.md)

---

## 1. Overview

Plugin Communication defines how modular plugins exchange events and data within a single server process and, where needed, across processes via the broader messaging layer.

---

## 2. Patterns

- In-process event bus for same-JVM plugin interaction
- Explicit service interfaces for core shared functionality
- Cross-process messaging for instance-to-instance and service-to-service needs
- Avoidance of tight circular dependencies between plugin modules

---

## 3. Design Rules

1. Plugins prefer well-defined events and APIs over reaching into each other’s internals.
2. Communication that affects player state or economy is always authoritative and logged where appropriate.
3. Versioning and compatibility of cross-plugin contracts are considered when evolving APIs.


---

## Additional Detail: Event Bus Reliability

The event bus guarantees at-least-once delivery for critical gameplay events (loot grants, currency transactions) with idempotent handling on the receiving plugin's side, preventing duplicate processing in the event of a retry after a transient failure.

## Cross-Plugin Contract Stability

Plugin-to-plugin message contracts are versioned, allowing one plugin to be updated independently of another as long as the message contract version remains compatible, supporting the modular update goals described in [1200-Plugin-Architecture.md](1200-Plugin-Architecture.md).
