# 2012 — Maintenance

**Project:** Elysium MMORPG
**Category:** Operations
**Status:** Living Document
**Related:** [1230-Server-Maintenance.md](../1200-Technical/1230-Server-Maintenance.md) · [2011-Server-Restarts.md](2011-Server-Restarts.md)

---

## 1. Overview

This document covers the operational planning and communication side of routine and emergency maintenance, complementing the technical maintenance procedures in [1230-Server-Maintenance.md](../1200-Technical/1230-Server-Maintenance.md) and the restart-specific communication covered in [2011-Server-Restarts.md](2011-Server-Restarts.md).

## 2. Maintenance Categories

* **Routine Maintenance** — database upkeep, infrastructure patching, scheduled during low-traffic windows.
* **Deployment Maintenance** — accompanies content and system updates ([2001-Updates.md](2001-Updates.md)).
* **Emergency Maintenance** — unscheduled response to critical issues.

## 3. Advance Planning

Routine maintenance windows are planned on a predictable monthly or quarterly cadence where feasible, distinct from the more frequent weekly restart cadence in [2011-Server-Restarts.md](2011-Server-Restarts.md), and communicated well in advance through the channels in [2004-Community-Management.md](2004-Community-Management.md).

## 4. Downtime Minimization

Where technically feasible, maintenance is designed to minimize player-facing downtime — for example, database maintenance that doesn't require a full service interruption is preferred over approaches that do, balanced against the operational risk of more complex zero-downtime procedures.

## 5. Extended Maintenance Communication

For maintenance windows expected to run longer than a typical restart, regular status updates are posted at defined intervals throughout the window, preventing the community from feeling left in the dark during an extended outage.

## 6. Post-Maintenance Verification

A documented post-maintenance verification checklist confirms core systems (login, character loading, economy transactions, group finder) are functioning correctly before the server is reopened to the general playerbase, catching issues before they become widespread player-facing problems.
