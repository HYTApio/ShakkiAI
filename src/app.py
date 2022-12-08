""" Module providing chess game base"""
import chess
from checks.checkmate import possible_moves as checkmate
from checks.check import is_check
from ai.minmax import find_best_move

def play():
    """User interface for the chess game

    User gives values to it as moves
    """
    board = chess.Board()
    last_move = None
    while True:
        print(board)
        #checks if the game is in check / checkmate
        check = is_check(board, last_move)
        if check[0]:
            print("shakki")
            if not checkmate(board, check[1]):
                print("shakkimatti")
                break

        if board.turn == chess.WHITE:
            print("valkoisen vuoro")
            move = find_best_move(board)
            board.push(move)
            last_move = move

        else:
            print("mustan vuoro")
            while True:
                move = input("mitä siirretään? ")
                if move == "":
                    return
                try:
                    if chess.Move.from_uci(move) not in board.legal_moves:
                        print("väärä siirto kokeile uudestaan")
                    else:
                        break
                except:
                    print("väärä siirto kokeile uudestaan")

            board.push(chess.Move.from_uci(move))
            last_move = chess.Move.from_uci(move)
