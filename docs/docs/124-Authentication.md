# 124 — Authentication

## Overview
Account authentication ties a player's Minecraft client to an Elysium account, verified through the launcher ([110-Launcher.md](110-Launcher.md)) before connecting to the game server.

## Flow
1. Player logs into the launcher with Elysium account credentials.
2. Launcher requests a short-lived session token from the auth backend.
3. Token is presented to the game server on connection and validated before the player is allowed past the login screen.

## Security Considerations
* Passwords are never stored in plaintext; standard salted hashing practices apply.
* Session tokens are short-lived and single-use per connection attempt to reduce replay risk.
* Account security features (2FA, login alerts) are planned ahead of Closed Beta — see [003-Roadmap.md](003-Roadmap.md).

## Relationship to Other Systems
Authentication underpins account-wide systems like cross-character storage ([106-Banking.md](106-Banking.md)) and is jointly owned with the broader security posture in [126-Security.md](126-Security.md) and anti-cheat systems in [127-Anti-Cheat.md](127-Anti-Cheat.md).
