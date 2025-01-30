import numpy as np
import pygame
from src.sudokuboard import Board
from src.solver import Solver


board = np.array([
    [1, 0, 0, 0, 0, 7, 0, 9, 0],
    [0, 3, 0, 0, 2, 0, 0, 0, 8],
    [0, 0, 9, 6, 0, 0, 5, 0, 0],
    [0, 0, 5, 3, 0, 0, 9, 0, 0],
    [0, 1, 0, 0, 8, 0, 0, 0, 2],
    [6, 0, 0, 0, 0, 4, 0, 0, 0],
    [3, 0, 0, 0, 0, 0, 0, 1, 0],
    [0, 4, 0, 0, 0, 0, 0, 0, 7],
    [0, 0, 7, 0, 0, 0, 3, 0, 0]
])


for i in range(9):
    for j in range(9):
        print(board[i][j], end=" ")
    print()

solver = Solver(board)
solver.solve()
print(solver.backtrack_count)

for i in range(9):
    for j in range(9):
        print(solver.board[i][j].value, end=" ")
    print()

pygame.init()
board = Board(solver.board)
board.run()