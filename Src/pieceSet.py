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

    def __init__(self, type):
        self.type = type
        self.styles = ["classic", "1kb_gambit"]
        self.style = self.styles[1]

        self.piece_map = {
            "r" : Rook,
            "n" : Knight,
            "b" : Bishop,
            "k" : King,
            "q" : Queen,
            "p" : Pawn,
            "x" : "None"
        }

        self.piece_map_str = {
            "r" : "Rook",
            "n" : "Knight",
            "b" : "Bishop",
            "k" : "King",
            "q" : "Queen",
            "p" : "Pawn",
            "x" : "None"
        }

        self.piece_object = self.piece_map[self.type]

    def draw_piece(self, surface, color, col, row):

        self.surface = surface
        self.color = color
        self.row = row
        self.col = col

        if self.piece_object != "None":
            self.piece_object(self.col, self.row).draw_piece(self.piece_map_str[self.type].lower(), self.surface, self.color, self.style)
    
    def get_legal_moves(self, col, row) -> list:
        if self.piece_object != "None":
            piece = self.piece_object(col, row)
            piece.generate_legal_moves()
            legal_moves = piece.filter_legal_moves()
            return legal_moves
    
    def update_set() -> str:
        pass