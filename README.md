# Pygame 2D Puzzle Game Prototype

A modular, lightweight 2D grid-based puzzle game prototype built from scratch with Python and Pygame. Designed with clean separation of concerns across game logic, level management, rendering, and configuration.

---

## 🎮 Game Concept & Mechanics

- **Core Mechanic:** Grid-based Sokoban puzzle system.
- **Objective:** Navigate the player, push interactive crates onto target sockets, and solve the room to complete the level.
- **Controls:**
  - `W / A / S / D` or `Arrow Keys`: Move player
  - `R`: Restart current level
  - `Window Close / Quit`: Exit game
- **Level Design:** Handcrafted grid layouts using intuitive ASCII map representations.

---

## 🏗 Architecture & Code Structure

The project follows a decoupled 4-module architecture:

```text
PuzzleGame/
├── main.py        # Application entry point, event handling, and rendering pipeline
├── constants.py   # Screen dimensions (16:9), target FPS, tile sizes, and color palette
├── level.py       # ASCII level map layouts and coordinate matrix parser
└── gameLogic.py   # Movement verification, box-pushing physics, and win conditions
```

---

## ⚙️ Installation & Requirements

### Prerequisites
- Python 3.10 or higher
- `pip` package manager

### Setup

1. **Clone the repository:**
   ```bash
   git clone https://github.com/YagYz/PuzzleGame.git
   cd PuzzleGame
   ```

2. **Create and activate a virtual environment (optional but recommended):**
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
- **Target Frame Rate:** Stable 60 FPS capped via `pygame.time.Clock()`.

---

## 📝 Note on AI Assistance

> All source code, logic, and implementations in this repository were entirely hand-written by the developer. Only this `README.md` documentation file was generated with the assistance of **Gemini 3.8 Flash** for formatting and presentation purposes.
