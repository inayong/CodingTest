import unittest

from src.bfs.maze_escape import maze_escape
from src.bfs.word_conversion import word_conversion

class TestBFS(unittest.TestCase):

    def test_maze_escape(self):
        self.assertEqual(maze_escape(0,0,[[1,0,1,0,1,0],[1,1,1,1,1,1],[0,0,0,0,0,1],[1,1,1,1,1,1],[1,1,1,1,1,1]]), 10)

    def test_word_conversion(self):
        self.assertEqual(word_conversion("hit", "cog", ["hot", "dot", "dog", "lot", "log", "cog"]), 4)