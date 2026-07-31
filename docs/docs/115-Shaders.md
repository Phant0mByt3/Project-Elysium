# 115 — Shaders

## Overview
A custom shader pack bundled with the client, used to achieve lighting, weather, and atmosphere well beyond vanilla Minecraft's default rendering — critical to selling Elysium's fantasy tone per [01-Vision.md](01-Vision.md).

## Scope
* **Dynamic Lighting** — supporting day/night cycles, dungeon/cave atmosphere, and spell/ability visual effects tied to [44-Combat.md](44-Combat.md).
* **Weather Effects** — storms (tied to Maelithir world boss content, [18-World-Bosses.md](18-World-Bosses.md)), fog, snow across Vethmoor's colder regions.
* **Water & Reflections** — particularly important for the launch raid's flooded setting ([17-Raids.md](17-Raids.md)).
* **Post-Processing** — color grading matching each continent's palette ([132-Colour-Palette.md](132-Colour-Palette.md)).

## Performance Considerations
Shader presets should be tiered (Low/Medium/High/Ultra) to support a wide range of player hardware without excluding lower-end machines from participating in group content, coordinated with the performance targets in [128-Performance.md](128-Performance.md).

## Accessibility
A reduced-effects shader mode should be available for photosensitivity and performance-accessibility reasons — see [116-Accessibility.md](116-Accessibility.md).
