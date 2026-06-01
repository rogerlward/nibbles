"""Snake entity — manages body, direction, growth, and collision detection."""

from __future__ import annotations

import curses
from dataclasses import dataclass, field
from typing import List, Tuple

# Type alias for grid coordinates
Coord = Tuple[int, int]


@dataclass
class Snake:
    """Represents the player's snake."""

    body: List[Coord] = field(default_factory=list)
    direction: int = curses.KEY_RIGHT
    growing: bool = False

    def __post_init__(self) -> None:
        """Initialize the snake in the center of the grid."""
        if not self.body:
            center_y, center_x = 10, 20
            self.body = [(center_y, center_x)]

    def move(self) -> Coord:
        """Advance the snake one step in the current direction.

        Returns the new head coordinate.
        """
        # ``self.body`` stores coordinates as (row, col) i.e. (y, x).
        head_y, head_x = self.body[-1]

        if self.direction == curses.KEY_UP:
            head_y -= 1
        elif self.direction == curses.KEY_DOWN:
            head_y += 1
        elif self.direction == curses.KEY_LEFT:
            head_x -= 1
        elif self.direction == curses.KEY_RIGHT:
            head_x += 1

        new_head: Coord = (head_y, head_x)
        self.body.append(new_head)

        if not self.growing:
            self.body.pop(0)
        else:
            self.growing = False

        return new_head

    def grow(self) -> None:
        """Mark the snake to grow on the next move."""
        self.growing = True

    def change_direction(self, new_direction: int) -> bool:
        """Attempt to change direction. Returns True if valid, False if opposite."""
        opposites = {
            curses.KEY_UP: curses.KEY_DOWN,
            curses.KEY_DOWN: curses.KEY_UP,
            curses.KEY_LEFT: curses.KEY_RIGHT,
            curses.KEY_RIGHT: curses.KEY_LEFT,
        }
        if new_direction == opposites.get(self.direction):
            return False
        self.direction = new_direction
        return True

    def check_wall_collision(self, width: int, height: int) -> bool:
        """Return True if the head is outside the grid boundaries."""
        head = self.body[-1]
        # The coordinate tuple is stored as (y, x) where y is the row and x is
        # the column.  The original implementation unpacked it as ``x, y``
        # which swapped the values and caused an immediate collision when
        # ``y`` (the row) was compared against the width.  This resulted in
        # the game ending on the first frame.
        y, x = head  # correct order: row then column
        # The border occupies the outermost rows/columns. The snake should
        # not enter these cells, so we treat positions <=0 or >=width-1 / height-1
        return x <= 0 or x >= width - 1 or y <= 0 or y >= height - 1

    def check_self_collision(self) -> bool:
        """Return True if the head collides with any part of its own body."""
        head = self.body[-1]
        return head in self.body[:-1]

    def reset(self, center_y: int, center_x: int) -> None:
        """Reset the snake to its initial state."""
        self.body = [(center_y, center_x)]
        self.direction = curses.KEY_RIGHT
        self.growing = False
