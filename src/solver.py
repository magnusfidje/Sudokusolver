import numpy as np

class Cell:
    def __init__(self, value, position):
        self.position = position
        print(self.position)
        self.value = value
        self.domain = set(range(1, 10))
        self.is_solved = False
    
    def remove_from_domain(self, value):
        self.domain.remove(value)

    def check_solved(self):
        if len(self.domain) == 1:
            self.value = self.domain.pop()
            self.is_solved = True

class Solver:
    def __init__(self, board):
        self.board = self.create_board(board)
        self.arcs = self.create_arcs()
    
    def create_board(self, board):
        return [[Cell(board[i][j], (i, j)) for j in range(9)] for i in range(9)]

    def create_arcs(self):
        arcs = {}
        # Initialize dictionary for each cell
        for i in range(9):
            for j in range(9):
                arcs[(i, j)] = set()
                
                # Add row constraints
                arcs[(i, j)].update((i, k) for k in range(9) if k != j)
                
                # Add column constraints 
                arcs[(i, j)].update((k, j) for k in range(9) if k != i)
                
                # Add box constraints
                box_row, box_col = 3 * (i // 3), 3 * (j // 3)
                for r in range(box_row, box_row + 3):
                    for c in range(box_col, box_col + 3):
                        if (r, c) != (i, j):
                            arcs[(i, j)].add((r, c))              
        return arcs

    def ac3(self):
        pass
        






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

    solver = Solver(board)
