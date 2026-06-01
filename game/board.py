"""Board — manages game state: score, speed, pause, and game-over."""

from __future__ import annotations

from dataclasses import dataclass, field

from config import INITIAL_SPEED, MIN_SPEED, SPEED_INCREMENT


@dataclass
class Board:
    """Holds the mutable game state."""

    score: int = 0
    speed: int = field(default=INITIAL_SPEED)
    paused: bool = False
    game_over: bool = False
    high_score: int = 0

    def eat_food(self) -> None:
        """Process eating food: update score and increase speed."""
        self.score += 10
        self.speed = max(MIN_SPEED, self.speed - SPEED_INCREMENT)

    def toggle_pause(self) -> None:
        """Pause or resume the game."""
        self.paused = not self.paused

    def end_game(self) -> None:
        """Mark the game as over and update the high score."""
        self.game_over = True
        if self.score > self.high_score:
            self.high_score = self.score

    def reset(self) -> None:
        """Reset all game state to initial values."""
        self.score = 0
        self.speed = INITIAL_SPEED
        self.paused = False
        self.game_over = False
