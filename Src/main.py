import settings
import pygame
import sys

from board import Board
from fen import Fen
from logic.moves import Moves

# ------------------------
# PYGAME INITIALIZATION
# ------------------------

pygame.init()
pygame.display.set_caption("Chess")
clock = pygame.time.Clock()
screen = pygame.display.set_mode((settings.WIDTH, settings.HEIGHT))


# --------------
# GAME SETTINGS
# --------------

# board theme
standard = [(240, 217, 181), (139, 71, 38)]
kb_gambit = ["#e5e5e5", "#fc00e7"]
themes = [standard, kb_gambit]

mode = "ai"  # game mode


# ------
# BOARD
# ------

board_scale = 2.5
board_width, board_height = screen.get_width() // board_scale, screen.get_width() // board_scale

# surfaces
board_surface = pygame.Surface((board_width, board_height), pygame.SRCALPHA)
highlight_surface = pygame.Surface((board_width, board_height), pygame.SRCALPHA)
piece_surface = pygame.Surface((board_width, board_height), pygame.SRCALPHA)

board = Board(board_surface, board_height, themes[1])
square_size = board_height // 8

screen.fill("#1E1E1E")
global player
player = 1  # 1 for white, 2 for black

def start_game(board, fen, fenStr:str, player):
    curr_pos = fenStr

    fenBoard = fen.read_fen()

    # print board for debug purposes
    for i in fenBoard:
        print(i)

    # ---------------
    # MAIN GAME LOOP
    # ---------------
    while True:

        clock.tick(settings.FPS)
        
        # draw pieces and board
        pieces = fen
        
        board.draw_board(board_surface, player)
        pieces.draw_pieces(piece_surface)
        
        boardX = screen.get_width()//3.5
        boardY = screen.get_height()//8

        # blitting surfaces
        screen.blit(board_surface, (boardX, boardY))
        screen.blit(highlight_surface, (boardX, boardY))
        screen.blit(piece_surface, (boardX, boardY))

        color = ["White", "Black"]

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            
            # __________CONTROLS__________

            if event.type == pygame.MOUSEBUTTONDOWN:
                mouseX = event.pos[0]
                mouseY = event.pos[1]

                # if board is clicked
                if (mouseX >= boardX and mouseY >= boardY) and (mouseX <= boardX + board_width and mouseY <= boardY + board_height):
                    mouseX = event.pos[0] - boardX
                    mouseY = event.pos[1] - boardY

                    col = int(mouseX // square_size)
                    row = int(mouseY // square_size)

                    active_piece = fen.read_fen()[row][col]
                    moves = Moves(highlight_surface, board_height, color[player-1], active_piece, fenBoard)
                    if active_piece != "x":
                        if player == 1 and fen.read_fen()[row][col].isupper():
                            moves.active_square(col, row)
                            moves.show_all(col, row)  # highlight all legal moves
                        if player == 2 and fen.read_fen()[row][col].islower():
                            moves.active_square(col, row)
                            moves.show_all(col, row)
                    else:
                        moves.refresh()
        
        # curr_pos = pieces.update_board()

        if mode == "multiplayer":
            player = player % 2 + 1  # change player
        
        curr_pos = Fen(curr_pos, player).update_board()

        pygame.display.flip()
        pygame.display.update()

def main():
    # --------
    # PIECES
    # --------
    starting_pos = "rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR w KQkq - 0 1"
    test_pos = "rnbqkbnr/pppp1ppp/8/4p3/4P3/8/PPPP1PPP/RNBQKBNR w KQkq - 0 1"
    puzzle_pos = "2kr1b1r/p1p3pp/1p3n2/4B3/1q6/2NB4/PPP2PbP/R2QK2R w k - 0 1"
    curr_pos = puzzle_pos

    fen = Fen(curr_pos, player)

    start_game(board, fen, curr_pos, player)


if __name__ == "__main__":
    main()