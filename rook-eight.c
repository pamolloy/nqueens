/*
 * rook-eight.c - Rook style solution to the nqueens problem when n=8
 *
 * BUILD
 *      gcc -std=c99 -o rook-eight rook-eight.c
 *
 * TODO
 *      - Solve half the board then reflect
 *      - Read the value of n from stdin
 *      - Place the first queen in a column other than the first
 */

#include <stdio.h>
#include <stdbool.h>

/* If the given row value exists in a preceding column return the first
 * match otherwise return -1. Note that there should only be one match
 */
int find_index_preceding_value(int row, int column, int *queens) {
    printf("Row: %d, Column: %d\n", row, column);
    if (column == 0) {
        return -1;
    }
    for (int precede = 0; precede < column; precede++) {
        if (queens[precede] == row) {
            printf("Row conflicted with column %d\n", queens[precede]);
            return precede;
        }
        int difference = column - precede;
        if (queens[precede] == row + difference) {
            printf("Row conflicted with column %d\n", queens[precede]);
            return precede;
        }
        if (queens[precede] == row - difference) {
            printf("Row conflicted with column %d\n", queens[precede]);
            return precede;
        }
    }
    return -1;
}

int main(int ac, char **av) {
    int dimension = 8;
    printf("Solving for n=%d\n", dimension);
    int queens[dimension];
    // Place the first queen and then iterate through the remainder while
    // checking for conflicts. If the iteration fails move the first queen and
    // try iterating again
    for (int i = 0; i < dimension; i++) {
        int last_row = i;
        // Place a queen in each column
        for (int column = 0; column < dimension; column++) {
            int row;
            bool row_found = false;
            // Get the row of the last queen placed on the board, unless
            // we're placing the first queen
            if (column != 0) {
                int last_column = column - 1;
                last_row = queens[last_column];
                row = last_row + 2;
            } else {
                row = last_row;
            }
            // Try placing the new queen in each row starting with the row
            // two rows above the last queen
            for (; row < dimension; row++) {
                // Check if the row doesn't conflict
                if (find_index_preceding_value(row, column, queens) == -1) {
                    row_found = true;
                    break;
                }
            }
            // If the previous loop hit the top continue from the bottom
            if (row >= dimension) {
                for (row = 0; row < last_row; row++) {
                    // Check if the row doesn't conflict
                    if (find_index_preceding_value(row, column, queens) == -1) {
                        row_found = true;
                        break;
                    }
                }
            }
            if (row_found) {
                printf("Placing a queen on (%d, %d)\n", column, row);
                queens[column] = row;
            } else {
                // Iterating the placement of the first queen and starting over
                printf("Failed to place all queens starting from row %d\n",
                        i);
                break;
            }
        }
    }
    return 0;
}
