import os
import unittest

from task7 import *


class SimpleClass(object):
    __metaclass__ = MetaClass
    file_name = "test_attributes.txt"


class MetaClassTests(unittest.TestCase):
    def setUp(self):
        self.simple = SimpleClass()

    def tearDown(self):
        del self.simple

    def test_attributes(self):
        self.assertEqual(self.simple.a, "1")
        self.assertEqual(self.simple.b, "2")
        self.assertEqual(self.simple.c, "3")
