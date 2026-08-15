# 1212 — Logging

**Project:** Elysium MMORPG  
**Category:** Technical  
**Status:** Design Complete — Implementation Pending  
**Related:** [1200-Plugin-Architecture.md](1200-Plugin-Architecture.md) · [1206-Security.md](1206-Security.md) · [1216-Monitoring.md](1216-Monitoring.md) · [1407-Bug-Tracking.md](../1400-Development/1407-Bug-Tracking.md)

---

## 1. Overview

Logging captures structured and unstructured events from the server processes, plugins, and supporting services for debugging, auditing, security review, and operational insight.

---

## 2. Log Categories

| Category | Purpose |
|----------|---------|
| **Application** | Plugin and framework events, errors, warnings |
| **Combat / Gameplay** | Optional detailed combat logs for balance and support |
| **Economy** | Currency and item transfers of note |
| **Security / Anti-Cheat** | Suspicious actions, auth failures, rate-limit hits |
| **Access / Admin** | Staff commands and privileged actions |
| **Performance** | Slow queries, tick overruns, resource warnings |

---

## 3. Design Rules

1. Logs are structured (JSON or equivalent) where possible for easy querying.
2. Sensitive data (passwords, full session tokens) is never written in plain form.
3. Retention and rotation policies balance usefulness with storage cost and privacy.
4. Log volume is managed so that high-frequency events do not overwhelm the system under load.

---

## 4. Technical Notes

Logging is centralised through a shared library used by all plugins. Aggregation and search are handled by the operations stack (see Monitoring).


---

## Additional Detail: Log Retention and Levels

Logs are categorized by severity (debug, info, warning, error, critical) with retention periods scaled accordingly — debug logs rotate quickly while error and critical logs are retained long enough to support post-incident review and the security processes in [1206-Security.md](1206-Security.md).

## Structured Logging

All server logs use a structured (queryable) format rather than plain text, enabling the monitoring and analytics systems ([1216-Monitoring.md](1216-Monitoring.md), [2006-Analytics.md](../2000-Operations/2006-Analytics.md)) to efficiently search and aggregate log data during both routine operations and incident investigation.
