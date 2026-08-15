# 0210 — Dialogue System

## Overview

The Elysium Dialogue System is the framework used for conversations between players and NPCs.

It is designed around the idea that NPCs are characters first and quest interfaces second.

Dialogue can be used to:

* Speak with NPCs.
* Accept and complete quests.
* Learn about Elysium.
* Discover hidden lore.
* Make choices.
* Influence reputation.
* Unlock or lose opportunities.
* Develop relationships.
* React to previous player actions.
* React to faction allegiance.
* React to race and class.
* Respond to changes in the world.

The system should support simple conversations with ordinary villagers as well as complex multi-stage conversations with rulers, companions, scholars, and major story characters.

---

# Core Philosophy

The dialogue system follows five principles.

## 1. Characters Have Knowledge Limits

NPCs should only know what they reasonably could know.

A farmer should not know the details of the Sundering unless they learned them from somewhere.

A scholar may know historical records.

An orc elder may know an oral tradition that contradicts those records.

A soldier may know what happened on a battlefield but not why the war started.

---

## 2. Dialogue Reflects the World

NPC dialogue should react to the player's current circumstances.

Possible factors include:

* Race
* Class
* Faction
* Kingdom reputation
* NPC reputation
* Quest progress
* Completed quests
* Previous dialogue choices
* World events
* Current region
* Current expansion
* Player achievements
* Group or guild context

---

## 3. Dialogue Does Not Always Have a Correct Answer

Players should sometimes have to choose between different reasonable responses.

A choice may represent:

* Compassion
* Aggression
* Curiosity
* Greed
* Loyalty
* Independence
* Honesty
* Deception
* Fear
* Pragmatism

Choices should not always be reduced to "good" and "evil."

---

## 4. Consequences Should Be Understandable

Important choices should have consequences, but the player should not constantly be punished for selecting the "wrong" dialogue option.

Consequences can be small.

For example:

* An NPC remembers an insult.
* A discount is lost.
* A side quest becomes available.
* A faction reputation value changes.
* A different response becomes available later.

Major irreversible consequences should be reserved for important story moments.

---

## 5. Dialogue Should Respect Player Agency

The system should not force the player to agree with every NPC.

Players should be able to question characters, disagree with them, or refuse their requests.

A character can still continue the conversation even when the player disagrees.

---

# Dialogue Interface

The dialogue interface follows a traditional MMORPG conversation layout while allowing more cinematic presentation for major scenes.

Example:

```text
┌─────────────────────────────────────────┐
│                                         │
│            NPC CHARACTER                │
│                                         │
│         Captain Arlen                   │
│         Commander of Dawnwatch          │
│                                         │
│  "The old kingdoms fell during the      │
│   Sundering. Now we rebuild what was    │
│   lost."                                │
│                                         │
│  > Tell me about Aurelia.               │
│  > What happened during the Sundering?  │
│  > Why should I help you?               │
│  > I need a quest.                      │
│  > Leave.                               │
│                                         │
└─────────────────────────────────────────┘
```

The interface should adapt depending on the importance of the conversation.

---

# NPC Presentation

The dialogue interface may display:

* NPC model
* NPC portrait
* NPC name
* NPC title
* Race
* Faction
* Kingdom
* Reputation
* Current location
* Dialogue text
* Available responses
* Quest options
* Lore options

Example:

```text
Lady Seraphine
Royal Archivist of Solmere

High Elf
Dawnbound Concord
Concord Dominion

Reputation:
Friendly
```

Not every piece of information needs to be displayed in every conversation.

Minor NPCs should have a simple interface.

Major characters can receive a more detailed presentation.

---

# Dialogue Types

## Ambient Dialogue

Short conversations that provide atmosphere.

Examples:

```text
"The caravans have started coming through again."

"Strange seeing Vethmoor traders in Solmere."

"Keep away from the old ruins. Something isn't right there."
```

Ambient dialogue does not need player choices.

---

## Standard Conversation

A normal interaction between the player and an NPC.

```text
Hello.
    │
    ├── Ask about the town.
    ├── Ask about the faction.
    ├── Ask about recent events.
    └── Leave.
```

---

## Quest Dialogue

Dialogue connected to a quest.

The NPC explains the situation and provides the player with possible responses.

---

## Lore Dialogue

Optional conversations that provide information about:

* History
* Gods
* Races
* Kingdoms
* Factions
* Regions
* The Sundering
* Ancient civilizations

