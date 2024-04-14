import math

from Figure import Figure


class Circle(Figure):
    def __init__(self, radius):
        super().__init__("Circle")
        if radius <= 0:
            raise ValueError("Радиус не может быть равен или быть меньше 0")
        self.radius = radius
        self.name = "Circle"

    def get_area(self):
        return math.pi * self.radius ** 2

    def get_perimeter(self):
        return 2 * math.pi * self.radius


cir = Circle(3)
