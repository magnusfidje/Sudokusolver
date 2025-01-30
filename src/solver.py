import numpy as np

class Cell:
    def __init__(self, value, position):
        self.position = position
        self.value = value
        if value == 0:
            self.domain = set(range(1, 10))
        else:
            self.domain = {value}


class Solver:
    def __init__(self, board):
        self.board = [[Cell(board[i][j], (i, j)) for j in range(9)] for i in range(9)]
        self.initialize_domains()

    def initialize_domains(self):

        for i in range(9):
            for j in range(9):
                if self.board[i][j].value == 0:
                    used_values = self.get_used_values(i, j)
                    self.board[i][j].domain -= used_values

    def get_used_values(self, row, col):
        
        used = set()

        # Check row
        for j in range(9):
            if self.board[row][j].value != 0:
                used.add(self.board[row][j].value)

        # Check column
        for i in range(9):
            if self.board[i][col].value != 0:
                used.add(self.board[i][col].value)

        # Check box
        box_row, box_col = 3 * (row // 3), 3 * (col // 3)
        for i in range(box_row, box_row + 3):
            for j in range(box_col, box_col + 3):
                if self.board[i][j].value != 0:
                    used.add(self.board[i][j].value)

        return used

    def get_mrv(self):
        min_remaining = 10
        min_cell = None
        min_pos = None
        
        for i in range(9):
            for j in range(9):
                cell = self.board[i][j]

                if cell.value == 0 and len(cell.domain) < min_remaining:

                    min_remaining = len(cell.domain)
                    min_cell = cell
                    min_pos = (i, j)

        return min_pos, min_cell

    def solve(self):

        return self.backtrack()

    def backtrack(self):
        pos, cell = self.get_mrv()
        if not pos:
            return True

        row, col = pos
        for value in cell.domain: 
            if self.is_valid(row, col, value):

                old_value = cell.value
                cell.value = value
                
                if self.backtrack():  
                    return True
                    
                
                cell.value = old_value
                
        return False

    def is_valid(self, row, col, value):

        # Check row
        for j in range(9):
            if j != col and self.board[row][j].value == value:
                return False
            
        # Check column
        for i in range(9):
            if i != row and self.board[i][col].value == value:
                return False
            
        # Check box
        box_row, box_col = 3 * (row // 3), 3 * (col // 3)
        for i in range(box_row, box_row + 3):
            for j in range(box_col, box_col + 3):
                if (i,j) != (row,col) and self.board[i][j].value == value:
                    return False
        

        return True

    def print_board(self):
        for row in self.board:
            print(' '.join(str(cell.value) for cell in row))

if __name__ == "__main__":

    board = np.array([
    [5, 3, 0, 0, 7, 0, 0, 0, 0],
    [6, 0, 0, 1, 9, 5, 0, 0, 0],
    [0, 9, 8, 0, 0, 0, 0, 6, 0],
    [8, 0, 0, 0, 6, 0, 0, 0, 3],
    [4, 0, 0, 8, 0, 3, 0, 0, 1],
    [7, 0, 0, 0, 2, 0, 0, 0, 6],
    [0, 6, 0, 0, 0, 0, 2, 8, 0],
    [0, 0, 0, 4, 1, 9, 0, 0, 5],
    [0, 0, 0, 0, 8, 0, 0, 7, 9]
    ])  

    solver = Solver(board)
    solver.print_board()
    print()
    solver.solve()
    solver.print_board()

