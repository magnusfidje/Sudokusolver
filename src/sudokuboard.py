"""This module contains the class for the sudoku board"""

import numpy as np
import pygame

class Board:
    def __init__(self, board):
        self.board = board
        self.selected = None
        self.rows = len(board)
        self.cols = len(board[0])
        self.width = 540
        self.height = 540
        self.cell_size = self.width // 9
        self.font = pygame.font.Font(None, 40)

    def draw(self, window):
        window.fill((255, 255, 255))
        self.draw_grid(window)
        self.draw_numbers(window)
    
    def draw_grid(self, window):
        for i in range(10):
            if i % 3 == 0:
                thickness = 4
            else:
                thickness = 1
            pygame.draw.line(window, (0, 0, 0), (0, i * self.cell_size), (self.width, i * self.cell_size), thickness)
            pygame.draw.line(window, (0, 0, 0), (i * self.cell_size, 0), (i * self.cell_size, self.height), thickness)
    
    def draw_numbers(self, window):
        for i in range(self.rows):
            for j in range(self.cols):
                if self.board[i][j] != 0:
                    number = self.font.render(str(self.board[i][j]), True, (0, 0, 0))
                    x = j * self.cell_size + (self.cell_size // 3)
                    y = i * self.cell_size + (self.cell_size // 3)
                    window.blit(number, (x, y))
    
    def run(self):
        window = pygame.display.set_mode((self.width, self.height))
        pygame.display.set_caption("Sudoku")
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
            self.draw(window)
            pygame.display.update()



if __name__ == "__main__":
    board = np.array([
        [0, 0, 0, 1, 0, 0, 0, 0, 0],
        [0, 0, 0, 2, 0, 0, 0, 0, 0],
        [0, 0, 0, 3, 0, 0, 0, 0, 0],
        [0, 0, 0, 4, 0, 0, 0, 0, 0],
        [0, 0, 0, 5, 0, 0, 0, 0, 0],
        [0, 0, 0, 6, 0, 0, 0, 0, 0],
        [0, 0, 0, 7, 0, 0, 0, 0, 0],
        [0, 0, 0, 8, 0, 0, 0, 0, 0],
        [0, 0, 0, 9, 0, 0, 0, 0, 0]
    ])

    pygame.init()
    board = Board(board)
    board.run()


