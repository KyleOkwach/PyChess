from pieceSet import PieceSet

class Fen:

    def __init__(self, fen):
        self.fen = fen
        split_fen = fen.split()
        self.position = split_fen[0]  # pieces fen board
        self.player = split_fen[1]  # player to play

        self.piece_map = {
            "r" : "Rook",
            "n" : "Knight",
            "b" : "Bishop",
            "k" : "King",
            "q" : "Queen",
            "p" : "Pawn",
            "x" : "None"
        }

    def read_fen(self):
        size= 8
        board = []

        for row in self.position.split("/"):
            board_row = []
            for symbol in row:
                if symbol.isdigit():
                    board_row.extend(['x'] * int(symbol))
                else:
                    board_row.append(symbol)
            board.append(board_row)
            
        return board

    def draw_pieces(self, surface, player):
        position = self.position
        if player == 2:
            position = self.position[::-1]
            self.player = "b"
        else:
            self.player = "w"

        for (i, y) in zip(self.read_fen(), range(8)):
            for (j, x) in zip(i, range(8)):
                if j.isupper():
                    color = "White"
                else:
                    color = "Black"
                PieceSet(surface, color, x, y, self.piece_map[j.lower()]).draw_piece()
            
    def update_board(self) -> str:
        # update fen board after move

        # after joining elements of fen
        return self.fen