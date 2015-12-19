import unittest

from task3 import Vector


class VectorTests(unittest.TestCase):
    def setUp(self):
        self.vector = Vector([1, 2, 3, 5])

    def tearDown(self):
        del self.vector

    def test_init(self):
        self.assertEqual([1, 2, 3, 5], self.vector)

    def test_length(self):
        self.vector = Vector([2, 4, 4])
        self.assertEqual(6, self.vector.length())

        self.vector = Vector([-1, 0, 3])
        self.assertEqual(10 ** 0.5, self.vector.length())

        self.vector = Vector([3, -4])
        self.assertEqual(5, self.vector.length())

    def test_normalize(self):
        self.vector = Vector([2, 4, 4])
        self.assertEqual(6, self.vector.length())

        self.vector = Vector([-1, 0, 3])
        self.assertEqual(10 ** 0.5, self.vector.length())

        self.vector = Vector([3, -4])
        self.assertEqual(5, self.vector.length())

    def test_addition(self):
        self.vector = Vector([2, 4, 4])
        self.assertEqual(self.vector + Vector([1, 0, 3]), Vector([3, 4, 7]))

        self.vector = Vector([0, -3, -2])
        self.assertEqual(self.vector + Vector([0, 3, 2]), Vector([0, 0, 0]))

    def test_subtraction(self):
        self.vector = Vector([9, 4, 6])
        self.assertEqual(self.vector - Vector([2, 2, 2]), Vector([7, 2, 4]))

        self.vector = Vector([0, 0, 0])
        self.assertEqual(self.vector - Vector([10, 9, 8]), Vector([-10, -9, -8]))

    def test_multiply(self):
        self.vector = Vector([7, 6, 5])
        self.assertEqual(self.vector * 3, Vector([21, 18, 15]))

        self.vector = Vector([-5, -4, -3])
        self.assertEqual(self.vector * -1, Vector([5, 4, 3]))

    def test_division(self):
        self.vector = Vector([24, 12, 6])
        self.assertEqual(self.vector / 6, Vector([4, 2, 1]))

        self.vector = Vector([1, 2, 3])
        self.assertEqual(self.vector / 2, Vector([0, 1, 1]))