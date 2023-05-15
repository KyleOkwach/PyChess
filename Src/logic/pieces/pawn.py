from logic.pieces.piece import Piece

class Pawn(Piece):
    
    def generate_legal_moves(self):
        self.legal_moves = [
            [self.col, self.row - 1],
            [self.col, self.row - 2]
        ]
        if self.row != 6:
            self.legal_moves.remove([self.col, self.row - 2])
        
        return self.legal_moves

    def can_promote(self, col, row) -> bool:
        pass