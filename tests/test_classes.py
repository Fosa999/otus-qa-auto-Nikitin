from src.Rectangle import Rectangle
from src.Square import Square
from src.Circle import Circle
from src.Triangle import Triangle
import pytest


@pytest.mark.parametrize(("side_a", "side_b", "area", "perimeter"),
                         [(4, 6, 24, 20)])
def test_rectangle(side_a, side_b, area, perimeter):
    r = Rectangle(side_a, side_b)
    assert r.name == "Rectangle"
    assert r.get_area() == area
    assert r.get_perimeter() == perimeter


@pytest.mark.parametrize(("side_a", "side_b", "area", "perimeter"),
                         [( -2, 4, 24, 20),
                          (0, 0, 0, 0)])
def test_rectangle_negative(side_a, side_b, area, perimeter):
    with pytest.raises(ValueError):
        r = Rectangle(side_a, side_b)
        assert r.name == "Rectangle"
        assert r.get_area() == area
        assert r.get_perimeter() == perimeter


@pytest.mark.parametrize(("side_a", "area", "perimeter"),
                         [(4, 16, 16),
                          (1, 1, 4)])
def test_sqare(side_a, area, perimeter):
    r = Square(side_a)
    assert r.name == "Square"
    assert r.get_area() == area
    assert r.get_perimeter() == perimeter


@pytest.mark.parametrize(("side_a", "area", "perimeter"),
                         [(0, 16, 16),
                          (0, 1, 4)])
def test_sqare_negative(side_a, area, perimeter):
    with pytest.raises(ValueError):
        r = Square(side_a)
        assert r.name == "Square"
        assert r.get_area() == area
        assert r.get_perimeter() == perimeter



@pytest.mark.parametrize(("radius", "area", "perimeter"),
                         [(3, 28.274333882308138, 18.84955592153876)])
def test_circle(radius, area, perimeter):
    c = Circle(radius)
    assert c.name == "Circle"
    assert c.get_area() == area
    assert c.get_perimeter() == perimeter


@pytest.mark.parametrize(("radius", "area", "perimeter"),
                         [(-2, 0, 0)])
def test_circle_negative(radius, area, perimeter):
    with pytest.raises(ValueError):
        c = Circle(radius)
        assert c.name == "Circle"
        assert c.get_area() == area
        assert c.get_perimeter() == perimeter


@pytest.mark.parametrize(("side_a", "side_b", "side_c", "area", "perimeter"),
                         [(4, 4, 2, 8, 10),
                          (1, 2, 3, 1, 6)])
def test_triangle(side_a, side_b, side_c, area, perimeter):
    t = Triangle(side_a, side_b, side_c)
    assert t.name == "Triangle"
    assert t.get_area() == area
    assert t.get_perimeter() == perimeter


def test_add_area():
    r = Rectangle(2, 5)
    c = Circle(3)
    s = Square(3)
    t = Triangle(1,2,3)
    assert r.add_area(c) == 38.27433388230814
    assert s.add_area(t) == 10
    assert c.add_area(s) == 37.27433388230814
    assert t.add_area(r) == 11