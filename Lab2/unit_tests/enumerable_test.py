import unittest

from task10 import Enumerable


class EnumerableTests(unittest.TestCase):
    def setUp(self):
        self.enumerable = Enumerable([1, 2, 3, 4])

    def test_where(self):
        where_collection = self.enumerable.where(lambda x: x > 2)
        self.assertEqual(where_collection, [3, 4])

        where_collection = self.enumerable.where(lambda x: x <= 1)
        self.assertEqual(where_collection, [1])

        where_collection = self.enumerable.where(lambda x: x == 4)
        self.assertEqual(where_collection, [4])