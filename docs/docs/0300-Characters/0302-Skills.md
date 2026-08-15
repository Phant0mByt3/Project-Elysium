# 0302 — Skills

## Overview

Skills are the active and passive abilities used by Elysium characters in combat.

Skills unlock progressively as characters level rather than being given all at once. Specializations introduce additional abilities and mechanics that significantly change how a class is played.

See [0300-Classes.md](0300-Classes.md) and [0301-Specializations.md](0301-Specializations.md).

---

# Skill Categories

## Core Skills

Core Skills are abilities shared by every character of a class regardless of specialization.

They establish the fundamental identity and combat style of the class.

Examples include:

* Basic weapon attacks
* Class resource generation
* Core defensive abilities
* Fundamental class mechanics

A Guardian and Berserker may play very differently, but both should still feel like Vanguards.

---

## Specialization Skills

Specialization Skills become available after choosing a specialization at level 10.

These abilities define the unique mechanics and combat style of the chosen specialization.

For example:

```text
Vanguard
│
├── Guardian
│   └── Defensive and protection abilities
│
└── Berserker
    └── Aggressive and offensive abilities
```

Specialization skills should make the two paths feel substantially different without losing their shared class identity.

---

## Utility Skills

Utility Skills provide effects that are not primarily focused on dealing damage.

They may include:

* Movement
* Crowd control
* Interrupts
* Buffs
* Debuffs
* Defensive utility
* Mobility
* Exploration abilities
* Group support

Utility skills can differ between specializations when doing so reinforces their identity.

---

## Ultimate Skills

Each specialization receives a signature Ultimate Skill.

Ultimate Skills are powerful abilities with long cooldowns or other significant limitations.

They should represent the peak expression of the specialization rather than simply being its strongest damage ability.

Examples:

```text
Guardian
"Last Stand"

Berserker
"Bloodrage"

Frostweaver
"Absolute Zero"

Pyromancer
"Inferno"

Shadowblade
"Death from Shadow"

Trickster
"Grand Deception"

Wildshaper
"Primal Ascension"

Grovekeeper
"Heart of the Grove"

Sentinel
"Divine Bastion"

Lightbringer
"Radiant Salvation"

Marksman
"Deadeye"

Beastmaster
"Call of the Wild"
```

These names are placeholders until individual class design is finalized.

---

# Skill Anatomy

Every skill should be documented using a consistent structure.

Each skill entry should contain:

| Field               | Description                                  |
| ------------------- | -------------------------------------------- |
| **Name**            | The skill's in-game name                     |
| **Type**            | Core, Specialization, Utility, or Ultimate   |
| **Resource Cost**   | Resource required to activate the skill      |
| **Cooldown**        | Time before the skill can be used again      |
| **Range**           | Effective range                              |
| **Target**          | Valid target type                            |
| **Cast Time**       | Time required to activate the skill          |
| **Duration**        | How long the effect lasts, if applicable     |
| **Effect**          | Mechanical description                       |
| **Visual Identity** | Short description of how the ability appears |
| **Unlock Level**    | Level at which the skill becomes available   |

Example:

```text
Name:
Shieldbreak

Type:
Core

Resource Cost:
25 Resolve

Cooldown:
8 seconds

Range:
Melee

Target:
Enemy

Effect:
A powerful weapon strike that deals increased damage
against enemies currently affected by defensive effects.

Visual Identity:
The Vanguard drives their weapon into the target's guard,
creating a visible shockwave on impact.

Unlock Level:
6
```

---

# Skill Progression

Skills unlock throughout the leveling experience.

Early levels should introduce the fundamental mechanics of the class quickly.

A typical progression may follow:

```text
Level 1
Core ability

Level 2–4
Additional core abilities

Level 5–9
Class mechanics and utility

Level 10
Specialization unlocked

Level 10+
Specialization abilities

Higher levels
Advanced abilities and utility

Max level
Ultimate Skill
```

The exact unlock levels are determined during class implementation.

---

# Unlock Pacing

