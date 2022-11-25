""" Module providing chess game base"""
import chess



def is_check(board, last_move:chess.Move):
    """ Checks if board is in check

    return boolean value based on result
    """
    if last_move is None:
        return False

    from_square = last_move.from_square
    to_square = last_move.to_square
    to_rank = chess.square_rank(to_square)
    to_file = chess.square_file(to_square)
    from_rank = chess.square_rank(from_square)
    from_file = chess.square_file(from_square)
    king = board.king(board.turn)
    krank = chess.square_rank(king)
    kfile = chess.square_file(king)
    turn = board.turn

    # if moving piece is rook or queen and its in the same rank as king could become check
    if board.piece_type_at(to_square) in [4, 5] and to_rank == krank:
        if to_file < kfile:
            for file in range(krank-1, -1, -1):
                square_number = chess.square(file, krank)
                # if there is piece in the way
                if board.piece_type_at(square_number) is not None and file != to_file:
                    break
                return True
        else:
            for file in range(krank+1, 8):
                square_number = chess.square(file, krank)
                # if there is piece in the way
                if board.piece_type_at(square_number) is not None and file != to_file:
                    break
                return True

    # if moving piece is rook or queen and its in the same file as king could become check
    if board.piece_type_at(to_square) in [4, 5] and to_file == kfile:
        if to_rank < krank:
            for rank in range(krank-1, -1, -1):
                square_number = chess.square(kfile, rank)
                # if there is piece in the way
                if board.piece_type_at(square_number) is not None and rank != to_rank:
                    break
                return True
        else:
            for rank in range(krank+1, 8):
                square_number = chess.square(kfile, rank)
                # if there is piece in the way
                if board.piece_type_at(square_number) is not None and rank != to_rank:
                    break
                return True

    # if moving piece is bishop or queen and its diagonally to king could become check
    if board.piece_type_at(to_square) in [3, 5] and abs(to_file-kfile) == abs(krank-to_rank):
        if to_rank < krank and to_file < kfile:
            for rank, file in zip(range(krank-1, -1, -1), range(kfile-1, -1, -1)):
                square_number = chess.square(file, rank)
                if board.piece_type_at(square_number) is not None and rank != to_rank:
                    break
                return True
        elif to_rank > krank and to_file < kfile:
            for rank, file in zip(range(krank+1, 8), range(kfile-1, -1, -1)):
                square_number = chess.square(file, rank)
                if board.piece_type_at(square_number) is not None and rank != to_rank:
                    break
                return True
        elif to_rank > krank and to_file > kfile:
            for rank, file in zip(range(krank+1, 8), range(kfile+1, 8)):
                square_number = chess.square(file, rank)
                if board.piece_type_at(square_number) is not None and rank != to_rank:
                    break
                return True
        elif to_rank < krank and to_file > kfile:
            for rank, file in zip(range(krank-1, -1, -1), range(kfile+1, 8)):
                square_number = chess.square(file, rank)
                if board.piece_type_at(square_number) is not None and rank != to_rank:
                    break
                return True

    # if moving piece is knight it is check
    if board.piece_type_at(to_square) in [2] and (abs(to_file-kfile) ==  2 and abs(krank-to_rank) == 1
    or abs(to_file-kfile) ==  1 and abs(krank-to_rank) == 2):
        return True

    # if from behind moved move can be checked with queen / rook
    if krank == from_rank:
        if from_file < kfile:
            for file in range(krank-1, -1, -1):
                square_number = chess.square(file, krank)
                # if there is piece in the way
                if board.piece_type_at(square_number) in [1, 2, 3, 6, None]:
                    break
                if board.color_at(square_number) != turn:
                    break
                return True
        else:
            for file in range(krank+1, 8):
                square_number = chess.square(file, krank)
                # if there is piece in the way
                if board.piece_type_at(square_number) in [1, 2, 3, 6, None]:
                    break
                if board.color_at(square_number) != turn:
                    break
                return True

    if kfile == from_file:
        if from_rank < krank:
            for rank in range(krank-1, -1, -1):
                square_number = chess.square(kfile, rank)
                # if there is piece in the way
                if board.piece_type_at(square_number) in [1, 2, 3, 6]:
                    break
                if board.color_at(square_number) == turn:
                    break
                return True
        else:
            for rank in range(krank+1, 8):
                square_number = chess.square(kfile, rank)
                # if there is piece in the way
                if board.piece_type_at(square_number) in [1, 2, 3, 6]:
                    break
                if board.color_at(square_number) == turn:
                    break
                return True

    # if behind moving piece comes bishop / quen could be check
    if abs(from_file-kfile) == abs(from_rank-krank):
        if from_rank < krank and from_file < kfile:
            for rank, file in zip(range(krank-1, -1, -1), range(kfile-1, -1, -1)):
                square_number = chess.square(file, rank)
                # if there is piece in the way
                if board.piece_type_at(square_number) in [1, 2, 4, 6] or board.color_at(square_number) == turn:
                    break
                if board.piece_type_at(square_number) in [3,5]:
                    return True
        elif from_rank > krank and from_file < kfile:
            for rank, file in zip(range(krank+1, 8), range(kfile-1, -1, -1)):
                square_number = chess.square(file, rank)
                if board.piece_type_at(square_number) in [1, 2, 4, 6] or board.color_at(square_number) == turn:
                    break
                if board.piece_type_at(square_number) in [3,5]:
                    return True
        elif from_rank > krank and from_file > kfile:
            for rank, file in zip(range(krank+1, 8), range(kfile+1, 8)):
                square_number = chess.square(file, rank)
                if board.piece_type_at(square_number) in [1, 2, 4, 6] or board.color_at(square_number) == turn:
                    break
                if board.piece_type_at(square_number) in [3,5]:
                    return True
        elif from_rank < krank and from_file > kfile:
            for rank, file in zip(range(krank-1, -1, -1), range(kfile+1, 8)):
                square_number = chess.square(file, rank)
                if board.piece_type_at(square_number) in [1, 2, 4, 6] or board.color_at(square_number) == turn:
                    break
                if board.piece_type_at(square_number) in [3,5]:
                    return True

    # Checks for soldiers
    if (board.piece_type_at(to_square) in [1] and abs(to_file-kfile) == abs(krank-to_rank)
    and chess.square_distance(to_square, king) == 1 and (to_rank < krank and turn is False or to_rank > krank and turn is True)):
        return True

    return False