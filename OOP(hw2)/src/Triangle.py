from Figure import Figure


class Triangle(Figure):
    def __init__(self, side_a, side_b, side_c):
        super().__init__("Triangle")
        if side_a <= 0 or side_b <= 0 or side_c <= 0:
            raise ValueError("Одна или несколько сторон равна, либо меньше 0")
        self.side_a = side_a
        self.side_b = side_b
        self.side_c = side_c
        self.name = "Triangle"

    def get_area(self):
        return self.side_a * self.side_b / 2

    def get_perimeter(self):
        return self.side_a + self.side_b + self.side_c


tr = Triangle(3, 4, 5)
