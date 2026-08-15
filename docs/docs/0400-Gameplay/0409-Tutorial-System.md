# 0409 — Tutorial System

**Project:** Elysium MMORPG
**Category:** Gameplay
**Status:** Living Document
**Related:** [0400-Game-Mechanics.md](0400-Game-Mechanics.md) · [0100-World.md](../0100-World/0100-World.md), Section on Millhaven

---

## 1. Overview

The tutorial system introduces new players to Elysium's core systems gradually, embedded within the Southern Shires starting experience in Aurelia (see [0102-Regions.md](../0100-World/0102-Regions.md)) rather than as a separate, disconnected training area.

## 2. Design Principles

* Teach through doing, not through text walls — each mechanic is introduced via a short, low-stakes quest that requires using it.
* Never gate the player behind a mandatory tutorial screen that halts play.
* Reinforce, don't just introduce — early quests revisit taught mechanics in slightly varied contexts to build confidence.

## 3. Tutorial Sequence

1. **Movement and Camera** — introduced immediately on character creation, in Millhaven.
2. **Basic Attack and First Ability** — introduced via a low-threat combat encounter against a single weak enemy.
3. **Resource Management** — introduced once the player has 2–3 abilities, teaching cooldown and resource tradeoffs.
4. **Class Movement Ability** — introduced through a short traversal challenge.
5. **Interaction and Gathering** — introduced via a simple fetch quest involving a gathering node.
6. **Inventory and Equipment** — introduced when the player receives their first equipment upgrade.
7. **Grouping (optional)** — introduced through an optional, non-mandatory group quest for players who want to try cooperative play early.

## 4. Class-Specific Onboarding

Once a player selects their class (see [0310-Character-Creation.md](../0300-Characters/0310-Character-Creation.md)), a short class-specific quest chain introduces their unique kit and identity, ensuring the tutorial experience differs meaningfully by class rather than being fully generic.

## 5. Skip and Veteran Options

Experienced players (identified via account history) are offered a condensed tutorial path on subsequent characters, respecting their time while still ensuring core UI and control familiarity.

## 6. Accessibility

Tutorial prompts are designed to work with screen readers and remappable controls from the outset, in line with the accessibility standards in [1106-Accessibility.md](../1100-Client/1106-Accessibility.md).

## 7. Iteration

Tutorial completion and drop-off is tracked via analytics once live (see [2006-Analytics.md](../2000-Operations/2006-Analytics.md)) to identify friction points and iterate on pacing post-launch.
