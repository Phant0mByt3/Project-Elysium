# 1105 — Shaders

## Overview
A custom rendering pipeline (built on Unreal Engine's Lumen, Nanite, and Niagara systems) bundled with the client, used to achieve lighting, weather, and atmosphere well beyond a default engine template's rendering — critical to selling Elysium's fantasy tone per [0001-Vision.md](../0000-Project/0001-Vision.md).

## Scope
* **Dynamic Lighting** — supporting day/night cycles, dungeon/cave atmosphere, and spell/ability visual effects tied to [0401-Combat.md](../0400-Gameplay/0401-Combat.md).
* **Weather Effects** — storms (tied to Maelithir world boss content, [0108-World-Bosses.md](../0100-World/0108-World-Bosses.md)), fog, snow across Vethmoor's colder regions.
* **Water & Reflections** — particularly important for the launch raid's flooded setting ([0107-Raids.md](../0100-World/0107-Raids.md)).
* **Post-Processing** — color grading matching each continent's palette ([1302-Colour-Palette.md](../1300-Art/1302-Colour-Palette.md)).

## Performance Considerations
Graphics quality presets should be tiered (Low/Medium/High/Ultra) to support a wide range of player hardware without excluding lower-end machines from participating in group content, coordinated with the performance targets in [1208-Performance.md](../1200-Technical/1208-Performance.md).

## Accessibility
A reduced-effects post-process effect mode should be available for photosensitivity and performance-accessibility reasons — see [1106-Accessibility.md](1106-Accessibility.md).


## Graphics Preset Benchmarking

Each graphics quality preset is benchmarked against a defined range of target hardware specifications before release, ensuring the "Low" preset genuinely delivers playable performance on minimum-spec machines rather than being a token option.

## Screenshot and Photo Mode

A dedicated photo mode, building on the same rendering pipeline, allows players to capture high-quality screenshots with UI hidden and camera freedom — a popular feature for a game with as much bespoke visual content as Elysium's handcrafted world.
