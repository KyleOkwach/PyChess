import pygame

from board import Board

from pieceSet import PieceSet

class Moves:

    def __init__(self, surface, grid_size, piece, board):
        self.board_size = 8
        self.SQUARE_SIZE = grid_size // self.board_size
        self.transparent_color = pygame.Color(0, 0, 0, 0)
        self.piece = piece
        self.board = board
        self.surface = surface

    def refresh(self):
        # remove highlight
        self.surface.fill(self.transparent_color)

    def active_square(self,  col, row):
        # highlights the active square

        highlight_color = "#ff0000"

        self.refresh()

        highlight = pygame.Rect(col * self.SQUARE_SIZE, row * self.SQUARE_SIZE, self.SQUARE_SIZE, self.SQUARE_SIZE)
        self.surface.set_alpha(128)
        pygame.draw.rect(self.surface, highlight_color, highlight)
    
    def occupiable_squares(self, col, row):
        # highlights squares that can be occupied
        occupiable = PieceSet(self.piece.lower()).get_legal_moves(col, row)
        print(occupiable)

        circle_radius = int(self.SQUARE_SIZE // 8)
        circle_width = int(self.SQUARE_SIZE // 8)

        for i in occupiable:
            highlight_color = "#0000ff"

            self.surface.set_alpha(128)
            pygame.draw.circle(self.surface, highlight_color, (int(i[0] * self.SQUARE_SIZE + self.SQUARE_SIZE // 2), int(i[1] * self.SQUARE_SIZE + self.SQUARE_SIZE // 2)), circle_radius, circle_width)

    def attack_squares(self,  col, row, board):
        # highlights squares that can be attacked
        attackable = PieceSet(self.piece.lower()).get_legal_moves(col, row)
        print(attackable)

        circle_radius = int(self.SQUARE_SIZE // 2)
        circle_width = int(self.SQUARE_SIZE // 8)

        for i in attackable:
            highlight_color = "#0000ff"

            self.surface.set_alpha(128)
            pygame.draw.circle(self.surface, highlight_color, (int(i[0] * self.SQUARE_SIZE + self.SQUARE_SIZE // 2), int(i[1] * self.SQUARE_SIZE + self.SQUARE_SIZE // 2)), circle_radius, circle_width)
