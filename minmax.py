# References:
# itertools - https://docs.python.org/3/library/itertools.html

from math import inf
from copy import deepcopy
from itertools import cycle
from tictactoe import check_win

starting_grid = [
    [None, None, None],
    [None, None, None],
    [None, None, None]
]

test_grid = [
    ["X", None, "O"],
    [None, "O", None],
    ["X", "O", "X"]
]


players = ["X", "O"]
human_player = "O" # minimize
ai_player = "X" # maximize
human_turn = False

def check_terminal(grid):
    for row in grid:
        if None in row:
            return False
    return True

def print_grid(grid):

    for i in range(len(grid)):
        for j in range(len(grid)):
            if grid[i][j] is None:
                print("|", " ", end=" ")
            else:
                print("|", grid[i][j], end=" ")
        print("|")
    print("\n")

def get_value(grid, state):
    if check_terminal(grid):
        return check_win(grid)
    elif not human_turn:
        return max_value(grid, state)
    elif human_turn:
        return min_value(grid, state)

def max_value(grid, state):
    m = -inf

    if state == "X":
        next_state = "O"
    else:
        next_state = "X"
    
    global human_turn
    human_turn = not human_turn

    for successor in generate_actions(grid, next_state):
        v = get_value(successor, next_state)
        m = max(m, v)
    return m

def min_value(grid, state):
    m = inf

    if state == "X":
        next_state = "O"
    else:
        next_state = "X"
    
    global human_turn
    human_turn = not human_turn

    for successor in generate_actions(grid, next_state):
        v = get_value(successor, next_state)
        m = min(m, v)
    return m

def generate_actions(grid, state):

    generated_grids = []    
    # grid_info = {}
    # grid_info["grid"] = grid
    # grid_info["value"] = get_value(grid, state)


    empty_cells = 0
    for row in grid:
        empty_cells += sum(cell is None for cell in row)
    # print("\nEmpty cells:", empty_cells)

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
        generate_actions(grid, state)

generate_actions(test_grid, "X")
