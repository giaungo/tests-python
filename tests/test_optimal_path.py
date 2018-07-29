import unittest

from app.optimal_path import find_optimal_path


class TestOptimalPath(unittest.TestCase):

    def test_optimal_path(self):
        edges = [['A', 'B'], ['B', 'C'], ['A', 'C']]
        weight = {'A': 1, 'B': 2, 'C': 2}
        expected = 5
        actual = find_optimal_path(edges, 'A', weight)
        self.assertEqual(actual, expected)
