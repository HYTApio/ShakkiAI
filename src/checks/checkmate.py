""" Module providing chess game base"""
import chess


def _below(board, turn, krank, kfile):
    """Checks if king is attacked from below

    returns True if it is
            False if not
    """
    for rank in range(krank-1, -1, -1):
        square_number = chess.square(kfile, rank)
        # if rook or queen
        if board.piece_type_at(square_number) in [4, 5] and board.color_at(square_number) != turn:
            return True
        # if there is other pawn first than enemy queen / rook no threat
        if board.piece_type_at(square_number) is not None:
            return False

    return False


def _above(board, turn, krank, kfile):
    """Checks if king is attacked from above

    returns True if it is
            False if not
    """
    for rank in range(krank+1, 8):
        square_number = chess.square(kfile, rank)
        # if rook or queen
        if board.piece_type_at(square_number) in [4, 5] and board.color_at(square_number) != turn:
            return True

        # if there is other pawn first than enemy queen / rook no threat
        if board.piece_type_at(square_number) is not None:
            return False

    return False


def _left(board, turn, krank, kfile):
    """Checks if king is attacked from left

    returns True if it is
            False if not
    """
    for file in range(kfile-1, -1, -1):
        square_number = chess.square(file, krank)
        # if rook or queen
        if board.piece_type_at(square_number) in [4, 5] and board.color_at(square_number) != turn:
            return True

        # if there is other pawn first than enemy queen / rook no threat
        if board.piece_type_at(square_number) is not None:
            return False

    return False


def _right(board, turn, krank, kfile):
    """Checks if king is attacked from right

    returns True if it is
            False if not
    """
    for file in range(kfile+1, 8):
        square_number = chess.square(file, krank)
        # if rook or queen
        if board.piece_type_at(square_number) in [4, 5] and board.color_at(square_number) != turn:
            return True

        # if there is other pawn first than enemy queen / rook no threat
        if board.piece_type_at(square_number) is not None:
            return False

    return False


def _diag_above(board, turn, krank, kfile):
    """Checks if king is attacked diagonally from above

    returns True if it is
            False if not
    """
    right = True
    left = True
    rightkfile = kfile
    leftkfile = kfile
    for rank in range(krank+1, 8):
        rightkfile += 1
        leftkfile -= 1
        square_number = chess.square(rightkfile, rank)
        if rightkfile == kfile+1 and (-1 < square_number < 64):
            # if black pawn on square
            if board.piece_type_at(square_number) in [1] and board.color_at(square_number) != turn and turn == chess.WHITE:
                return True

        square_number = chess.square(leftkfile, rank)
        if leftkfile == kfile-1 and (-1 < square_number < 64):
            # if black pawn on square
            if board.piece_type_at(square_number) in [1] and board.color_at(square_number) != turn and turn == chess.WHITE:
                return True

        if leftkfile > -1 and left:
            # if rook or queen
            if board.piece_type_at(square_number) in [3, 5] and board.color_at(square_number) != turn:
                return True

            # if there is other pawn first than enemy queen / rook no threat
            if board.piece_type_at(square_number) is not None:
                left = False

        square_number = chess.square(rightkfile, rank)
        if rightkfile < 8 and right:
            # if rook or queen
            if board.piece_type_at(square_number) in [3, 5] and board.color_at(square_number) != turn:
                return True

            # if there is other pawn first than enemy queen / rook no threat
            if board.piece_type_at(square_number) is not None:
                right = False

    return False


