import unittest

from src.shortest_path.shortest import shortest

def test_short(self):
        self.assertEqual(shortest(6, [[3, 6], [4, 3], [3, 2], [1, 3], [1, 2], [2, 4], [5, 2]]), 3)