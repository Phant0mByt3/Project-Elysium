# 0408 — Physics Systems

**Project:** Elysium MMORPG  
**Category:** Gameplay  
**Status:** Design Complete — Implementation Pending  
**Related:** [0401-Combat.md](0401-Combat.md) · [0110-Travel.md](../0100-World/0110-Travel.md) · [1210-World-Management.md](../1200-Technical/1210-World-Management.md) · [0001-Vision.md](../0000-Project/0001-Vision.md)

---

## 1. Overview

Elysium uses Minecraft’s physics substrate for movement, collision, and basic projectile behaviour, then layers custom rules on top to support MMORPG combat and traversal design. Vanilla physics that conflict with the handcrafted world or combat clarity are restricted or replaced.

---

## 2. Core Principles

- **Server authority** — final positions, collision results, and knockback are determined server-side.
- **Predictable movement** — players should be able to learn the movement model and rely on it in combat and platforming sections.
- **No sequence-breaking** — physics exploits that would skip intended level design (Ender Pearls, unrestricted Elytra, etc.) are removed (see Vision and World Management).
- **Combat readability** — knockback, pulls, and forced movement are telegraphed and consistent so they can be used as intentional mechanics rather than chaos.

---

## 3. Customised Behaviours

| System | Custom Behaviour |
|--------|------------------|
| **Falling** | Standard fall damage with possible mitigation from abilities or gear; no vanilla “mlg water” reliance for intended paths |
| **Knockback / Pulls** | Ability-driven, directionally consistent, and budgeted so they do not fling players out of encounter arenas unintentionally |
| **Mounts** | Ground mounts with controlled speed curves; flying mounts gated to later content |
| **Swimming** | Functional but not a primary traversal method for most regions; underwater sections are deliberately designed |
| **Projectiles** | Server-validated hit detection with appropriate travel time and collision |

---

## 4. Design Rules

1. Physics should never be the primary source of player frustration in intended content.
2. Any forced-movement mechanic in a boss fight must have a readable telegraph and a fair recovery window.
3. World geometry is built with the final movement model in mind; designers do not rely on players “breaking” physics to progress.

---

## 5. Technical Notes

Custom physics adjustments live in the movement and combat plugins. Client-side prediction is used for responsiveness, but the server has the final say on position and collision outcomes.
