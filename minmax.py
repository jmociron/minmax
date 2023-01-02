from copy import *

current_grid = [
    ["X", "O", "X"],
    ["X", "O", None],
    [None, None, "O"]
]

players = ["O", "X"]
ai_player = players[1]
human_player = players[0]

def check_col(grid):
    for i in range(len(grid)):
        col = list(map(lambda row: row[i], grid))
        if col[0] in players:
            match = all(cell == col[0] for cell in col)
            if match:
                if col[0] == ai_player:
                    print("AI wins!")
                    return 1
                elif col[0] == human_player:
                    print("You win!")
                    return 0

def check_row(grid):

    for row in grid:
        if row[0] in players:
            match = all(cell == row[0] for cell in row)
            if match:
                if row[0] == ai_player:
                    print("AI wins!")
                    return 1
                elif row[0] == human_player:
                    print("You win!")
                    return 0

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
            if left_diag[0] == ai_player:
                print("AI wins!")
                return 1
            elif left_diag[0] == human_player:
                print("You win!")
                return 0

    # checks for the right diagonal
    elif right_diag[0] in players:
        match = all(cell == right_diag[0] for cell in right_diag)
        if match:
            if right_diag[0] == ai_player:
                print("AI wins!")
                return 1
            elif right_diag[0] == human_player:
                print("You win!")
                return 0
    
def check_win(grid):
    check_col(grid)
    check_row(grid)
    check_diag(grid)

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

    # print("\nCurrent grid:")
    # print_grid(grid)

    for i in range(len(grid)):
        for j in range(len(grid)):
            if grid[i][j] is None:
                new_grid = deepcopy(grid)
                new_grid[i][j] = ai_player
                if new_grid not in generated_grids:
                    generated_grids.append(new_grid)

    return generated_grids
    # print("\nPossible moves for " + player_state + ":")
    # for grid in generated_grids:
    #     print_grid(grid)

def calculate_score(all_grids):

    for grid in all_grids:
        grid_info = {}
        grid_info["grid"] = grid

        if check_col(grid) or check_row(grid) or check_row(grid):
            pass

    pass

generated_grids = generate_moves(current_grid)