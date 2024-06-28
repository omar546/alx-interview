#!/usr/bin/python3
'''0x09. Island Perimeter'''


def island_perimeter(grid):
    '''Returns the perimeter of the island described in the grid'''
    perimeter = 0
    # Index of the last row in the grid
    max_row_index = len(grid) - 1
    # Index of the last column in the first row
    max_col_index = len(grid[0]) - 1

    for row_index, row in enumerate(grid):
        for col_index, cell in enumerate(row):
            if cell == 1:
                # Check left and right neighbors
                if col_index == 0:
                    # Left edge
                    perimeter += 1
                elif row[col_index - 1] == 0:
                    # Neighbor to the left is water
                    perimeter += 1

                if col_index == max_col_index:
                    # Right edge
                    perimeter += 1
                elif row[col_index + 1] == 0:
                    # Neighbor to the right is water
                    perimeter += 1

                # Check top and bottom neighbors
                if row_index == 0:
                    # Top edge
                    perimeter += 1
                elif grid[row_index - 1][col_index] == 0:
                    # Neighbor above is water
                    perimeter += 1

                if row_index == max_row_index:
                    # Bottom edge
                    perimeter += 1
                elif grid[row_index + 1][col_index] == 0:
                    # Neighbor below is water
                    perimeter += 1

    return perimeter
