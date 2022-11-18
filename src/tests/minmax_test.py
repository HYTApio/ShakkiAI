import unittest
import chess
from minmax import max_value


class TestCheckmate(unittest.TestCase):
    def setUp(self):
        self.board = chess.Board()
        self.BIG_NUMBER = 100000000000
        self.SMALL_NUMBER = -10000000000


    def test_does_check_mate(self):
        board = chess.Board('k7/8/6Q1/6Q1/4K3/8/8/8 w KQkq - 0 1')
        (value, move) = max_value(board, self.SMALL_NUMBER, self.BIG_NUMBER, 3)

        self.assertEqual(value, self.BIG_NUMBER)