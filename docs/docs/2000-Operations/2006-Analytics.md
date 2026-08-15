# 2006 — Analytics

**Project:** Elysium MMORPG
**Category:** Operations
**Status:** Living Document
**Related:** [2015-Game-Metrics.md](2015-Game-Metrics.md) · [2016-Player-Retention.md](2016-Player-Retention.md) · [1216-Monitoring.md](../1200-Technical/1216-Monitoring.md)

---

## 1. Overview

Analytics covers the collection, aggregation, and interpretation of gameplay data used to inform live-service decisions, distinct from the technical health monitoring described in [1216-Monitoring.md](../1200-Technical/1216-Monitoring.md), though built on similar underlying infrastructure.

## 2. Data Categories

* **Engagement** — session length, login frequency, feature usage.
* **Progression** — leveling pace, quest completion rates, dungeon/raid clear rates.
* **Economy** — currency flow, Auction House activity, material prices ([1000-Economy.md](../1000-Economy/1000-Economy.md)).
* **Retention** — new player funnel, churn indicators ([2016-Player-Retention.md](2016-Player-Retention.md)).

## 3. Privacy Principles

Analytics collection is scoped to gameplay-relevant data, anonymized or aggregated wherever individual identification isn't necessary for the analysis, and disclosed clearly in the game's privacy policy.

## 4. Use in Design Decisions

Analytics inform, rather than dictate, design decisions — a metric showing low engagement with a system prompts investigation and design review, not an automatic removal, consistent with the principle in [2000-Live-Service.md](2000-Live-Service.md) that "metrics inform decisions without replacing design judgment."

## 5. Dashboards and Reporting

Key metrics are surfaced through regularly reviewed dashboards accessible to relevant team members, with deeper ad-hoc analysis available for specific investigations (e.g. diagnosing a sudden drop in a specific dungeon's completion rate).

## 6. A/B Testing

Where appropriate, targeted experiments (comparing two onboarding flows, for example) may be run on a subset of players to validate design decisions with real data before a full rollout, always disclosed in the privacy policy and scoped to non-sensitive, quality-of-life-focused changes.

## 7. Ownership

Analytics infrastructure is owned by the Technical Lead; analytics interpretation and design response is a shared responsibility between the Lead Game Designer and the relevant discipline leads, per [0007-Team-Structure.md](../0000-Project/0007-Team-Structure.md).
