""" Module providing chess game base"""
import chess


def _below(board, turn, squarerank, squarefile):
    """Checks if square is attacked from below

    returns True if it is
            False if not
    """
    for rank in range(squarerank-1, -1, -1):
        square_number = chess.square(squarefile, rank)
        # if rook or queen is in square
        if board.piece_type_at(square_number) in [4, 5] and board.color_at(square_number) != turn:
            return True
        # if there is other pawn first than enemy queen / rook no threat
        if board.piece_type_at(square_number) is not None:
            return False

    return False


def _above(board, turn, squarerank, squarefile):
    """Checks if square is attacked from above

    returns True if it is
            False if not
    """
    for rank in range(squarerank+1, 8):
        square_number = chess.square(squarefile, rank)
        # if rook or queen is in square
        if board.piece_type_at(square_number) in [4, 5] and board.color_at(square_number) != turn:
            return True

        # if there is other pawn first than enemy queen / rook no threat
        if board.piece_type_at(square_number) is not None:
            return False

    return False


def _left(board, turn, squarerank, squarefile):
    """Checks if square is attacked from left

    returns True if it is
            False if not
    """
    for file in range(squarefile-1, -1, -1):
        square_number = chess.square(file, squarerank)
        # if rook or queen in square
        if board.piece_type_at(square_number) in [4, 5] and board.color_at(square_number) != turn:
            return True

        # if there is other pawn first than enemy queen / rook no threat
        if board.piece_type_at(square_number) is not None:
            return False

    return False


def _right(board, turn, squarerank, squarefile):
    """Checks if square is attacked from right

    returns True if it is
            False if not
    """
    for file in range(squarefile+1, 8):
        square_number = chess.square(file, squarerank)
        # if rook or queen in square
        if board.piece_type_at(square_number) in [4, 5] and board.color_at(square_number) != turn:
            return True

        # if there is other pawn first than enemy queen / rook no threat
        if board.piece_type_at(square_number) is not None:
            return False

    return False


def _diag_above(board, turn, squarerank, squarefile):
    """Checks if square is attacked diagonally from above

    returns True if it is
            False if not
    """
    right = True
    left = True
    rightsquarefile = squarefile
    leftsquarefile = squarefile
    for rank in range(squarerank+1, 8):
        rightsquarefile += 1
        leftsquarefile -= 1
        square_number = chess.square(rightsquarefile, rank)
        if rightsquarefile == squarefile+1 and (-1 < square_number < 64):
            # if black pawn on square
            if board.piece_type_at(square_number) in [1] and board.color_at(square_number) != turn and turn == chess.WHITE:
                return True

        square_number = chess.square(leftsquarefile, rank)
        if leftsquarefile == squarefile-1 and (-1 < square_number < 64):
            # if black pawn on square
            if board.piece_type_at(square_number) in [1] and board.color_at(square_number) != turn and turn == chess.WHITE:
                return True

        if leftsquarefile > -1 and left:
            # if bishop or queen in square
            if board.piece_type_at(square_number) in [3, 5] and board.color_at(square_number) != turn:
                return True

            # if there is other pawn first than enemy queen / rook no threat
            if board.piece_type_at(square_number) is not None:
                left = False

        square_number = chess.square(rightsquarefile, rank)
        if rightsquarefile < 8 and right:
            # if bishop or queen in square
            if board.piece_type_at(square_number) in [3, 5] and board.color_at(square_number) != turn:
                return True

            # if there is other pawn first than enemy queen / rook no threat
            if board.piece_type_at(square_number) is not None:
                right = False

    return False


def _diag_below(board, turn, squarerank, squarefile):
    """Checks if square is attacked diagonally from below

    returns True if it is
            False if not
    """
    right = True
    left = True
    rightsquarefile = squarefile
    leftsquarefile = squarefile
    for rank in range(squarerank-1, -1, -1):
        rightsquarefile += 1
        leftsquarefile -= 1
        square_number = chess.square(rightsquarefile, rank)
        if rightsquarefile == squarefile+1 and (-1 < square_number < 64) :
            # if white pawn on black king
            if board.piece_type_at(square_number) in [1] and board.color_at(square_number) != turn and turn == chess.BLACK:
                return True

        square_number = chess.square(leftsquarefile, rank)
        if leftsquarefile == squarefile-1 and (-1 < square_number < 64):
            # if white pawn on black king
            if board.piece_type_at(square_number) in [1] and board.color_at(square_number) != turn and turn == chess.BLACK:
                return True

        if leftsquarefile > -1 and left:
            # if bishop or queen in square
            if board.piece_type_at(square_number) in [3, 5] and board.color_at(square_number) != turn:
                return True

            # if there is other pawn first than enemy queen / rook no threat
            if board.piece_type_at(square_number) is not None:
                left = False

        square_number = chess.square(rightsquarefile, rank)
        if rightsquarefile < 8 and right:
            # if bishop or queen in square
            if board.piece_type_at(square_number) in [3, 5] and board.color_at(square_number) != turn:
                return True

            # if there is other pawn first than enemy queen / rook no threat
            if board.piece_type_at(square_number) is not None:
                right = False

    return False


