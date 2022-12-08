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

    def test_checkmate_from_two_directions(self):
        board = chess.Board('k7/8/q7/q7/q3K3/q7/8/8 w KQkq - 0 1')
        self.assertEqual(checkmate.possible_moves(board, [40, 24]), False)

    def test_checkmate_from_left(self):
        board = chess.Board('k7/8/8/q7/q3K3/q7/8/8 w KQkq - 0 1')
        self.assertEqual(checkmate.possible_moves(board, [24]), False)

    def test_checkmate_from_right(self):
        board = chess.Board('k7/8/8/q7/4K2q/q7/8/8 w KQkq - 0 1')
        self.assertEqual(checkmate.possible_moves(board, [31]), False)

    def test_checkmate_from_above(self):
        board = chess.Board('k2qqq2/8/8/q7/4K3/q7/8/8 w KQkq - 0 1')
        self.assertEqual(checkmate.possible_moves(board, [60]), False)

    def test_checkmate_from_below(self):
        board = chess.Board('k7/8/8/q7/4K3/q7/8/3qqq2 w KQkq - 0 1')
        self.assertEqual(checkmate.possible_moves(board, [4]), False)

    def test_can_eliminate_checker_above(self):
        board = chess.Board('k3q2Q/8/8/q7/4K3/q7/8/3q1q2 w KQkq - 0 1')
        self.assertEqual(checkmate.possible_moves(board, [60]), True)

    def test_can_eliminate_checker_below(self):
        board = chess.Board('k7/8/8/q7/4K3/2Q5/8/3qqq2 w KQkq - 0 1')
        self.assertEqual(checkmate.possible_moves(board, [4]), True)

    def test_can_eliminate_checker_left(self):
        board = chess.Board('k7/8/8/7q/q3K3/Q6q/8/8 w KQkq - 0 1')
        self.assertEqual(checkmate.possible_moves(board, [24]), True)

    def test_can_eliminate_checker_right(self):
        board = chess.Board('k7/8/8/q7/4K2q/q6Q/8/8 w KQkq - 0 1')
        self.assertEqual(checkmate.possible_moves(board, [31]), True)

    def test_can_block_checker_above(self):
        board = chess.Board('k3q3/7Q/8/q7/4K3/q7/8/3q1q2 w KQkq - 0 1')
        self.assertEqual(checkmate.possible_moves(board, [60]), True)

    def test_can_block_checker_below(self):
        board = chess.Board('k2q1q2/8/8/8/4K3/8/Q7/4q3 w KQkq - 0 1')
        self.assertEqual(checkmate.possible_moves(board, [4]), True)

    def test_can_block_checker_left(self):
        board = chess.Board('k7/8/8/7q/q3K3/3Q3q/8/8 w KQkq - 0 1')
        self.assertEqual(checkmate.possible_moves(board, [24]), True)

    def test_can_block_checker_right(self):
        board = chess.Board('k7/8/8/q7/4K2q/q7/8/6Q1 w KQkq - 0 1')
        self.assertEqual(checkmate.possible_moves(board, [31]), True)

    def test_can_block_checker_right_up_diag(self):
        board = chess.Board('k7/1q6/7Q/q7/4K3/q7/8/8 w KQkq - 0 1')
        self.assertEqual(checkmate.possible_moves(board, [49]), True)

    def test_can_block_checker_left_up_diag(self):
        board = chess.Board('k7/7q/Q7/q7/4K3/q7/8/8 w KQkq - 0 1')
        self.assertEqual(checkmate.possible_moves(board, [55]), True)

    def test_can_block_checker_right_down_diag(self):
        board = chess.Board('k7/8/8/q7/4K3/q7/7Q/1q6 w KQkq - 0 1')
        self.assertEqual(checkmate.possible_moves(board, [1]), True)

    def test_can_block_checker_left_down_diag(self):
        board = chess.Board('k7/7q/Q7/q7/4K3/q7/Q7/7q w KQkq - 0 1')
        self.assertEqual(checkmate.possible_moves(board, [7]), True)