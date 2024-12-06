#!/usr/bin/python3
"""
Function that contain the island_perimeter
"""


def island_perimeter(grid):
    """
    Function that returns the perimeter of the island described in grid
    
    Returns:
        Perimeter of the island
    """
    per = 0
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            if grid[i][j] == 1:
                per = per + 4
                if i > 0 and grid[i - 1][j] == 1:
                    per = per - 2
                if j > 0 and grid[i][j - 1] == 1:
                    per = per - 2
    return per
