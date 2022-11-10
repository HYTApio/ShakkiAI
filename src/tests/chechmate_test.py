import unittest
import checkmate
import chess

class TestCheckmate(unittest.TestCase):
    def setUp(self):
        self.board = chess.Board()
    
    def test_beginning_not_check(self):
        self.assertEqual(checkmate.is_check(self.board), False)
