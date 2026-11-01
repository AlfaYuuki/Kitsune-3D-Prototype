# 🦊 Kitsune FunZone 3D

**A browser-based 3D RPG prototype by Alfa Yuuki.**

Explore a fantasy world, take on quests, grow stronger, meet fox companions, and discover special domains — all from your browser.

🌐 **Play now:** https://alfayuuki.github.io/Kitsune-3D-Prototype/

> **Current version:** v6.6  
> This is an evolving prototype. Features, balance, and performance may change as development continues.

## ✨ Features

- **3D world exploration** with a third-person camera.
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
| Open quests | **Q** |
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
3. Keep an internet connection available: the current page imports Three.js modules from jsDelivr.

The game is published through GitHub Pages from the repository's configured Pages source.

## 🧰 Built With

- **HTML, CSS, and JavaScript** for the game page and interface.
- **Three.js** for browser-based 3D rendering.
- **jsDelivr** to load the Three.js modules.
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

Kitsune FunZone 3D is a work in progress. Expect iteration, fixes, and new ideas as the prototype develops.

## 👤 Author

**Alfa Yuuki**  
GitHub: [@AlfaYuuki](https://github.com/AlfaYuuki)

## 📄 License

No license is currently specified in this repository. Unless a license is added, reuse and redistribution are not automatically granted.
