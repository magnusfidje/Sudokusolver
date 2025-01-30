//This is the driver file for a sudoku solver program.

#include <iostream>
#include <vector>
#include "solver.h"

using namespace std;

int main(){

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

    Solver solver(board);
    print(cout, solver);
    solver.solve();
    print(cout, solver);
}