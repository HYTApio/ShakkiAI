import unittest
import checks.checkmate as checkmate
import chess


class TestCheckmate(unittest.TestCase):
    def setUp(self):
        self.board = chess.Board()

    def test_beginning_not_check(self):
        self.assertEqual(checkmate.is_attacked(self.board, self.board.king(chess.WHITE)), False)

    def test_check_from_above(self):
        board = chess.Board('3qk3/8/8/8/8/8/8/3K4 w KQkq - 0 1')
        self.assertEqual(checkmate.is_attacked(board, board.king(chess.WHITE)), True)
        board = chess.Board('3rk3/8/8/8/8/8/8/3K4 w KQkq - 0 1')
        self.assertEqual(checkmate.is_attacked(board, board.king(chess.WHITE)), True)
        board = chess.Board('4k3/8/8/8/8/8/8/3K4 w KQkq - 0 1')
        self.assertEqual(checkmate.is_attacked(board, board.king(chess.WHITE)), False)

    def test_check_from_below(self):
        board = chess.Board('4K3/8/8/8/8/8/8/3kq3 w KQkq - 0 1')
        self.assertEqual(checkmate.is_attacked(board, board.king(chess.WHITE)), True)
        board = chess.Board('4K3/8/8/8/8/8/8/3kr3 w KQkq - 0 1')
        self.assertEqual(checkmate.is_attacked(board, board.king(chess.WHITE)), True)
        board = chess.Board('4K3/8/8/8/8/8/8/4k3 w KQkq - 0 1')
        self.assertEqual(checkmate.is_attacked(board, board.king(chess.WHITE)), False)

    def test_check_from_left(self):
        board = chess.Board('1q1K4/8/8/8/8/8/8/3k4 w KQkq - 0 1')
        self.assertEqual(checkmate.is_attacked(board, board.king(chess.WHITE)), True)
        board = chess.Board('1r1K4/8/8/8/8/8/8/3k4 w KQkq - 0 1')
        self.assertEqual(checkmate.is_attacked(board, board.king(chess.WHITE)), True)
        board = chess.Board('3k4/8/8/8/8/8/8/3K4 w KQkq - 0 1')
        self.assertEqual(checkmate.is_attacked(board, board.king(chess.WHITE)), False)

    def test_check_from_right(self):
        board = chess.Board('4K1q1/8/8/8/8/8/8/3k4 w KQkq - 0 1')
        self.assertEqual(checkmate.is_attacked(board, board.king(chess.WHITE)), True)
        board = chess.Board('4K1r1/8/8/8/8/8/8/3k4 w KQkq - 0 1')
        self.assertEqual(checkmate.is_attacked(board, board.king(chess.WHITE)), True)
        board = chess.Board('4k3/8/8/8/8/8/8/3K4 w KQkq - 0 1')
        self.assertEqual(checkmate.is_attacked(board, board.king(chess.WHITE)), False)

    def test_check_from_diag_above(self):
        board = chess.Board('8/5p2/4K3/8/8/8/8/3k4 w KQkq - 0 1')
        self.assertEqual(checkmate.is_attacked(board, board.king(chess.WHITE)), True)
        board = chess.Board('8/3p4/4K3/8/8/8/8/3k4 w KQkq - 0 1')
        self.assertEqual(checkmate.is_attacked(board, board.king(chess.WHITE)), True)
        board = chess.Board('8/8/8/2q5/8/4K3/8/3k4 w KQkq - 0 1')
        self.assertEqual(checkmate.is_attacked(board, board.king(chess.WHITE)), True)
        board = chess.Board('8/8/8/6q1/8/4K3/8/3k4 w KQkq - 0 1')
        self.assertEqual(checkmate.is_attacked(board, board.king(chess.WHITE)), True)
        board = chess.Board('8/8/2b5/8/4K3/8/8/3k4 w KQkq - 0 1')
        self.assertEqual(checkmate.is_attacked(board, board.king(chess.WHITE)), True)
        board = chess.Board('8/8/6b1/8/4K3/8/8/3k4 w KQkq - 0 1')
        self.assertEqual(checkmate.is_attacked(board, board.king(chess.WHITE)), True)

    def test_check_from_diag_below(self):
        board = chess.Board('8/8/4k3/8/5P2/8/8/3K4 w KQkq - 0 1')
        board.push(chess.Move.from_uci("f4f5"))
        self.assertEqual(checkmate.is_attacked(board, board.king(chess.BLACK)), True)
        board = chess.Board('8/8/4k3/8/3P4/8/8/3K4 w KQkq - 0 1')
        board.push(chess.Move.from_uci("d4d5"))
        self.assertEqual(checkmate.is_attacked(board, board.king(chess.BLACK)), True)
        board = chess.Board('8/4K3/8/2q5/8/8/8/3k4 w KQkq - 0 1')
        self.assertEqual(checkmate.is_attacked(board, board.king(chess.WHITE)), True)
        board = chess.Board('8/4K3/8/6q1/8/8/8/3k4 w KQkq - 0 1')
        self.assertEqual(checkmate.is_attacked(board, board.king(chess.WHITE)), True)
        board = chess.Board('4K3/8/2b5/8/8/8/8/3k4 w KQkq - 0 1')
        self.assertEqual(checkmate.is_attacked(board, board.king(chess.WHITE)), True)
        board = chess.Board('4K3/8/6b1/8/8/8/8/3k4 w KQkq - 0 1')
        self.assertEqual(checkmate.is_attacked(board, board.king(chess.WHITE)), True)
        board = chess.Board('4K3/5P2/6b1/8/8/8/8/3k4 w KQkq - 0 1')
        self.assertEqual(checkmate.is_attacked(board, board.king(chess.WHITE)), False)
        board = chess.Board('4K3/3P4/2b5/8/8/8/8/3k4 w KQkq - 0 1')
        self.assertEqual(checkmate.is_attacked(board, board.king(chess.WHITE)), False)

    def test_check_knight(self):
        board = chess.Board('k7/8/8/2n5/4K3/8/8/8 w KQkq - 0 1')
        self.assertEqual(checkmate.is_attacked(board, board.king(chess.WHITE)), True)

    def test_move_from_checkmate(self):
        board = chess.Board('KPPPPPPP/8/qqqqqqqq/8/4k3/8/8/PPPPPPPP w KQkq - 0 1')
        self.assertEqual(checkmate.possible_moves(board, [40]), True)

    def test_move_from_check(self):
        board = chess.Board('k7/8/q7/8/4K3/8/8/8 w KQkq - 0 1')
        self.assertEqual(checkmate.possible_moves(board, [40]), True)
