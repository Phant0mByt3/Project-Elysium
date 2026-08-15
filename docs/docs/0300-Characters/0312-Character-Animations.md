# 0312 — Character Animations

**Project:** Elysium MMORPG
**Category:** Characters
**Status:** Design Complete — Implementation Pending
**Related:** 0300-Classes.md · 0301-Specializations.md · 0302-Skills.md · 0311-Character-Customisation.md · [0401-Combat.md](../0400-Gameplay/0401-Combat.md) · [1306-Models.md](../1300-Art/1306-Models.md) · [1307-Animation-Style.md](../1300-Art/1307-Animation-Style.md) · [1318-Animation-Guidelines.md](../1300-Art/1318-Animation-Guidelines.md)

---

## 1. Overview

Animations are one of the primary ways Elysium communicates character identity, combat state, and gameplay feedback.

A player should be able to recognise what another character is doing from their movement and animation before relying on particle effects, floating combat text, or UI indicators.

Animation therefore serves both visual presentation and gameplay readability.

Every class should have a distinct physical language.

A Warrior should move and attack with weight and commitment.

A Rogue should appear fast, controlled, and precise.

A Mage should use deliberate casting motions that clearly distinguish different spell types.

A Druid should have movement and attack animations that support its connection to nature and shapeshifting.

---

# 2. Animation Categories

| Category               | Purpose                                 | Examples                                              |
| ---------------------- | --------------------------------------- | ----------------------------------------------------- |
| **Locomotion**         | Movement through the world              | Walk, run, sprint, swim, climb, jump                  |
| **Combat Stance**      | Communicates combat readiness           | Weapon-ready idle, defensive stance, casting stance   |
| **Basic Attacks**      | Core combat actions                     | Weapon swings, ranged attacks, basic spells           |
| **Ability Animations** | Communicates skill activation           | Casts, strikes, channels, finishers                   |
| **Movement Abilities** | Communicates mobility skills            | Charges, dashes, leaps, teleports                     |
| **Hit Reactions**      | Communicates incoming impact            | Light hit, heavy hit, stagger, knockback              |
| **Crowd Control**      | Communicates disabled states            | Stun, root, silence, fear, freeze                     |
| **Death & Resurrect**  | Communicates character death and return | Collapse, spirit state, resurrection                  |
| **Emotes & Social**    | Non-combat character expression         | Wave, cheer, sit, dance                               |
| **Mount Animations**   | Mounted interaction                     | Mounting, dismounting, mounted movement               |
| **Interaction**        | World interaction                       | Opening doors, gathering, crafting, examining objects |

Emotes and social animations are documented further in [0904-Emotes.md](../0900-Player-Systems/0904-Emotes.md).

---

# 3. Class Animation Identity

Animation is part of class design rather than an art layer added after gameplay is complete.

Each class should have a recognisable movement and combat language.

| Class           | Animation Identity                                             |
| --------------- | -------------------------------------------------------------- |
| **Warrior**     | Heavy, committed movements with strong follow-through          |
| **Paladin**     | Controlled, disciplined attacks with defensive movements       |
| **Rogue**       | Fast, compact, precise movements                               |
| **Ranger**      | Agile movement and deliberate ranged attacks                   |
| **Mage**        | Controlled casting gestures with strong spell preparation      |
| **Necromancer** | Deliberate, unsettling gestures and ritualistic casting        |
| **Cleric**      | Controlled motions associated with protection and restoration  |
| **Druid**       | Fluid natural movements and distinct shapeshifting transitions |

Specialisations should modify this identity without completely replacing the base class animation language.

For example, two Mage specialisations may cast differently, but both should still feel like Mage abilities.

---

# 4. Animation and Combat Readability

Animations must communicate gameplay information.

Players should be able to identify:

* An attack beginning.
* An attack landing.
* A spell being prepared.
* A powerful ability being activated.
* A movement ability being used.
* A character being interrupted.
* A character being stunned or otherwise crowd-controlled.
* A character entering a defensive state.
* A character dying.

