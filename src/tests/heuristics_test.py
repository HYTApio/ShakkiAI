import unittest
import chess
from ai.heuristics import heuristic

class TestHeuristic(unittest.TestCase):
    def setUp(self):
        self.board = chess.Board()

    def test_beginning_value_equal(self):
        self.assertEqual(heuristic(self.board), 0)