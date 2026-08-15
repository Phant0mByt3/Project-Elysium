# 0404 — AI Behaviour

**Project:** Elysium MMORPG
**Category:** Gameplay
**Status:** Living Document
**Related:** [0402-Enemy-Design.md](0402-Enemy-Design.md) · [0405-Aggro-System.md](0405-Aggro-System.md) · [0403-Boss-Mechanics.md](0403-Boss-Mechanics.md)

---

## 1. Overview

Enemy AI in Elysium is built around behaviour trees that produce readable, learnable patterns rather than purely reactive or random behaviour. The goal is for a player to be able to predict and counter enemy behaviour once they've fought a given enemy type a few times.

## 2. Behaviour Categories

* **Passive** — does not engage unless attacked or approached too closely (wildlife, non-hostile NPCs).
* **Aggressive** — attacks on sight within an aggro radius (bandits, hostile beasts).
* **Territorial** — attacks only within a defined area, disengaging if the player leaves it (guardians, elites tied to a landmark).
* **Pack-coordinated** — multiple enemies share awareness and call for reinforcements (bandit camps, orc warbands).
* **Boss-scripted** — full state-machine driven behaviour per [0403-Boss-Mechanics.md](0403-Boss-Mechanics.md).

## 3. Perception

Enemies use a combination of sight cone, hearing radius, and aggro radius to determine awareness of the player, allowing stealth-oriented classes (Shade) to route around or past enemies where appropriate (see [0300-Classes.md](../0300-Characters/0300-Classes.md)).

## 4. Combat Behaviour Trees

Each enemy template is assigned a behaviour tree defining its ability rotation, positioning preferences (kiting for ranged enemies, closing distance for melee), and reaction to player status effects such as crowd control.

## 5. Difficulty Scaling Interaction

AI aggression and ability usage frequency scale with the difficulty settings described in [0406-Difficulty-System.md](0406-Difficulty-System.md), allowing the same enemy template to be used across Normal, Heroic, and Mythic tiers with meaningfully different behaviour.

## 6. Group Coordination

Pack-coordinated enemies use a shared awareness system so that pulling one member of a group appropriately alerts nearby allies, reinforcing careful pull management as a skill expression in dungeon content (see [0106-Dungeons.md](../0100-World/0106-Dungeons.md)).

## 7. Technical Notes

AI behaviour trees run server-authoritatively to prevent client-side manipulation. Designers configure behaviour trees through a data-driven tool rather than hard-coded logic, allowing rapid iteration during playtesting — see [1200-Plugin-Architecture.md](../1200-Technical/1200-Plugin-Architecture.md).
