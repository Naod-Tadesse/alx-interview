#!/usr/bin/python3
"""
rotating a 2d matrix
"""


def rotate_2d_matrix(matrix):
    """
    rotate a given matrix 90 degree clock wize
    """
    length = len(matrix)
    for i in range(int(length / 2)):
        y = (length - i - 1)
        for j in range(i, y):
            x = (length - 1 - j)
            tmp = matrix[i][j]
            matrix[i][j] = matrix[x][i]
            matrix[x][i] = matrix[y][x]
            matrix[y][x] = matrix[j][y]
            matrix[j][y] = tmp
