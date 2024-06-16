#!/usr/bin/python3
"""
Rotate a 2D matrix 90 degrees clockwise.
"""


def rotate_2d_matrix(matrix):
    """ 
    Rotate a given 2D matrix 90 degrees clockwise in-place.
    
    Args:
        matrix (list of list of int): The 2D matrix to rotate.
    
    Returns:
        None
    """
    size = len(matrix)
    for layer in range(size // 2):
        for element in range((size + 1) // 2):
            temp = matrix[layer][element]
            matrix[layer][element] = matrix[size - 1 - element][layer]
            matrix[size - 1 - element][layer] = matrix[size - 1 - layer][size - 1 - element]
            matrix[size - 1 - layer][size - 1 - element] = matrix[element][size - 1 - layer]
            matrix[element][size - 1 - layer] = temp