This is especially important in:

* Dungeons.
* Raids.
* World bosses.
* PvP.
* Large-scale world events.

Animation should never be so subtle that players cannot reasonably react to an important mechanic.

---

# 5. Ability Telegraphs

Abilities with significant gameplay consequences require readable animation telegraphs.

This includes abilities that:

* Deal heavy burst damage.
* Apply hard crowd control.
* Create dangerous area effects.
* Interrupt players.
* Change a boss encounter.
* Trigger major defensive mechanics.
* Perform large movement or displacement effects.

A telegraph can consist of:

* Character preparation animation.
* Weapon positioning.
* Casting gesture.
* Charge-up motion.
* Animation timing.
* Ground effects.
* Projectile preparation.

Particle effects and UI indicators can reinforce the telegraph but should not be the only source of information.

---

# 6. Animation Timing

Animation timing must work with the combat system.

Animations should communicate the relationship between:

```text
Ability Input
     ↓
Cast / Preparation
     ↓
Impact
     ↓
Recovery
     ↓
Next Action
```

Gameplay-critical timing should be determined by the combat system rather than being hidden entirely inside animation assets.

This prevents animation changes from unintentionally changing ability timing.

Animation cancellation may be supported where explicitly allowed by the combat system.

---

# 7. Animation States

Characters use a state-driven animation system.

Typical states include:

```text
Idle
 ↓
Locomotion
 ↓
Combat
 ├── Basic Attack
 ├── Ability
 ├── Block / Defend
 ├── Hit Reaction
 ├── Crowd Control
 └── Death
```

The animation system must handle transitions between states without visible snapping or incorrect pose changes.

Priority rules should determine which animation takes control when multiple states occur simultaneously.

For example:

```text
Death
  >
Hard Crowd Control
  >
Major Ability
  >
Basic Attack
  >
Locomotion
  >
Idle
```

Exact priority behaviour is defined by the combat and animation implementation.

---

# 8. Race Compatibility

Playable races should share animation infrastructure where practical.

Humanoid races should use shared skeletons or compatible rigs where possible.

Race-specific adjustments may be required for:

* Body proportions.
* Height.
* Facial structure.
* Ears.
* Horns.
* Tusks.
* Tails.
* Fur.
* Other racial features.

Animation must respect the visual differences established by [0311-Character-Customisation.md](0311-Character-Customisation.md).

A custom appearance should not require a completely separate animation set unless the body structure makes it necessary.

---

# 9. Weapons and Equipment

Weapon type affects combat animation.

Examples include:

* One-handed sword.
* Two-handed sword.
* Axe.
* Mace.
* Dagger.
* Staff.
* Bow.
* Crossbow.
* Shield.

Animations should account for:

* Weapon size.
* Weapon weight.
* Attack range.
* Fighting style.
* Class identity.

A Warrior using a two-handed weapon should not use the same attack language as a Rogue using paired daggers.

Equipment animations must also avoid obvious clipping with armour and cosmetic items.

---

# 10. Shapeshifting

Druid shapeshifting requires dedicated transition animations.

A transformation should communicate:

1. The player begins the transformation.
2. The character changes form.
3. The transformation completes.
4. The new form enters its appropriate state.

Transformations should not simply swap models instantly unless required for technical reasons.

Different Druid forms should have their own:

* Locomotion.
* Combat stance.
* Basic attacks.
* Ability animations.
* Hit reactions.
* Death behaviour where applicable.

---

# 11. Casting Animations

Spellcasting animations should communicate:

* Spell preparation.
* Spell type.
* Casting direction.
* Casting completion.
* Interrupted casts.
* Channeled abilities.

Different elemental and magical abilities should have recognisable casting language.

For example:

* Fire spells may use aggressive forward motions.
* Frost spells may use controlled, restrained movements.
* Nature spells may use flowing gestures.
* Holy spells may use deliberate protective motions.
* Shadow and death magic may use darker, ritualistic gestures.
* Arcane spells may use precise geometric or focused gestures.

