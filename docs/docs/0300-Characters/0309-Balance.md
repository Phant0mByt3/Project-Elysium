# 0309 — Balance

**Project:** Elysium MMORPG
**Category:** Characters
**Status:** Design Complete — Implementation Pending
**Related Systems:** 0300-Classes.md · 0301-Specializations.md · 0302-Skills.md · 0303-Talent-Trees.md · 0304-Stats.md · 0305-Leveling.md · 0308-Class-Progression.md · 0401-Combat.md · 0804-PvP.md

---

## 1. Overview

Balance in Elysium is an ongoing process rather than a final pre-launch task.

The goal is not to make every class, specialisation, ability, or build mathematically identical. The goal is to ensure that every intended playstyle has a meaningful place in the game.

Balance work covers:

* Base classes
* Specialisations
* Skills
* Talent Trees
* Stats
* Gear
* Elements
* Class resources
* PvE
* PvP
* Endgame progression

Specific numerical values belong in version-specific balance data and patch notes rather than this document.

---

# 2. Core Balance Philosophy

Elysium follows five major balance principles.

### 2.1 Every Class Has a Purpose

Every class should have a clear identity.

A class should not exist simply because it fills the same role as another class.

For example:

* Paladin and Cleric can both heal, but should heal differently.
* Warrior and Paladin can both tank, but should have different defensive mechanics.
* Rogue and Ranger can both deal physical damage, but should play around different ranges and resources.

---

### 2.2 Every Specialisation Should Be Viable

Each specialisation should be capable of performing its intended role in meaningful content.

A specialisation does not need to be the highest-performing option.

It does need to be viable enough that players can choose it because they enjoy its gameplay rather than feeling forced into another option.

---

### 2.3 Builds Should Matter

Talent Trees should create real differences between builds.

Two players using the same class and specialisation should be able to make different choices without one build automatically invalidating the other.

Balance should therefore consider complete builds rather than individual abilities in isolation.

---

### 2.4 Power Should Have Trade-Offs

Strong abilities should have meaningful costs, limitations, cooldowns, positioning requirements, resource requirements, or opportunity costs.

An ability that is strong in one situation should generally have a reason not to use it in every situation.

---

### 2.5 Numbers Are Not the Only Form of Balance

Balance is not only:

```text
Damage = Damage
Healing = Healing
Health = Health
```

It also includes:

* Range
* Mobility
* Crowd control
* Defensive tools
* Utility
* Resource generation
* Cooldowns
* Ease of execution
* Group synergy
* Burst potential
* Sustained performance
* Target requirements
* Positioning requirements

A class with slightly lower raw damage may still be appropriately balanced if it provides significantly stronger utility or survivability.

---

# 3. PvE Balance

PvE balance is divided into three major areas.

## Questing

Every class should be capable of progressing through the open world without requiring another player.

Solo viability includes:

* Reasonable damage output
* Reliable survivability
* Access to class-appropriate utility
* Ability to handle normal enemy groups
* Reasonable downtime between encounters

Classes should not all kill enemies at the same speed.

Different classes may trade damage, survivability, mobility, and utility against each other.

---

## Dungeons

Dungeon balance focuses on group roles.

The three primary roles are:

* Tank
* Healer
* Damage

Every class capable of a role should have a meaningful way to contribute to that role.

Dungeon balance should also account for:

* Single-target damage
* Area damage
* Crowd control
* Interrupts
* Defensive cooldowns
* Group utility
* Mobility
* Encounter-specific mechanics

---

## Raids

Raid balance focuses more heavily on specialization and encounter requirements.

Not every specialisation needs to be optimal for every encounter.

Instead, raid encounters should naturally create situations where different strengths matter.

For example:

* Burst damage
* Sustained damage
* Area damage
* Cleave
* Defensive utility
* Healing throughput
* Mobility
* Crowd control
* Target switching

Raid encounters should avoid being designed around a single mandatory class whenever possible.

---

# 4. PvP Balance

PvP is balanced separately from PvE when necessary.

See [0804-PvP.md](../0800-Multiplayer/0804-PvP.md).

PvP may use separate modifiers for:

* Damage
* Healing
* Crowd control
* Defensive abilities
* Cooldowns
* Resource generation

A change made specifically for PvP should not automatically weaken a class in PvE unless the change is intended to affect both systems.

---

# 5. Class Balance

Class balance is evaluated at the base-class level first.

The eight launch classes are:

