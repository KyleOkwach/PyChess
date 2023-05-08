import pygame
import os

class Piece:

    def __init__(self, surface, color, rank, file, theme):
        self.surface = surface
        self.theme = theme
        self.board_size = 8
        self.color = color
        self.file = file
        self.rank = rank
        self.SQUARE_SIZE = surface.get_height() // self.board_size
        # self.SQUARE_SIZE = 60
    
    def draw_piece(self, type):
        # piece surface
        piece_surface = pygame.Surface((self.SQUARE_SIZE, self.SQUARE_SIZE), pygame.SRCALPHA, 32)
        surface_size = piece_surface.get_height()
        
        piece_art = pygame.image.load(os.path.join("Assets/img", self.theme+"/"+type+"_"+self.color.lower()+".png")).convert_alpha()
        piece_art = pygame.transform.scale(piece_art, (60, 60))
        piece_rect = piece_art.get_rect(center = (surface_size//2, surface_size//2))

        piece_surface.blit(piece_art, piece_rect)
        self.surface.blit(piece_surface, (self.rank * self.SQUARE_SIZE, self.file * self.SQUARE_SIZE))

    def debug_move(self, color, file, rank):
        # for testing purposes
        pass

    def debug_move(self, color, file, rank):
        # for testing purposes
        pass
