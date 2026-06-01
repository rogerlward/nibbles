"""All game constants — grid dimensions, speeds, colors, and symbols."""

# --- Grid ---
GRID_WIDTH = 40
GRID_HEIGHT = 20

# --- Speed (milliseconds between frames) ---
INITIAL_SPEED = 100
MIN_SPEED = 50
SPEED_INCREMENT = 2

# --- Colors (curses color pair IDs) ---
COLOR_SNAKE = 1   # Green on Black
COLOR_FOOD = 2    # Red on Black
COLOR_SCORE = 3   # Yellow on Black
COLOR_BORDER = 4  # White on Black

# --- Symbols ---
SYMBOL_SNAKE_BODY = "o"
SYMBOL_SNAKE_HEAD = "*"
SYMBOL_FOOD = "@"
SYMBOL_PAUSE = "PAUSED"

# --- Scoring ---
POINTS_PER_FOOD = 10