Early progression should introduce new skills frequently enough that the player continues learning their class.

Skills should generally unlock every **1–3 levels during the early game**.

After specialization is selected, new skill unlocks should gradually become less frequent.

This prevents the ability bar from becoming overloaded while allowing talent choices to become the primary source of build customization.

---

# Skill Interaction

Skills should interact with one another rather than existing as isolated buttons.

Examples:

```text
Skill A
    ↓
applies Bleeding
    ↓
Skill B
    ↓
consumes Bleeding
    ↓
Skill C
    ↓
gains bonus effect
```

This creates class-specific combat loops and gives players meaningful decisions during combat.

Different specializations should create different interactions even when they share some Core Skills.

---

# Resource Systems

Each class may use its own resource system when appropriate.

Possible resources include:

* Rage
* Mana
* Resolve
* Energy
* Focus
* Nature
* Faith

Resources should reinforce the class fantasy rather than exist purely as a technical requirement.

For example:

**Berserker**

Builds Rage through aggressive combat and spends it on powerful attacks.

**Arcanist**

Uses Mana to cast spells and manage sustained magical output.

**Shade**

Uses Energy to perform rapid attacks and mobility abilities.

**Oathkeeper**

Uses Faith or a similar sacred resource to power protective abilities.

The final resource systems are documented alongside class mechanics during implementation.

---

# Skill Scaling

Skill effectiveness should scale with the character's attributes and relevant combat statistics.

Cooldowns, resource costs and numerical values must remain compatible with the formulas defined in [0304-Stats.md](0304-Stats.md).

Skills should avoid excessive dependence on flat numerical scaling where possible.

The goal is for an ability's identity to remain recognizable as the character progresses.

---

# Visual Identity

Every major skill should have a recognizable visual identity.

Players should be able to understand what is happening in combat without reading every combat log entry.

Visual differences should communicate:

* Class
* Specialization
* Ability type
* Target
* Major effects
* Dangerous enemy abilities

Examples:

**Arcanist**

Arcane energy, elemental effects and magical formations.

**Shade**

Darkness, brief visual distortions, movement effects and precise weapon strikes.

**Warden**

Natural growth, roots, leaves, spectral beasts and shapeshifting.

**Oathkeeper**

Radiant energy, sacred symbols, barriers and protective effects.

---

# Skill Design Rules

1. Every skill must have a clear purpose.
2. Core Skills establish the identity of the class.
3. Specialization Skills establish the identity of the specialization.
4. Utility Skills should provide meaningful options rather than filler abilities.
5. Every specialization receives an Ultimate Skill.
6. Skills should interact with other abilities wherever practical.
7. Skill effects should be visually readable.
8. No skill should exist solely to increase a damage number without adding meaningful gameplay.
9. Resource costs and cooldowns must follow the game's stat and combat systems.
10. Skills should not create unnecessary ability-bar bloat.
11. Specializations should share enough Core Skills to feel like the same class.
12. Specializations should have enough unique skills to feel meaningfully different.
13. Skills must remain useful across the appropriate stages of progression.
14. Numerical balance is handled through [0309-Balance.md](0309-Balance.md).
15. Full skill lists are created during gameplay systems implementation.

---

# Class Skill Structure

Each launch class follows the same overall structure:

```text
Class
│
├── Core Skills
│   ├── Shared by both specializations
│   └── Establish class identity
│
├── Utility Skills
│   ├── Movement
│   ├── Control
│   └── Support
│
├── Specialization A
│   ├── Unique Skills
│   ├── Passive Mechanics
│   └── Ultimate
│
└── Specialization B
    ├── Unique Skills
    ├── Passive Mechanics
    └── Ultimate
```

This keeps the six classes structurally consistent while allowing each specialization to develop its own combat identity.

---

# Future Development

Full skill lists for:

* Vanguard
* Arcanist
* Shade
* Warden
* Oathkeeper
* Wayfarer

will be developed during Phase 2 gameplay systems development.

See [0003-Roadmap.md](../0000-Project/0003-Roadmap.md).
