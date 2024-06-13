#!/usr/bin/env python3
""" this script will solve the island perimeter problem """


def island_perimeter(grid):
    """ the perimeter of the island described in grid """

    if not grid:
        return 0
    per = 0
    for row in range(len(grid)):
        for col in range(len(grid[row])):
            if grid[row][col] == 1:
                if row == 0 or grid[row - 1][col] == 0:
                    per += 1
                if col == 0 or grid[row][col - 1] == 0:
                    per += 1
                if row == len(grid) - 1 or grid[row + 1][col] == 0:
                    per += 1
                if col == len(grid[row]) - 1 or grid[row][col + 1] == 0:
                    per += 1
    return per
