//This file contains the solver methods for a sudoku solver program.

#include "solver.h"
#include <iostream>
#include <vector>
#include <set>

//Default constructor
Solver::Solver() {
    board = vector<vector<int> >(9, vector<int>(9, 0));
}

//Constructor
Solver::Solver(vector<vector<int> > board) {
    this->board = board;
    for (int i = 0; i < 9; i++) {
        for (int j = 0; j < 9; j++) {
            cell_board[i][j] = Cell(board[i][j], {i, j});
        }
    }
    initialize_cell_domain();
}

//Initialize the domain of each cell
void Solver::initialize_cell_domain() {
    set<int> used_values;
    for (int i = 0; i < 9; i++) {
        for (int j = 0; j < 9; j++) {
            if (cell_board[i][j].get_value() != 0) {
                used_values = get_used_values(i, j);
                for (int value : used_values) {
                    cell_board[i][j].remove_from_domain(value);
                }
            }
        }
    }
}

//Get the used values in the row, column, and box of a cell
set<int> Solver::get_used_values(int row, int col){

    set<int> used_values;

    for (int i = 0; i < 9; i++) {
        if (cell_board[row][i].get_value() != 0) {
            used_values.insert(cell_board[row][i].get_value());
        }
        if (cell_board[i][col].get_value() != 0) {
            used_values.insert(cell_board[i][col].get_value());
        }
    }
    int box_row = row / 3 * 3;
    int box_col = col / 3 * 3;
    for (int i = box_row; i < box_row + 3; i++) {
        for (int j = box_col; j < box_col + 3; j++) {
            if (cell_board[i][j].get_value() != 0) {
                used_values.insert(cell_board[i][j].get_value());
            }
        }
    }
    return used_values;
}

//Get the cell with the minimum remaining values
Cell Solver::get_mrv(){
    int min_domain_size = 10;
    Cell mrv;
    for (int i = 0; i < 9; i++) {
        for (int j = 0; j < 9; j++) {
            if (cell_board[i][j].get_value() == 0 && cell_board[i][j].get_domain().size() < min_domain_size) {
                min_domain_size = cell_board[i][j].get_domain().size();
                mrv = cell_board[i][j];
            }
        }
    }
    return mrv;
}

//is_valid function
bool Solver::is_valid(int row, int col, int value) {
    //Check the row and column
    for (int i = 0; i < 9; i++) {
        if (cell_board[row][i].get_value() == value) {
            return false;
        }
        if (cell_board[i][col].get_value() == value) {
            return false;
        }
    }
    //Check the box
    int box_row = row / 3 * 3;
    int box_col = col / 3 * 3;
    for (int i = box_row; i < box_row + 3; i++) {
        for (int j = box_col; j < box_col + 3; j++) {
            if (cell_board[i][j].get_value() == value) {
                return false;
            }
        }
    }
    return true;
}

bool Solver::backtrack() {
    
    if (is_solved()) {
        return true;
    }

    Cell mrv = get_mrv();
    // Add check for valid position
    if(mrv.get_position().empty()) return false;
    
    int x = mrv.get_position()[0];
    int y = mrv.get_position()[1];
    Cell& cell = cell_board[x][y];
    
    for (int value : cell.get_domain()) {
        if (is_valid(x, y, value)) {
            cell.set_value(value);
            if (backtrack()) {
                return true;
            }
            cell.set_value(0);
        }
    }
    return false;
}

//Solve function
void Solver::solve() {
    if (backtrack()) {
        cout << "Solved!" << endl;
    } else {
        cout << "No solution found." << endl;
    }
}

//is_solved function
bool Solver::is_solved() {
    for (int i = 0; i < 9; i++) {
        for (int j = 0; j < 9; j++) {
            if (cell_board[i][j].get_value() == 0) {
                return false;
            }
        }
    }
    return true;
}


//Print the board
ostream& print(ostream& os, const Solver& solver) {
    for (int i = 0; i < 9; i++) {
        for (int j = 0; j < 9; j++) {
            os << solver.cell_board[i][j].get_value() << " ";
        }
        os << endl;
    }
    return os;
}