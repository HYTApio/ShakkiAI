""" Module providing chess game base"""
import chess

from chessboard import display
from checks.checkmate import possible_moves as checkmate
from checks.check import is_check
from ai.minmax import find_best_move

def play():
    """User interface for the chess game

    User gives values to it as moves
    """
    board = chess.Board()
    last_move = None
    game_board = display.start()
    while True:
        #print(board)
        display.check_for_quit()
        display.update(board.fen(), game_board)
        #checks if the game is in check / checkmate
        check = is_check(board, last_move)
        if check[0]:
            print("shakki")
            if not checkmate(board, check[1]):
                print("shakkimatti")
                break

        if board.turn == chess.WHITE:
            print("valkoisen vuoro")
            move = find_best_move(board)[0]
            board.push(move)
            last_move = move

        else:
            print("mustan vuoro")
            while True:
                move = input("mitä siirretään (kirjoita poistu lopettaaksesi)? ")
                if move == "poistu":
                    return
                try:
                    if chess.Move.from_uci(move) not in board.legal_moves:
                        print("väärä siirto kokeile uudestaan")
                    else:
                        break
                except ValueError:
                    print("väärä siirto kokeile uudestaan")

            board.push(chess.Move.from_uci(move))
            last_move = chess.Move.from_uci(move)
    display.terminate()
