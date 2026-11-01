# 🦊 Kitsune FunZone 3D

**A browser-based 3D RPG prototype by Alfa Yuuki.**

Explore a fantasy world, take on quests, grow stronger, meet fox companions, and discover special domains — all from your browser.

🌐 **Play now:** https://alfayuuki.github.io/Kitsune-3D-Prototype/

> **Current version:** v6.7 — Expand the World  
> **Next update:** v6.8 — **[Soon]**  
> This is an evolving prototype. Features, balance, and performance may change as development continues.

## ✨ Features

- **3D world exploration** with a third-person camera.
- **Expanded world** with four new regions beyond the original map edges.
- **Character progression** with levels, health, and experience points.
- **Quests and a journal** to follow objectives and keep track of your adventure.
- **Combat and encounters** with enemies and boss-style challenges.
- **Inventory and shop** interfaces for managing items and progression.
- **Fox companions** to bring along on your journey.
- **Special domains** with unique abilities and interactions.
- **Day and time display** to add atmosphere to the world.
- **Save support** for keeping game progress where supported by the browser.
- **Desktop and mobile controls**, including an on-screen joystick and action buttons.
- **Performance and troubleshooting tools** to help diagnose loading issues.

## 🗺️ v6.7 — Expand the World

The v6.7 update opens up four new regions to explore, each with its own scenery, tougher spirits, a hidden chest, a waypoint, and a first-entry reward.

| Region | Direction | Scenery | Spirit HP | Spirit damage multiplier |
| --- | --- | --- | ---: | ---: |
| 🎋 **Bamboo Hollow** | South of the meadow | Bamboo forest, mossy pagoda ruin, lantern path | 70 | ×1.25 |
| 🍁 **Maple Ridge** | East, along the river's south bank | Red maples, falling leaves, river source spring, giant torii | 95 | ×1.45 |
| 🌫️ **Mistwater Marsh** | West, along the river's south bank | Reeds, pools, wisps, sunken pillar ruins | 120 | ×1.65 |
| ❄️ **Frostpeak Pass** | North, past the arena | Snowy pines, glowing ice crystals, ice spire | 150 | ×1.9 |

### New in v6.7

- **Five regional spirits per area**, with greater XP and crystal rewards than the valley's spirits.
- **First-entry rewards**, a hidden chest, waypoint stone, and region banner in each new region.
- **Location HUD** showing the player's current area.
- **World Map in the Quests tab**, listing regions, spirit defeat counts, and chest status.
- **Fast travel** to discovered regions or back home. Travel is blocked during boss fights.
- **Four new legends:** Beyond the Edge, Cartographer, Frontier Hunter, and Far-Flung Fortune.
- **Regions tab in the admin console** for discovering regions and teleporting.
- **Chest tracking compatibility:** the original “all 6 chests” quest and legend still count only the original six chests; the chest popup shows the total across all ten.
- **Adaptive scenery detail** to help reduce rendering load on weaker devices.

The regions and their spirit spawn points and chests were checked for on-foot reachability in a headless test environment. The 3D scenery and real-device performance may vary by browser and device.

## 🔜 Next Update — v6.8 **[Soon]**

The next update is marked **[Soon]**. More details will be added when the v6.8 plans are ready.

## 🎮 How to Play

Open the [live game](https://alfayuuki.github.io/Kitsune-3D-Prototype/) in a modern browser and wait for the world to load.

### Desktop controls

| Action | Control |
| --- | --- |
| Move | **W A S D** or **Arrow keys** |
| Run | **Shift** |
| Rotate camera | **Drag with the mouse** |
| Zoom camera | **Mouse wheel** |
| Attack | **Space** or click |
| Interact | **E** |
| Use a potion | **H** |
| Dodge | **V** |
| Open bag | **I** |
| Open shop | **B** |
| Open quests / World Map | **Q** |
| Open journal | **J** |
| Open fox companions | **C** |
| Open domains | **G** |
| Use Anahita ability | **R** |
| Use Demiurge ability | **F** |

### Mobile controls

Use the on-screen joystick to move and the action buttons to attack, dodge, interact, use a potion, and activate available abilities. The layout may vary with screen size and game state.

## 🚀 Run Locally

This project is a browser-based HTML prototype and does not require a package installation for basic use.

1. Clone or download this repository.
   ```bash
   git clone https://github.com/AlfaYuuki/Kitsune-3D-Prototype.git
   cd Kitsune-3D-Prototype
   ```
2. Open `index.html` in a modern browser, or serve the folder with a local static web server.
3. Keep an internet connection available: the game imports Three.js modules from public CDNs.

The game is published through GitHub Pages from the repository's configured Pages source.

## 🧰 Built With

- **HTML, CSS, and JavaScript** for the game page and interface.
- **Three.js** for browser-based 3D rendering.
- **Public CDNs** to load the Three.js modules.
- **Browser storage and service workers** for supported save/offline-related behavior.

## 📁 Repository Files

| File | Purpose |
| --- | --- |
| `index.html` | Main game, interface, and gameplay code |
| `manifest.json` | Web app manifest |
| `sw.js` | Service worker |
| `kfz_diag.html` | Diagnostic page |
| `favicon.png` | Icon image |

## 🛠️ Troubleshooting

- **The game stays on the loading screen:** check your internet connection and reload the page.
- **The game seems to use an old version:** try a normal refresh first. If the issue persists, use the in-game **Clear cache & reload** option if it appears.
- **Performance is slow:** close other heavy tabs or apps, lower other browser workloads, and try a supported, up-to-date browser.
- **Controls feel different on mobile:** rotate the device or adjust the browser view; the interface is designed to adapt to smaller screens.

## 🗺️ Project Status

Kitsune FunZone 3D is a work in progress. **v6.7 — Expand the World** is the current release, and **v6.8 — [Soon]** is the next update announcement.

## 👤 Author

**Alfa Yuuki**  
GitHub: [@AlfaYuuki](https://github.com/AlfaYuuki)

## 📄 License

No license is currently specified in this repository. Unless a license is added, reuse and redistribution are not automatically granted.
