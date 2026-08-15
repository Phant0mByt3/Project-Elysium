# 0307 — Elements

## Overview

Elemental damage is a major part of Elysium's combat system.

Elements define the magical or physical nature of an attack and can interact with:

* Classes
* Specializations
* Skills
* Status effects
* Enemy resistances
* Equipment
* Environmental hazards
* Other elements

Elemental damage is divided into seven primary types:

* Fire
* Frost
* Nature
* Shadow
* Holy
* Arcane
* Physical

Each element has its own identity rather than functioning as a simple damage colour.

---

# Elemental Damage Types

## Fire

**Associated with:** Ignareth

Fire represents destruction, heat, passion and the power of the forge.

Common users include:

* Warrior abilities
* Mage fire abilities
* Blacksmith-related effects
* Ignareth-themed enemies

### Primary Condition

**Burning**

Deals damage over time.

Fire may also interact with other conditions.

Example:

```text
Frozen + Fire
→ Shatter
→ Bonus Fire/Physical damage
→ Removes Frozen
```

Fire is particularly effective against creatures vulnerable to heat and cold-based enemies.

---

# Frost

**Associated with:** Maelithir and arcane frost traditions

Frost represents cold, control and the slowing of natural movement.

Common users include:

* Frostweaver
* Certain environmental hazards
* Ice-based enemies

### Primary Conditions

**Chilled**

Reduces movement speed.

**Frozen**

A stronger Frost condition that may temporarily immobilize a target.

Frozen targets may be vulnerable to specific interactions.

Example:

```text
Frozen
+
Fire attack
↓
Shatter
```

Frost is particularly useful for controlling groups of enemies.

---

# Nature

**Associated with:** Aeloria

Nature represents life, growth, decay and the natural world.

Common users include:

* Druids
* Rangers
* Nature-based creatures
* Aeloria's followers

### Primary Condition

**Poisoned**

Deals damage over time and may reduce healing received.

Nature abilities may also interact with existing conditions.

For example, a Druid ability may consume Poisoned stacks to produce additional damage or healing.

Nature is not inherently good or evil.

The same force that creates forests can also produce disease, venom and decay.

---

# Shadow

**Associated with:** Nyxara and Voranthe

Shadow represents secrecy, death, fear and forces that exist beyond ordinary light.

Common users include:

* Rogues
* Necromancers
* Shadow-focused Clerics
* Revenants
* Certain undead enemies

### Primary Condition

**Weakened**

Reduces outgoing healing and/or damage.

Shadow effects may also interact with death-related mechanics.

Shadow is not automatically associated with evil.

Nyxara's Shadow represents secrecy and the unknown, while Voranthe's Shadow is more closely associated with death and fate.

---

# Holy

**Associated with:** Solthar

Holy represents light, protection, restoration and divine power.

Common users include:

* Paladins
* Clerics
* Solthar's followers
* Certain relics and ancient weapons

Holy damage behaves differently from most elemental types.

It is primarily designed around:

* Healing
* Protection
* Undead damage
* Cleansing
* Defensive effects

### Primary Interaction

Holy damage deals increased damage against certain undead and corrupted creatures.

Holy abilities may also amplify healing or remove harmful effects.

Example:

```text
Holy Strike
→ Deals Holy damage
→ Deals bonus damage against undead
```

Holy should not simply function as "Light Fire".

Its primary identity is restoration and opposition to unnatural forces.

---

# Arcane

**Associated with:** No specific god

Arcane represents raw magical energy and the fundamental forces underlying spellcasting.

It is not tied to the Elysian Circle.

Common users include:

* Mages
* Arcane scholars
* Ancient magical constructs
* Concord-era magical technology

### Primary Condition

Arcane has no universal status condition.

Instead, Arcane abilities may have unique effects depending on the spell.

Examples include:

* Spell amplification
* Mana manipulation
* Teleportation
* Temporal effects
* Magical barriers
* Arcane corruption

Arcane represents controlled magical power rather than a natural element.

---

# Physical

Physical damage represents direct force rather than magical energy.

Common sources include:

* Swords
* Axes
* Spears
* Bows
* Daggers
* Unarmed attacks
* Physical abilities

Physical damage is primarily mitigated by **Armor**.

It does not use elemental Resistance.

Physical damage may still apply non-elemental status effects such as:

* Bleeding
* Stagger
* Sundered
* Crippled

Physical damage is the primary damage type for many weapon-based builds.

---

# Elemental Conditions

Elements can apply status effects.

The default relationships are:

| Element  | Primary Condition | General Effect                      |
| -------- | ----------------- | ----------------------------------- |
| Fire     | Burning           | Damage over time                    |
| Frost    | Chilled / Frozen  | Movement reduction / immobilization |
| Nature   | Poisoned          | Damage over time / reduced healing  |
| Shadow   | Weakened          | Reduced outgoing healing and damage |
| Holy     | —                 | Healing and undead interactions     |
| Arcane   | —                 | Ability-specific effects            |
| Physical | —                 | Ability-specific physical effects   |

These are default behaviours rather than mandatory rules.

Individual abilities may apply different effects.

See [0306-Status-Effects.md](0306-Status-Effects.md).

---

# Elemental Interactions

Elements can interact when different effects are applied to the same target.

These interactions are designed to encourage cooperation between classes and specializations.

They should reward players for understanding combat mechanics rather than simply stacking the same damage type.

---

## Frost + Fire

A Frozen target hit by Fire can trigger **Shatter**.

