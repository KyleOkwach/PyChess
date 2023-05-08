import pygame

class Board:

    def __init__(self, surface, size, theme):
        self.board_size = 8
        self.LIGHT_COLOR = theme[0]
        self.DARK_COLOR = theme[1]
        self.SQUARE_SIZE = size // self.board_size
        self.surface = surface

    def draw_board(self, surface, player):
        # loop through each square
        for row in range(self.board_size):
            for col in range(self.board_size):
                x = col * self.SQUARE_SIZE
                y = row * self.SQUARE_SIZE
                self.file = chr(col + 97)  # converting it to char
                self.rank = self.board_size - row
                if player == 2:  # if player is black
                    self.rank = row + 1
                    self.file = chr((self.board_size - col - 1) + 97)

                font = pygame.font.SysFont('Poppins', 11, bold = True)
                padding = self.SQUARE_SIZE // 8

                square = pygame.Rect(x, y, self.SQUARE_SIZE, self.SQUARE_SIZE)
                text_color = (0, 0, 0)

                text = font.render("", True, text_color)
                text_rect = text.get_rect(center = (x + padding, y + padding))

                if (row + col) % 2 == 0 and player == 1:
                    color = self.LIGHT_COLOR
                    pygame.draw.rect(surface, color, square)
                    text_color = self.DARK_COLOR
                elif (row + col) % 2 == 0 and player == 2:
                    color = self.DARK_COLOR
                    pygame.draw.rect(surface, color, square)
                    text_color = self.LIGHT_COLOR
                elif (row + col) % 2 != 0 and player == 1:
                    color = self.DARK_COLOR
                    pygame.draw.rect(surface, color, square)
                    text_color = self.LIGHT_COLOR
                else:
                    color = self.LIGHT_COLOR
                    pygame.draw.rect(surface, color, square)
                    text_color = self.DARK_COLOR

                if col == 0:
                    text = font.render(str(self.rank), True, text_color)
                    text_rect = text.get_rect(center = (x + padding, y + padding))
                    surface.blit(text, text_rect)
                if row == self.board_size - 1:
                    text = font.render(self.file, True, text_color)
                    text_rect = text.get_rect(center = (x + self.SQUARE_SIZE -padding, y + self.SQUARE_SIZE -padding))
                    
                    surface.blit(text, text_rect)
