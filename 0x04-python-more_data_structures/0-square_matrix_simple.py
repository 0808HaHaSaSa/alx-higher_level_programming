#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    m = matrix.copy()
    a = len(matrix)
    i = 0
    while i < a:
        j = 0
        while j < a:
            m[i][j] = matrix[i][j]*matrix[i][j]
            j = j + 1
        i = i + 1
    return m
