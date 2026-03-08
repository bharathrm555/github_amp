import os
import sys

sys.path.append(os.path.dirname(os.path.dirname(__file__)))

from src.geometry_calculator import GeometryCalculator


def run_tests():
    g = GeometryCalculator()

    circle = g.calculate_circle_area(5)
    rectangle = g.calculate_rectangle_area(10, 6)

    assert round(circle, 6) == round(78.53981633974483, 6)
    assert rectangle == 60

    print("All geometry tests passed.")

if __name__ == "__main__":
    run_tests()
