# 122 — Network

## Overview
Networking architecture covering both the Minecraft protocol layer (Paper server ↔ Fabric client) and any auxiliary services (launcher backend, website account services) the game depends on.

## Server-Side
* Standard Minecraft protocol over Paper, optimized via the performance-focused client/server mods described in [111-Client-Mods.md](111-Client-Mods.md) and [128-Performance.md](128-Performance.md).
* Custom plugin messaging channels used for launcher-to-server communication where needed (e.g. account verification handshakes with [124-Authentication.md](124-Authentication.md)).

## Auxiliary Services
* **Launcher Backend** — serves update manifests and news content to the launcher ([110-Launcher.md](110-Launcher.md)).
* **Website/Account Services** — handles account creation and management outside of the game client itself (see the README's `website/` project structure entry).
* **Auction House / Economy APIs** — internal APIs supporting cross-system economy features, documented alongside [125-API.md](125-API.md).

## Scalability
The server architecture should support horizontal scaling for world instances (dungeons/raids run as isolated instances rather than on the main world server) as player population grows, aligning with the README's "scalable architecture" project goal.

## Security
Network-layer security (DDoS mitigation, rate limiting, packet validation) is covered jointly with [126-Security.md](126-Security.md).
