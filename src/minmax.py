""" Module providing chess game base"""
import chess
from checkmate import is_check, possible_moves as checkmate
from heuristics import heuristic

BIG_NUMBER = 100000000000
SMALL_NUMBER = -10000000000

def max_value(board, alpha, beta, depth):

    if is_check(board):
        if not checkmate(board):
            if board.turn == True:
                    return (SMALL_NUMBER, None)
            else:
                return (BIG_NUMBER, None)


    if depth < 1:
        return (heuristic(board), None)

    value = SMALL_NUMBER
    best_move = None

    possible_moves = board.legal_moves
    best_moves = {}

    # Makes dictionary for all moves and next outcomes board heuristic
    for move in possible_moves:
        board.push(move)
        best_moves[move] = heuristic(board)
        board.pop()

    for move in sorted(best_moves, key=best_moves.get, reverse=True):
        board.push(move)
        (child_value, child_best_move) =  min_value(board, alpha, beta, depth-1)
        board.pop()

        if child_value > value:
            value = child_value
            best_move = move
        alpha = max(alpha, child_value)
        if alpha >= beta: 
            break

    return (value, best_move)

def min_value(board, alpha, beta, depth):

    if is_check(board):
        if not checkmate(board):
            if board.turn == True:
                    return (SMALL_NUMBER, None)
            else:
                return (BIG_NUMBER, None)

    if depth < 1:
        return (heuristic(board), None)

    value = BIG_NUMBER
    best_move = None
    
    possible_moves = board.legal_moves
    best_moves = {}
    for move in possible_moves:
        board.push(move)
        best_moves[move] = heuristic(board)
        board.pop()

    for move in sorted(best_moves, key=best_moves.get, reverse=False):
        board.push(move)
        (child_value, child_best_move) =  max_value(board, alpha, beta, depth-1)
        board.pop()

        if child_value < value:
            v = child_value
            best_move = move
        beta = min(beta, child_value)
        if alpha >= beta: 
            break

    return (value, best_move)
