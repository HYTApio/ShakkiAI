import unittest
import chess
from minmax import find_best_move


class TestCheckmate(unittest.TestCase):

    def test_does_check_mate(self):
        board = chess.Board('k7/7Q/8/6Q1/4K3/8/8/8 w KQkq - 0 1')        
        move = find_best_move(board)
        self.assertEqual(move, chess.Move.from_uci('e4f3'))