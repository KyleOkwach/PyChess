from logic.pieces.piece import Piece

class Bishop(Piece):

    def generate_legal_moves(self):
        # for i in range(8):
        #     self.legal_moves.append([self.col - i, self.row - i])
        #     self.legal_moves.append([self.col + i, self.row - i])
        #     self.legal_moves.append([self.col - i, self.row + i])
        #     self.legal_moves.append([self.col + i, self.row + i])

        grid_size = 8
        x, y = 1, 0

        # Ascending diagonal
        for i in range(grid_size):
            curr_square = [self.col - i, self.row + i]
            if self.row - i in range(grid_size):
                if self.board[curr_square[y]][curr_square[x]] == "x":
                    self.legal_moves.append(curr_square)
                else:
                    self.legal_moves.append(curr_square)  # terminating square
                    break

            else:
                break

        for j in range(grid_size):
            curr_square = [self.col + i, self.row - i]
            if self.row + j in range(grid_size):
                if self.board[curr_square[y]][curr_square[x]] == "x":
                    self.legal_moves.append(curr_square)
                else:
                    self.legal_moves.append(curr_square)  # terminating square
                    break

            else:
                break


        # Descending diagonal
        for k in range(grid_size):
            curr_square = [self.col - i, self.row - i]
            if self.col - k in range(grid_size):
                if self.board[curr_square[y]][curr_square[x]] == "x":
                    self.legal_moves.append(curr_square)
                else:
                    self.legal_moves.append(curr_square)  # terminating square
                    break

            else:
                break

        for l in range(grid_size):
            curr_square = [self.col + i, self.row + i]
            if self.col + l in range(grid_size):
                if self.board[curr_square[y]][curr_square[x]] == "x":
                    self.legal_moves.append(curr_square)
                else:
                    self.legal_moves.append(curr_square)  # terminating square
                    break

            else:
                break
        
        return self.legal_moves
