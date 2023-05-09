import pygame
import os

# ------------------------
# PARENT CLASS FOR PIECES
# ------------------------

class Piece:

    def __init__(self, col, row, board):
        self.col = col
        self.row = row
        self.board = board
        self.legal_moves = []
        self.test_legal_moves = [
            [self.col - 2, self.row - 1],
            [self.col + 2, self.row - 1],
            [self.col - 2, self.row + 1],
            [self.col + 2, self.row + 1],
            [self.col - 1, self.row - 2],
            [self.col + 1, self.row - 2],
            [self.col - 1, self.row + 2],
            [self.col + 1, self.row + 2]
        ]
        self.legal_captures_list = []

        self.possible_captures = {
            "White": ["p", "n", "b", "r", "q", "k"],
            "Black": ["P", "N", "B", "R", "Q", "K"]
        }
    
    def filter_legal_moves(self, color) -> list:
        self.filtered_moves = []
        for i in self.legal_moves:
            if i[0] not in range(8) or i[1] not in range(8):
                pass
            else:
                # filter out same color pieces
                # board[i[row]][i[column]] a bit confusing but bare with me XD
                piece = self.board[i[1]][i[0]]
                if piece == "x":
                    self.filtered_moves.append(i)
                elif piece not in self.possible_captures[color]:
                    pass
                elif piece in self.possible_captures[color]:
                    self.legal_captures_list.append(i)
                else:
                    # in the case of a pawn
                    pass
        
        return self.filtered_moves
    
    def legal_captures(self) -> list:
        return self.legal_captures_list

    def draw_piece(self, type, surface, color, theme):
        self.surface = surface
        self.theme = theme
        self.board_size = 8
        self.color = color
        self.SQUARE_SIZE = surface.get_height() // self.board_size

        # piece surface
        piece_surface = pygame.Surface((self.SQUARE_SIZE, self.SQUARE_SIZE), pygame.SRCALPHA)
        surface_size = piece_surface.get_height()
        
        piece_art = pygame.image.load(os.path.join("Assets/img", self.theme+"/"+type+"_"+self.color.lower()+".png")).convert_alpha()
        piece_art = pygame.transform.scale(piece_art, (60, 60))
        piece_rect = piece_art.get_rect(center = (surface_size//2, surface_size//2))

        piece_surface.blit(piece_art, piece_rect)
        self.surface.blit(piece_surface, (self.col * self.SQUARE_SIZE, self.row * self.SQUARE_SIZE))

    def check() -> bool:
        pass
