//This is the cell class for a sudoku solver program. The cell class represents a single cell in a sudoku board.


#include "cell.h"

Cell::Cell() {
    value = 0;
    domain = {1, 2, 3, 4, 5, 6, 7, 8, 9};
}

Cell::Cell(int value) {
    this->value = value;
    if (value == 0) {
        domain = {1, 2, 3, 4, 5, 6, 7, 8, 9};
    } else {
        domain = {value};
    }
}

Cell::Cell(int value, set<int> domain) {
    this->value = value;
    this->domain = domain;
}

void Cell::remove_from_domain(int value) {
    domain.erase(value);
}