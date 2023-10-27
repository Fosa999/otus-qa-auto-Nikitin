import math

from src.Figure import Figure


class Circle(Figure):
    def __init__(self, radius):
        super().__init__()
        if radius <= 0:
            raise ValueError("Can't create circle")
        self.radius = radius
        self.name = "Circle"

    def get_area(self):
        return math.pi * self.radius ** 2

    def get_perimeter(self):
        return 2 * math.pi * self.radius


c = Circle
