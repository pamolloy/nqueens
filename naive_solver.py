#!/usr/bin/env python

import sys
import itertools
import subprocess

def naive_solver(board_size):
    permutations = list(itertools.permutations(range(board_size)))
    solutions = []
    for permutation in permutations:
        try:
            board_size = int(board_size)

            assert len(permutation) == board_size
            assert len(permutation) == len(set(perm))

            # Verify the diagonals using brute force
            for x, y in enumerate(permutation):
                for n in range(1, board_size):
                    #print("x=%s, y=%s, n=%s" % (x, y, n))
                    if x + n < board_size and x - n >= 0:
                        assert y + n != permutation[x + n], "%s != %s" % (y + n, permutation[x + n])
                        assert y - n != permutation[x + n], "%s != %s" % (y - n, permutation[x + n])
                    if x - n < board_size and x - n >= 0:
                        assert y - n != permutation[x - n], "%s != %s" % (y - n, permutation[x - n])
                        assert y + n != permutation[x - n], "%s != %s" % (y + n, permutation[x - n])

            solutions.append(permutation)
        except: pass
    print len(solutions)

if __name__ == "__main__":
    naive_solver(int(sys.argv[1]))
