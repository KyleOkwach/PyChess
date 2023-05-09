import pygame
import os

# ------------------------
# PARENT CLASS FOR PIECES
# ------------------------

class Piece:

    def __init__(self, col, row):
        self.col = col
        self.row = row
        self.legal_moves = []
        self.test_legal_moves = [
            [self.col - 1, self.row - 2],
            [self.col - 1, self.row + 2],
            [self.col + 1, self.row - 2],
            [self.col + 1, self.row + 2],
            [self.col - 2, self.row - 1],
            [self.col - 2, self.row + 1],
            [self.col + 2, self.row - 1],
            [self.col + 2, self.row + 1]
        ]
    
    def filter_legal_moves(self) -> list:
        self.filtered_moves = []
        for i in self.legal_moves:
            if i[0] > 7 or i[1] > 7 or i[0] < 0 or i[1] < 0:
                pass
            else:
                self.filtered_moves.append(i)
        
        return self.filtered_moves
    
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

    def debug_move(self, color, col, row):
        # for testing purposes
        pass

    def debug_move(self, color, col, row):
        # for testing purposes
        pass
