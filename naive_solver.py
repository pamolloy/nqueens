#!/usr/bin/env python

import sys
import itertools
import subprocess

from verify import *

def naive_solver(board_size):
    permutations = list(itertools.permutations(range(board_size)))
    solutions = []
    for permutation in permutations:
        try:
            verify_num_queens(permutation, board_size)
            verify_columns()
            verify_rows(permutation)
            verify_diagonals(permutation, board_size)
            solutions.append(permutation)
        except: pass
    print len(solutions)

if __name__ == "__main__":
    naive_solver(int(sys.argv[1]))
