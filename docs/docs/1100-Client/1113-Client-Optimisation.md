# 1113 — Client Optimisation

**Project:** Elysium MMORPG  
**Category:** Client  
**Status:** Design Complete — Implementation Pending  
**Related:** [1208-Performance.md](../1200-Technical/1208-Performance.md) · [1105-Shaders.md](1105-Shaders.md) · [1101-Client-Modules.md](1101-Client-Modules.md) · [1106-Accessibility.md](1106-Accessibility.md)

---

## 1. Overview

Client Optimisation ensures that Elysium remains playable and visually coherent across a wide range of hardware, from minimum-spec machines to high-end setups. It covers rendering, entity counts, UI cost, and configuration options.

---

## 2. Focus Areas

| Area | Approaches |
|------|------------|
| **Rendering** | LOD, distance culling, texture and model budgets |
| **Entities** | Caps and prioritisation in crowded scenes (raids, cities, world events) |
| **UI** | Efficient updates, optional reduction of animated elements |
| **Rendering & Effects** | Tiered quality presets |
| **Background work** | Controlled streaming and preloading |

---

## 3. Design Rules

1. Minimum-spec targets are real requirements, not aspirations.
2. Players can trade visual fidelity for performance via clear presets and granular options.
3. Optimisation never silently removes gameplay-critical information (nameplates, telegraphs, etc.).
4. Changes that affect performance are tested on representative hardware before release.

---

## 4. Technical Notes

Optimisation work is shared between the native client moduleule stack, content pack guidelines, and any custom rendering code. Profiling tools and automated performance checks are part of the development pipeline.


---

## Additional Detail: Optimization Targets

Optimization work is prioritized by measured impact — texture streaming and LOD tuning for open-world performance, draw-call batching for large group encounters (raids, world bosses), and network prediction smoothing for combat responsiveness — rather than optimizing uniformly across all systems regardless of actual bottleneck data.

## Continuous Performance Monitoring

Post-launch, client performance telemetry (opt-in, anonymized) feeds into the analytics pipeline ([2006-Analytics.md](../2000-Operations/2006-Analytics.md)), helping the technical team identify real-world performance issues across the diverse hardware the actual playerbase uses, beyond internal QA hardware.
