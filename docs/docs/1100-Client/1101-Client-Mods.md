# 1101 — Client Modules

## Overview
A curated set of native C++/Blueprint modules, installed automatically by the launcher ([1100-Launcher.md](1100-Launcher.md)), that together transform the base engine template into Elysium's MMORPG interface.

## Categories
* **Custom UI Framework** — replaces default template HUD elements with Elysium-specific health/resource bars, action bars, and menus supporting the class/skill systems ([0300-Classes.md](../0300-Characters/0300-Classes.md), [0302-Skills.md](../0300-Characters/0302-Skills.md)).
* **Performance Optimization Mods** — client-side rendering and network optimization to keep large-scale content (raids, world events, [0109-World-Events.md](../0100-World/0109-World-Events.md)) performant.
* **Immersion Mods** — disable or hide default template elements that would break immersion (default template spawns, crafting UI, and survival-status bars) per [0001-Vision.md](../0000-Project/0001-Vision.md).
* **Accessibility Mods** — see [1106-Accessibility.md](1106-Accessibility.md) for the specific accessibility features implemented at the client-mod layer.

## Design Rules
* The mod list should be treated as a single curated bundle, versioned and shipped together via the launcher rather than requiring players to manage individual mods.
* Every client module must be compatible with the target Unreal Engine version tracked in [1208-Performance.md](../1200-Technical/1208-Performance.md)'s and [1205-API.md](../1200-Technical/1205-API.md)'s version support notes, and with cross-version update support as described in the README's technical goals.
