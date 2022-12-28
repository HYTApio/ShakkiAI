import unittest
import chess
from ai.minmax import find_best_move


class TestCheckmate(unittest.TestCase):

    def test_does_check_mate(self):
        board = chess.Board('k7/7Q/8/6Q1/4K3/8/8/8 w KQkq - 0 1')        
        move = find_best_move(board)
        self.assertEqual(move[1], 100000000000)

    # from internet check in 3 moves puzzles fens https://wtharvey.com/m8n3.txt

    def test_does_check_mate_puzzle1(self):
        board = chess.Board('r5rk/5p1p/5R2/4B3/8/8/7P/7K w KQkq - 0 1')        
        move = find_best_move(board)
        self.assertEqual(move[1], 100000000000)

    def test_does_check_mate_puzzle2(self):
        board = chess.Board('r3k2r/ppp2Npp/1b5n/4p2b/2B1P2q/BQP2P2/P5PP/RN5K w kq - 1 0')        
        move = find_best_move(board)
        self.assertEqual(move[1], 100000000000)

    def test_does_check_mate_puzzle3(self):
        board = chess.Board('3q1r1k/2p4p/1p1pBrp1/p2Pp3/2PnP3/5PP1/PP1Q2K1/5R1R w - - 1 0')        
        move = find_best_move(board)
        self.assertEqual(move[1], 100000000000)

    def test_does_check_mate_puzzle4(self):
        board = chess.Board('1q2r3/k4p2/prQ2b1p/R7/1PP1B1p1/6P1/P5K1/8 w - - 1 0')        
        move = find_best_move(board)
        self.assertEqual(move[1], 100000000000)


    def test_does_check_mate_puzzle5(self):
        board = chess.Board('rnbk1b1r/ppqpnQ1p/4p1p1/2p1N1B1/4N3/8/PPP2PPP/R3KB1R w - - 1 0')        
        move = find_best_move(board)
        self.assertEqual(move[1], 100000000000)


    def test_does_check_mate_puzzle6(self):
        board = chess.Board('k7/1p1rr1pp/pR1p1p2/Q1pq4/P7/8/2P3PP/1R4K1 w - - 1 0')        
        move = find_best_move(board)
        self.assertEqual(move[1], 100000000000)

    def test_does_check_mate_puzzle7(self):
        board = chess.Board('r2qkb1r/pp2nppp/3p4/2pNN1B1/2BnP3/3P4/PPP2PPP/R2bK2R w KQkq - 1 0')        
        move = find_best_move(board)
        self.assertEqual(move[1], 100000000000)