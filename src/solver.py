import numpy as np

class Cell:
    def __init__(self, value, position):
        self.position = position
        self.value = value
        if value == 0:
            self.domain = set(range(1, 10))
            self.is_solved = False
        else:
            self.domain = {value}
            self.is_solved = True

    def remove_from_domain(self, value):
        if value in self.domain:
            self.domain.remove(value)
            if len(self.domain) == 1:
                self.value = list(self.domain)[0]
                self.is_solved = True
                return True
        return False
    

class Solver:
    def __init__(self, board):
        self.board = self.create_board(board)
        self.arcs = self.create_arcs()
        self.initialize_domains() 
    
    def solve(self):
        self.ac3()
        return self.backtracking() 
    
    def create_board(self, board):
        return [[Cell(board[i][j], (i, j)) for j in range(9)] for i in range(9)]

    def initialize_domains(self):
        for i in range(9):
            for j in range(9):
                cell = self.board[i][j]
                if not cell.is_solved:
                    # Remove values from same row, column, and box
                    for pos in self.arcs[(i,j)]:
                        neighbor = self.board[pos[0]][pos[1]]
                        if neighbor.is_solved:
                            cell.remove_from_domain(neighbor.value)

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
        queue = []
        for cell_pos, neighbors in self.arcs.items():
            cell = self.board[cell_pos[0]][cell_pos[1]]
            if not cell.is_solved:  # Only add arcs for unsolved cells
                for neighbor in neighbors:
                    queue.append((cell_pos, neighbor))
        
        while queue:
            (xi, xj) = queue.pop(0)
            if self.revise(xi, xj):
                if len(self.board[xi[0]][xi[1]].domain) == 0:
                    return False
                for xk in self.arcs[xi]:
                    if xk != xj:
                        queue.append((xk, xi))
        return True
    
    def revise(self, i, j):
        revised = False
        cell = self.board[i[0]][i[1]]
        neighbor = self.board[j[0]][j[1]]
        
        if cell.is_solved:
            return False
                
        # Current check isn't strong enough
        if neighbor.is_solved:
            if neighbor.value in cell.domain:
                if cell.remove_from_domain(neighbor.value):
                    revised = True
        
        # Need to check if any values in domain have NO support
        for x in cell.domain.copy():
            if not neighbor.is_solved:
                if not any(x != v for v in neighbor.domain):
                    cell.remove_from_domain(x)
                    revised = True
                    
        return revised
    
    def get_mrv(self):
        min_remaining = 10  
        mrv_cell = None
        mrv_pos = None
        
        for i in range(9):
            for j in range(9):
                cell = self.board[i][j]
                if not cell.is_solved and len(cell.domain) < min_remaining:
                    min_remaining = len(cell.domain)
                    mrv_cell = cell
                    mrv_pos = (i, j)
                    
        return mrv_pos, mrv_cell
    
    def backtracking(self):
        if self.is_solved():
            return True
            
        pos, cell = self.get_mrv()
        
        # Save entire board state
        old_states = {}
        for i in range(9):
            for j in range(9):
                old_states[(i,j)] = {
                    'domain': self.board[i][j].domain.copy(),
                    'value': self.board[i][j].value,
                    'is_solved': self.board[i][j].is_solved
                }
        
        for value in cell.domain.copy():
            if self.is_consistent(pos, value):
                cell.domain = {value}
                cell.value = value
                cell.is_solved = True
                
                if self.ac3():
                    if self.backtracking():
                        return True
                
                # Restore entire board state
                for i in range(9):
                    for j in range(9):
                        self.board[i][j].domain = old_states[(i,j)]['domain']
                        self.board[i][j].value = old_states[(i,j)]['value']
                        self.board[i][j].is_solved = old_states[(i,j)]['is_solved'] 
        return False
    
    def is_solved(self):
        for i in range(9):
            for j in range(9):
                if not self.board[i][j].is_solved:
                    return False
        return True

    def is_consistent(self, pos, value):
        row, col = pos
        
        # Check row
        for j in range(9):
            if j != col and self.board[row][j].is_solved and self.board[row][j].value == value:
                return False
                
        # Check column
        for i in range(9):
            if i != row and self.board[i][col].is_solved and self.board[i][col].value == value:
                return False
                
        # Check 3x3 box
        box_row, box_col = 3 * (row // 3), 3 * (col // 3)
        for i in range(box_row, box_row + 3):
            for j in range(box_col, box_col + 3):
                if (i,j) != pos and self.board[i][j].is_solved and self.board[i][j].value == value:
                    return False
                    
        return True

    def print_board(self):
        for i in range(9):
            for j in range(9):
                print(self.board[i][j].value, end=" ")
            print()


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

