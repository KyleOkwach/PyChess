from logic.pieces.piece import Piece

class Rook(Piece):

    def generate_legal_moves(self):
        grid_size = 8
        x, y = 1, 0
        # vertical moves
        for i in range(grid_size):
            curr_square = [self.col, self.row - i]
            if self.row - i in range(grid_size):
                if self.board[curr_square[y]][curr_square[x]] == "x":
                    self.legal_moves.append(curr_square)
                else:
                    self.legal_moves.append(curr_square)  # terminating square
                    break

            else:
                break

        for j in range(grid_size):
            curr_square = [self.col, self.row + j]
            if self.row + j in range(grid_size):
                if self.board[curr_square[y]][curr_square[x]] == "x":
                    self.legal_moves.append(curr_square)
                else:
                    self.legal_moves.append(curr_square)  # terminating square
                    break

            else:
                break


        # horizontal moves
        for k in range(grid_size):
            curr_square = [self.col - k, self.row]
            if self.col - k in range(grid_size):
                if self.board[curr_square[y]][curr_square[x]] == "x":
                    self.legal_moves.append(curr_square)
                else:
                    self.legal_moves.append(curr_square)  # terminating square
                    break

            else:
                break

        for l in range(grid_size):
            curr_square = [self.col + l, self.row]
            if self.col + l in range(grid_size):
                if self.board[curr_square[y]][curr_square[x]] == "x":
                    self.legal_moves.append(curr_square)
                else:
                    self.legal_moves.append(curr_square)  # terminating square
                    break

            else:
                break

            print(curr_square)
        
        return self.legal_moves
