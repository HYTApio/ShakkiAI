""" Module providing chess game base"""
import chess
from checkmate import possible_moves as checkmate
from new_checkmate import is_check
from minmax import find_best_move

BIG_NUMBER = 100000000000
SMALL_NUMBER = -10000000000

def play():
    """Shakkipelin käyttöliittymä jolle annetaan siirtojen arvoja"""
    board = chess.Board()
    last_move = None
    while True:
        print(board)
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
