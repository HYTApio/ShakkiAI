""" Module providing chess base"""
import chess


# Pelinappuloiden pistelaudat
piece_position_values = [
    [],
    [
    0, 0, 0, 0, 0, 0, 0, 0,
    5, 10, 10, -20, -20, 10, 10, 5,
    5, -5, 0, 0, 0, 0, -5, 5,
    0, 0, 5, 20, 20, 5, 0, 0,
    5, 5, 10, 25, 25, 10, 5, 5,
    10, 10, 20, 30, 30, 20, 10, 10,
    50, 50, 50, 50, 50, 50, 50, 50,
    0, 0, 0, 0, 0, 0, 0, 0],

    [
    -50, -40, -40, -40, -40, -40, -40, -50,
    -40, -20, 0, 0, 0, 0, -20, -40,
    -40, 5, 15, 15, 15, 15, 5, -40,
    -40, 5, 15, 20, 20, 15, 5, -40,
    -40, 5, 15, 20, 20, 15, 5, -40,
    -40, 0, 15, 15, 15, 15, 0, -40,
    -40, -20, 0, 0, 0, 0, -20, -40,
    -50, -40, -40, -40, -40, -40, -40, -50],
    [
    -20, -10, -10, -10, -10, -10, -10, -20,
    -10, 5, 0, 0, 0, 0, 5, -10,
    -10, 10, 10, 10, 10, 10, 10, -10,
    -10, 0, 10, 10, 10, 10, 0, -10,
    -10, 5, 5, 10, 10, 5, 5, -10,
    -10, 0, 5, 10, 10, 5, 0, -10,
    -10, 0, 0, 0, 0, 0, 0, -10,
    -20, -10, -10, -10, -10, -10, -10, -20],
    [
    0, 0, 5, 5, 5, 5, 0, 0,
    -5, 0, 0, 0, 0, 0, 0, -5,
    -5, 0, 0, 0, 0, 0, 0, -5,
    -5, 0, 0, 0, 0, 0, 0, -5,
    -5, 0, 0, 0, 0, 0, 0, -5,
    -5, 0, 0, 0, 0, 0, 0, -5,
    5, 10, 10, 10, 10, 10, 10, 5,
    0, 0, 0, 0, 0, 0, 0, 0],
    [
    -20, -10, -10, -5, -5, -10, -10, -20,
    -10, 0, 0, 0, 0, 0, 0, -10,
    -10, 5, 5, 5, 5, 5, 0, -10,
    0, 0, 5, 5, 5, 5, 0, -5,
    -5, 0, 5, 5, 5, 5, 0, -5,
    -10, 0, 5, 5, 5, 5, 0, -10,
    -10, 0, 0, 0, 0, 0, 0, -10,
    -20, -10, -10, -5, -5, -10, -10, -20],
    [
    20, 30, 10, 0, 0, 10, 30, 20,
    20, 20, 0, 0, 0, 0, 20, 20,
    -10, -20, -20, -20, -20, -20, -20, -10,
    -20, -30, -30, -40, -40, -30, -30, -20,
    -30, -40, -40, -50, -50, -40, -40, -30,
    -30, -40, -40, -50, -50, -40, -40, -30,
    -30, -40, -40, -50, -50, -40, -40, -30,
    -30, -40, -40, -50, -50, -40, -40, -30]
]


# Peli nappuloiden arvot
# 0 = tyhjä, 1 = sotilas, 2 = ratsu, 3 = lähetti,
# 4 = torni, 5 = kuningatar, 6 = kuningas
piece_values = [None, 1, 3.1, 3.2, 5, 9, 10]

def _value(board, piece, color):
    """ Calculates values for a type of pawn

    returns value
    """
    if color:
        score = ((len(board.pieces(piece, color)) * piece_values[piece])
        + sum(piece_position_values[piece][i] for i in board.pieces(piece, color)))

    else:
        score = ((len(board.pieces(piece, color)) * piece_values[piece]) +
        sum(piece_position_values[piece][chess.square_mirror(i)] for i in board.pieces(piece, color)))
    return score

def heuristic(board):
    """ Calculates boards value

    returns value
    """
    score = 0

    for pawn in range(1, 7):
        score += _value(board, pawn, True)
        score -= _value(board, pawn, False)

    return score
