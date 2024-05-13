from TicToeGame.Board.board import Board
from TicToeGame.Pieaces.playing_piece import PlayingPieceO, PlayingPieceX
from TicToeGame.Pieaces.peaces import Piece
from TicToeGame.Players.player import Player
from collections import deque


if __name__ == "__main__":

    # Initialize board
    board = Board(3)

    akshay = Player(name="Akshay", piece_type=PlayingPieceX())
    shreya = Player(name="Shreya", piece_type=PlayingPieceO())

    players = deque()
    players.append(akshay)
    players.append(shreya)

    board.play(players)


