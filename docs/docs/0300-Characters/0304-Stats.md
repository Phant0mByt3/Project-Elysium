# 0304 — Stats

## Overview

Stats determine the power, survivability and effectiveness of an Elysium character.

They interact with classes, specializations, skills, talents, equipment and combat.

Stats are divided into:

* Primary Stats
* Secondary Stats
* Defensive Stats
* Resource Stats

The exact importance of each stat depends on the character's class and specialization.

---

# Primary Stats

## Strength

Strength represents physical power and weapon force.

It primarily increases physical damage for strength-based combat styles.

Strength may also improve certain defensive or physical abilities depending on the specialization.

**Common users:**

* Vanguard
* Oathkeeper
* Wildshaper

---

## Intellect

Intellect represents magical knowledge and mental power.

It primarily increases magical damage and healing effectiveness.

**Common users:**

* Arcanist
* Warden
* Oathkeeper

---

## Agility

Agility represents speed, precision and physical coordination.

It primarily improves finesse-based physical attacks and may increase Critical Strike Chance.

**Common users:**

* Shade
* Wayfarer

Agility may also be useful to other specializations depending on their mechanics.

---

## Stamina

Stamina represents physical endurance.

It increases maximum health and contributes to survivability.

Stamina is valuable to every class, although its importance varies depending on role.

---

# Secondary Stats

## Critical Strike Chance

Determines the chance for an attack or healing effect to critically strike.

Critical effects deal increased damage or healing depending on the ability.

Some classes and specializations may have additional mechanics that interact with Critical Strike.

---

## Haste

Haste improves the speed at which a character performs actions.

Depending on the ability, Haste can affect:

* Ability cooldowns
* Cast times
* Attack speed
* Damage-over-time intervals
* Healing-over-time intervals
* Resource generation

Not every ability is affected by Haste.

---

## Mastery

Mastery is a specialization-focused stat.

Each specialization has its own Mastery effect that strengthens its defining mechanic.

For example:

```text
Berserker Mastery
Increases the effectiveness of Rage-based abilities.

Grovekeeper Mastery
Increases the effectiveness of healing-over-time effects.

Marksman Mastery
Increases damage dealt from long-range attacks.
```

Mastery should feel different for every specialization rather than being a universal percentage increase.

Exact Mastery effects are documented alongside individual specialization designs.

---

## Versatility

Versatility provides a general increase to combat effectiveness.

It increases:

* Damage dealt
* Healing performed
* Damage reduction

Versatility is intended to provide a reliable baseline stat that remains useful across different builds.

---

# Defensive Stats

## Armor

Armor reduces incoming physical damage.

Armor is primarily provided by equipment and may also be increased through abilities or talents.

The effectiveness of Armor depends on the attacker's damage type and the character's level.

---

## Resistance

Resistance reduces incoming elemental damage.

Different forms of Resistance may apply to different elemental damage types.

Examples include:

* Fire Resistance
* Frost Resistance
* Lightning Resistance
* Nature Resistance
* Shadow Resistance

Resistance is particularly relevant to certain enemies, encounters and equipment choices.

See [0307-Elements.md](0307-Elements.md).

---

# Resource Stats

Some classes use unique combat resources.

Resources are separate from the primary and secondary stat systems.

Examples include:

| Class / Specialization | Possible Resource |
| ---------------------- | ----------------- |
| **Vanguard**           | Resolve / Rage    |
| **Arcanist**           | Mana              |
| **Shade**              | Energy            |
| **Warden**             | Nature / Spirit   |
| **Oathkeeper**         | Faith             |
| **Wayfarer**           | Focus             |

These names and mechanics are subject to class design.

Resource generation and spending should be primarily controlled by abilities, talents and combat actions rather than simply stacking a resource-related stat.

---

# Stat Priorities

Different specializations naturally prefer different statistics.

Example:

```text
Berserker
Strength
Critical Strike
Haste
Mastery

Frostweaver
Intellect
Haste
Mastery
Critical Strike

Shadowblade
Agility
Critical Strike
Haste
Mastery

Grovekeeper
Intellect
Haste
Mastery
Versatility
```

These are examples rather than fixed stat priorities.

Stat weights should change based on build, equipment and content.

