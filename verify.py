#!/usr/bin/env python3
#
# NAME
#   verify.py - Verify a solution to the N Queens problem
#
# SYNOPSIS
#   verify.py FILENAME N
#
# DESCRIPTION
#   Run an executable that takes an integer as an argument and verify the
#   output as a solution to the N Queens problem. The integer specifies the
#   dimensions of the board and the number of queens that should be placed on
#   it. The solution should be formated as space delimited integers. The index
#   of each element represents the x coordinate while the value represents the
#   y coordinate.
#

import subprocess
import sys
import os

if __name__ == "__main__":
    filename = sys.argv[1]
    dimension = sys.argv[2]
    pwd = os.getcwd()
    # TODO: Will break for executables not in PWD. Note that unlike popen(),
    # check_output() does not take the CWD as an argument
    output = subprocess.check_output([pwd + "/" + filename, dimension])
    dimension = int(dimension)

    queens = []
    for n in output.split():
        queens.append(int(n))
    queens = tuple(queens)  # Make immutable since order matters

    # Since the x coordinates are represented by indices, columns may only
    # contain one queen

    # A set cannot contain duplicate elements. Therefore if the set and tuple
    # structures contain the same number of elements no duplicates existed and
    # each row only contains one queen
    assert len(queens) == len(set(queens))

    # Verify the diagonals using brute force
    for x, y in enumerate(queens):
        for n in range(1, dimension):
            print("x=%s, y=%s, n=%s" % (x, y, n))
            if x + n < dimension and x - n >= 0:
                assert y + n != queens[x + n], "%s != %s" % (y + n, queens[x + n])
                assert y - n != queens[x + n], "%s != %s" % (y - n, queens[x + n])
            if x - n < dimension and x - n >= 0:
                assert y - n != queens[x - n], "%s != %s" % (y - n, queens[x - n])
                assert y + n != queens[x - n], "%s != %s" % (y + n, queens[x - n])
