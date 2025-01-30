// This program is the solver class for a sudoku solver program.
#ifndef SOLVER_H
#define SOLVER_H

#include <iostream>
#include <vector>
#include <set>
#include "cell.h"


using namespace std;

class Solver {
    private:
       //board member
       vector<vector<int> > board;
       vector<vector<Cell> > cell_board = vector<vector<Cell> >(9, vector<Cell>(9, Cell()));
       
    public:
        //Constructors
        Solver();
        Solver(vector<vector<int> > board);

        //Member functions
        void solve();
        void initialize_cell_domain();
        set<int> get_used_values(int row, int col);
        Cell get_mrv();
        bool is_valid(int row, int col, int value);
        bool backtrack();
        bool is_solved();

        //Print the board
        friend ostream& print(ostream& os, const Solver& solver);

};

#endif // SOLVER_H