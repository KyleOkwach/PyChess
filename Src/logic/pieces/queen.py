from logic.pieces.piece import Piece

# moves inherited from rook and bishop
from logic.pieces.rook import Rook
from logic.pieces.bishop import Bishop

class Queen(Piece):

    def generate_legal_moves(self):
        straight_moves = Rook(self.col, self.row, self.board).generate_legal_moves()
        diagonal_moves = Bishop(self.col, self.row, self.board).generate_legal_moves()
        
        for i in straight_moves:
            self.legal_moves.append(i)
        
        for j in diagonal_moves:
            self.legal_moves.append(j)
        
        return self.legal_moves

    def legal_move(self, col, row) -> bool:
        pass

    def move_queen(self, col, row):
        pass