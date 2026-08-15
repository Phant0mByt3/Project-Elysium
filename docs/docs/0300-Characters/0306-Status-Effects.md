# 0306 — Status Effects

## Overview

Status effects are temporary effects that modify a character, enemy, ability or combat encounter.

They are a core part of Elysium's combat system and are used to create meaningful interactions between classes, specializations, abilities and elemental mechanics.

Status effects are divided into four primary categories:

* Buffs
* Debuffs
* Crowd Control
* Elemental Conditions

Status effects may be applied by:

* Player abilities
* Talents
* Equipment
* Consumables
* Enemies
* Boss mechanics
* Environmental hazards
* Elemental interactions

---

# Buffs

Buffs are positive effects applied to a player or allied target.

Examples include:

* Increased damage
* Increased healing
* Increased movement speed
* Increased Haste
* Increased Armor
* Shields
* Damage reduction
* Resource regeneration
* Increased Critical Strike Chance

Buffs can be temporary or persistent.

Example:

```text
Blessing of Dawn
Increases healing received by 10%
for 15 seconds.
```

Buffs should generally have a clear visual indicator and appear in the player's status interface.

---

# Debuffs

Debuffs are negative effects applied to enemies or players.

Examples include:

* Damage over time
* Armor reduction
* Reduced healing
* Reduced movement speed
* Reduced damage
* Reduced attack speed
* Reduced resistance
* Increased damage taken

Example:

```text
Sundered Armor
Reduces the target's Armor by 15%
for 10 seconds.
```

Debuffs are particularly important for coordinated group combat.

Players should be able to identify important debuffs without needing to inspect every minor effect individually.

---

# Damage Over Time

Damage-over-time effects deal damage periodically rather than immediately.

Common examples include:

* Bleeding
* Burning
* Poison
* Shadow damage
* Arcane corruption

DoT effects should use predictable tick intervals.

For example:

```text
Bleeding
Deals physical damage every 2 seconds
for 10 seconds.
```

Different abilities may use different durations and tick frequencies, but the timing should remain consistent enough for players to understand.

---

# Healing Over Time

Healing-over-time effects restore health periodically.

Examples include:

* Regeneration
* Nature-based healing
* Renewing magic
* Healing spores

HoTs are particularly important for healing specializations.

Example:

```text
Rejuvenation
Restores health every 2 seconds
for 12 seconds.
```

Multiple HoTs may be active on the same target.

---

# Crowd Control

Crowd Control, commonly abbreviated as **CC**, limits an enemy or player's ability to act.

CC is divided into several categories.

## Stun

Prevents the target from performing actions.

Example:

```text
Hammerstrike
Stuns the target for 3 seconds.
```

---

## Root

Prevents movement while allowing the target to perform some actions.

Example:

```text
Entangling Roots
Roots the target for 5 seconds.
```

---

## Silence

Prevents the target from using magical or spell-based abilities.

Physical abilities may remain available depending on the target.

---

## Fear

Forces the target to lose control and move unpredictably for the duration.

Fear effects should be used carefully in group content because uncontrolled movement can interfere with encounter mechanics.

---

## Disorient

Temporarily prevents normal actions without necessarily forcing movement.

Disorient effects are primarily intended for tactical or PvP situations.

---

## Polymorph

Transforms the target into another form and prevents normal combat actions.

Polymorph-style abilities should generally break when the target takes significant damage.

---

## Slow

Reduces movement speed without completely preventing movement.

Slows are generally less restrictive than roots and are useful for controlling groups of enemies.

---

## Knockback

Forcibly moves the target away from the caster or toward a specified location.

Knockbacks may interact with the environment.

For example, players may be able to knock enemies from elevated platforms.

---

# Crowd Control Immunity

Some enemies have resistance or immunity to specific CC types.

Bosses will generally have strong CC resistance or complete immunity to hard-control effects.

Instead of completely disabling bosses, encounter mechanics may allow limited versions of CC.

For example:

```text
Boss:
Immune to Stun

Interrupt:
Still possible

Slow:
50% effectiveness

Knockback:
Immune
```

This allows class utility to remain useful without allowing players to trivialize encounters.

---

# Diminishing Returns

PvP uses diminishing returns for repeated Crowd Control.

Repeated applications of the same CC category against the same target become progressively less effective.

Example:

```text
First Stun
100% duration

Second Stun
50% duration

Third Stun
25% duration

Fourth Stun
Immune
```

The diminishing-return state resets after a defined period without receiving that CC category.

Exact durations and percentages are balance values and may change during PvP testing.

---

# PvE Crowd Control

PvE enemies use different CC rules depending on their importance.

### Normal Enemies

Most normal enemies can be affected by common CC.

### Elite Enemies

Elite enemies may have reduced CC duration or partial resistance.

### Dungeon Enemies

Dungeon enemies are designed around controlled use of CC.

Certain abilities may be interrupted, slowed, rooted or temporarily disabled.

### Bosses

Bosses are generally immune to hard CC.

Some encounters may intentionally allow specific CC mechanics as part of the encounter design.

See [0106-Dungeons.md](../0100-World/0106-Dungeons.md) and [0107-Raids.md](../0100-World/0107-Raids.md).

---

# Elemental Conditions

Elemental conditions are status effects produced by elemental damage.

