#!/usr/bin/python3
def print_matrix_integer(matrix=[]):
    for row in matrix:
        for items in row:
            print("{:d}".format(items), end=" " if items != row[-1] else "")
        print()
