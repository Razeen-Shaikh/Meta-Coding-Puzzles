"""Battleship"""

from typing import List

def getHitProbability(R: int, C: int, G: List[List[int]]) -> float:
    """
    Calculate the hit probability based on the grid G with dimensions R x C.
    
    Parameters:
        R (int): Number of rows in the grid.
        C (int): Number of columns in the grid.
        G (List[List[int]]): 2D grid containing integers.

    Returns:
        float: The hit probability calculated based on the grid.
    """
    total = 0
    for row in G:
        for element in row:
            total += element

    return total/(R*C)

getHitProbability(3, 3, [[0, 0, 0], [0, 0, 0], [0, 0, 0]])
