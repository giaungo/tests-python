import unittest

from app.flattern_json import flatten


class TestFlatternJSON(unittest.TestCase):

    def test_flattern(self):
        dic = {"a": 1, "b": {"c": 2, "d": [3, 4]}}
        expected = {"a": 1, "b.c": 2, "b.d": [3, 4]}
        actual = flatten(dic)
        self.assertEqual(actual, expected)
