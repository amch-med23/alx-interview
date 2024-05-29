#!/usr/bin/env python3
""" a script to retate a 2 dimensions matrix 90 degree clockwise """


def rotate_2d_matrix(matrix):
    """ given n x n 2d matrix, retate it 90 degree clockwise """
    first = 0
    last = len(matrix) - 1
    while first < last:
        for i in range(first, last):
            aux = matrix[i][last]
            matrix[i][last] = matrix[first][i]
            aux2 = matrix[last][last + first - i]
            matrix[last][last + first - i] = aux
            aux = matrix[last + first - i][first]
            matrix[last + first - i][first] = aux2
            matrix[first][i] = aux
            # aux is used here to swap values
        # increamenting the first (moving forward)
        first += 1
        # decreasing the last (moving backwards)
        last -= 1
