// This file contains the cell class for a sudoku solver program.
// The cell class represents a single cell in a sudoku board.

#ifndef CELL_H
#define CELL_H

#include <iostream>
#include <vector>
#include <set>

using namespace std;

class Cell {
    private:
        int value;
        set<int> domain;
        vector<int> position;

    public:

        Cell();
        Cell(int value, vector<int> position);

        int get_value() const {return value;};
        void set_value(int value) {this->value = value;};
        set<int> get_domain() const {return domain;};
        void remove_from_domain(int value);
        vector<int> get_position() const {return position;};
    
};

#endif // CELL_H