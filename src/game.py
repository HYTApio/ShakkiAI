import chess
from checkmate import is_check, possible_moves


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
            while True:
                siirto = input("mitä siirretään? ")
                if siirto == "":
                    return
                if chess.Move.from_uci(siirto) not in board.legal_moves:
                    print("väärä siirto kokeile uudestaan")
                else:
                    break
            board.push(chess.Move.from_uci(siirto))

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
