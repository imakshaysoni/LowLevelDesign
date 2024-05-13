from TicToeGame.Pieaces.peaces import Piece


class Board:

    def __init__(self, size: int):
        self.size = size
        self.board = [[Piece for _ in range(size)] for _ in range(size)]

    def _is_valid(self, row, col):
        if row >= self.size or row < 0 or col >= self.size or col < 0 or self.board[row][col] != "":
            return False
        return True

    def _is_full(self):
        for i in range(self.size):
            for j in range(self.size):
                if self.board[i][j] == "":
                    return False
        return True

    def _print_board(self):
        for row in range(self.size):
            for col in range(self.size):
                print(f"{self.board[row][col]} | ", end="")
            print("\n")

    def _check_winner(self, player, row, col):

        # Check row
        game_over: bool
        for i in range(self.size):
            if (self.board[i][col] != player.piece_type
                    or self.board[i][col] == ""):
                return False

        # check Col
        for j in range(self.size):
            if (self.board[row][i] != player.piece_type
                    or self.board[row][j] == ""):
                return False
        # Check Diagonal

    def put_piece(self, player, row, col):

        is_valid = self._is_valid(row, col)
        if not is_valid:
            return "Invalid Place, Please try again"

        self.board[row][col] = player.piece_type

        winner = self._check_winner(player)
        if winner:
            return player

        # Get Board status
        is_full = self._is_full()
        if is_full:
            return False
        return True

    def play(self, players):

        while True:
            self._print_board()
            player1 = players.pop()
            move = input("Enter Position to put piece")
            row, col = move.split(",")
            row = int(row)
            col = int(col)
            obj = self.put_piece(player1, row, col)
            if obj == player1:
                message = f"{player1.name} is winner, Thanks for playing"
                return message
            elif not obj:
                message = f"Game Over, Tie"
                return message
            players.append(player1)
