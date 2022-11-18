""" Module providing chess game base"""
import chess
from checkmate import is_check, possible_moves
from minmax import max_value, min_value

BIG_NUMBER = 100000000000
SMALL_NUMBER = -10000000000

def play():
    """Shakkipelin käyttöliittymä jolle annetaan siirtojen arvoja"""
    board = chess.Board()
    while True:
        print(board)
        if is_check(board):
            if not possible_moves(board):
                print("shakkimatti")
                break

        if board.turn == chess.WHITE:
            print("valkoisen vuoro")
            (value, move) = max_value(board, SMALL_NUMBER, BIG_NUMBER, 2)
            board.push(move)

        else:
            print("mustan vuoro")
            while True:
                siirto = input("mitä siirretään? ")
                if siirto == "":
                    return
                if chess.Move.from_uci(siirto) not in board.legal_moves:
                    print("väärä siirto kokeile uudestaan")
                else:
                    break
            board.push(chess.Move.from_uci(siirto))


if __name__ == "__main__":
    play()
