from Figure import Figure


class Rectangle(Figure):
    def __init__(self, side_a, side_b):
        super().__init__('Rectangle')
        if side_a <= 0 or side_b <= 0:
            raise ValueError("Одна или несколько сторон равна, либо меньше 0")
        self.side_a = side_a
        self.side_b = side_b
        self.name = 'Rectangle'

    # @property
    def get_area(self):
        return self.side_a * self.side_b

    def get_perimeter(self):
        return 2 * (self.side_a + self.side_b)


r = Rectangle(2, 3)