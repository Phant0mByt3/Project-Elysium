# Doc-Structure

This document outlines the documentation structure for Project Elysium. Every major system of the game has its own dedicated Markdown file, organised into category folders and identified with a four-digit code, to keep planning organized, scalable, and easy to maintain throughout development.

**Status:** All listed files are populated (no empty stubs). This tree is generated from the live `docs/` directory.

```text
docs/

├── 0000-Project/
│   ├── 0000-Overview.md
│   ├── 0001-Vision.md
│   ├── 0002-Core-Pillars.md
│   ├── 0003-Roadmap.md
│   ├── 0004-Version-History.md
│   ├── 0005-Future-Plans.md
│   ├── 0006-Documentation-Guide.md
│   ├── 0007-Team-Structure.md
│   ├── 0008-Development-Philosophy.md
│   └── 0009-Project-Glossary.md
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
│   ├── 0112-Maps.md
│   ├── 0113-Biomes.md
│   ├── 0114-Weather-System.md
│   ├── 0115-Day-Night-Cycle.md
│   ├── 0116-World-Generation.md
│   └── 0117-Environmental-Hazards.md
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
│   ├── 0209-NPCs.md
│   ├── 0210-Dialogue-System.md
│   ├── 0211-Languages.md
│   ├── 0212-Religions.md
│   ├── 0213-Mythology.md
│   ├── 0214-Ancient-Civilisations.md
│   └── 0215-Ancient-Archivarium.md
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
│   ├── 0308-Class-Progression.md
│   ├── 0309-Balance.md
│   ├── 0310-Character-Creation.md
│   ├── 0311-Character-Customisation.md
│   ├── 0312-Character-Animations.md
│   └── 0313-Death-System.md
│
├── 0400-Gameplay/
│   ├── 0400-Game-Mechanics.md
│   ├── 0401-Combat.md
│   ├── 0402-Enemy-Design.md
│   ├── 0403-Boss-Mechanics.md
│   ├── 0404-AI-Behaviour.md
│   ├── 0405-Aggro-System.md
│   ├── 0406-Difficulty-System.md
│   ├── 0407-World-Interactions.md
│   ├── 0408-Physics-Systems.md
│   └── 0409-Tutorial-System.md
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
│   ├── 0509-Enchanting.md
│   ├── 0510-Item-Rarity.md
│   ├── 0511-Item-Upgrading.md
│   ├── 0512-Item-Sets.md
│   ├── 0513-Transmog-System.md
│   ├── 0514-Item-Binding.md
│   ├── 0515-Item-Durability.md
│   ├── 0516-Item-Attributes.md
│   ├── 0517-Unique-Effects.md
│   ├── 0518-Artifact-Items.md
│   └── 0519-Item-Storage.md
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
│   ├── 0609-Tailoring.md
│   ├── 0610-Leatherworking.md
│   ├── 0611-Profession-Progression.md
│   ├── 0612-Profession-Materials.md
│   ├── 0613-Resource-Nodes.md
│   ├── 0614-Profession-Recipes.md
│   ├── 0615-Profession-Specialisations.md
│   └── 0616-Profession-Mastery.md
│
├── 0700-Quests/
│   ├── 0700-Quests.md
│   ├── 0701-Quest-Chains.md
│   ├── 0702-Daily-Quests.md
│   ├── 0703-Weekly-Quests.md
│   ├── 0704-Achievements.md
│   ├── 0705-Titles.md
│   ├── 0706-Reputation.md
│   ├── 0707-Factions-Reputation.md
│   ├── 0708-Main-Quest.md
│   ├── 0709-Side-Quests.md
│   ├── 0710-Quest-Objectives.md
│   ├── 0711-Quest-Rewards.md
│   ├── 0712-Cinematics.md
│   ├── 0713-Quest-Tracking.md
│   ├── 0714-Quest-Branches.md
│   ├── 0715-Dynamic-Quests.md
│   ├── 0716-World-Quest-System.md
│   └── 0717-Quest-Scripting.md
│
├── 0800-Multiplayer/
│   ├── 0800-Guilds.md
│   ├── 0801-Parties.md
│   ├── 0802-Raiding.md
│   ├── 0803-Dungeon-Finder.md
│   ├── 0804-PvP.md
│   ├── 0805-Arenas.md
│   ├── 0806-Territory-Control.md
│   ├── 0807-Seasons.md
│   ├── 0808-Leaderboards.md
│   ├── 0809-Friend-System.md
│   ├── 0810-Social-Features.md
│   ├── 0811-Party-Finder.md
│   ├── 0812-Voice-Communication.md
│   ├── 0813-Group-Roles.md
│   ├── 0814-Guild-Progression.md
│   ├── 0815-Guild-Halls.md
│   ├── 0816-World-PvP.md
│   └── 0817-Competitive-Systems.md
│
├── 0900-Player-Systems/
│   ├── 0900-Housing.md
│   ├── 0901-Mounts.md
│   ├── 0902-Pets.md
│   ├── 0903-Cosmetics.md
│   ├── 0904-Emotes.md
│   ├── 0905-Player-Progression.md
│   ├── 0906-Simulated-Civilisation.md
│   ├── 0907-Collections.md
│   ├── 0908-Journals.md
│   ├── 0909-Achievement-Tracking.md
│   ├── 0910-Player-Statistics.md
│   ├── 0911-Character-Profile.md
│   ├── 0912-Loadouts.md
│   ├── 0913-Inventory-System.md
│   ├── 0914-Bank-System.md
│   ├── 0915-Player-Rewards.md
│   ├── 0916-Player-Milestones.md
│   └── 0917-Account-Progression.md
│
├── 1000-Economy/
│   ├── 1000-Economy.md
│   ├── 1001-Currency.md
│   ├── 1002-Vendors.md
│   ├── 1003-Auction-House.md
│   ├── 1004-Trading.md
│   ├── 1005-Mail.md
│   ├── 1006-Banking.md
│   ├── 1007-Market-System.md
│   ├── 1008-Economic-Balance.md
│   ├── 1009-Inflation-Control.md
│   ├── 1010-Currency-Sinks.md
│   ├── 1011-Currency-Sources.md
│   ├── 1012-Player-Trading-Rules.md
│   ├── 1013-Merchant-System.md
│   ├── 1014-NPC-Economy.md
│   ├── 1015-Regional-Economies.md
│   └── 1016-Economic-Events.md
│
├── 1100-Client/
│   ├── 1100-Launcher.md
│   ├── 1101-Client-Modules.md
│   ├── 1102-Content-Pack.md
│   ├── 1103-Custom-Models.md
│   ├── 1104-Soundtrack.md
│   ├── 1105-Rendering Effects.md
│   ├── 1106-Accessibility.md
│   ├── 1107-Controls.md
│   ├── 1108-UI-Systems.md
│   ├── 1109-Settings.md
│   ├── 1110-Loading-Screens.md
│   ├── 1111-Animations.md
│   ├── 1112-Cutscenes.md
│   ├── 1113-Client-Optimisation.md
│   ├── 1114-Main-Menu.md
│   ├── 1115-Character-Select.md
│   ├── 1116-Interface-Layouts.md
│   ├── 1117-Dialogue-UI.md
│   ├── 1118-Inventory-UI.md
│   ├── 1119-Map-UI.md
│   ├── 1120-Quest-UI.md
│   ├── 1121-Combat-UI.md
│   ├── 1122-Notification-System.md
│   └── 1123-Client-Configuration.md
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
│   ├── 1208-Performance.md
│   ├── 1209-Instance-System.md
│   ├── 1210-World-Management.md
│   ├── 1211-Server-Synchronisation.md
│   ├── 1212-Logging.md
│   ├── 1213-Backup-System.md
│   ├── 1214-Admin-Tools.md
│   ├── 1215-Developer-Tools.md
│   ├── 1216-Monitoring.md
│   ├── 1217-Server-Architecture.md
│   ├── 1218-Plugin-Communication.md
│   ├── 1219-Data-Storage.md
│   ├── 1220-Database-Schema.md
│   ├── 1221-Caching-System.md
│   ├── 1222-Load-Balancing.md
│   ├── 1223-Server-Scaling.md
│   ├── 1224-Region-Servers.md
│   ├── 1225-Matchmaking-Architecture.md
│   ├── 1226-Command-System.md
│   ├── 1227-Permission-System.md
│   ├── 1228-Account-System.md
│   ├── 1229-Player-Data-System.md
│   └── 1230-Server-Maintenance.md
│
├── 1300-Art/
│   ├── 1300-Art-Style.md
│   ├── 1301-UI-Style.md
│   ├── 1302-Colour-Palette.md
│   ├── 1303-Fonts.md
│   ├── 1304-Icons.md
│   ├── 1305-Textures.md
│   ├── 1306-Models.md
│   ├── 1307-Animation-Style.md
│   ├── 1308-VFX.md
│   ├── 1309-Cinematics.md
│   ├── 1310-Environment-Art.md
│   ├── 1311-Character-Art.md
│   ├── 1312-Weapon-Art.md
│   ├── 1313-Armour-Art.md
│   ├── 1314-Architecture-Style.md
│   ├── 1315-Iconography.md
│   ├── 1316-Particle-Effects.md
│   ├── 1317-Lighting-Style.md
│   ├── 1318-Animation-Guidelines.md
│   └── 1319-Art-Asset-Pipeline.md
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
│   ├── 1408-Release-Process.md
│   ├── 1409-Content-Pipeline.md
│   ├── 1410-Developer-Environment.md
│   ├── 1411-Git-Workflow.md
│   ├── 1412-Code-Review.md
│   ├── 1413-Documentation-Standards.md
│   ├── 1414-Asset-Management.md
│   ├── 1415-Version-Control.md
│   ├── 1416-Branch-Strategy.md
│   ├── 1417-Development-Tools.md
│   ├── 1418-Local-Testing.md
│   ├── 1419-Staging-Environment.md
│   ├── 1420-Production-Deployment.md
│   ├── 1421-Build-Automation.md
│   ├── 1422-Quality-Assurance.md
│   ├── 1423-Performance-Testing.md
│   ├── 1424-Security-Testing.md
│   └── 1425-Developer-Guidelines.md
│
├── 1500-Expansions/
│   ├── 1500-Expansion-01.md
│   ├── 1501-Expansion-Planning.md
│   ├── 1502-Expansion-Story-Structure.md
│   ├── 1503-Expansion-World-Design.md
│   ├── 1504-Expansion-Feature-Planning.md
│   ├── 1505-Expansion-Release-Strategy.md
│   ├── 1600-Expansion-02.md
│   ├── 1601-Expansion-Planning.md
│   ├── 1700-Expansion-03.md
│   ├── 1800-Expansion-04.md
│   └── 1900-Expansion-05.md
│
├── 2000-Operations/
│   ├── 2000-Live-Service.md
│   ├── 2001-Updates.md
│   ├── 2002-Patch-Notes.md
│   ├── 2003-Moderation.md
│   ├── 2004-Community-Management.md
│   ├── 2005-Support-System.md
│   ├── 2006-Analytics.md
│   ├── 2007-Player-Reports.md
│   ├── 2008-Staff-Tools.md
│   ├── 2009-Community-Events.md
│   ├── 2010-Seasonal-Events.md
│   ├── 2011-Server-Restarts.md
│   ├── 2012-Maintenance.md
│   ├── 2013-Player-Feedback.md
│   ├── 2014-Bug-Reports.md
│   ├── 2015-Game-Metrics.md
│   ├── 2016-Player-Retention.md
│   ├── 2017-Community-Guidelines.md
│   └── 2018-Operations-Checklist.md
│
└── 9000-Future/
    ├── 9000-Ancient-Mysteries.md
    ├── 9001-Future-Characters.md
    ├── 9002-Future-Regions.md
    ├── 9003-Future-Threats.md
    ├── 9004-Long-Term-Story.md
    ├── 9005-Unused-Concepts.md
    ├── 9006-Future-Gameplay-Systems.md
    ├── 9007-Future-Technologies.md
    ├── 9008-Future-Classes.md
    ├── 9009-Future-Races.md
    ├── 9010-Future-Expansions.md
    ├── 9011-Experimental-Mechanics.md
    ├── 9012-Rejected-Ideas.md
    ├── 9013-Prototype-Systems.md
    ├── 9014-Community-Suggestions.md
    ├── 9015-Unconfirmed-Features.md
    └── 9999-Ideas.md
```

## Notes

- Four-digit codes group systems into categories (0000 Project, 0100 World, 0200 Lore, …).
- Cross-links between documents use relative Markdown paths and the `NNNN-Name.md` form.
- See [0006-Documentation-Guide.md](0000-Project/0006-Documentation-Guide.md) for what each area covers.
- Holding / future documents live under `9000-Future/`; committed future work graduates into `0005-Future-Plans.md` or expansion docs.
