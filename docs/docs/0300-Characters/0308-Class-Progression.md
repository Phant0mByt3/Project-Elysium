# 0308 — Class Progression

**Project:** Elysium MMORPG
**Category:** Characters
**Status:** Design Complete — Implementation Pending
**Related Systems:** [0300-Classes.md](0300-Classes.md) · [0301-Specializations.md](0301-Specializations.md) · [0302-Skills.md](0302-Skills.md) · [0303-Talent-Trees.md](0303-Talent-Trees.md) · [0305-Leveling.md](0305-Leveling.md) · [0309-Balance.md](0309-Balance.md) · [../0400-Gameplay/0400-Game-Mechanics.md](../0400-Gameplay/0400-Game-Mechanics.md) · [../0400-Gameplay/0401-Combat.md](../0400-Gameplay/0401-Combat.md)

---

## 1. Overview

Class Progression is the connective layer that ties together every character-facing system in Elysium. Where [0300-Classes.md](0300-Classes.md) defines *what a class is*, [0302-Skills.md](0302-Skills.md) defines *what a class can do*, and [0303-Talent-Trees.md](0303-Talent-Trees.md) defines *how a class specializes*, this document defines *how a character moves through all of that over time*.

Class Progression answers a single design question: **as a player levels up, in what order and by what rules do they gain access to their class's identity?**

Progression in Elysium is deliberately non-linear in feel but fully deterministic under the hood — every unlock is level-gated and milestone-gated, never random, so players can plan a build from level 1 without guesswork.

### 1.1 Design Goals

