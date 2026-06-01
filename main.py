"""Nibbles — MS-DOS Snake Clone.

Entry point: initializes curses, creates game objects, and runs the main loop.
"""

from __future__ import annotations

import curses
import sys

from config import GRID_HEIGHT, GRID_WIDTH  # kept for backward compatibility but not used directly
from game.board import Board
from game.food import Food
from game.snake import Snake
from ui.renderer import Renderer


def main(stdscr) -> None:
    """Initialize and run the Nibbles game loop."""

    # --- Create game objects ---
    snake = Snake()
    food = Food()
    board = Board()
    renderer = Renderer(stdscr)

    # Initial food spawn using dynamic terminal size
    max_y, max_x = stdscr.getmaxyx()
    food.spawn(max_x, max_y, snake.body)

    # Get current terminal size for collision checks
    max_y, max_x = stdscr.getmaxyx()

    # --- Main game loop ---
    while not board.game_over:
        # Input
        key = renderer.get_input()
        if key is not None:
            if key == ord("q"):
                board.end_game()
                break
            elif key == ord("p"):
                board.toggle_pause()
            elif key in (curses.KEY_UP, curses.KEY_DOWN, curses.KEY_LEFT, curses.KEY_RIGHT):
                snake.change_direction(key)

        if board.paused:
            renderer.render(snake, food, board)
            continue

        # Move snake
        new_head = snake.move()

        # Collision checks
        if snake.check_wall_collision(max_x, max_y):
            board.end_game()
            break
        if snake.check_self_collision():
            board.end_game()
            break

        # Food check
        if new_head == food.position:
            board.eat_food()
            snake.grow()
            food.spawn(max_x, max_y, snake.body)

        # Render
        renderer.render(snake, food, board)

        # Frame timing
        import time
        time.sleep(board.speed / 1000.0)

    # Game over
    board.end_game()
    renderer.show_game_over(board.score)
    renderer.cleanup()


if __name__ == "__main__":
    try:
        curses.wrapper(main)
    except ImportError:
        print("Error: curses module not found. On Windows, please install 'windows-curses'.")
        sys.exit(1)