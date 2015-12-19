import unittest

from task2 import new_json


class JSONTests(unittest.TestCase):
    def setUp(self):
        self.to_json = new_json.JSONEncoder()
        self.from_json = new_json.JSONDecoder()

    def tearDown(self):
        del self.to_json
        del self.from_json

    def test_number_json(self):
        number = 9999
        self.assertEqual("9999", self.to_json.to_json(number))
        self.assertEqual(number, self.from_json.from_json("9999"))

        number = 9.9
        self.assertEqual("9.9", self.to_json.to_json(number))
        self.assertEqual(number, self.from_json.from_json("9.9"))

    def test_iterable_json(self):
        test_list = [1, 2, 3, 4, 5]
        self.assertEqual('[1,2,3,4,5]', self.to_json.to_json(test_list))
        self.assertEqual(test_list, self.from_json.from_json('[1,2,3,4,5]'))

        test_set = {"a", "b", "c", "d"}
        self.assertEqual('["a","c","b","d"]', self.to_json.to_json(test_set))

        test_tuple = (5, 4, 3, 2, 1)
        self.assertEqual('[5,4,3,2,1]', self.to_json.to_json(test_tuple))

    def test_str_json(self):
        text = "the text from the json into the json"
        self.assertEqual('"{0}"'.format(text), self.to_json.to_json(text))

    def test_dict_json(self):
        d = {"red": 1, "yellow": 2, "green": 3, "dark": 4, "blue": 5}
        self.assertEqual('{"dark":4,"blue":5,"green":3,"yellow":2,"red":1}', self.to_json.to_json(d))
        self.assertEqual(d, self.from_json.from_json("{'dark':4,'blue':5,'green':3,'yellow':2,'red':1}"))

    def test_bool_and_none_json(self):
        self.assertEqual("null", self.to_json.to_json(None))
        self.assertEqual(None, self.from_json.from_json("null"))
        self.assertEqual("true", self.to_json.to_json(True))
        self.assertEqual(True, self.from_json.from_json("true"))
        self.assertEqual("false", self.to_json.to_json(False))
        self.assertEqual(False, self.from_json.from_json("false"))

