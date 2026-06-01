# Nibbles — MS-DOS Snake Clone

A terminal-based clone of the classic MS-DOS **Nibbles** game, written in Python with minimal dependencies.

## Features

- 🐍 Classic snake gameplay with growing tail
- 🎨 Colorful terminal rendering via `curses`
- ⚡ Progressive speed increase as you eat
- 🏆 Score tracking
- 🖥️ Runs on **Windows**, **macOS**, and **Linux**

## Installation

### Prerequisites

- Python 3.10 or higher

### Windows

```powershell
# 1. Clone or create the project folder
cd C:\Users\netga\source\repos\nibbles

# 2. Create a virtual environment (if not already done)
python -m venv venv
.\venv\Scripts\activate

# 3. Install dependencies (installs windows-curses on Windows)
pip install -r requirements.txt

# 4. Run the game
python main.py
```

### macOS / Linux

```bash
# 1. Navigate to the project folder
cd path/to/nibbles

# 2. Create a virtual environment (if not already done)
python3 -m venv venv
source venv/bin/activate

# 3. Install dependencies (no extra packages needed on Mac/Linux)
pip install -r requirements.txt

# 4. Run the game
python main.py
```

## Controls

| Key        | Action          |
|------------|-----------------|
| `↑` `↓` `←` `→` | Move snake     |
| `q`        | Quit game       |
| `p`        | Pause / Resume  |

## Architecture

```
nibbles/
├── main.py              # Entry point — initializes and runs the game loop
├── config.py            # All constants (grid size, speed, colors)
├── requirements.txt     # Dependencies (windows-curses on Windows only)
├── README.md            # This file
├── game/                # Core game logic
│   ├── __init__.py
│   ├── snake.py         # Snake class — movement, growth, collision
│   ├── food.py          # Food class — random spawn logic
│   └── board.py         # Board class — score, speed, game state
└── ui/                  # Rendering and input
    ├── __init__.py
    └── renderer.py      # Curses drawing, color pairs, input handling
```

## Design Decisions

- **`curses`** — The standard library terminal UI module. Zero dependencies on macOS/Linux; one lightweight package (`windows-curses`) on Windows.
- **No external GUI framework** — Keeps the game lightweight and true to the retro terminal aesthetic.
- **Modular structure** — Game logic (`game/`) is fully decoupled from rendering (`ui/`), making it easy to swap in a different renderer later (e.g., `pygame`).

## License

MIT