Lore dialogue should not be required for players who prefer to focus on gameplay.

---

## Companion Dialogue

Companion conversations should be more personal.

The player may discuss:

* Their past
* Their goals
* Their relationships
* Their fears
* Their opinions
* Their reaction to the player's actions

Companion dialogue can unlock additional character development.

---

## Faction Dialogue

Faction-aligned NPCs can react to the player's allegiance.

For example:

```text
Player:
Dawnbound Concord

Dawnbound Guard:
"Welcome, friend. The Concord appreciates those
willing to help rebuild."

Duskward Guard:
"So you're with the Concord."

[I'm only here to trade.]
[I'm proud to serve them.]
[Does that bother you?]
```

The same NPC can provide different dialogue depending on faction.

---

# Dialogue Choices

Players should often receive multiple responses.

Example:

```text
"The forest creatures are attacking our roads.
Will you help?"

> I'll help defend Aurelia.

> Why should I care?

> What's in it for me?

> Tell me what's actually happening.

> Not my problem.
```

Each response can have different consequences.

Possible effects include:

* Quest acceptance
* Quest rejection
* Reputation changes
* Faction reputation
* NPC relationship changes
* Unlocking dialogue
* Unlocking side quests
* Changing quest objectives
* Changing future NPC reactions

---

# Hidden Dialogue Conditions

Dialogue options can be conditionally unlocked.

Example:

```text
[Ask about the ancient forge]
Requirement:
Ironpeak Reputation ≥ Friendly
```

Or:

```text
[Reveal that you are a Revenant]
Requirement:
Player Race = Revenant
```

Or:

```text
[Discuss Kaelgorath]
Requirement:
Quest 0207_ACT_II_14 completed
```

Conditions should allow dialogue to feel reactive without creating completely separate conversations for every player.

---

# Race Reactions

NPCs may react differently depending on the player's race.

For example, a Revenant entering a settlement may receive different dialogue from an NPC who has never encountered one before.

A High Elf may receive additional dialogue from an ancient elven scholar.

A dwarf may receive special dialogue from an Ironpeak clan elder.

Race-specific dialogue should provide additional world-building rather than making certain races universally better.

---

# Class Reactions

Classes can also unlock specialized dialogue.

A warrior might understand military terminology.

A mage might recognize magical phenomena.

A rogue might identify criminal organizations.

A druid might recognize unusual changes in nature.

A paladin might receive additional dialogue from religious NPCs.

A ranger might understand tracking or wilderness problems.

Class dialogue should usually provide flavor rather than mandatory advantages.

---

# Faction Reactions

The player's faction should influence dialogue.

Possible factors include:

```text
Faction:
Dawnbound Concord

Faction Reputation:
Honored

Kingdom Reputation:
Friendly

Local Reputation:
Neutral
```

NPCs can respond accordingly.

A highly respected Dawnbound character may be greeted differently from a newly created character.

A Duskward character may be refused entry to certain faction-controlled locations unless they have sufficient reputation or another reason to enter.

---

# Reputation Integration

Dialogue is directly connected to the reputation system.

Reputation can:

* Unlock conversations.
* Change greetings.
* Unlock quests.
* Change prices.
* Change NPC attitudes.
* Unlock lore.
* Unlock special rewards.
* Change how factions describe the player.

Reputation should not simply change a numerical value.

It should be visible through the behavior of the world.

---

# Relationship System

Important NPCs can have individual relationship values with the player.

Example:

```text
Peren Vale

Relationship:
42 / 100

Status:
Trusted Associate
```

Possible relationship stages:

```text
Unknown
Acquainted
Friendly
Trusted
Close
Devoted
Rival
Hostile
```

Not every NPC needs this system.

It should primarily be used for:

* Companions
* Major NPCs
* Side-story characters
* Romance characters if romance is introduced
* Long-term faction representatives

---

# World-State Dialogue

NPC dialogue should be able to react to changes in the world.

Example:

Before a quest:

```text
"The road to Millhaven has been dangerous lately."
```

After the player clears the bandits:

```text
"The road is finally safe again.
Merchants have already started returning."
```

After a different outcome:

```text
"The road is technically open, but nobody trusts it yet."
```

This makes player actions visible.

---

# Main Story Dialogue

Major story NPCs should have dialogue that changes throughout the campaign.

For example:

