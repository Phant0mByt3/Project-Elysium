# 2008 — Staff Tools

**Project:** Elysium MMORPG
**Category:** Operations
**Status:** Living Document
**Related:** [1214-Admin-Tools.md](../1200-Technical/1214-Admin-Tools.md) · [1227-Permission-System.md](../1200-Technical/1227-Permission-System.md) · [2005-Support-System.md](2005-Support-System.md)

---

## 1. Overview

This document covers the operational usage of staff tooling by the live operations team, complementing the underlying technical implementation described in [1214-Admin-Tools.md](../1200-Technical/1214-Admin-Tools.md).

## 2. Staff Roles and Tool Access

Following the permission tiers in [1227-Permission-System.md](../1200-Technical/1227-Permission-System.md):

* **Support Staff** — player-specific fixes (item restoration, quest state correction, account inquiries).
* **Moderators** — chat/name enforcement, report review, temporary account actions ([2003-Moderation.md](2003-Moderation.md)).
* **Community Managers** — event tools, announcement systems ([2004-Community-Management.md](2004-Community-Management.md), [2009-Community-Events.md](2009-Community-Events.md)).
* **Senior Admins** — full access including permanent account actions and server-level tools.

## 3. Training and Onboarding

New staff members complete a documented onboarding process covering tool usage, escalation procedures, and the community guidelines they'll be enforcing ([2017-Community-Guidelines.md](2017-Community-Guidelines.md)), before receiving live tool access.

## 4. Tool Usage Standards

Every staff action performed through admin tools follows the audit trail requirement described in [1214-Admin-Tools.md](../1200-Technical/1214-Admin-Tools.md) — no untracked manual database intervention is permitted outside these tools, even for urgent fixes.

## 5. Shift Coverage

Staff tool access and on-call responsibilities are scheduled to provide reasonable coverage across peak playtime windows, with a clear escalation path to engineering for issues beyond support/moderation scope.

## 6. Tool Feedback Loop

Staff using these tools daily are a primary source of feedback for improving them — recurring friction points are fed back to the technical team maintaining [1214-Admin-Tools.md](../1200-Technical/1214-Admin-Tools.md) and [1215-Developer-Tools.md](../1200-Technical/1215-Developer-Tools.md) and [1417-Development-Tools.md](../1400-Development/1417-Development-Tools.md) for iteration.
