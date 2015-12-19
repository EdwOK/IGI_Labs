import unittest
import time

from task8 import cached


@cached
def function1_cached(n):
    return 0


@cached
def function2_cached(n):
    return 1


def forced_delay_normal(some_number):
    time.sleep(0.01)
    return some_number


@cached
def forced_delay_cached(some_number):
    time.sleep(0.01)
    return some_number


class CacheDecoratorTests(unittest.TestCase):
    def test_correctly_cached(self):
        self.assertEqual(function1_cached(1), 0)
        self.assertEqual(function2_cached(1), 1)

        self.assertEqual(function1_cached(1), 0)
        self.assertEqual(function2_cached(1), 1)

    def test_validate_timing(self):
        start = time.time()
        for _ in range(0, 10):
            forced_delay_normal(5)
        stop = time.time()
        normal_duration = (stop - start) * 1000

        start = time.time()
        for _ in range(0, 10):
            forced_delay_cached(6)
        stop = time.time()
        cached_duration = (stop - start) * 1000

        self.assertTrue(cached_duration < normal_duration,
                        msg="normal: %dms < cached: %dms" % (normal_duration, cached_duration))