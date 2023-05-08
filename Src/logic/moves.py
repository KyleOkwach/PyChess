import pygame
from board import Board

class Moves(Board):

    def __init__(self, grid_size):
        self.board_size = 8
        self.SQUARE_SIZE = grid_size // self.board_size

    def highlight_active_square(self, surface,  col, row, board):
        transparent_color = pygame.Color(0, 0, 0, 0)
        highlight_color = "#ff0000"

        surface.fill(transparent_color)

        highlight = pygame.Rect(col * self.SQUARE_SIZE, row * self.SQUARE_SIZE, self.SQUARE_SIZE, self.SQUARE_SIZE)
        surface.set_alpha(128)
        pygame.draw.rect(surface, highlight_color, highlight)
        # self.surface.blit()
        
        print(f"{chr(int(col+97))}{int(self.board_size - row)}")
    
    def highlight_attack_square(self, surface,  col, row, board):
        pass