# 1413 — Documentation Standards

**Project:** Elysium MMORPG  
**Category:** Development  
**Status:** Design Complete — Implementation Pending  
**Related:** [0006-Documentation-Guide.md](../0000-Project/0006-Documentation-Guide.md) · [1400-Development-Standards.md](1400-Development-Standards.md) · [0002-Core-Pillars.md](../0000-Project/0002-Core-Pillars.md)

---

## 1. Overview

Documentation Standards define how GDD and technical docs are written, linked, and kept current. Documentation is part of development (Pillar 6).

---

## 2. Rules

- Use the established four-digit structure and linking style  
- Status lines and related links on major docs  
- Update docs in the same change set as behaviour changes when practical  
- Prefer clear prose and tables over ambiguity  
- Mark speculative content explicitly  


---

## Additional Detail: Documentation Freshness

Each `docs/` file's "Status" field (Living Document, Design Complete, etc.) is reviewed periodically to ensure it still accurately reflects implementation reality, with stale documents flagged for a review pass during each phase transition described in [0003-Roadmap.md](../0000-Project/0003-Roadmap.md).

## Cross-Linking Requirements

New documentation is required to cross-link to genuinely related existing documents rather than existing in isolation, keeping the `docs/` set navigable as a connected web of information rather than a flat, disconnected file list.
