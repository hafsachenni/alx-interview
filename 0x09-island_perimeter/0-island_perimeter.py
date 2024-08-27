#!/usr/bin/python3
"""island perimeter task"""


def island_perimeter(grid):
    """function that calculates the perimeter
     of a single island in a grid"""
    perim = 0
    for i in range(len(grid)):
        for x in range(len(grid[i])):
            if grid[i][x] == 1:
                perim += 4
                if i > 0 and grid[i - 1][x] == 1:
                    perim -= 2

                if x > 0 and grid[i][x - 1] == 1:
                    perim -= 2

    return perim
