import os
import unittest

from task1 import merge_sort, generate_file


def array_sorted(array):
    first = array[0]
    for current in xrange(1, len(array)):
        if first < current:
            first = current
        else:
            return False
    return True


class ExternalMergeSortTests(unittest.TestCase):
    def setUp(self):
        self.file_name = "_numbers.txt"
        for count in xrange(2, 6):
            generate_file(str(10 ** count) + self.file_name, 10 ** count)

    def tearDown(self):
        for count in xrange(2, 6):
            file_path = str(10 ** count) + self.file_name
            if os.path.isfile("sorted_" + file_path):
                os.remove("sorted_" + file_path)
            if os.path.isfile(file_path):
                os.remove(file_path)
        del self.file_name

    def test_hundred_numbers(self):
        merge_sort(str(100) + self.file_name, 10)
        with open("sorted_" + str(100) + self.file_name, "r") as file:
            numbers = map(int, file.read().split())
            self.assertTrue(True, array_sorted(numbers))

    def test_thousand_numbers(self):
        merge_sort(str(1000) + self.file_name, 100)
        with open("sorted_" + str(1000) + self.file_name, "r") as file:
            numbers = map(int, file.read().split())
            self.assertTrue(True, array_sorted(numbers))

    def test_ten_thousand_numbers(self):
        merge_sort(str(10000) + self.file_name, 1000)
        with open("sorted_" + str(10000) + self.file_name, "r") as file:
            numbers = map(int, file.read().split())
            self.assertTrue(True, array_sorted(numbers))

    def test_one_hundred_thousand_numbers(self):
        merge_sort(str(100000) + self.file_name, 10000)
        with open("sorted_" + str(100000) + self.file_name, "r") as file:
            numbers = map(int, file.read().split())
            self.assertTrue(True, array_sorted(numbers))