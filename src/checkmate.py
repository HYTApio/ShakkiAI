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
        if rightkfile == kfile+1:
            # if black pawn on white king
            if board.piece_type_at(square_number) in [1] and board.color_at(square_number) != turn and turn == chess.WHITE:
                return True

        square_number = chess.square(leftkfile, rank)
        if leftkfile == kfile-1:
            # if black pawn on white king
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
        if rightkfile == kfile+1:
            # if white pawn on black king
            if board.piece_type_at(square_number) in [1] and board.color_at(square_number) != turn and turn == chess.BLACK:
                return True

        square_number = chess.square(leftkfile, rank)
        if leftkfile == kfile-1:
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
                    if board.piece_type_at(square_number) in [2] and board.color_at(square_number) != turn and square_number >= 0:
                        return True
    return False


def is_check(board):
    """Checks if current game state is in check

    return Boolean value
    """

    king = board.king(board.turn)
    krank = chess.square_rank(king)
    kfile = chess.square_file(king)

    if _below(board, board.turn, krank, kfile) or _above(board, board.turn, krank, kfile):
        return True
    if _left(board, board.turn, krank, kfile) or _right(board, board.turn, krank, kfile):
        return True
    if _knight(board, board.turn, krank, kfile):
        return True
    if _diag_above(board, board.turn, krank, kfile) or _diag_below(board, board.turn, krank, kfile):
        return True

    return False