They are directly connected to the elemental system documented in [0307-Elements.md](0307-Elements.md).

Examples include:

| Condition | Element   | Example Effect                               |
| --------- | --------- | -------------------------------------------- |
| Burning   | Fire      | Damage over time                             |
| Frozen    | Frost     | Reduced movement or temporary immobilization |
| Shocked   | Lightning | Additional electrical effects                |
| Poisoned  | Nature    | Damage over time                             |
| Sundered  | Earth     | Reduced defenses                             |
| Drenched  | Water     | Increased interaction with certain elements  |
| Corrupted | Shadow    | Reduced healing or additional damage         |

The exact list of elemental conditions is defined by the Elemental system.

Elemental conditions should provide a secondary gameplay effect beyond simply dealing damage.

---

# Status Effect Interaction

Status effects can interact with one another.

Interactions should be intentional and clearly documented.

Example:

```text
Frozen + Fire
→ Removes Frozen
→ Deals bonus Fire damage

Drenched + Lightning
→ Applies Shocked
→ Increased Lightning damage

Poisoned + Nature
→ Extends Poison duration
```

Elemental interactions are documented in [0307-Elements.md](0307-Elements.md) rather than duplicated here.

---

# Buff and Debuff Stacking

Multiple copies of the same status effect do not automatically stack.

Each effect should define one of the following behaviours:

### Refresh

A new application resets the duration.

```text
Poison
10 seconds remaining
↓
New Poison applied
↓
10 seconds remaining
```

### Stack

Multiple applications increase the effect's intensity.

```text
Bleed ×1
Bleed ×2
Bleed ×3
```

### Replace

The stronger version replaces the weaker version.

```text
Armor Break I
↓
Armor Break II
```

### Independent

Multiple applications can exist separately.

This should be used sparingly because it can create unnecessary UI and combat complexity.

---

# Status Effect Priority

When multiple effects modify the same statistic, the system uses predefined stacking rules.

For example:

```text
Ability Buff: +10% Damage
Talent Buff: +5% Damage
Potion: +8% Damage
```

The final result should follow the game's defined modifier hierarchy rather than simply multiplying every modifier together.

This prevents extreme stat scaling from stacking unintentionally.

---

# Purging and Cleansing

Certain abilities can remove status effects.

## Purge

Removes positive effects from an enemy.

## Cleanse

Removes negative effects from an ally.

## Dispel

A broader term covering effects that remove magical buffs or debuffs.

Different classes may specialize in different forms of removal.

Not every status effect should be removable.

Some effects may be:

* Undispellable
* Partially removable
* Removed only by specific abilities
* Removed through encounter mechanics

---

# Visual Feedback

Every important status effect must have a clear visual identity.

Players should be able to understand major effects without opening a character panel.

Visual feedback may include:

* Character effects
* Particle effects
* Floating indicators
* Status icons
* Screen effects
* Animation changes
* Audio cues

For example:

```text
Burning
→ Fire particles
→ Burning animation
→ Status icon
→ Damage ticks
```

CC effects should be especially readable during group combat.

---

# User Interface

The player UI should display important active effects.

Buffs and debuffs should show:

* Icon
* Name
* Remaining duration
* Stack count
* Source when relevant

Major effects may receive additional visual emphasis.

Players should be able to distinguish:

```text
Buff
Debuff
CC
Elemental Condition
```

without needing to memorize every icon.

---

# Class Interaction

Status effects are an important part of class identity.

Different classes and specializations should interact with them in different ways.

Examples:

```text
Shade
Applies Bleeding and Shadow effects.

Wayfarer
Uses slows, marks and ranged conditions.

Arcanist
Manipulates elemental conditions.

Druid
Applies Nature conditions and interacts with
existing elemental effects.

Necromancer
Uses curses, diseases and death-related debuffs.

Oathkeeper
Provides defensive buffs and cleanses.

Warrior
Applies physical debuffs and controls enemies.

Cleric
Provides healing buffs and removes harmful effects.
```

These examples are subject to final class and specialization design.

---

# Status Effect Duration

Status effect duration depends on the type of effect.

Short-duration effects are generally used for:

* Burst windows
* Crowd control
* Interrupt opportunities
* Defensive reactions

Longer-duration effects are generally used for:

* Damage over time
* Healing over time
* Persistent buffs
* Debuffs
* Encounter mechanics

Some effects may have their duration modified by Haste, Mastery, talents or encounter mechanics.

---

# Design Rules

1. Every major status effect must have a clear gameplay purpose.
2. Every important CC effect must have a readable visual tell.
3. Status effects must not create excessive UI clutter.
4. PvP CC must use diminishing returns.
5. Bosses must not be trivialized by hard CC.
6. DoTs and HoTs should use predictable tick intervals.
7. Status effects must have clearly defined stacking behaviour.
8. Elemental conditions are defined alongside the elemental system.
9. Cleansing and dispelling must have clearly defined rules.
10. Class-specific status interactions should reinforce class identity.
11. Status effects should be readable without requiring external tools.
12. New status effects must be documented before being added to abilities or encounters.
13. PvE and PvP may use different effectiveness values when required for balance.
14. Status effects should add meaningful combat decisions rather than simply increasing the number of icons on screen.
15. Exact durations, coefficients and diminishing-return values are balance parameters documented through [0309-Balance.md](0309-Balance.md).