- **Clarity** — a player should always know what their *next* unlock is and at what level it arrives.
- **Identity early, mastery late** — core class fantasy (e.g. a Mage's first fireball) should land in the first hour; full build expression arrives at endgame.
- **No dead levels** — every level should grant *something* tangible: a skill point, a talent point, a passive tick, or a milestone.
- **Respec-friendly** — progression unlocks access; talent/skill allocation remains flexible (see [0303-Talent-Trees.md](0303-Talent-Trees.md) §Respeccing).

---

## 2. How Players Advance Their Chosen Class

Advancement is driven by three parallel currencies, all fed by the same source (character level, from [0305-Leveling.md](0305-Leveling.md)) but spent in different systems:

| Currency | Earned From | Spent In |
|---|---|---|
| **Skill Points** | Every character level | [0302-Skills.md](0302-Skills.md) — unlocking/ranking active & passive skills |
| **Talent Points** | Every odd character level (1, 3, 5…) starting at level 10 | [0303-Talent-Trees.md](0303-Talent-Trees.md) — talent tree nodes |
| **Mastery Points** | Class milestones only (not every level) | Specialisation Evolution & Advanced Class Paths (this document, §9–§10) |

A player's overall progression is therefore the sum of three trees growing at different rates, converging at milestone levels where the game pauses to let the player make a defining choice (e.g. choosing a specialisation at level 20).

---

## 3. Relationship Between Classes, Specialisations, Skills, Talents, and Levels

```text
                     ┌───────────────────┐
                     │   0300-Classes     │   WHO you are (Mage, Warrior, Druid...)
                     └─────────┬──────────┘
                               │ chosen at character creation
                     ┌─────────▼──────────┐
                     │ 0305-Leveling       │   WHEN things unlock (drives all point income)
                     └─────────┬──────────┘
              ┌────────────────┼────────────────┐
     ┌────────▼───────┐ ┌──────▼───────┐ ┌───────▼────────┐
     │ 0302-Skills     │ │0303-Talent-  │ │0301-Special-    │
     │ WHAT you can do │ │Trees         │ │isations         │
     │                 │ │HOW you play  │ │WHO you become   │
     └────────┬────────┘ └──────┬───────┘ └───────┬────────┘
              └──────────────────┼──────────────────┘
                                  │
                        ┌─────────▼──────────┐
                        │ 0308-Class-         │   THIS DOCUMENT
                        │ Progression          │   the timeline that binds
                        │ (this document)      │   all of the above together
                        └─────────┬──────────┘
                                  │
                        ┌─────────▼──────────┐
                        │ 0309-Balance         │   ensures no path outperforms
                        └────────────────────┘   another at the same level
```

**In short:**
- **Class** is the container.
- **Leveling** is the clock.
- **Skills** are the verbs.
- **Talents** are the modifiers.
- **Specialisation** is the identity branch.
- **Class Progression** is the schedule that says when each of the above becomes available.
- **Balance** validates that the schedule produces fair outcomes across all classes.

---

## 4. Starting Class Progression (Levels 1–9)

The first nine levels exist to teach class fantasy fast, with zero decision paralysis.

| Level | Unlock | System |
|---|---|---|
| 1 | Class chosen, starting weapon, 1 basic attack | [0300-Classes.md](0300-Classes.md) |
| 2 | First active ability (bound to `Q`, see [../1100-Client/1107-Controls.md](../1100-Client/1107-Controls.md)) | [0302-Skills.md](0302-Skills.md) |
| 3 | First passive skill | [0302-Skills.md](0302-Skills.md) |
| 4 | Second active ability (`E`) | [0302-Skills.md](0302-Skills.md) |
| 5 | First Talent Point banked (spend opens at 10) | [0303-Talent-Trees.md](0303-Talent-Trees.md) |
| 6 | Third active ability (`R`) | [0302-Skills.md](0302-Skills.md) |
| 7 | Resource system fully unlocked (e.g. full mana pool, combo points) | [../0400-Gameplay/0401-Combat.md](../0400-Gameplay/0401-Combat.md) |
| 8 | Fourth active ability (`T`) | [0302-Skills.md](0302-Skills.md) |
| 9 | Class movement ability unlocked (`ALT`) | [../0400-Gameplay/0401-Combat.md](../0400-Gameplay/0401-Combat.md) |

> **Developer Note:** Levels 1–9 intentionally never require a player-facing decision beyond stat allocation. All four core ability slots (`Q E R T`) are filled automatically in a fixed order so early combat always feels complete, never half-built.

---

## 5. Unlocking Abilities

Abilities unlock through two channels:

1. **Level-gated unlocks** — automatic, tied to the table above and to milestone levels (§7).
2. **Talent-gated unlocks** — optional, spent from the Talent Tree once a prerequisite level and node are reached (see [0303-Talent-Trees.md](0303-Talent-Trees.md)).

| Unlock Type | Source | Example |
|---|---|---|
| Core ability | Level threshold | Level 2 Mage gains *Firebolt* |
| Talent-locked ability | Talent Point spent on a keystone node | Level 30 Mage spends a keystone talent to unlock *Meteor* |
| Specialisation ability | Choosing a specialisation at level 20 | *Fire Mage* gains *Combustion* |
| Milestone ability | Reaching a class milestone | Level 50 grants every class one **Signature Ability** |

**Rule:** an ability's *unlock level* is fixed and identical across all players of that class — this is what [0309-Balance.md](0309-Balance.md) audits against. What players choose is *which optional branch* of abilities to invest points into, not *when* core power spikes happen.

---

## 6. Passive Progression

Passive progression represents growth that happens without the player pressing a button — it is felt, not activated.

| Passive Layer | Description | Growth Curve |
|---|---|---|
| **Stat scaling** | Base stats (from [0304-Stats.md](0304-Stats.md)) increase automatically per level | Linear |
| **Passive skill ranks** | Passive skills gain rank via Skill Points, increasing their effect magnitude | Stepped (5 ranks per passive) |
| **Elemental affinity growth** | Classes tied to an element (see [0307-Elements.md](0307-Elements.md)) gain a small passive resistance/damage bonus per 10 levels | Stepped |
| **Talent passives** | "Minor nodes" in the Talent Tree that grant flat, always-on bonuses | Player-chosen, stacking |

**Example — Druid passive growth:**

| Level | Passive Effect |
|---|---|
| 1 | +2% Nature damage (base) |
| 10 | +4% Nature damage, +5% out-of-combat move speed |
| 20 | +6% Nature damage, unlocks *Regrowth* passive healing-over-time |
| 30 | +8% Nature damage, +10% healing received while shapeshifted |

---

## 7. Active Ability Progression

Active abilities progress along two axes: **rank** (power) and **modification** (behavior change).

- **Ranking** costs Skill Points and increases damage/healing/duration in fixed steps (see table in [0302-Skills.md](0302-Skills.md)).
- **Modification** is unlocked via Talent Tree nodes that change *how* an ability behaves (e.g. *Firebolt* becomes a piercing projectile) rather than simply increasing its numbers.

| Rank | Skill Points Required (cumulative) | Typical Power Increase |
|---|---|---|
| Rank 1 | 1 | Baseline (unlock) |
| Rank 2 | 3 | +15% |
| Rank 3 | 6 | +30% |
| Rank 4 | 10 | +45% |
| Rank 5 (Max) | 15 | +60% + minor behavior bonus (e.g. reduced cooldown) |

> **Developer Note:** Rank costs are intentionally quadratic-ish (1, 2, 3, 4, 5 additional points per rank) so that maxing a single ability early is a genuine opportunity cost against breadth. This interacts directly with [0309-Balance.md](0309-Balance.md)'s "breadth vs. depth" balance pass.

---

## 8. Class Milestones

Milestones are fixed levels at which the game pauses normal drip-feed progression to deliver a meaningful, class-defining moment. Milestones are identical in *level number* across all classes (for balance and content-pacing reasons) but unique in *content* per class.

| Level | Milestone | System Touched |
|---|---|---|
| 10 | Talent Tree unlocked | [0303-Talent-Trees.md](0303-Talent-Trees.md) |
| 20 | **Specialisation Choice** (see §9) | [0301-Specializations.md](0301-Specializations.md) |
| 30 | First Keystone Talent available | [0303-Talent-Trees.md](0303-Talent-Trees.md) |
| 40 | Advanced Class Path preview quest unlocked (see §10) | [0400-Gameplay/0400-Game-Mechanics.md](../0400-Gameplay/0400-Game-Mechanics.md) |
| 50 | Signature Ability granted; Advanced Class Path selection | This document, §10 |
| 60 (cap) | Endgame Class Progression begins (see §11) | This document, §11 |

Milestones are the only points at which progression is **gated by content**, not just by point spend — e.g. the level 20 specialisation choice requires completing a short class quest, ensuring narrative and mechanical progression stay in sync (see [0207-Main-Story.md](../0200-Lore/0207-Main-Story.md) for how class quests tie into the wider story).

---

## 9. Specialisation Evolution

At level 20, a player commits to one of their class's specialisations (defined in [0301-Specializations.md](0301-Specializations.md)). This is not a one-time flat bonus — the specialisation *evolves* at further milestones.

| Level | Specialisation State |
|---|---|
| 20 | Specialisation chosen — unlocks specialisation-exclusive ability + passive |
| 35 | Specialisation Tier 1 evolution — ability gains a secondary effect |
| 50 | Specialisation Tier 2 evolution — ability gains a third effect, visual upgrade |
| 60 | Specialisation Mastery — ability reaches final form, unlocks Mastery Point sink |

**Example — Fire Mage specialisation evolution:**

| Level | *Combustion* Ability State |
|---|---|
| 20 | Deals fire damage over time to target |
| 35 | Also spreads to nearby enemies on target death |
| 50 | Also grants the Mage a stacking damage buff per target burning |
| 60 | Fully evolved into *Combustion: Wildfire* — persistent, refreshes on crit |

Respeccing a specialisation is possible (see [0301-Specializations.md](0301-Specializations.md) §Respeccing) but resets specialisation evolution progress; base class level and Talent Points are unaffected.

---

## 10. Advanced Class Paths

At level 40–50, each base class branches into **two Advanced Class Paths** — a deeper identity layer above specialisation, unlocked via a class quest chain rather than points alone.

| Base Class | Advanced Path A | Advanced Path B |
|---|---|---|
| Mage | Archmage (control/utility) | Battlemage (burst/melee-hybrid) |
| Warrior | Warlord (tank/leadership) | Berserker (pure damage) |
| Druid | Warden (shapeshift/tank) | Sage (healing/support) |

Advanced Class Paths grant:
- A unique passive that alters a core resource rule (see [../0400-Gameplay/0401-Combat.md](../0400-Gameplay/0401-Combat.md))
- Access to a small pool of path-exclusive abilities
- A distinct visual effect on existing abilities (see [../1300-Art/1306-Models.md](../1300-Art/1306-Models.md))

**Rule:** Advanced Class Path choice does **not** override specialisation — the two systems stack. A Fire Mage can become either an Archmage or a Battlemage, producing four distinct level-60 identities per base class before Legendary upgrades (§12) are even considered.

---

## 11. Endgame Class Progression (Level 60+)

Once a character reaches the level cap, vertical (level) progression stops and **horizontal progression** takes over, spent through Mastery Points earned from endgame content (raids, world bosses, high-tier quests — see [../0800-Multiplayer/0802-Raiding.md](../0800-Multiplayer/0802-Raiding.md) and [../0100-World/0108-World-Bosses.md](../0100-World/0108-World-Bosses.md)).

| Endgame System | Currency | Effect |
|---|---|---|
| Mastery Tree | Mastery Points | Small, stacking percentage bonuses to the chosen specialisation |
| Legendary Upgrades | Legendary Items (see [../0500-Items/0505-Legendary-Items.md](../0500-Items/0505-Legendary-Items.md)) | Ability-transforming effects (§12) |
| Relic Slots | Relics (see [../0500-Items/0506-Relics.md](../0500-Items/0506-Relics.md)) | Passive-only bonuses, no active changes |

Endgame progression is intentionally horizontal (not raw power inflation) to keep world content relevant — see [0309-Balance.md](0309-Balance.md) §Endgame Power Curve for the numeric caps that keep Mastery bonuses from outweighing base kit design.

---

## 12. Legendary Class Upgrades

Legendary Items are the final layer of class progression. Unlike talents or specialisation nodes, Legendary effects are **found or crafted**, not simply unlocked by level, tying class progression directly into the itemization loop.

| Legendary Slot | Effect Type | Example |
|---|---|---|
| Weapon Legendary | Transforms one active ability entirely | Mage staff: *Firebolt* becomes a chain-bounce projectile |
| Armour Legendary | Adds a new passive trigger | Warrior chestplate: blocking grants a stacking damage buff |
| Accessory Legendary | Alters resource generation | Druid amulet: shapeshifting no longer costs resource |

A character can equip a limited number of Legendary effects at once (see [../0500-Items/0505-Legendary-Items.md](../0500-Items/0505-Legendary-Items.md) for slot rules), forcing endgame build decisions that are qualitatively different from the talent/skill decisions made while leveling.

---

## 13. Future Expansion Compatibility

Class Progression is built to extend without breaking existing characters:

- **New milestone levels** can be inserted at any future level cap increase (e.g. a level 70 cap adds a new milestone row to §8) without altering existing unlock levels below it.
- **New Advanced Class Paths** can be added per class without touching the base 1–20 progression, since paths only branch at level 40+.
- **New Legendary tiers** slot into §12 without changing the talent/skill/specialisation math, keeping itemization and progression as separable systems.
- Expansion-specific systems (see [../1500-Expansions/](../1500-Expansions/)) should hook into this document via new milestone rows rather than modifying existing ones, to preserve backward compatibility for existing characters.

> **Developer Note:** Whenever a future expansion adds a new resource (a "fourth currency" beyond Skill/Talent/Mastery Points), it must be documented as an addition to the table in §2, and cross-referenced here before being implemented — this file is the source of truth for "what currency unlocks what, and when."

---

## 14. System Rules Summary

1. Unlock **levels** are fixed per class and identical in position across classes (balance requirement).
2. Unlock **content** is unique per class (identity requirement).
3. Skill Points accrue every level; Talent Points accrue every odd level from 10 onward; Mastery Points accrue only from milestone/endgame content.
4. Specialisation is chosen once per "build slot" but can evolve automatically at fixed levels without further player input.
5. Advanced Class Paths and Specialisations are independent, stacking systems.
6. Endgame progression must be horizontal, not vertical — see [0309-Balance.md](0309-Balance.md) for the enforced power ceiling.
7. All new expansion content extends this document via new milestone rows, never by editing existing unlock levels.

---

## 15. Open Questions / Future Design Work

- Should Advanced Class Path be respeccable, or a permanent choice per character (currently leaning permanent, pending [0309-Balance.md](0309-Balance.md) review)?
- Should Mastery Points be account-wide or per-character? (Affects alt-friendliness vs. endgame investment weight.)
- Legendary effect acquisition rate needs a first pass from the Itemization team before §12 numeric drop rates can be finalized.
