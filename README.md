# Pygame 2D Puzzle Game Prototype

A modular, lightweight 2D grid-based puzzle game prototype built from scratch with Python and Pygame. Designed with strict separation of concerns across game logic, rendering, level management, and audio.

---

## 🎮 Game Concept & Mechanics

- **Core Mechanic:** Grid-based Sokoban & Switch-Door puzzle system.
- **Objective:** Navigate the player, push interactive blocks onto pressure plates / target sockets, activate switches to unlock doors, and reach the exit portal.
- **Controls:**
  - `W / A / S / D` or `Arrow Keys`: Move player
  - `R`: Restart current level
  - `ESC`: Return to Main Menu / Pause
  - `M`: Toggle Sound / Music
- **Levels:** 4 handcrafted progressive levels introducing movement, crate pushing, switch-door triggers, and multi-objective puzzle solving.

---

## 🏗 Architecture & Code Structure

The project follows a clean, decoupled modular design:

```
pythonGameSchool/
│
├── main.py             # Application entry point & core game loop
├── constants.py        # Screen dimensions (16:9), colors, grid config, tile types
├── game.py             # State machine (MENU, PLAYING, LEVEL_CLEAR, GAME_OVER)
├── level.py            # Level loader, ASCII map parser, level progression
├── grid.py             # Core puzzle logic, collision detection, push/switch rules
├── renderer.py         # Pure rendering pipeline (surfaces, scaling, UI, HUD)
├── sound.py            # Audio manager (SFX triggers, mixer initialization)
└── levels/             # Handcrafted level map definitions (.txt or data structures)
    ├── level1.txt
    ├── level2.txt
    ├── level3.txt
    └── level4.txt
```

---

## ⚙️ Installation & Requirements

### Prerequisites
- Python 3.10 or higher
- `pip` package manager

### Setup

1. **Clone or navigate to the repository:**
   ```bash
   cd /mnt/Depo/Projeler/pythonGameSchool
   ```

2. **Create and activate a virtual environment (recommended):**
   ```bash
   python3 -m venv .venv
   source .venv/bin/activate  # On Windows: .venv\Scripts\activate
   ```

3. **Install dependencies:**
   ```bash
   pip install pygame
   ```

4. **Run the game:**
   ```bash
   python main.py
   ```

---

## 📐 Screen & Resolution

- **Base Resolution:** 1280x720 (16:9 Aspect Ratio)
- **Scaling:** Dynamic virtual surface rendered at native 16:9 and cleanly scaled with aspect ratio preservation for window resizing.
- **Target Frame Rate:** Stable 60 FPS capped via `pygame.time.Clock()`.

---

## 🎥 Recording & Verification

For submission/demo recording:
- Record 30–60 seconds in OBS Studio showing:
  1. Main menu navigation & game start.
  2. Completion of at least one full puzzle level.
  3. Win / Level Clear state transition.
