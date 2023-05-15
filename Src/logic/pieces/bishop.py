from logic.pieces.piece import Piece

class Bishop(Piece):

    def generate_legal_moves(self):
        for i in range(8):
            self.legal_moves.append([self.col - i, self.row - i])
            self.legal_moves.append([self.col + i, self.row - i])
            self.legal_moves.append([self.col - i, self.row + i])
            self.legal_moves.append([self.col + i, self.row + i])
        
        return self.legal_moves
