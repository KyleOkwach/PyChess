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

    def __init__(self, color,type, board):
        self.type = type
        self.board = board
        self.styles = ["classic", "1kb_gambit"]
        self.style = self.styles[1]
        self.color = color

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

    def draw_piece(self, surface, col, row):

        self.surface = surface
        self.row = row
        self.col = col

        if self.piece_object != "None":
            self.piece_object(self.col, self.row, self.board).draw_piece(self.piece_map_str[self.type].lower(), self.surface, self.color, self.style)
    
    def get_legal_moves(self, col, row) -> list:
        if self.piece_object != "None":
            piece = self.piece_object(col, row, self.board)
            piece.generate_legal_moves()
            legal_moves = piece.filter_legal_moves(self.color)
            legal_captures = piece.legal_captures()
            moveset = [legal_moves, legal_captures]
            return moveset
    
    def update_set() -> str:
        pass