```text
Frozen
    ↓
Fire attack
    ↓
Shatter
    ↓
Bonus damage
    ↓
Frozen removed
```

This provides a simple interaction that rewards coordination between Frost and Fire users.

---

## Drenched + Lightning

Future elemental mechanics may introduce temporary conditions such as **Drenched**.

Lightning applied to a Drenched target may trigger **Conductive Shock**.

```text
Drenched
    ↓
Lightning
    ↓
Conductive Shock
    ↓
Bonus Lightning damage
```

Additional elemental conditions may be introduced as the combat system develops.

---

# Combination Effects

Some abilities may deliberately interact with existing elemental conditions.

Examples:

```text
Burning + Nature
→ Spreading Wildfire

Poisoned + Shadow
→ Withering Venom

Frozen + Physical
→ Cracked Ice

Weakened + Holy
→ Purification
```

These are examples of possible mechanics rather than finalized abilities.

Combination effects should only be added when they create meaningful gameplay.

---

# Elemental Priority

Not every elemental interaction should trigger automatically.

Each interaction has a defined priority.

For example:

```text
Target:
Frozen
Burning
Poisoned

Fire ability:
Triggers Shatter

The other conditions remain unless
the interaction specifically removes them.
```

This prevents combat from becoming unpredictable when several conditions are active simultaneously.

---

# Elemental Resistances

Enemies may have resistance or vulnerability to specific elements.

Examples:

```text
Fire Elemental
Fire Resistance: High
Frost Resistance: Low

Undead
Shadow Resistance: Moderate
Holy Vulnerability: High

Ice Wraith
Frost Resistance: Very High
Fire Vulnerability: High
```

Resistance should modify damage rather than completely invalidating a class.

A player should still be able to contribute when fighting an enemy resistant to their primary element.

---

# Resistance Types

Elemental resistance is separate from Armor.

### Armor

Primarily reduces Physical damage.

### Elemental Resistance

Reduces magical elemental damage.

Possible resistance types include:

* Fire Resistance
* Frost Resistance
* Nature Resistance
* Shadow Resistance
* Holy Resistance
* Arcane Resistance

Resistance values may be provided by:

* Equipment
* Talents
* Buffs
* Consumables
* Racial abilities
* Encounter mechanics

---

# Environmental Elements

Elements are not limited to combat abilities.

The environment can contain elemental hazards.

Examples:

### Fire

* Lava
* Burning buildings
* Volcanic vents
* Fire traps

### Frost

* Frozen rivers
* Blizzard zones
* Ice caves
* Freezing winds

### Nature

* Poisonous plants
* Toxic swamps
* Corrupted forests
* Venomous environments

### Shadow

* Corrupted ruins
* Death zones
* Shadow portals
* Sundering scars

### Arcane

* Magical anomalies
* Ancient portals
* Unstable constructs
* Concord-era machinery

Environmental hazards can be used for exploration puzzles as well as combat.

---

# Elemental Equipment

Equipment may have elemental properties.

Examples include:

```text
Flameforged Sword
→ Adds Fire damage to attacks.

Frostbound Staff
→ Improves Frost abilities.

Shadowglass Dagger
→ Increases Shadow damage.

Sunspire Mace
→ Improves Holy abilities.
```

Elemental equipment should not completely replace class abilities.

It should instead provide additional build options.

---

# Elemental Weapons

Certain weapons may have inherent elemental effects.

Examples:

* Flame-forged weapons
* Frostbound weapons
* Venom-coated weapons
* Shadow-infused weapons
* Holy relics
* Arcane constructs

These effects may be cosmetic, mechanical, or both.

---

# Class Relationships

Different classes naturally interact with different elements.

| Class       | Common Elements       |
| ----------- | --------------------- |
| Warrior     | Physical / Fire       |
| Paladin     | Holy / Physical       |
| Rogue       | Physical / Shadow     |
| Ranger      | Physical / Nature     |
| Mage        | Arcane / Fire / Frost |
| Necromancer | Shadow / Nature       |
| Cleric      | Holy / Shadow         |
| Druid       | Nature / Frost        |

These are thematic relationships rather than restrictions.

Any class may gain access to additional elemental effects through skills, talents, equipment or future content.

---

# Elemental Identity

Each element should communicate a different gameplay idea.

```text
Fire
Aggression and damage

Frost
Control and slowing

Nature
Growth, decay and sustained effects

Shadow
Weakening and death

Holy
Protection and restoration

Arcane
Raw magical power

Physical
Weapon force and martial combat
```

This makes elemental effects recognizable even before the player reads the ability description.

---

# Design Rules

1. Every element must have a distinct gameplay identity.
2. Elemental damage must be visually readable.
3. Physical damage is mitigated primarily through Armor.
4. Magical elemental damage is affected by Resistance.
5. Elemental conditions are documented alongside the Status Effect system.
6. Elemental interactions should reward coordination without being mandatory for every encounter.
7. Resistance should rarely make a class completely useless.
8. Boss encounters may use special elemental mechanics.
9. Environmental hazards may use the same elemental rules as combat.
10. Elements should support class identity without restricting class choice.
11. New elements should not be added without updating this document.
12. New elemental conditions should be documented in [0306-Status-Effects.md](0306-Status-Effects.md).
13. Elemental combinations must have predictable outcomes.
14. Elemental mechanics should remain understandable during fast-paced combat.
15. Exact damage modifiers, resistance values and interaction coefficients are part of the ongoing balance process documented in [0309-Balance.md](0309-Balance.md).