def _diag_below(board, turn, krank, kfile):
    """Checks if king is attacked diagonally from below

    returns True if it is
            False if not
    """
    right = True
    left = True
    rightkfile = kfile
    leftkfile = kfile
    for rank in range(krank-1, -1, -1):
        rightkfile += 1
        leftkfile -= 1
        square_number = chess.square(rightkfile, rank)
        if rightkfile == kfile+1 and (-1 < square_number < 64) :
            # if white pawn on black king
            if board.piece_type_at(square_number) in [1] and board.color_at(square_number) != turn and turn == chess.BLACK:
                return True

        square_number = chess.square(leftkfile, rank)
        if leftkfile == kfile-1 and (-1 < square_number < 64):
            # if white pawn on black king
            if board.piece_type_at(square_number) in [1] and board.color_at(square_number) != turn and turn == chess.BLACK:
                return True

        if leftkfile > -1 and left:
            # if rook or queen
            if board.piece_type_at(square_number) in [3, 5] and board.color_at(square_number) != turn:
                return True

            # if there is other pawn first than enemy queen / rook no threat
            if board.piece_type_at(square_number) is not None:
                left = False

        square_number = chess.square(rightkfile, rank)
        if rightkfile < 8 and right:
            # if rook or queen
            if board.piece_type_at(square_number) in [3, 5] and board.color_at(square_number) != turn:
                return True

            # if there is other pawn first than enemy queen / rook no threat
            if board.piece_type_at(square_number) is not None:
                right = False

    return False


def _knight(board, turn, krank, kfile):
    """Checks if knight is attacking the king

    returns True if it is
            False if not
    """
    for rank in range(-2, +3):
        for file in range(-2, +3):
            if rank ** 2 + file ** 2 == 5:
                square_number = chess.square(kfile-file, krank-rank)
                if 0 <= square_number < 64:
                    # if knight
                    if (board.piece_type_at(square_number) in [2] and
                    board.color_at(square_number) != turn and square_number >= 0):
                        return True
    return False


def is_attacked(board, square):
    """Checks if current game state is in check

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
    krank = chess.square_rank(king)
    kfile = chess.square_file(king)

    # check possible king moves
    for rank in range(krank-1, krank+2):
        for file in range(kfile-1, kfile+2):
            square_number = chess.square(file, rank)
            if -1 < file < 8 and -1 < rank < 8:
                if board.piece_type_at(square_number) is None or board.color_at(square_number) != turn:
                    copy = board.copy()
                    copy.push(chess.Move(king, square_number))
                    copy.turn = turn
                    if not is_attacked(copy, square_number):
                        return True

    if len(attacked) > 1:
        return False

    defended = []
    # checks if it is possible to kill the attacker
    for square in attacked:
        if not is_attacked(board, square):
            defended.append(square)

    if len(defended)==len(attacked):
        return True

    defended = []

    for square in attacked:
        arank = chess.square_rank(square)
        afile = chess.square_file(square)
        if krank == arank:
            if afile < kfile:
                for file in range(kfile-1, -1, -1):
                    square_number = chess.square(file, krank)
                    print(is_attacked(board, square_number))
                    if is_attacked(board, square_number):
                        defended.append(square_number)
                        break

            else:
                for file in range(kfile+1, 8):
                    square_number = chess.square(file, krank)
                    if is_attacked(board, square_number):
                        defended.append(square_number)
                        break

        elif kfile == afile:
            if arank < krank:
                for rank in range(krank-1, -1, -1):
                    square_number = chess.square(kfile, rank)
                    if is_attacked(board, square_number):
                        defended.append(square_number)
                        break
            else:
                for rank in range(krank+1, 8):
                    square_number = chess.square(kfile, rank)
                    if is_attacked(board, square_number):
                        defended.append(square_number)
                        break

        elif abs(afile-kfile) == abs(arank-krank):
            if arank < krank and afile < kfile:
                for rank, file in zip(range(krank-1, -1, -1), range(kfile-1, -1, -1)):
                    square_number = chess.square(file, rank)
                    if is_attacked(board, square_number):
                        defended.append(square_number)
                        break

            elif arank > krank and afile < kfile:
                for rank, file in zip(range(krank+1, 8), range(kfile-1, -1, -1)):
                    square_number = chess.square(file, rank)
                    if is_attacked(board, square_number):
                        defended.append(square_number)
                        break

            elif arank > krank and afile > kfile:
                for rank, file in zip(range(krank+1, 8), range(kfile+1, 8)):
                    square_number = chess.square(file, rank)
                    if is_attacked(board, square_number):
                        defended.append(square_number)
                        break

            elif arank < krank and afile > kfile:
                for rank, file in zip(range(krank-1, -1, -1), range(kfile+1, 8)):
                    square_number = chess.square(file, rank)
                    if is_attacked(board, square_number):
                        defended.append(square_number)
                        break

    if len(defended)==len(attacked):
        return True

    return False
