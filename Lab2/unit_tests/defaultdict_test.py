import unittest

from task6 import DefaultDict


class DefaultDictTests(unittest.TestCase):
    def setUp(self):
        self.dd = DefaultDict(list)

    def tearDown(self):
        del self.dd

    def test_addition(self):
        items = [("yellow", 1), ("blue", 2), ("green", 3), ("dark", 4), ("red", 5)]
        for k, v in items:
            self.dd[k][v] = v

        self.assertTrue({2: 2} in self.dd.values())
        self.assertTrue({5: 5} in self.dd.values())
        self.assertFalse({-1, -1} in self.dd.values())