"""Renderer — handles all curses drawing, color setup, and input processing."""

from __future__ import annotations

import curses
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from game.snake import Snake
    from game.food import Food
    from game.board import Board

from config import (
    COLOR_BORDER,
    COLOR_FOOD,
    COLOR_SNAKE,
    COLOR_SCORE,
    SYMBOL_FOOD,
    SYMBOL_PAUSE,
    SYMBOL_SNAKE_BODY,
    SYMBOL_SNAKE_HEAD,
)


class Renderer:
    """Encapsulates all curses rendering and input logic."""

    def __init__(self, stdscr) -> None:
        self.stdscr = stdscr
        # Store the current terminal size for dynamic calculations.
        self._max_y, self._max_x = stdscr.getmaxyx()
        self._setup_colors()

    # ------------------------------------------------------------------
    # Initialization
    # ------------------------------------------------------------------

    def _setup_colors(self) -> None:
        """Configure curses color pairs and basic settings."""
        curses.curs_set(0)
        curses.start_color()
        curses.use_default_colors()

        curses.init_pair(COLOR_SNAKE, curses.COLOR_GREEN, -1)
        curses.init_pair(COLOR_FOOD, curses.COLOR_RED, -1)
        curses.init_pair(COLOR_SCORE, curses.COLOR_YELLOW, -1)
        curses.init_pair(COLOR_BORDER, curses.COLOR_WHITE, -1)

        self.stdscr.nodelay(True)
        self.stdscr.keypad(True)

    # ------------------------------------------------------------------
    # Input
    # ------------------------------------------------------------------

    def get_input(self) -> int | None:
        """Get the next key press. Returns None if no key pressed."""
        return self.stdscr.getch()

    # ------------------------------------------------------------------
    # Rendering
    # ------------------------------------------------------------------

    def render(self, snake: Snake, food: Food, board: Board) -> None:
        """Draw the entire game state to the screen."""
        self.stdscr.clear()
        self._draw_border()
        self._draw_snake(snake)
        self._draw_food(food)
        self._draw_score(board)

        if board.paused:
            self._draw_pause()

        self.stdscr.refresh()

    def _draw_border(self) -> None:
        """Draw the game border."""
        self.stdscr.attron(curses.color_pair(COLOR_BORDER))
        self.stdscr.border()
        self.stdscr.attroff(curses.color_pair(COLOR_BORDER))

    def _draw_snake(self, snake: Snake) -> None:
        """Draw the snake body and head."""
        for i, (sy, sx) in enumerate(snake.body):
            if i == len(snake.body) - 1:
                ch = SYMBOL_SNAKE_HEAD
            else:
                ch = SYMBOL_SNAKE_BODY
            self.stdscr.addch(sy, sx, ch, curses.color_pair(COLOR_SNAKE))

    def _draw_food(self, food: Food) -> None:
        """Draw the food."""
        fy, fx = food.position
        self.stdscr.addch(fy, fx, SYMBOL_FOOD, curses.color_pair(COLOR_FOOD))

    def _draw_score(self, board: Board) -> None:
        """Draw the score centered at the top."""
        text = f" Score: {board.score} "
        x = self._max_x // 2 - len(text) // 2
        self.stdscr.addstr(0, x, text, curses.color_pair(COLOR_SCORE))

    def _draw_pause(self) -> None:
        """Draw a PAUSED overlay in the center of the screen."""
        center_y = self._max_y // 2
        text = SYMBOL_PAUSE
        x = GRID_WIDTH // 2 - len(text) // 2
        self.stdscr.addstr(center_y, x, text, curses.color_pair(COLOR_SCORE))

    # ------------------------------------------------------------------
    # Post-game
    # ------------------------------------------------------------------

    def show_game_over(self, score: int) -> None:
        """Display the game-over message and wait for a key press."""
        self.stdscr.nodelay(False)
        self.stdscr.clear()
        self.stdscr.border()

        msg = f" Game Over! Score: {score} "
        y = self._max_y // 2
        x = self._max_x // 2 - len(msg) // 2
        self.stdscr.addstr(y, x, msg, curses.color_pair(COLOR_SCORE))

        self.stdscr.addstr(y + 2, x, " Press any key to quit... ")
        self.stdscr.refresh()
        self.stdscr.getch()
        self.stdscr.nodelay(True)

    def cleanup(self) -> None:
        """Restore the terminal to its original state."""
        curses.endwin()
