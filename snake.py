from controls import DIRECTIONS
from config import COLORS, CONFIG

class Snake():
    def __init__(self):
        self.X = CONFIG["X"] / 2
        self.Y = CONFIG["Y"] / 2
        self.Direction = DIRECTIONS.NONE
        self.Color = COLORS["Red"]
        self.Length = 0
        self.Tail = []

    def Move(self):
        if self.Direction == DIRECTIONS.LEFT:
            self.X -= CONFIG["SIZE"]
        if self.Direction == DIRECTIONS.RIGHT:
            self.X += CONFIG["SIZE"]
        if self.Direction == DIRECTIONS.UP:
            self.Y -= CONFIG["SIZE"]
        if self.Direction == DIRECTIONS.DOWN:
            self.Y += CONFIG["SIZE"]