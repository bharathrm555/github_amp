import os
import sys

sys.path.append(os.path.dirname(os.path.dirname(__file__)))

from src.calculator_plus import Calculator


def run_tests():
    c = Calculator()

    assert c.add(16, 4) == 20
    assert c.subtract(16, 4) == 12
    assert c.multiply(16, 4) == 64
    assert c.divide(16, 4) == 4
    assert c.square_root(25) == 5

    try:
        c.divide(10, 0)
        raise AssertionError("Expected ValueError for division by zero")
    except ValueError as err:
        assert str(err) == "Cannot divide by zero."

    print("All calculator tests passed.")


if __name__ == "__main__":
    run_tests()