| Class       | Roles           |
| ----------- | --------------- |
| Warrior     | Tank / Damage   |
| Paladin     | Tank / Healer   |
| Rogue       | Damage          |
| Ranger      | Damage          |
| Mage        | Damage          |
| Necromancer | Damage          |
| Cleric      | Healer          |
| Druid       | Healer / Damage |

Each class should have a recognizable mechanical identity.

Balance should not erase those differences in an attempt to make classes symmetrical.

---

# 6. Specialisation Balance

Each class has two specialisations.

Specialisations should be compared primarily against other specialisations performing the same role.

For example:

```text
Warrior
├── Vanguard
└── Berserker
```

The goal is not:

```text
Vanguard = Berserker
```

The goal is:

```text
Vanguard
→ defensive frontline gameplay

Berserker
→ aggressive damage gameplay
```

Both should be strong within their intended roles.

---

# 7. Talent Tree Balance

Talent Trees are one of the largest sources of potential balance problems.

Every talent should have a clear reason to exist.

### Avoid:

* Mandatory talents
* Obvious filler nodes
* Completely useless choices
* One path being universally superior
* Talents that only increase numbers with no meaningful decision
* Talents that become mandatory for basic class functionality

### Encourage:

* Different playstyles
* Situational choices
* Build specialization
* Trade-offs
* Synergy between abilities
* Different approaches to different content

Capstone talents should be powerful enough to influence a build without becoming mandatory.

---

# 8. Skill Balance

Skills are evaluated using more than raw damage or healing.

Important variables include:

* Resource cost
* Cooldown
* Cast time
* Range
* Area of effect
* Target restrictions
* Damage type
* Status effects
* Utility
* Animation time
* Ability interactions

A powerful ability may be balanced by having:

* A long cooldown
* High resource cost
* Limited range
* Difficult positioning
* A specific target condition
* A meaningful opportunity cost

---

# 9. Resource Balance

Class resources should create gameplay decisions rather than simply limiting ability usage.

Examples include:

* Rage
* Mana
* Energy
* Combo Points
* Focus
* Essence
* Faith
* Nature or Spirit resources

Resource systems should be balanced around:

* Generation speed
* Maximum resource
* Spending efficiency
* Burst windows
* Resource starvation
* Resource overflow
* Recovery mechanics

No class should spend most of its combat time unable to use meaningful abilities because of poor resource design.

---

# 10. Stat Balance

Primary and secondary stats are balanced around their intended class and specialisation interactions.

See [0304-Stats.md](0304-Stats.md).

Important considerations include:

* Stat scaling
* Stat weights
* Diminishing returns
* Critical strike interactions
* Haste breakpoints
* Mastery scaling
* Versatility efficiency
* Armor scaling
* Resistance scaling

No secondary stat should become so universally powerful that it makes other stats irrelevant.

---

# 11. Elemental Balance

Elemental abilities should be balanced independently while maintaining their thematic identities.

See [0307-Elements.md](0307-Elements.md).

Elemental interactions should reward strategic combinations without creating mandatory class compositions.

For example:

```text
Frost
   ↓
Frozen
   ↓
Fire
   ↓
Shatter
```

Interactions should create opportunities for coordinated groups without making a specific Mage or class mandatory for successful content.

---

# 12. Gear and Class Balance

Gear should improve a character without completely replacing class skill.

Balance testing must consider:

```text
Base Class
    +
Specialisation
    +
Talents
    +
Stats
    +
Gear
    +
Player Skill
```

A poorly performing build should not automatically become strong simply because it has higher item level.

Likewise, high-quality gear should not make class mechanics irrelevant.

---

# 13. Endgame Balance

Level 50 is the launch level cap.

Endgame balance should focus on build refinement rather than uncontrolled vertical power growth.

Important systems include:

* Talent optimization
* Specialisation Mastery
* Legendary items
* Relics
* High-level gear
* Raid rewards
* Heroic dungeons

Endgame progression should not create a situation where fully geared characters trivialize all lower-level content permanently.

---

# 14. Balance Testing

Balance should be tested using controlled scenarios as well as normal gameplay.

### Controlled Testing

Used to isolate individual mechanics.

Examples:

* Single-target damage tests
* Area damage tests
* Healing throughput tests
* Defensive mitigation tests
* Resource generation tests

### Real Gameplay Testing

Used to measure how systems actually behave during:

* Questing
* Dungeons
* Raids
* PvP
* Open-world events

Both are required.

A class that performs perfectly on a training dummy may still perform poorly in real encounters.

---

# 15. Data Sources

