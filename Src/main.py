import settings
import pygame
import sys

from board import Board
from fen import Fen

def main():
    pygame.init()
    pygame.display.set_caption("Chess")
    clock = pygame.time.Clock()
    screen = pygame.display.set_mode((settings.WIDTH, settings.HEIGHT))

    # BOARD
    board_scale = 2.5
    board_width, board_height = screen.get_width() // board_scale, screen.get_width() // board_scale
    board_surface = pygame.Surface((board_width, board_height), pygame.SRCALPHA)
    board = Board(board_height)

    screen.fill("#1E1E1E")

    player = 1  # 1 for white, 2 for black

    mode = "ai"

    # PIECES
    starting_pos = "rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR w KQkq - 0 1"
    test_pos = "rnbqkbnr/pppp1ppp/8/4p3/4P3/8/PPPP1PPP/RNBQKBNR w KQkq - 0 1"
    puzzle_pos = "2kr1b1r/p1p3pp/1p3n2/4B3/1q6/2NB4/PPP2PbP/R2QK2R w k - 0 1"
    curr_pos = puzzle_pos

    fen = Fen(curr_pos)

    # print board
    for i in fen.read_fen():
        print(i)

    while True:
        clock.tick(settings.FPS)
        
        # draw pieces and board
        pieces = fen
        
        board.draw_board(board_surface, player)
        pieces.draw_pieces(board_surface, player)
        
        boardX = screen.get_width()//3.5
        boardY = screen.get_height()//8
        screen.blit(board_surface, (boardX, boardY))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            
            if event.type == pygame.MOUSEBUTTONDOWN:
                mouseX = event.pos[0]
                mouseY = event.pos[1]

                # if board is clicked
                if (mouseX >= boardX and mouseY >= boardY) and (mouseX <= boardX + board_width and mouseY <= boardY + board_height):
                    mouseX = event.pos[0] - boardX
                    mouseY = event.pos[1] - boardY

                    row = 1
                    col = 1

                print(f"{col}, {row}")
        
        # curr_pos = pieces.update_board()

        if mode == "multiplayer":
            player = player % 2 + 1  # change player
        
        curr_pos = Fen(curr_pos).update_board()

        pygame.display.flip()
        pygame.display.update()

if __name__ == "__main__":
    main()