#!/usr/bin/python3
""" a script to retate a 2 dimensions matrix 90 degree clockwise """


def rotate_2d_matrix(matrix):
    """ given n x n 2d matrix, retate it 90 degree clockwise """
    f = 0
    last = len(matrix) - 1
    while f < last:
        for i in range(f, last):
            tmp = matrix[i][last]
            matrix[i][last] = matrix[f][i]
            tmp2 = matrix[last][last + f - i]
            matrix[last][last + f - i] = tmp
            tmp = matrix[last + f - i][f]
            matrix[last + f - i][f] = tmp2
            matrix[f][i] = tmp
            # aux is used here to swap values
        # increamenting the first (moving forward)
        f += 1
        # decreasing the last (moving backwards)
        last -= 1
