# 111 — Client Mods

## Overview
A curated set of Fabric client mods, installed automatically by the launcher ([110-Launcher.md](110-Launcher.md)), that together transform Minecraft's client into Elysium's MMORPG interface.

## Categories
* **Custom UI Framework** — replaces vanilla HUD elements with Elysium-specific health/resource bars, action bars, and menus supporting the class/skill systems ([040-Classes.md](040-Classes.md), [042-Skills.md](042-Skills.md)).
* **Performance Optimization Mods** — client-side rendering and network optimization to keep large-scale content (raids, world events, [019-World-Events.md](019-World-Events.md)) performant.
* **Immersion Mods** — disable or hide vanilla elements that would break immersion (vanilla mob spawns, vanilla crafting UI, vanilla hunger bar) per [001-Vision.md](001-Vision.md).
* **Accessibility Mods** — see [116-Accessibility.md](116-Accessibility.md) for the specific accessibility features implemented at the client-mod layer.

## Design Rules
* The mod list should be treated as a single curated bundle, versioned and shipped together via the launcher rather than requiring players to manage individual mods.
* Every client mod must be compatible with the target Fabric/Minecraft version tracked in [128-Performance.md](128-Performance.md)'s and [125-API.md](125-API.md)'s version support notes, and with cross-version update support as described in the README's technical goals.
