import chess


def is_check(board):
    """Checks if current game state is in check
    
    return Boolean value
    """

    king = board.king(board.turn)
    krank = chess.square_rank(king)
    kfile = chess.square_file(king)

    if board.turn == chess.WHITE:
        #checks if white king is attacked from below
        for rank in range(krank, 0, -1):
            square_number = chess.square(kfile, rank)
            if square_number != king:
                if board.piece_type_at(square_number) in [1, 2, 3, 4, 5] and board.color_at(square_number) == chess.WHITE or board.piece_type_at(square_number) in [1, 2, 3, 6] and board.color_at(square_number) == chess.BLACK: #if there is other pawn first than enemy queen / rook no threat
                    break
                elif board.piece_type_at(square_number) in [4, 5] and board.color_at(square_number) == chess.BLACK: #if rook or queen
                    return True

        #checks if white king is attacked from above
        for rank in range(krank, 8):
            square_number = chess.square(kfile, rank)
            if square_number != king:
                if board.piece_type_at(square_number) in [1, 2, 3, 4, 5] and board.color_at(square_number) == chess.WHITE or board.piece_type_at(square_number) in [1, 2, 3, 6] and board.color_at(square_number) == chess.BLACK: #if there is other pawn first than enemy queen / rook no threat
                    break
                elif board.piece_type_at(square_number) in [4, 5] and board.color_at(square_number) == chess.BLACK: #if rook or queen
                    return True

        #checks if white king is attacked from left
        for file in range(kfile, 0, -1):
            square_number = chess.square(file, krank)
            if square_number != king:
                if board.piece_type_at(square_number) in [1, 2, 3, 4, 5] and board.color_at(square_number) == chess.WHITE or board.piece_type_at(square_number) in [1, 2, 3, 6] and board.color_at(square_number) == chess.BLACK: #if there is other pawn first than enemy queen / rook no threat
                    break
                elif board.piece_type_at(square_number) in [4, 5] and board.color_at(square_number) == chess.BLACK: #if rook or queen
                    return True

        #checks if white king is attacked from right
        for file in range(kfile, 8):
            square_number = chess.square(file, krank)
            if square_number != king:
                if board.piece_type_at(square_number) in [1, 2, 3, 4, 5] and board.color_at(square_number) == chess.WHITE or board.piece_type_at(square_number) in [1, 2, 3, 6] and board.color_at(square_number) == chess.BLACK: #if there is other pawn first than enemy queen / rook no threat
                    break
                elif board.piece_type_at(square_number) in [4, 5] and board.color_at(square_number) == chess.BLACK: #if rook or queen
                    return True


        #checks if white king is attacked diagonally from below
        right = True
        left = True
        rightkfile = kfile
        leftkfile = kfile
        for rank in range(krank-1, 0, -1):
            rightkfile += 1
            leftkfile -= 1

            if rightkfile < 8 and right:
                square_number = chess.square(rightkfile, rank)
                if board.piece_type_at(square_number) in [1, 2, 3, 4, 5] and board.color_at(square_number) == chess.WHITE or board.piece_type_at(square_number) in [1, 2, 4, 6] and board.color_at(square_number) == chess.BLACK: #if there is other pawn first than enemy queen / rook no threat
                    right = False
                elif board.piece_type_at(square_number) in [3, 5] and board.color_at(square_number) == chess.BLACK: #if rook or queen
                    return True

            if leftkfile > -1 and left:
                square_number = chess.square(leftkfile, rank)
                if board.piece_type_at(square_number) in [1, 2, 3, 4, 5] and board.color_at(square_number) == chess.WHITE or board.piece_type_at(square_number) in [1, 2, 4, 6] and board.color_at(square_number) == chess.BLACK: #if there is other pawn first than enemy queen / rook no threat
                    left = False
                elif board.piece_type_at(square_number) in [3, 5] and board.color_at(square_number) == chess.BLACK: #if rook or queen
                    return True

        #checks if white king is attacked diagonally from above
        right = True
        left = True
        rightkfile = kfile
        leftkfile = kfile
        for rank in range(krank+1, 8):
            rightkfile += 1
            leftkfile -= 1
            if rightkfile == kfile+1:
                square_number = chess.square(rightkfile, rank)
                if board.piece_type_at(square_number) in [1] and board.color_at(square_number) == chess.BLACK: #if pawn
                    return True

            if leftkfile == kfile-1:
                square_number = chess.square(leftkfile, rank)
                if board.piece_type_at(square_number) in [1] and board.color_at(square_number) == chess.BLACK: #if pawn
                    return True

            if rightkfile < 8 and right:
                if board.piece_type_at(square_number) in [1, 2, 3, 4, 5] and board.color_at(square_number) == chess.WHITE or board.piece_type_at(square_number) in [1, 2, 4, 6] and board.color_at(square_number) == chess.BLACK: #if there is other pawn first than enemy queen / rook no threat
                    right = False
                elif board.piece_type_at(square_number) in [3, 5] and board.color_at(square_number) == chess.BLACK: #if rook or queen
                    return True

            if leftkfile > -1 and left:
                square_number = chess.square(leftkfile, rank)
                if board.piece_type_at(square_number) in [1, 2, 3, 4, 5] and board.color_at(square_number) == chess.WHITE or board.piece_type_at(square_number) in [1, 2, 4, 6] and board.color_at(square_number) == chess.BLACK: #if there is other pawn first than enemy queen / rook no threat
                    left = False
                elif board.piece_type_at(square_number) in [3, 5] and board.color_at(square_number) == chess.BLACK: #if rook or queen
                    return True
        
        #checks if knights attack the king
        for rank in range(-2, +3):
            for file in range(-2, +3):
                if rank ** 2 + file ** 2 ==5:
                    square_number = chess.square(kfile-file, krank-rank)
                    if 0<=square_number<64:
                        if board.piece_type_at(square_number) in [2] and board.color_at(square_number) == chess.BLACK and square_number>=0: #if knight
                            return True
                    



    else:
        #checks if black king is attacked from left
        for file in range(kfile, 0, -1):
            square_number = chess.square(file, krank)
            if square_number != king:
                if board.piece_type_at(square_number) in [1, 2, 3, 4, 5] and board.color_at(square_number) == chess.BLACK or board.piece_type_at(square_number) in [1, 2, 3, 6] and board.color_at(square_number) == chess.WHITE: #if there is other pawn first than enemy queen / rook no threat
                    break
                elif board.piece_type_at(square_number) in [4, 5] and board.color_at(square_number) == chess.WHITE: #if rook or queen
                    return True

        #checks if black king is attacked from right
        for file in range(kfile, 8):
            square_number = chess.square(file, krank)
            if square_number != king:
                if board.piece_type_at(square_number) in [1, 2, 3, 4, 5] and board.color_at(square_number) == chess.BLACK or board.piece_type_at(square_number) in [1, 2, 3, 6] and board.color_at(square_number) == chess.WHITE: #if there is other pawn first than enemy queen / rook no threat
                    break
                elif board.piece_type_at(square_number) in [4, 5] and board.color_at(square_number) == chess.WHITE: #if rook or queen
                    return True

        #checks if black king is attacked diagonally from below
        right = True
        left = True
        rightkfile = kfile
        leftkfile = kfile
        for rank in range(krank-1, 0, -1):
            rightkfile += 1
            leftkfile -= 1

            if rightkfile == kfile+1:
                square_number = chess.square(rightkfile, rank)
                if board.piece_type_at(square_number) in [1] and board.color_at(square_number) == chess.WHITE: #if pawn
                    return True

            if leftkfile == kfile-1:
                square_number = chess.square(leftkfile, rank)
                if board.piece_type_at(square_number) in [1] and board.color_at(square_number) == chess.WHITE: #if pawn
                    return True

            if rightkfile < 8 and right:
                square_number = chess.square(rightkfile, rank)
                if board.piece_type_at(square_number) in [1, 2, 3, 4, 5] and board.color_at(square_number) == chess.BLACK or board.piece_type_at(square_number) in [1, 2, 4, 6] and board.color_at(square_number) == chess.WHITE: #if there is other pawn first than enemy queen / rook no threat
                    right = False
                elif board.piece_type_at(square_number) in [3, 5] and board.color_at(square_number) == chess.WHITE: #if rook or queen
                    return True

            if leftkfile > -1 and left:
                square_number = chess.square(leftkfile, rank)
                if board.piece_type_at(square_number) in [1, 2, 3, 4, 5] and board.color_at(square_number) == chess.BLACK or board.piece_type_at(square_number) in [1, 2, 4, 6] and board.color_at(square_number) == chess.WHITE: #if there is other pawn first than enemy queen / rook no threat
                    left = False
                elif board.piece_type_at(square_number) in [3, 5] and board.color_at(square_number) == chess.WHITE: #if rook or queen
                    return True

        #checks if black king is attacked diagonally from above
        right = True
        left = True
        rightkfile = kfile
        leftkfile = kfile
        for rank in range(krank+1, 8):
            rightkfile += 1
            leftkfile -= 1

            if rightkfile < 8 and right:
                if board.piece_type_at(square_number) in [1, 2, 3, 4, 5] and board.color_at(square_number) == chess.BLACK or board.piece_type_at(square_number) in [1, 2, 4, 6] and board.color_at(square_number) == chess.WHITE: #if there is other pawn first than enemy queen / rook no threat
                    right = False
                elif board.piece_type_at(square_number) in [3, 5] and board.color_at(square_number) == chess.WHITE: #if rook or queen
                    return True

            if leftkfile > -1 and left:
                square_number = chess.square(leftkfile, rank)
                if board.piece_type_at(square_number) in [1, 2, 3, 4, 5] and board.color_at(square_number) == chess.BLACK or board.piece_type_at(square_number) in [1, 2, 4, 6] and board.color_at(square_number) == chess.WHITE: #if there is other pawn first than enemy queen / rook no threat
                    left = False
                elif board.piece_type_at(square_number) in [3, 5] and board.color_at(square_number) == chess.WHITE: #if rook or queen
                    return True


        #checks if knights attack the king
        for rank in range(-2, +3):
            for file in range(-2, +3):
                if rank ** 2 + file ** 2 ==5:
                    square_number = chess.square(kfile-file, krank-rank)
                    if 0<=square_number<64:
                        if board.piece_type_at(square_number) in [2] and board.color_at(square_number) == chess.WHITE: #if knight
                            return True


    return False