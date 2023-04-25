import sys
from pathlib import Path

sys.path.append(str(Path(__file__).resolve().parents[1]))

from job04.job04 import Forme, Rectangle
from math import pi

class Cercle(Forme):
    def __init__(self, radius):
        self.radius = radius
    
    def aire(self):
        super().aire()
        return pi * (self.radius ** 2)

if __name__ == "__main__":
    rectangle = Rectangle(10, 15)
    print(rectangle.aire())

    cercle = Cercle(10)
    print(cercle.aire())
# end main