"""Food entity — handles random food placement on the grid."""

from __future__ import annotations

import random
from dataclasses import dataclass
from typing import List, Tuple

Coord = Tuple[int, int]


@dataclass
class Food:
    """Represents food on the game board."""

    position: Coord = (0, 0)

    def spawn(self, width: int, height: int, occupied: List[Coord]) -> None:
        """Generate a random position not occupied by the snake or existing food."""
        while True:
            y = random.randint(1, height - 2)
            x = random.randint(1, width - 2)
            candidate: Coord = (y, x)
            if candidate not in occupied:
                self.position = candidate
                break
