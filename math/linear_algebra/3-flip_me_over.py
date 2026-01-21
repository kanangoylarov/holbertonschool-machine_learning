#!/usr/bin/env python3
"""docs"""


def matrix_transpose(matrix):
    """Return the transpose of a matrix"""
    tras = []
    rows = len(matrix)
    cols = len(matrix[0])

    for i in range(cols):
        new = []
        new = [matrix[j][i] for j in range(rows)]
        tras.append(new)
    return tras
