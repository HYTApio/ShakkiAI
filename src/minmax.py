""" Timer for minmax loops"""
import time
from checkmate import possible_moves as checkmate
from new_checkmate import is_check
from heuristics import heuristic

BIG_NUMBER = 100000000000
SMALL_NUMBER = -10000000000

def find_best_move(board):
    """Finds best possible move with best outcome

    returns move
    """
    possible_moves = board.legal_moves
    moves = {}

    for move in possible_moves:
        board.push(move)
        moves[move] = heuristic(board)
        board.pop()

    moves = sorted(moves, key=moves.get, reverse=True)
    best_move = moves[0]


    for depth in range(3, 12):
        start = time.time()
        value = SMALL_NUMBER
        valid_moves = board.legal_moves

        board.push(best_move)
        last_move = best_move
        value = _minmax(board, SMALL_NUMBER, BIG_NUMBER, depth, last_move)
        board.pop()

        end = time.time()
        for move in valid_moves:
            board.push(move)
            last_move = move
            score = _minmax(board, SMALL_NUMBER, BIG_NUMBER, depth, last_move)
            board.pop()
            if score > value:
                value, best_move = score, move
        end = time.time()
        print(f"{depth} syvyyden aika: {end-start}s")
        if end - start > 2:
            break
    return best_move

def _minmax(board, alpha, beta, depth, last_move):
    check = is_check(board, last_move)
    if check[0]:
        if checkmate(board, check[1]) is False:
            if board.turn is True:
                return SMALL_NUMBER
            return BIG_NUMBER

    if depth <= 0:
        return heuristic(board)

    return (_max_value(board, alpha, beta, depth, last_move)
    if board.turn is True else _min_value(board, alpha, beta, depth, last_move))

def _max_value(board, alpha, beta, depth, last_move):
    """ max value from min max

    return best move and its value"""

    value = SMALL_NUMBER

    valid_moves = board.legal_moves
    for move in valid_moves:
        board.push(move)
        last_move = move
        value = max(value, _minmax(board, alpha, beta, depth -1, last_move))
        board.pop()
        if value >= beta:
            return value
        alpha = max(alpha, value)
    return value

def _min_value(board, alpha, beta, depth, last_move):
    """ Min value from minmax

    return best move and its value
    """

    value = BIG_NUMBER

    valid_moves = board.legal_moves
    for move in valid_moves:
        board.push(move)
        last_move = move
        value = min(value, _minmax(board, alpha, beta, depth -1, last_move))
        board.pop()
        if value <= alpha:
            return value
        beta = min(beta, value)
    return value
