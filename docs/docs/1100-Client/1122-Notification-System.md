# 1122 — Notification System

**Project:** Elysium MMORPG  
**Category:** Client  
**Status:** Design Complete — Implementation Pending  
**Related:** [1108-UI-Systems.md](1108-UI-Systems.md) · [0704-Achievements.md](../0700-Quests/0704-Achievements.md) · [0810-Social-Features.md](../0800-Multiplayer/0810-Social-Features.md) · [1301-UI-Style.md](../1300-Art/1301-UI-Style.md)

---

## 1. Overview

The Notification System delivers timely, non-modal information to the player: quest updates, loot, achievements, social events, system messages, and warnings.

---

## 2. Types

| Type | Examples |
|------|----------|
| **Toasts** | Achievement earned, level up, rare loot |
| **Combat Text / Floating Combat Text** | Damage, healing, misses (optional) |
| **Chat / System Messages** | Zone changes, group events, errors |
| **Quest / Objective Updates** | Progress ticks, completion |
| **Social** | Friend online, guild messages, invites |

---

## 3. Design Rules

1. Notifications are prioritised so that critical combat information is never drowned out by social or cosmetic spam.
2. Players can configure density and types of notifications.
3. Visual and audio cues are distinct and consistent.
4. Accessibility options include text alternatives and reduced motion where relevant.


---

## Additional Detail: Notification Categories

Notifications are categorized (loot, achievement, social, system) with independently configurable display duration and position, letting players prioritize the notification types most relevant to their current activity (e.g. muting social notifications during a raid pull).

## Non-Intrusive Design

Notifications are designed to inform without obstructing critical combat UI elements, using edge-of-screen placement and fade timing tuned to avoid overlapping with action bars, health bars, or boss mechanic telegraphs.