---

# Stat Scaling

Stats should scale smoothly throughout the leveling experience.

Early-game increases should feel meaningful without making low-level characters excessively weak compared to higher-level characters.

The system should avoid requiring major stat squishes whenever a new expansion is released.

Stat values should therefore be designed around scalable formulas rather than endlessly increasing flat numbers.

See [0305-Leveling.md](0305-Leveling.md).

---

# Diminishing Returns

Secondary stats use diminishing returns after reaching certain thresholds.

This prevents players from stacking a single statistic indefinitely.

For example:

```text
0–20%
Normal effectiveness

20–30%
Reduced effectiveness

30–40%
Further reduced effectiveness

40%+
Strong diminishing returns
```

The actual thresholds and curves are implementation details and may change during balance testing.

Diminishing returns should encourage balanced builds without making specialized builds impossible.

---

# Stat Conversion

Some abilities and talents may temporarily convert one statistic into another.

Examples:

```text
A Warden talent may convert a portion of
Intellect into additional Nature damage.

A Vanguard ability may temporarily convert
defensive power into offensive power.
```

Permanent stat conversion should be used carefully to prevent confusing itemization.

---

# Gear Interaction

Stats are one of the main ways equipment differentiates itself beyond raw item level.

Different weapons and armour pieces may emphasize different statistics.

For example:

```text
Heavy Vanguard weapon
Strength + Stamina

Arcanist staff
Intellect + Haste

Shade daggers
Agility + Critical Strike

Oathkeeper shield
Strength + Stamina + Versatility

Wayfarer bow
Agility + Critical Strike
```

Players should be encouraged to evaluate equipment based on their build rather than automatically equipping the item with the highest item level.

See [0500-Weapons.md](../0500-Items/0500-Weapons.md) and the rest of the Itemization documentation.

---

# Stat Budget

Equipment uses a controlled stat budget.

Higher-level equipment should generally provide more total statistical power, but the distribution of that power can vary.

For example:

```text
Item A
+100 Strength
+40 Critical Strike

Item B
+70 Strength
+70 Haste

Item C
+50 Strength
+90 Versatility
```

All three can be useful for different builds.

This allows itemization to support meaningful choices rather than a single obvious upgrade path.

---

# Stat Scaling by Role

Different roles value different defensive statistics.

### Tank

Typically values:

* Stamina
* Armor
* Versatility
* Mastery
* Class-specific defensive stats

### Healer

Typically values:

* Intellect
* Haste
* Mastery
* Critical Strike
* Versatility

### Damage

Typically values:

* Primary offensive stat
* Critical Strike
* Haste
* Mastery
* Versatility

Exact stat priorities are specialization-specific.

---

# Design Philosophy

Stats should support gameplay rather than replace it.

A stronger character should not simply have larger numbers.

The most important source of power should remain a combination of:

* Player decisions
* Skills
* Talents
* Specialization mechanics
* Equipment
* Stats

A well-built character should feel stronger because their systems work together, not because one statistic has been stacked to an extreme level.

---

# Design Rules

1. Every class must have at least one useful primary-stat configuration.
2. Every specialization must have a meaningful Mastery effect.
3. No secondary stat should be mandatory for every specialization.
4. Diminishing returns should prevent extreme stat stacking.
5. Stats should scale smoothly across expansions.
6. Equipment should provide meaningful stat choices.
7. Stat priorities should vary between specializations.
8. Talents may modify stat interactions but should not make the underlying system confusing.
9. Defensive stats should remain relevant throughout progression.
10. Stats should complement skill and talent mechanics rather than replace them.
11. Exact formulas should be tested across leveling, endgame PvE and PvP.
12. Stat balance is part of the ongoing balance process documented in [0309-Balance.md](0309-Balance.md).

---

# Formula Philosophy

Stat formulas should scale smoothly across the leveling range.

The system should avoid requiring hard stat squishes at expansion boundaries.

Secondary stats should use diminishing-return curves where necessary to prevent single-stat itemization dominance.

Exact formulas, coefficients, level scaling and diminishing-return curves are engineering and balance tasks tracked through [0003-Roadmap.md](../0000-Project/0003-Roadmap.md).
