from logic.pieces.piece import Piece

class Bishop(Piece):

    def generate_legal_moves(self):
        for i in range(8):
            # if (self.row + 1 - y + 1) != 0 and (self.col + 1 - x + 1) != 0:
            #     gradient = (self.row - y) / (self.col - x)
            # if gradient == 1 or  gradient == -1:
            self.legal_moves.append([self.col - i, self.row - i])
            self.legal_moves.append([self.col + i, self.row - i])
            self.legal_moves.append([self.col - i, self.row + i])
            self.legal_moves.append([self.col + i, self.row + i])
        
        return self.legal_moves
    
    def legal_move(self, col, row) -> bool:
        pass

    def move_bishop(self, col, row):
        pass