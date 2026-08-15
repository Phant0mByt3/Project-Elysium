# 0303 — Talent Trees

## Overview

Talent Trees are Elysium's primary build-customization system.

They allow players to develop their chosen specialization in different directions rather than simply increasing the power of existing abilities.

A player may have the same class and specialization as another player while having a substantially different build.

Talent Trees work alongside Skills (0302-Skills.md), Specializations (0301-Specializations.md), and Stats (0304-Stats.md).

---

# Tree Structure

Each specialization has one Talent Tree containing three distinct sub-paths.

The three paths represent different approaches to playing the specialization.

For example, a Berserker might have:

```text
Berserker
│
├── Fury
│   └── Sustained damage
│
├── Execution
│   └── Burst and finishing attacks
│
└── Blood
    └── Survivability and self-sustain
```

Players are not required to follow a single path.

Points can be distributed across the tree to create hybrid builds.

---

# Talent Points

Talent Points become available after specialization.

Players earn approximately one Talent Point per level from level 10 onward.

The exact number of points and level requirements may change during balance testing.

Talent Points are spent to unlock talents within the player's specialization tree.

A typical progression looks like:

```text
Level 10
│
└── Specialization chosen
      │
      └── Talent Tree unlocked
            │
            ├── Path A
            ├── Path B
            └── Path C
```

Higher-tier talents require previous talents within the tree to be unlocked.

---

# Talent Types

Talents can provide different types of gameplay changes.

## Passive Talents

Small or moderate improvements to existing abilities or attributes.

Examples:

* Increased critical chance
* Reduced cooldown
* Increased movement speed
* Improved resource generation
* Increased healing received

Passive talents should not make up the majority of a tree.

---

## Ability Modifiers

These change how an existing skill works.

Example:

```text
Shieldbreak

Base:
Deals heavy physical damage.

Talent:
Shieldbreak now creates a short defensive barrier
after striking an enemy.
```

Ability modifiers are one of the main ways Talent Trees should change gameplay.

---

## New Abilities

Some talents unlock completely new abilities.

These should be relatively rare and should have a clear purpose within the specialization.

Example:

```text
Berserker

Talent:
Bloodrush

Effect:
Charge toward an enemy and gain Rage based on
the distance travelled.
```

---

## Keystone Talents

Keystone Talents are major talents that significantly change a build.

They should alter mechanics rather than simply providing larger numerical bonuses.

Examples:

```text
Berserker

Keystone:
Unrelenting Fury

Effect:
Spending Rage no longer resets the Berserker's
momentum chain.

Instead, momentum is reduced gradually over time.
```

A player choosing this talent may build their entire rotation around maintaining momentum.

---

## Capstone Talents

Capstones are the final talents at the end of each sub-path.

They should be build-defining.

A capstone should feel like the conclusion of the path rather than:

```text
+5% Damage
```

Instead, it should introduce a major mechanic, interaction or playstyle.

Example:

```text
Execution Path

Capstone:
Final Cut

Effect:
Your finishing abilities can be used against targets
above the normal execution threshold.

The bonus effect scales with the target's missing health.
```

---

# Three-Path Philosophy

Each specialization's three paths should represent meaningful choices.

They should generally follow three different gameplay goals:

### Path A — Core Strength

Improves the specialization's primary combat identity.

### Path B — Advanced Playstyle

Introduces more complex mechanics, combinations or burst windows.

### Path C — Alternative Function

Provides survivability, utility, resource management or another alternative way to approach the specialization.

The exact themes can change between specializations.

They should not become a rigid template.

---

# Example Talent Tree

A simplified Berserker tree might look like:

```text
                         BERSERKER
                             │
              ┌──────────────┼──────────────┐
              │              │              │
            FURY         EXECUTION        BLOOD
              │              │              │
          Talent 1        Talent 1        Talent 1
              │              │              │
          Talent 2        Talent 2        Talent 2
              │              │              │
          Talent 3        Talent 3        Talent 3
              │              │              │
          Keystone        Keystone        Keystone
              │              │              │
           Capstone       Capstone       Capstone
```

The player can focus heavily on one path or combine talents from multiple paths.

---

# Hybrid Builds

Players should not be forced into completely isolated builds.

For example:

```text
Fury:        6 points
Execution:   4 points
Blood:       2 points
```

could produce a Berserker that focuses on sustained damage while retaining some burst and survivability.

Hybrid builds may not always be the strongest option, but they should remain viable.

---

# Respec System

Players can fully reset their Talent Tree outside of combat.

Respecialization costs a modest amount of Aurum.

See [1001-Currency.md](../1000-Economy/1001-Currency.md).

The cost should be low enough that players can experiment regularly without making every choice meaningless.

Players should never feel permanently punished for trying an unusual build.

---

# Build Presets

Players should eventually be able to save multiple Talent Tree configurations.

Example:

```text
Vanguard — Guardian

Build 1:
Raid Tank

Build 2:
Dungeon Tank

Build 3:
Solo Defence
```

Switching between saved builds should only be possible outside combat and should still require any applicable respec restrictions.

This feature is especially useful when a specialization supports significantly different playstyles.

---

# Talent and Skill Interaction

Talent Trees directly modify and expand the Skills system.

A talent may:

* Modify an existing skill
* Change a resource interaction
* Add a secondary effect
* Unlock a new ability
* Change the conditions under which an ability is used
* Create interactions between multiple abilities
* Alter a specialization mechanic

Talents should therefore be designed alongside the corresponding specialization's skills.

See [0302-Skills.md](0302-Skills.md).

---

# Talent and Stats

Talents may interact with character statistics, but raw stat increases should not dominate the tree.

A talent such as:

```text
+2% Strength
```

may be useful, but it should generally be less interesting than:

```text
Your next melee ability after using a defensive skill
deals increased damage and generates additional threat.
```

The goal is for talent choices to change gameplay rather than simply increase a character's numbers.

Stat calculations are documented in [0304-Stats.md](0304-Stats.md).

---

# Talent Design Rules

1. Every talent must have a meaningful purpose.
2. There should be no deliberately useless talents.
3. Every path should be viable in at least one form of content.
4. Talents should change gameplay where possible rather than only increase statistics.
5. Keystone talents should create major build-defining decisions.
6. Capstone talents should feel powerful and unique.
7. Players should be able to create hybrid builds.
8. No path should be mandatory for a specialization.
9. Talents should interact with the specialization's existing skills.
10. Talent Trees should not replace the identity of the specialization.
11. Respecs should remain affordable.
12. Talent choices should be readable without requiring external guides.
13. Talent balance should account for solo, dungeon, raid and PvP environments.
14. Talent Trees should support experimentation rather than enforce a single optimal build.
15. Final talent layouts are subject to balance testing.

---

# Relationship to Other Systems

Talent Trees are directly connected to:

* [0300-Classes.md](0300-Classes.md)
* [0301-Specializations.md](0301-Specializations.md)
* [0302-Skills.md](0302-Skills.md)
* [0304-Stats.md](0304-Stats.md)
* [0401-Combat.md](../0400-Gameplay/0401-Combat.md)
* [0309-Balance.md](0309-Balance.md)

They form the main system through which players create their own version of a specialization.

---

# Development Status

Full Talent Tree layouts for all twelve launch specializations will be designed and iterated during Phase 2 gameplay systems development.

The final trees should be tested across:

* Open-world content
* Solo play
* Dungeons
* Raids
* PvP
* Group utility
* Different equipment builds

See [0003-Roadmap.md](../0000-Project/0003-Roadmap.md).