```text
Act I
↓
Aldwin knows the player as an adventurer.

Act II
↓
Aldwin recognizes the player's accomplishments.

Act III
↓
Aldwin treats the player as a major political actor.
```

The player's relationship with major NPCs should develop naturally.

---

# Branching Dialogue

The system should support branching conversations.

Example:

```text
NPC:
"You entered the ruins without authorization."

              |
      ┌───────┼────────┐
      ↓       ↓        ↓
 Admit it   Lie       Deflect
      |       |        |
      ↓       ↓        ↓
 Reputation  Hidden    Alternate
 change      check     dialogue
```

Branches do not always need to produce massive changes.

Most branches should eventually converge while preserving small differences.

This keeps content manageable while still making choices feel meaningful.

---

# Major Choices

Some conversations can create long-term consequences.

Examples:

* Choosing which faction receives an artifact.
* Supporting a particular kingdom.
* Deciding the fate of a criminal.
* Choosing whether to expose historical information.
* Deciding whether an ancient technology should be destroyed.
* Choosing whether to trust a major NPC.

Major choices should be clearly written and should not be hidden behind random dialogue options.

---

# Dialogue Memory

NPCs should be able to remember relevant previous interactions.

Example:

```text
Player:
Insulted Captain Arlen.

Later:

Captain Arlen:
"I remember what you said in Solmere.
Let's keep this professional."
```

Dialogue memory should be selective.

The system does not need to remember every sentence the player has ever spoken.

Important flags should be stored as structured data.

---

# Dialogue Data Structure

Dialogue should be data-driven rather than hardcoded into gameplay logic.

Example:

```yaml
dialogue_id: captain_arlen_intro

npc_id: aurelia_captain_arlen

speaker:
  name: Captain Arlen
  title: Commander of Dawnwatch

conditions:
  location: dawnwatch
  quest_state:
    main_act_1: available

lines:
  - text: "You've arrived at a bad time."
    choices:
      - text: "What's happening?"
        next: captain_arlen_problem

      - text: "I'm looking for work."
        next: captain_arlen_quest

      - text: "Then I'll leave you to it."
        next: exit
```

The exact format can change during implementation.

The important requirement is that dialogue remains separate from the core game code.

---

# Dialogue Conditions

The system should support conditions such as:

```text
Player Level
Player Race
Player Class
Player Faction
Faction Reputation
Kingdom Reputation
NPC Relationship
Quest State
Quest History
World State
Current Region
Current Expansion
Previous Dialogue Choice
Item Ownership
Achievement
Party State
```

This allows content creators to build reactive conversations without modifying gameplay systems.

---

# Dialogue Events

Dialogue can trigger gameplay events.

Examples:

```text
Start Quest
Complete Quest
Give Item
Remove Item
Add Reputation
Remove Reputation
Change Relationship
Unlock Location
Unlock Dialogue
Start Cinematic
Spawn NPC
Start World Event
Teleport Player
Update World State
```

Dialogue should call these events through the game's existing gameplay systems rather than directly manipulating unrelated systems.

---

# Quest Integration

Quest dialogue should be tightly connected to the quest system.

A typical quest conversation might follow:

```text
NPC
 ↓
Conversation
 ↓
Quest Introduction
 ↓
Player Choice
 ↓
Quest Accepted
 ↓
Objective Added
 ↓
Player Completes Objective
 ↓
NPC Conversation
 ↓
Reward
 ↓
World State Updated
```

The dialogue system should not contain the actual quest logic.

It should communicate with the quest system.

---

# Cinematic Dialogue

Important story conversations can temporarily switch from the normal dialogue interface into a cinematic presentation.

Cinematic dialogue can use:

* Camera movement
* Character animation
* Facial expressions
* Environment changes
* Lighting
* Music
* Sound effects
* NPC movement
* VFX

Example:

Aldwin may stop speaking through the normal dialogue window when Aethercrest is revealed.

The camera can move toward the ruins while the characters react naturally.

---

# Combat Dialogue

NPCs can speak during gameplay.

Examples:

```text
"Behind you!"

"Fall back!"

"There's too many of them!"

"That thing isn't human!"
```

Combat dialogue should be short and contextual.

It should not interrupt gameplay.

---

# Ambient NPC Dialogue

NPCs can have context-sensitive ambient dialogue.

Possible triggers:

* Time of day
* Weather
* Current world event
* Player reputation
* Recent quest completion
* Nearby combat
* Festivals
* Faction control
* Regional events

Example:

During a festival:

```text
"Come back tonight. The square will be packed."
```

During a war event:

```text
"Keep your head down. The Pact patrols are nearby."
```

---

# Voice Integration

The dialogue system should support voice acting without requiring every line to be voiced.

Possible levels include:

### Fully Voiced

Used for:

* Main story
* Major characters
* Major cinematic scenes

### Partial Voice

Used for:

* Important side stories
* Companions
* Major NPCs

### Text Only

Used for:

* Ambient dialogue
* Minor NPCs
* Repeated conversations
* Optional lore

The system should allow voice files to be attached to individual dialogue lines.

---

# AI-Assisted Dialogue

AI may eventually assist with content creation or dynamic conversations.

AI-generated dialogue must not be allowed to freely alter established lore.

The system should provide controlled context such as:

```text
NPC Identity
NPC Personality
NPC Knowledge
Current Location
Faction
Quest State
World State
Allowed Lore
Forbidden Lore
Conversation Goal
```

AI-generated dialogue should pass through validation before being displayed to players if used in a production system.

The AI should not be treated as the source of truth for Elysium's lore.

---

# Dialogue Localization

Dialogue should be stored separately from gameplay logic to support localization.

Each line should have a stable identifier.

Example:

```text
dialogue.aurelia.captain_arlen.intro_01
```

Translated text should map to the same identifier.

This prevents translated dialogue from breaking quest logic.

---

# Dialogue Accessibility

The system should support:

* Adjustable text speed
* Auto-advance
* Dialogue history
* Skip already-seen dialogue
* Subtitle sizing
* Subtitle background opacity
* Voice volume controls
* Cinematic subtitle support

Players should be able to review recent dialogue.

Important story conversations should not disappear permanently after being skipped.

---

# Dialogue History

Players should have access to a conversation history.

Example:

```text
Captain Arlen
────────────────────────

"You've arrived at a bad time."

"The roads have become dangerous."

"We need someone willing to investigate."

Player:
"What's happening?"

Captain Arlen:
"Bandits have been attacking the caravans."
```

This is especially useful for players who accidentally skip dialogue.

---

# Dialogue UI States

The interface should support several states.

```text
NORMAL
  ↓
QUEST
  ↓
LORE
  ↓
CHOICE
  ↓
CINEMATIC
  ↓
COMBAT
  ↓
END
```

The UI should transition between these states without feeling like separate systems.

---

# Design Rules

### Rule 1

Do not use dialogue to dump lore unnecessarily.

### Rule 2

Do not make every NPC speak like a historian.

### Rule 3

Do not give every conversation major choices.

### Rule 4

Do not make every choice permanently alter the game.

### Rule 5

Do not make faction dialogue morally one-sided.

### Rule 6

Do not make NPCs know information they could not reasonably know.

### Rule 7

Do not force players to agree with important NPCs.

### Rule 8

Do not hide critical quest information behind optional dialogue.

### Rule 9

Do not make every conversation about the Sundering or Kaelgorath.

### Rule 10

Keep dialogue consistent with the NPC's personality, culture, faction, and history.

---

# Example Conversation

```text
NPC:
Scholar Peren Vale

Title:
Ashen Circle Researcher

Faction:
Ashen Circle

Relationship:
Trusted

────────────────────────────────────────

Peren:
"You're back. I was beginning to think
the ruins had claimed another researcher."

> "What did you find?"

> "You seem nervous."

> "Did you learn anything about Kaelgorath?"

> "I need to leave."

────────────────────────────────────────

Player selects:

"What did you find?"

Peren:
"Three inscriptions. All from different
periods. And they all describe the same
event differently."

> "Which one is correct?"

> "Show me."

> "Then someone's lying."

────────────────────────────────────────

Player selects:

"Then someone's lying."

Peren:
"That's what worries me."

[New objective unlocked]
Investigate the Three Inscriptions
```

The conversation provides information, character development, and gameplay progression without turning the NPC into a lore encyclopedia.

---

# System Goal

The Elysium Dialogue System should make conversations feel like part of the world rather than a layer placed on top of it.

A player should be able to talk to:

* A king
* A soldier
* A blacksmith
* A farmer
* A scholar
* A companion
* A criminal
* A priest
* A merchant
* A child
* A rival adventurer

and have each conversation feel different.

The main story tells the player what is happening to Elysium.

Dialogue shows how the people of Elysium understand, experience, and react to those events.