Balance decisions should be informed by multiple sources.

### Combat Data

* Damage logs
* Healing logs
* Death statistics
* Damage taken
* Ability usage
* Cooldown usage
* Resource generation
* Resource spending

### Player Data

* Class popularity
* Specialisation popularity
* Talent choices
* Gear choices
* Completion rates
* Dungeon performance
* Raid performance
* PvP win rates

### Player Feedback

Community feedback should be considered alongside gameplay data.

Player feedback is useful for identifying:

* Abilities that feel bad to use
* Talents that feel pointless
* Classes that feel overly complicated
* Unfun mechanics
* Balance problems not visible in raw statistics

Feedback should not automatically determine balance changes.

---

# 16. Balance Thresholds

No single numerical threshold should automatically trigger a balance change.

For example, a specialisation being 2% behind another does not necessarily mean it requires a buff.

The development team should consider:

* Content difficulty
* Player skill
* Sample size
* Encounter type
* Build diversity
* Class popularity
* Intended role
* Utility
* Ease of execution

Large statistical differences are more concerning when they remain consistent across many types of content.

---

# 17. Overperformance

When a class or specialisation is significantly outperforming its intended position, the first step is identifying why.

Possible causes include:

* Excessive base numbers
* Talent synergy
* Item interaction
* Resource generation
* Cooldown interaction
* Elemental interaction
* Encounter design
* Gear scaling

Balance changes should target the underlying cause whenever possible rather than repeatedly reducing unrelated abilities.

---

# 18. Underperformance

Underperforming classes should not always receive raw damage or healing buffs.

Possible solutions include:

* Improving weak abilities
* Reworking talents
* Improving resource generation
* Reducing unnecessary complexity
* Improving utility
* Fixing ability interactions
* Improving survivability
* Adjusting cooldowns
* Improving specialization identity

The goal is to make the class feel better, not simply increase its damage-per-second number.

---

# 19. Balance Changes

Balance changes are divided into three levels.

### Minor

Small numerical adjustments.

Examples:

* Damage coefficient changes
* Cooldown changes
* Resource cost adjustments
* Minor talent changes

These can normally be included in regular balance patches.

### Moderate

Changes that alter a build's performance or rotation.

Examples:

* Talent reworks
* Ability interaction changes
* Resource generation changes
* Significant cooldown changes

These should be documented in the version history.

### Major

Changes that significantly alter class identity.

Examples:

* Specialisation redesign
* Major resource rework
* Role changes
* Talent Tree restructuring
* Core rotation replacement

Major changes require dedicated design documentation and should be clearly communicated to players.

---

# 20. Review Cadence

### Pre-Launch

Internal testing occurs after each major gameplay system is implemented.

Major balance passes should occur after:

* Classes
* Combat
* Skills
* Talent Trees
* Itemization
* Dungeons
* Raids
* PvP

### Alpha

Testing focuses on identifying fundamental class and system problems.

### Beta

Testing focuses on large-scale player data and real-world class interactions.

### Live Service

Balance is reviewed regularly alongside content updates.

Major changes should follow the release process defined in [1408-Release-Process.md](../1400-Development/1408-Release-Process.md).

---

# 21. Balance Documentation

Significant balance decisions should be recorded.

Major changes should include:

* What changed
* Why it changed
* What problem it addressed
* Expected result
* Actual result after release

Version-specific changes belong in [0004-Version-History.md](../0000-Project/0004-Version-History.md).

This document defines the philosophy and rules rather than individual patch values.

---

# 22. Balance Rules Summary

1. Every class must have a clear gameplay identity.
2. Every specialisation must be viable in its intended role.
3. No single build should dominate every content type.
4. PvE and PvP may use separate balance values.
5. Talent Trees must provide meaningful choices.
6. No talent should be mandatory simply to make a class functional.
7. Class resources must create meaningful gameplay decisions.
8. Secondary stats should remain useful without allowing one-stat dominance.
9. Elemental interactions should reward coordination without creating mandatory compositions.
10. Gear should enhance class identity rather than replace it.
11. Level 50 is the launch level cap.
12. Endgame progression should favor build refinement over uncontrolled power inflation.
13. Balance decisions should use gameplay data and player feedback.
14. Major class identity changes require deliberate documentation.
15. Balance should preserve the intended fantasy of every class and specialisation.

---

## 23. Design Principle

The ultimate balance goal is not perfect equality.

The goal is:

> Every class should have a reason to be played, every specialisation should have a reason to be chosen, and every build should have situations where it shines.
