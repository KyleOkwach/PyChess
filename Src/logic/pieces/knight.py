from logic.pieces.piece import Piece

class Knight(Piece):

    def generate_legal_moves(self) -> list:
        self.legal_moves = [
            [self.col - 1, self.row - 2],
            [self.col - 1, self.row + 2],
            [self.col + 1, self.row - 2],
            [self.col + 1, self.row + 2],
            [self.col - 2, self.row - 1],
            [self.col - 2, self.row + 1],
            [self.col + 2, self.row - 1],
            [self.col + 2, self.row + 1]
        ]
        
        return self.legal_moves

    def legal_move(self, col, row) -> bool:
        pass

    def move_knight(self, col, row):
        pass