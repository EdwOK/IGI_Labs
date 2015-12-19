import unittest

from task4 import LinearFunction


class LinearFunctionTests(unittest.TestCase):
    def setUp(self):
        self.function1 = LinearFunction()
        self.function2 = LinearFunction()

    def tearDown(self):
        del self.function1
        del self.function2

    def test_init(self):
        self.assertEqual(str(self.function1), "y = 1x + 0")

        self.function1 = LinearFunction(5, 3)
        self.assertEqual(str(self.function1), "y = 5x + 3")

    def test_addition(self):
        self.function1 = LinearFunction(9, 10)
        self.function2 = LinearFunction(3, 12)
        self.assertEqual(str(self.function1 + self.function2), "y = 12x + 22")

    def test_multiply(self):
        self.function1 = LinearFunction(-2, 9)
        self.assertEqual(str(self.function1 * 5), "y = -10x + 45")

    def test_composition(self):
        self.function1 = LinearFunction(1, 2)
        self.function2 = LinearFunction(3, 4)

        self.assertEqual(str(self.function1(self.function2)), "y = 3x + 6")

    def test_get_value(self):
        self.function1 = LinearFunction(5, -3)
        self.assertEqual(self.function1(1), 2)