import unittest

from task9 import XRange


class XRangeTests(unittest.TestCase):
    def setUp(self):
        self.r = XRange(0)

    def tearDown(self):
        del self.r

    def test_init(self):
        self.assertEqual(0, self.r._start)
        self.assertEqual(0, self.r._stop)
        self.assertEqual(1, self.r._step)

        self.r = XRange(1)
        self.assertEqual(0, self.r._start)
        self.assertEqual(1, self.r._stop)
        self.assertEqual(1, self.r._step)

        self.r = XRange(2)
        self.assertEqual(0, self.r._start)
        self.assertEqual(2, self.r._stop)
        self.assertEqual(1, self.r._step)

        self.assertRaises(TypeError, xrange, 1, 2, 3, 4)
        self.assertRaises(TypeError, xrange, "abc")
        self.assertRaises(ValueError, xrange, 1, 2, 0)

    def test_repr(self):
        self.assertEqual(repr(xrange(1)), "xrange(1)")
        self.assertEqual(repr(xrange(1, 2)), "xrange(1, 2)")
        self.assertEqual(repr(xrange(1, 3, 2)), "xrange(1, 3, 2)")

    def test_contains(self):
        self.r = [i for i in XRange(0, 5, 2)]
        self.assertFalse(-1 in self.r)
        self.assertFalse(1 in self.r)
        self.assertFalse(3 in self.r)
        self.assertTrue(0 in self.r)

    def test_iter_basic(self):
        self.assertEqual([], [x for x in XRange(0)])

        self.assertEqual([0], [x for x in XRange(1)])

        self.assertEqual([0, 1, 2], [x for x in XRange(3)])

        self.assertEqual([0, 2, 4], [x for x in XRange(0, 5, 2)])

        self.assertEqual([5, 3, 1], [x for x in XRange(5, 0, -2)])

        iterator = iter(XRange(5))
        self.assertTrue(iterator is iter(iterator))