#!/usr/bin/python3
"""
This module defines `matrix_divided`

The function returns the matrix divided by div
"""


def matrix_divided(matrix, div):
    """divide each element of a matrix by div

    Args:
        matrix (list): matrix to divide
        div (int): divisor

    Raises:
        TypeError: div must be a number
        TypeError: Each row of the matrix must have the same size
        TypeError: matrix must be a matrix (list of lists) of integers/floats
        ZeroDivisionError

    Returns:
        list: matrix divided by div
    """

    if not isinstance(div, (int, float)):
        raise TypeError('div must be a number')

    for line in matrix:
        if len(line) != len(matrix[0]):
            raise TypeError('Each row of the matrix must have the same size')

        for element_index, element in enumerate(line):
            if not isinstance(element, (int, float)):
                raise TypeError(
                    'matrix must be a matrix (list of lists)'
                    ' of integers/floats'
                )

            line[element_index] = round(element/div, 2)

    return matrix
