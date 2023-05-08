import pygame
import sys
import os

# import pieces
from logic.pieces.pawn import Pawn
from logic.pieces.knight import Knight
from logic.pieces.bishop import Bishop
from logic.pieces.rook import Rook
from logic.pieces.queen import Queen
from logic.pieces.king import King

class PieceSet:

    def __init__(self, surface, color, col, row, type):
        self.surface = surface
        self.color = color
        self.row = row
        self.col = col
        self.type = type
        self.theme = "1kb_gambit"

    def draw_piece(self):
        if self.type == "Pawn":
            Pawn(self.surface, self.color, self.col, self.row, self.theme).draw_piece(self.type.lower())
        elif self.type == "Knight":
            Knight(self.surface, self.color, self.col, self.row, self.theme).draw_piece(self.type.lower())
        elif self.type == "Bishop":
            Bishop(self.surface, self.color, self.col, self.row, self.theme).draw_piece(self.type.lower())
        elif self.type == "Rook":
            Rook(self.surface, self.color, self.col, self.row, self.theme).draw_piece(self.type.lower())
        elif self.type == "Queen":
            Queen(self.surface, self.color, self.col, self.row, self.theme).draw_piece(self.type.lower())
        elif self.type == "King":
            King(self.surface, self.color, self.col, self.row, self.theme).draw_piece(self.type.lower())
    
    def update_set() -> str:
        pass