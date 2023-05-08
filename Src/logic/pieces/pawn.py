from logic.pieces.piece import Piece

class Pawn(Piece):
    legal_moves = []

    def legal_move(self, file, rank) -> bool:
        pass

    def move_pawn(self, file, rank):
        pass