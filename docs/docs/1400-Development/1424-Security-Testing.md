# 1424 — Security Testing

**Project:** Elysium MMORPG  
**Category:** Development  
**Status:** Design Complete — Implementation Pending  
**Related:** [1206-Security.md](../1200-Technical/1206-Security.md) · [1207-Anti-Cheat.md](../1200-Technical/1207-Anti-Cheat.md) · [1406-Testing.md](1406-Testing.md)

---

## 1. Overview

Security Testing probes authentication, economy integrity, privilege boundaries, and common exploit classes before and after release.

---

## 2. Rules

- Sensitive systems get explicit test cases  
- Findings are triaged by severity with fast paths for critical issues  
- External review may be scheduled before major public launches  


---

## Additional Detail: Penetration Testing Cadence

Beyond continuous automated security scanning, periodic manual penetration testing (internal or third-party) is scheduled ahead of major milestones (Closed Beta, Public Release) to catch vulnerabilities that automated tools alone might miss, coordinated with [1206-Security.md](../1200-Technical/1206-Security.md).

## Economy Exploit Testing

Given the real value players place in in-game currency and items, security testing includes dedicated economy exploit scenarios (duplication attempts, transaction race conditions) as a distinct testing category from general application security.
