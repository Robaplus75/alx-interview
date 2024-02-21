#!/usr/bin/python3
"""
func that rotates 2D Matrix
"""


def rotate_2d_matrix(matrix):
    """The rotating Func"""
    k = len(matrix)
    for i in range(int(k / 2)):
        y = (k - i - 1)
        for j in range(i, y):
            x = (k - 1 - j)
            tempo = matrix[i][j]
            matrix[i][j] = matrix[x][i]
            matrix[x][i] = matrix[y][x]
            matrix[y][x] = matrix[j][y]
            matrix[j][y] = tempo
