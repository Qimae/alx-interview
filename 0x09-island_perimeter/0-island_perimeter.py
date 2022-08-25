#!/usr/bin/python3
"""
Module 0-island_perimeter
function returns the perimeter of the island described
in grid
"""


def island_perimeter(grid):
    """
    returns the perimeter of the island 
    described in grid
    """
    counter = 0
    grid_max = len(grid) - 1  # index of the last list in the grid
    list_max = len(grid[0]) - 1  # index of the last square in list

    for list_idx, list in enumerate(grid):
        for land_idx, land in enumerate(list):
            if land == 1:
                # left and right
                if land_idx == 0:
                    # left side
                    counter += 1

                    # right side
                    if list[land_idx + 1] == 0:
                        counter += 1
                elif land_idx == list_max:
                    # left side
                    if list[land_idx - 1] == 0:
                        counter += 1

                    # right side
                    counter += 1
                else:
                    # left side
                    if list[land_idx - 1] == 0:
                        counter += 1

                    # right side
                    if list[land_idx + 1] == 0:
                        counter += 1

                # top and down
                if list_idx == 0:
                    # top side
                    counter += 1

                    # bottom side
                    if grid[list_idx + 1][land_idx] == 0:
                        counter += 1
                elif list_idx == grid_max:
                    # top side
                    if grid[list_idx - 1][land_idx] == 0:
                        counter += 1

                    # bottom side
                    counter += 1
                else:
                    # top side
                    if grid[list_idx - 1][land_idx] == 0:
                        counter += 1

                    # bottom side
                    if grid[list_idx + 1][land_idx] == 0:
                        counter += 1

    return counter