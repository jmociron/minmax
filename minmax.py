from copy import *

current_grid = [
    ["X", "O", "X"],
    ["X", "O", None],
    [None, None, "O"]
]

player_state = "X"
players = ["O", "X"]

def check_col(grid):
    for i in range(len(grid)):
        col = list(map(lambda row: row[i], grid))
        if col[0] in players:
            match = all(cell == col[0] for cell in col)
            if match:
                print(col[0], "wins!")
                return True
    return False

def check_row(grid):

    for row in grid:
        if row[0] in players:
            match = all(cell == row[0] for cell in row)
            if match:
                print(row[0], "wins!")
                return True
    return False

def check_diag(grid):

    left_diag = []
    right_diag = []

    # retrieves cells in both possible diagonals
    for i in range(len(grid)):
        left_diag.append(grid[i][i])
        for j in range(len(grid)):
            if i+j == len(grid)-1:
                right_diag.append(grid[i][j])

    # checks for the left diagonal
    if left_diag[0] in players:
        match = all(cell == left_diag[0] for cell in left_diag)
        if match:
            print(left_diag[0], "wins!")
            return True

    # checks for the right diagonal
    elif right_diag[0] in players:
        match = all(cell == right_diag[0] for cell in right_diag)
        if match:
            print(right_diag[0], "wins!")
            return True
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

def generate_moves(grid):

    generated_grids = []

    print("\nCurrent grid:")
    print_grid(grid)

    for i in range(len(grid)):
        for j in range(len(grid)):
            if grid[i][j] is None:
                new_grid = deepcopy(grid)
                new_grid[i][j] = player_state
                if new_grid not in generated_grids:
                    generated_grids.append(new_grid)

    print("\nPossible moves for " + player_state + ":")
    for grid in generated_grids:
        print_grid(grid)
generate_moves(current_grid)