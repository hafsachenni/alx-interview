#!/usr/bin/python3
""" this is a function that rotates a 2d matrix"""


def rotate_2d_matrix(matrix):
    n = len(matrix)

    for i in range(n):
        for a in range(i, n):
            matrix[i][a], matrix[a][i] = matrix[a][i], matrix[i][a]
    for i in range(n):
        matrix[i].reverse()
