# 1420 — Production Deployment

**Project:** Elysium MMORPG  
**Category:** Development  
**Status:** Design Complete — Implementation Pending  
**Related:** [1408-Release-Process.md](1408-Release-Process.md) · [1230-Server-Maintenance.md](../1200-Technical/1230-Server-Maintenance.md) · [1100-Launcher.md](../1100-Client/1100-Launcher.md)

---

## 1. Overview

Production Deployment is the controlled process of shipping server, client, and data changes to live players.

---

## 2. Rules

- Follow the release checklist  
- Backups and rollback plans before risky changes  
- Launcher and server versions stay compatible  
- Post-deploy monitoring window is mandatory  


---

## Additional Detail: Deployment Automation

Production deployments are executed through automated deployment scripts rather than manual server-by-server steps, reducing the risk of human error during a process that directly affects live players, and ensuring deployments are consistently repeatable — see [1421-Build-Automation.md](1421-Build-Automation.md).

## Canary Deployment Consideration

Where infrastructure allows, deployments may roll out to a small subset of servers first (a canary deployment) before full rollout, catching environment-specific issues with limited player impact before they affect the entire playerbase.
