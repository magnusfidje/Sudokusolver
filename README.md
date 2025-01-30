# Sudoku Solver

A Sudoku solver implemented in both Python and C++, using CSP (Constraint Satisfaction Problem) backtracking algorithm with MRV (Minimum Remaining Values) heuristics.

## Features
- Python version includes visual solution display
- C++ version provides text-based output
- Both implementations solve Sudoku puzzles using efficient backtracking

## Usage

### Python Version
Run the solver:
```bash
python main.py
```

To solve a different puzzle, modify the board array in main.py
```
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
```

### Cpp Version

Compile and run:
```bash
clang++ driver.cpp solver.cpp cell.cpp -std=c++11 -o sudoku
./sudoku
```
In cpp, you can change the board in driver.cpp:
```
    vector<vector<int>> board = {
        {1, 0, 0, 0, 0, 7, 0, 9, 0},
        {0, 3, 0, 0, 2, 0, 0, 0, 8},
        {0, 0, 9, 6, 0, 0, 5, 0, 0},
        {0, 0, 5, 3, 0, 0, 9, 0, 0},
        {0, 1, 0, 0, 8, 0, 0, 0, 2},
        {6, 0, 0, 0, 0, 4, 0, 0, 0},
        {3, 0, 0, 0, 0, 0, 0, 1, 0},
        {0, 4, 0, 0, 0, 0, 0, 0, 7},
        {0, 0, 7, 0, 0, 0, 3, 0, 0}
        };
```