def _knight(board, turn, squarerank, squarefile):
    """Checks if knight is attacking the square

    returns True if it is
            False if not
    """
    for rank in range(-2, +3):
        for file in range(-2, +3):
            if rank ** 2 + file ** 2 == 5:
                square_number = chess.square(squarefile-file, squarerank-rank)
                if 0 <= square_number < 64:
                    # if knight
                    if (board.piece_type_at(square_number) in [2] and
                    board.color_at(square_number) != turn and square_number >= 0):
                        return True
    return False


def is_attacked(board, square):
    """Checks if if given square is attacked

    return Boolean value
    """

    rank = chess.square_rank(square)
    file = chess.square_file(square)

    if _below(board, board.turn, rank, file) or _above(board, board.turn, rank, file):
        return True
    if _left(board, board.turn, rank, file) or _right(board, board.turn, rank, file):
        return True
    if _knight(board, board.turn, rank, file):
        return True
    if _diag_above(board, board.turn, rank, file) or _diag_below(board, board.turn, rank, file):
        return True

    return False


def possible_moves(board, attacked):
    """Checks possible moves in check if none checkmate

    return Boolean value
    """
    turn = board.turn
    king = board.king(board.turn)
    kingrank = chess.square_rank(king)
    kingfile = chess.square_file(king)
    # check possible king moves
    for rank in range(kingrank-1, kingrank+2):
        for file in range(kingfile-1, kingfile+2):
            square_number = chess.square(file, rank)
            if -1 < file < 8 and -1 < rank < 8:
                if board.piece_type_at(square_number) is None or board.color_at(square_number) != turn:
                    copy = board.copy()
                    copy.push(chess.Move(king, square_number))
                    copy.turn = turn
                    if not is_attacked(copy, square_number):
                        copy.pop()
                        return True
                    copy.pop()

    # if king is attacked from 2 different positions
    # must be checkmate

    if len(attacked) > 1:
        return False

    # changes turn so works with is_attacked
    if board.turn == chess.WHITE:
        board.turn = chess.BLACK
    else:
        board.turn = chess.WHITE

    defended = []

    # checks if it is possible to kill the attacker
    for square in attacked:
        if is_attacked(board, square):
            defended.append(square)

    if len(defended)==len(attacked):
        board.turn = turn
        return True

    defended = []

    # checks if it is possible to block the attack by sacrifing a pawn
    for square in attacked:
        arank = chess.square_rank(square)
        afile = chess.square_file(square)
        if kingrank == arank:
            if afile < kingfile:
                for file in range(kingfile-1, -1, -1):
                    square_number = chess.square(file, kingrank)
                    if is_attacked(board, square_number):
                        defended.append(square_number)
                        break

            else:
                for file in range(kingfile+1, 8):
                    square_number = chess.square(file, kingrank)
                    if is_attacked(board, square_number):
                        defended.append(square_number)
                        break

        elif kingfile == afile:
            if arank < kingrank:
                for rank in range(kingrank-1, -1, -1):
                    square_number = chess.square(kingfile, rank)
                    if is_attacked(board, square_number):
                        defended.append(square_number)
                        break
            else:
                for rank in range(kingrank+1, 8):
                    square_number = chess.square(kingfile, rank)
                    if is_attacked(board, square_number):
                        defended.append(square_number)
                        break

        elif abs(afile-kingfile) == abs(arank-kingrank):
            if arank < kingrank and afile < kingfile:
                for rank, file in zip(range(kingrank-1, -1, -1), range(kingfile-1, -1, -1)):
                    square_number = chess.square(file, rank)
                    if is_attacked(board, square_number):
                        defended.append(square_number)
                        break

            elif arank > kingrank and afile < kingfile:
                for rank, file in zip(range(kingrank+1, 8), range(kingfile-1, -1, -1)):
                    square_number = chess.square(file, rank)
                    if is_attacked(board, square_number):
                        defended.append(square_number)
                        break

            elif arank > kingrank and afile > kingfile:
                for rank, file in zip(range(kingrank+1, 8), range(kingfile+1, 8)):
                    square_number = chess.square(file, rank)
                    if is_attacked(board, square_number):
                        defended.append(square_number)
                        break

            elif arank < kingrank and afile > kingfile:
                for rank, file in zip(range(kingrank-1, -1, -1), range(kingfile+1, 8)):
                    square_number = chess.square(file, rank)
                    if is_attacked(board, square_number):
                        defended.append(square_number)
                        break

    if len(defended)==len(attacked):
        board.turn = turn
        return True
    board.turn = turn
    return False
