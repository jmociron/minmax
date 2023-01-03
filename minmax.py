# References:
# itertools - https://docs.python.org/3/library/itertools.html

from copy import deepcopy
from itertools import cycle

starting_grid = [
    [None, None, None],
    [None, None, None],
    [None, None, None]
]

test_grid = [
    ["X", "O", None],
    [None, None, None],
    [None, None, None]
]

generated_grids = []

players = ["X", "O"]

def check_terminal(grid):
    for row in grid:
        if None in row:
            return False
    return False

def print_grid(grid):

    for i in range(len(grid)):
        for j in range(len(grid)):
            if grid[i][j] is None:
                print("|", " ", end=" ")
            else:
                print("|", grid[i][j], end=" ")
        print("|")
    print("\n")

def generate_actions(grid, state):

    empty_cells = 0
    for row in grid:
        empty_cells += sum(cell is None for cell in row)
    print("\nEmpty cells:", empty_cells)

    for e in range(empty_cells):
        for i in range(len(grid)):
            for j in range(len(grid)):
                if grid[i][j] is None:
                    new_grid = deepcopy(grid)
                    new_grid[i][j] = state
                    if new_grid not in generated_grids:
                        generated_grids.append(new_grid)
    
    print("\nGenerated grids:")
    for grid in generated_grids:
        print_grid(grid)

generate_actions(test_grid, "X")
