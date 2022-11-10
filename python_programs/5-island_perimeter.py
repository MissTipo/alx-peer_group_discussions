#!/usr/bin/python3
'''returns the perimeter of the island described in grid'''
def island_perimeter(grid):
    cell_per = 0
    for y in range(len(grid)):
        for x in range(len(grid[y])):
            if grid[y][x] == 1:
                if y >= 0 and grid[y - 1][x] == 0:
                    cell_per = cell_per + 1
                if grid[y][x - 1] == 0:
                    cell_per = cell_per + 1
                if grid[y][x + 1] == 0:
                    cell_per = cell_per + 1
                if grid[y + 1][x] == 0:
                    cell_per = cell_per + 1
    return (cell_per)



