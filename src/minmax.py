""" Timer for minmax loops"""
import time
from checkmate import possible_moves as checkmate
from new_checkmate import is_check
from heuristics import heuristic

BIG_NUMBER = 100000000000
SMALL_NUMBER = -10000000000

def minmax(board, last_move):
    possible_moves = board.legal_moves
    moves = {}

    # Makes dictionary for all moves and next outcomes board heuristic
    for move in possible_moves:
        board.push(move)
        moves[move] = heuristic(board)
        board.pop()

    moves = sorted(moves, key=moves.get, reverse=True)

    best_moves = {}

    for depth in range (3, 12):
        start = time.time()
        for move in moves:
            board.push(move)
            (_, move) = _max_value(board, SMALL_NUMBER, BIG_NUMBER, depth, last_move)
            board.pop()
        end = time.time()
        print(end - start)
        if end - start > 2:
            return move

def _max_value(board, alpha, beta, depth, last_move):
    """ max value from min max

    return best move and its value"""

    if is_check(board, last_move):
        if not checkmate(board):
            if board.turn is True:
                return (SMALL_NUMBER, None)

            return (BIG_NUMBER, None)


    if depth < 1:
        return (heuristic(board), None)

    value = SMALL_NUMBER
    best_move = None

    possible_moves = board.legal_moves

    for move in possible_moves:
        board.push(move)
        (child_value, _) =  _min_value(board, alpha, beta, depth-1, move)
        board.pop()

        if child_value > value:
            value = child_value
            best_move = move
        alpha = max(alpha, child_value)
        if alpha >= beta:
            break

    return (value, best_move)

def _min_value(board, alpha, beta, depth, last_move):
    """ Min value from minmax

    return bets move and its value
    """

    if is_check(board, last_move):
        if not checkmate(board):
            if board.turn is True:
                return (SMALL_NUMBER, None)

            return (BIG_NUMBER, None)

    if depth < 1:
        return (heuristic(board), None)

    value = BIG_NUMBER
    best_move = None

    possible_moves = board.legal_moves

    for move in possible_moves:
        board.push(move)
        (child_value, _) =  _max_value(board, alpha, beta, depth-1, move)
        board.pop()

        if child_value < value:
            value = child_value
            best_move = move
        beta = min(beta, child_value)
        if alpha >= beta:
            break

    return (value, best_move)
