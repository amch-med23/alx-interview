#!/usr/bin/python3
""" a script to retate a 2 dimensions matrix 90 degree clockwise """


def rotate_2d_matrix(matrix):
    """ given n x n 2d matrix, retate it 90 degree clockwise """
    f = 0
    l = len(matrix) - 1
    while f < l:
        for i in range(f, l):
            tmp = matrix[i][l]
            matrix[i][l] = matrix[f][i]
            tmp2 = matrix[l][l + f - i]
            matrix[l][l + f - i] = tmp
            tmp = matrix[l + f - i][f]
            matrix[l + f - i][f] = tmp2
            matrix[f][i] = tmp
            # aux is used here to swap values
        # increamenting the first (moving forward)
        f += 1
        # decreasing the last (moving backwards)
        l -= 1
