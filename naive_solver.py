#!/usr/bin/env python

import sys
import itertools
import subprocess

def naive_solver(board_size):
    perm_list = list(itertools.permutations(range(board_size)))
    solutions = []
    for perm in perm_list:
        try:
            board_size = int(board_size)

            assert len(perm) == board_size
            assert len(perm) == len(set(perm))

            # Verify the diagonals using brute force
            for x, y in enumerate(perm):
                for n in range(1, board_size):
                    #print("x=%s, y=%s, n=%s" % (x, y, n))
                    if x + n < board_size and x - n >= 0:
                        assert y + n != perm[x + n], "%s != %s" % (y + n, perm[x + n])
                        assert y - n != perm[x + n], "%s != %s" % (y - n, perm[x + n])
                    if x - n < board_size and x - n >= 0:
                        assert y - n != perm[x - n], "%s != %s" % (y - n, perm[x - n])
                        assert y + n != perm[x - n], "%s != %s" % (y + n, perm[x - n])

            solutions.append(perm)
        except: pass
    print len(solutions)

naive_solver(int(sys.argv[1]))
