import numpy as np
import pygame
from src.sudokuboard import Board
from src.solver import Solver


board = np.array([
    [0, 7, 1, 0, 0, 0, 9, 0, 0],
    [0, 0, 6, 0, 0, 8, 0, 0, 3],
    [3, 4, 0, 6, 0, 0, 0, 5, 0],
    [1, 0, 2, 9, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 3, 0, 0, 0, 9],
    [5, 0, 8, 0, 0, 0, 7, 0, 0],
    [0, 0, 0, 0, 8, 0, 3, 0, 0],
    [6, 0, 0, 0, 5, 0, 0, 9, 7],
    [0, 0, 7, 3, 0, 0, 0, 6, 8]
])

solver = Solver(board)
solver.solve()

for i in range(9):
    for j in range(9):
        print(solver.board[i][j].value, end=" ")
    print()

pygame.init()
board = Board(solver.board)
board.run()