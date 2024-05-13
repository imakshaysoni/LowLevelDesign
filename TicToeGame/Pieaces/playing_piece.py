from TicToeGame.Pieaces.enums import PieceTypes
from TicToeGame.Pieaces.peaces import Piece


class PlayingPieceX(Piece):

    def __init__(self):
        super().__init__(PieceTypes.X)


class PlayingPieceO(Piece):

    def __init__(self):
        super().__init__(PieceTypes.O)
