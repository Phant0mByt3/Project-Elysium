# 0210 — Dialogue System

## Overview

The Elysium Dialogue System is designed to provide an immersive MMORPG-style conversation experience. Inspired by systems found in games like World of Warcraft and Final Fantasy XIV, it replaces simple NPC interactions with a fully structured dialogue interface.

The goal is to make NPCs feel like actual characters within the world rather than simple quest markers.

Players should be able to:

* Talk with NPCs.
* Learn about the world and lore.
* Accept and complete quests.
* Make dialogue choices.
* Influence reputation and future interactions.

---

# Dialogue Interface

The dialogue interface follows a traditional MMORPG layout.

Example:

```
┌─────────────────────────────────────┐
│                                     │
│        NPC Character Display        │
│                                     │
│  ┌───────────────────────────────┐  │
│  │ Captain Arlen                  │  │
│  │                               │  │
│  │ "The old kingdoms fell during │  │
│  │  the Sundering. Now we rebuild│  │
│  │  what was lost."              │  │
│  └───────────────────────────────┘  │
│                                     │
│  > Tell me about Aurelia            │
│  > What happened during the         │
│    Sundering?                       │
│  > I need a quest                   │
│  > Leave                            │
│                                     │
└─────────────────────────────────────┘
```

---

# NPC Presentation

NPCs should provide more information than just a name.

The dialogue interface can display:

* NPC portrait or model.
* NPC name.
* NPC title.
* Faction affiliation.
* Player reputation.
* Location information.

Example:

```
Lady Seraphine

Royal Archivist of Aurelia

Faction:
The Silver Council

Reputation:
Friendly
```

This allows players to understand the importance of characters they interact with.

---

# Dialogue Choices

Players should have multiple response options instead of a single conversation path.

Example:

```
"The forest creatures are attacking our roads. Will you help?"

[I'll help defend Aurelia.]
[Why should I care?]
[How much is the reward?]
[Not my problem.]
```

Different choices can influence:

* Quest availability.
* Reputation.
* Faction relationships.
* Future dialogue.
* World events.

---

# Lore Integration

The dialogue system is heavily connected to the world-building of Elysium.

Because the world was shattered during the Sundering, NPCs are not simply quest providers. They are:

* Survivors.
* Historians.
* Explorers.
* Researchers.
* Leaders rebuilding civilization.

Dialogue should help players understand:

* What happened during the Sundering.
* How civilizations survived.
* What ancient secrets remain hidden.
* Why the world is changing.

---

# Data-Driven Dialogue

Dialogue should not be hardcoded.

Each NPC should use external data files.

Example:

```
npc_id:
aurelia_guard_001

name:
Captain Arlen

title:
Commander of Dawnwatch

location:
Aurelia - Dawnwatch

dialogue:
captain_arlen_intro.json

quests:
quest_004
quest_005

lore:
sundering_history_02
```

This allows developers and content creators to add new NPCs and conversations without modifying the core game code.

---

# Future Features

Possible future improvements:

## Voice Integration

NPC dialogue could support:

* Voice acting.
* Dynamic speech.
* AI-assisted dialogue generation.

## Dynamic Conversations

NPCs could react to:

* Player choices.
* Reputation.
* Completed quests.
* Current world events.

## Cinematic Conversations

Important story moments could include:

* Camera changes.
* NPC animations.
* Character expressions.
* Special effects.

---

# Design Goal

The purpose of the Elysium Dialogue System is to make every conversation feel meaningful.

Players should not feel like they are clicking through text boxes. They should feel like they are speaking with the inhabitants of a living world.
