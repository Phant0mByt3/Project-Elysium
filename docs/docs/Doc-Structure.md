# Structure

This document outlines the documentation structure for Project Elysium. Every major system of the game has its own dedicated Markdown file, organised into category folders and identified with a four-digit code, to keep planning organized, scalable, and easy to maintain throughout development.

```text
docs/

├── 0000-Project/
│   ├── 0000-Overview.md
│   ├── 0001-Vision.md
│   ├── 0002-Core-Pillars.md
│   ├── 0003-Roadmap.md
│   ├── 0004-Version-History.md
│   ├── 0005-Future-Plans.md
│   └── 0006-Documentation-Guide.md
│
├── 0100-World/
│   ├── 0100-World.md
│   ├── 0101-Continents.md
│   ├── 0102-Regions.md
│   ├── 0103-Cities.md
│   ├── 0104-Villages.md
│   ├── 0105-Landmarks.md
│   ├── 0106-Dungeons.md
│   ├── 0107-Raids.md
│   ├── 0108-World-Bosses.md
│   ├── 0109-World-Events.md
│   ├── 0110-Travel.md
│   ├── 0111-Fast-Travel.md
│   └── 0112-Maps.md
│
├── 0200-Lore/
│   ├── 0200-Lore.md
│   ├── 0201-Timeline.md
│   ├── 0202-Gods.md
│   ├── 0203-Factions.md
│   ├── 0204-Races.md
│   ├── 0205-Kingdoms.md
│   ├── 0206-History.md
│   ├── 0207-Main-Story.md
│   ├── 0208-Side-Stories.md
│   └── 0209-NPCs.md
│
├── 0300-Characters/
│   ├── 0300-Classes.md
│   ├── 0301-Specializations.md
│   ├── 0302-Skills.md
│   ├── 0303-Talent-Trees.md
│   ├── 0304-Stats.md
│   ├── 0305-Leveling.md
│   ├── 0306-Status-Effects.md
│   ├── 0307-Elements.md
│   └── 0309-Balance.md
│
├── 0400-Gameplay/
│   ├── 0400-Game-Mechanics.md
│   └── 0401-Combat.md
│
├── 0500-Items/
│   ├── 0500-Weapons.md
│   ├── 0501-Armour.md
│   ├── 0502-Accessories.md
│   ├── 0503-Loot.md
│   ├── 0504-Loot-Tables.md
│   ├── 0505-Legendary-Items.md
│   ├── 0506-Relics.md
│   ├── 0507-Consumables.md
│   ├── 0508-Crafting.md
│   └── 0509-Enchanting.md
│
├── 0600-Professions/
│   ├── 0600-Professions.md
│   ├── 0601-Mining.md
│   ├── 0602-Woodcutting.md
│   ├── 0603-Fishing.md
│   ├── 0604-Herbalism.md
│   ├── 0605-Alchemy.md
│   ├── 0606-Blacksmithing.md
│   ├── 0607-Cooking.md
│   ├── 0608-Jewelcrafting.md
│   └── 0609-Tailoring.md
│
├── 0700-Quests/
│   ├── 0700-Quests.md
│   ├── 0701-Quest-Chains.md
│   ├── 0702-Daily-Quests.md
│   ├── 0703-Weekly-Quests.md
│   ├── 0704-Achievements.md
│   ├── 0705-Titles.md
│   ├── 0706-Reputation.md
│   └── 0707-Factions-Reputation.md
│
├── 0800-Multiplayer/
│   ├── 0800-Guilds.md
│   ├── 0801-Parties.md
│   ├── 0802-Raiding.md
│   ├── 0803-Dungeon-Finder.md
│   ├── 0804-PvP.md
│   ├── 0805-Arenas.md
│   ├── 0806-Territory-Control.md
│   └── 0807-Seasons.md
│
├── 0900-Player-Systems/
│   ├── 0900-Housing.md
│   ├── 0901-Mounts.md
│   ├── 0902-Pets.md
│   ├── 0903-Cosmetics.md
│   ├── 0904-Emotes.md
│   ├── 0905-Player-Progression.md
│   └── 0906-Simulated-Civilisation.md
│
├── 1000-Economy/
│   ├── 1000-Economy.md
│   ├── 1001-Currency.md
│   ├── 1002-Vendors.md
│   ├── 1003-Auction-House.md
│   ├── 1004-Trading.md
│   ├── 1005-Mail.md
│   └── 1006-Banking.md
│
├── 1100-Client/
│   ├── 1100-Launcher.md
│   ├── 1101-Client-Mods.md
│   ├── 1102-Resource-Pack.md
│   ├── 1103-Custom-Models.md
│   ├── 1104-Soundtrack.md
│   ├── 1105-Shaders.md
│   └── 1106-Accessibility.md
│
├── 1200-Technical/
│   ├── 1200-Plugin-Architecture.md
│   ├── 1201-Database.md
│   ├── 1202-Network.md
│   ├── 1203-Server-Structure.md
│   ├── 1204-Authentication.md
│   ├── 1205-API.md
│   ├── 1206-Security.md
│   ├── 1207-Anti-Cheat.md
│   └── 1208-Performance.md
│
├── 1300-Art/
│   ├── 1300-Art-Style.md
│   ├── 1301-UI-Style.md
│   ├── 1302-Colour-Palette.md
│   ├── 1303-Fonts.md
│   ├── 1304-Icons.md
│   ├── 1305-Textures.md
│   └── 1306-Models.md
│
├── 1400-Development/
│   ├── 1400-Development-Standards.md
│   ├── 1401-Coding-Standards.md
│   ├── 1402-Building-Standards.md
│   ├── 1403-Quest-Writing-Guide.md
│   ├── 1404-NPC-Writing-Guide.md
│   ├── 1405-Naming-Conventions.md
│   ├── 1406-Testing.md
│   ├── 1407-Bug-Tracking.md
│   └── 1408-Release-Process.md
│
├── 1500-Expansions/
│   ├── 1500-Expansion-01.md
│   ├── 1600-Expansion-02.md
│   ├── 1700-Expansion-03.md
│   ├── 1800-Expansion-04.md
│   └── 1900-Expansion-05.md
│
└── 9000-Future/
    ├── 9000-Ancient-Mysteries.md
    ├── 9001-Future-Characters.md
    ├── 9002-Future-Regions.md
    ├── 9003-Future-Threats.md
    ├── 9004-Long-Term-Story.md
    └── 9999-Ideas.md
```
