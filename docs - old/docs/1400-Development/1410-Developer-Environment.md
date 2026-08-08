# 1410 — Developer Environment

**Project:** Elysium MMORPG  
**Category:** Development  
**Status:** Design Complete — Implementation Pending  
**Related:** [1401-Coding-Standards.md](1401-Coding-Standards.md) · [1417-Development-Tools.md](1417-Development-Tools.md) · [1200-Plugin-Architecture.md](../1200-Technical/1200-Plugin-Architecture.md)

---

## 1. Overview

The Developer Environment is the standard local setup for engineers: JDK, Gradle, Paper/dev server, IDE config, database, and required tools so that “works on my machine” is minimised.

---

## 2. Components

- Agreed JDK and build tool versions  
- Local Paper (or equivalent) server with plugin hot-reload support  
- Local or containerised database matching production engine  
- EditorConfig / formatter / linter configs  
- Access to internal artifact and doc repositories  

---

## 3. Rules

Onboarding documentation must get a new engineer to a running local server quickly. Environment drift is treated as a bug.
