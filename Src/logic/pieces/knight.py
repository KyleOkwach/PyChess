from logic.pieces.piece import Piece

class Knight(Piece):

    def legal_move(self, file, rank) -> bool:
        legal_moves = [
            [self.file - 1, self.rank - 2],
            [self.file - 1, self.rank + 2],
            [self.file + 1, self.rank - 2],
            [self.file + 1, self.rank + 2],
            [self.file - 2, self.rank - 1],
            [self.file - 2, self.rank + 1],
            [self.file + 2, self.rank - 1],
            [self.file + 2, self.rank + 1]
        ]

        pass

    def move_knight(self, file, rank):
        pass