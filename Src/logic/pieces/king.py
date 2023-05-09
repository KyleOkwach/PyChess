from logic.pieces.piece import Piece

class King(Piece):

    def generate_legal_moves(self):
        self.legal_moves = [
            [self.col - 1, self.row - 1],
            [self.col, self.row - 1],
            [self.col + 1, self.row - 1],
            [self.col - 1, self.row],
            [self.col + 1, self.row],
            [self.col - 1, self.row + 2],
            [self.col, self.row + 2],
            [self.col + 1, self.row + 2]
        ]
        
        return self.legal_moves

    def legal_move(self, col, row) -> bool:
        pass

    def move_king(self, col, row):
        pass

    def check() -> bool:
        pass

    def checkmate() -> bool:
        pass

    def castle():
        pass