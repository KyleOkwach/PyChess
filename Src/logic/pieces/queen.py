from logic.pieces.piece import Piece

class Queen(Piece):

    def generate_legal_moves(self):
        self.legal_moves = self.test_legal_moves
        
        return self.legal_moves

    def legal_move(self, col, row) -> bool:
        pass

    def move_queen(self, col, row):
        pass