The animation should support the elemental identity defined in [0307-Elements.md](0307-Elements.md).

---

# 12. Hit Reactions

Hit reactions provide immediate feedback when characters take damage.

Different levels of impact should have distinct reactions.

### Light Hit

Small reaction with minimal interruption.

### Heavy Hit

Strong body movement and brief disruption.

### Knockback

Character is physically displaced and transitions into an appropriate recovery state.

### Stagger

Character temporarily loses control or balance.

### Crowd Control

A persistent animation communicates the active control state.

Hit reactions should not excessively interrupt combat animations unless the combat mechanic specifically requires it.

---

# 13. Death and Resurrection

Death animations are part of the character experience and should reflect the character's current state.

Death may include:

* Final hit reaction.
* Collapse.
* Class-specific death behaviour.
* Spirit or spectator transition.
* Respawn transition.

Certain races or abilities may have visually distinct behaviour.

Revenants may have unique visual effects associated with their relationship to Sundering energy and death.

The complete death and respawn system is documented in [0313-Death-System.md](0313-Death-System.md).

---

# 14. Emotes and Social Animation

Social animations allow characters to express personality outside combat.

Examples include:

* Wave.
* Bow.
* Point.
* Laugh.
* Cheer.
* Sit.
* Kneel.
* Dance.
* Sleep.
* Applaud.

Emotes should be usable without interfering with normal gameplay.

Certain emotes may be unlocked through:

* Achievements.
* Quests.
* Factions.
* Events.
* Cosmetics.
* The Archivarium.

See [0904-Emotes.md](../0900-Player-Systems/0904-Emotes.md).

---

# 15. Animation Performance

Animation budgets must account for situations where hundreds of characters may be visible simultaneously.

Performance considerations include:

* Animation complexity.
* Bone count.
* Update frequency.
* Level of detail.
* Crowd animation systems.
* Distance-based animation updates.
* Particle and effects interaction.

Large raids and world events should remain playable without requiring every distant character to use full animation fidelity.

See [1208-Performance.md](../1200-Technical/1208-Performance.md).

---

# 16. Animation Production Pipeline

Animations are produced according to the Art team's animation standards.

The general workflow is:

```text
Gameplay Design
      ↓
Ability Specification
      ↓
Animation Concept
      ↓
Animation Production
      ↓
Engine Integration
      ↓
Combat Testing
      ↓
Readability Testing
      ↓
Performance Testing
      ↓
Content Complete
```

An ability should not be considered content-complete until its required animation set has been implemented and tested.

Animation testing must include both:

* First-person gameplay readability from the player's own character.
* Third-person readability from other players and observers.

---

# 17. Animation Guidelines

All animation work should follow:

* [1307-Animation-Style.md](../1300-Art/1307-Animation-Style.md)
* [1318-Animation-Guidelines.md](../1300-Art/1318-Animation-Guidelines.md)
* [1306-Models.md](../1300-Art/1306-Models.md)

These documents define the visual style, technical requirements, production standards, and asset requirements.

---

# 18. Design Rules

1. Animation is part of gameplay readability, not purely visual decoration.
2. Every important combat action must have a readable visual state.
3. Class animations must communicate class identity.
4. Specialisations may modify animation language without losing base-class identity.
5. Important attacks and crowd-control abilities require clear telegraphs.
6. Animation timing must remain synchronised with combat logic.
7. Shared rigs should be used wherever practical.
8. Race-specific anatomy must be respected.
9. Weapon animations must reflect weapon type and class identity.
10. Shapeshifting requires dedicated transition and form animations.
11. Animation performance must support raids and large world events.
12. New abilities require their necessary animations before being considered content-complete.
13. Cosmetic customisation must not break animation readability.
14. Animation systems must remain data-driven where practical so new classes, races, abilities, and cosmetics can be added without rewriting the core animation system.
15. Animation should communicate what is happening without requiring players to rely entirely on UI elements.
