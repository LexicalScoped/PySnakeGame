import random
from config import COLORS, CONFIG

class Food():
    def __init__(self):
        self.X = round(random.randrange(0,CONFIG["X"] - CONFIG["SIZE"]), -1)
        self.Y = round(random.randrange(0,CONFIG["Y"] - CONFIG["SIZE"]), -1)
        self.Color = COLORS["LightBlue"]