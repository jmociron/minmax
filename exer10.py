from copy import *
from math import *
from random import *
from tkinter import *
from tkinter import messagebox

buttons = [
    [None, None, None],
    [None, None, None],
    [None, None, None]
]

game_grid = [
    [None, None, None],
    [None, None, None],
    [None, None, None]
]

human_turn = None # flagger for game sequence
ai_turn = True # flagger for minimax function

# holds "X" or "O" depending on user input
human_player = None
ai_player = None
players = ["X", "O"]

# checks for all columns for any matches
def check_col(grid):

    for i in range(len(grid)):
        col = list(map(lambda row: row[i], grid))
        if col[0] in players:
            match = all(cell == col[0] for cell in col)
            if match:
                if col[0] == ai_player:
                    return 1
                elif col[0] == human_player:
                    return -1
    return 0

# checks for all row for any matches
def check_row(grid):

    for row in grid:
        if row[0] in players:
            match = all(cell == row[0] for cell in row)
            if match:
                if row[0] == ai_player:
                    return 1
                elif row[0] == human_player:
                    return -1
    return 0

# checks for both diagonals for any matches
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
                return 1
            elif left_diag[0] == human_player:
                return -1

    # checks for the right diagonal
    if right_diag[0] in players:
        match = all(cell == right_diag[0] for cell in right_diag)
        if match:
            if right_diag[0] == ai_player:
                return 1
            elif right_diag[0] == human_player:
                return -1

    return 0

# shows a messagebox for when human wins
def human_wins():
    print("You win!")
    messagebox.showinfo("Game over!", "You win!")

# shows a messagebox for when ai wins
def ai_wins():
    print("AI wins!")
    messagebox.showinfo("Game over!", "AI wins!")

# shows a messagebox for when ai wins
def player_draw():
    print("Draw!")
    messagebox.showinfo("Game over!", "Draw!")

# checks if board has any winning condition
def check_win(grid):

    # AI = 1
    # human = -1
    # neither (or draw) = 0

    col_value = check_col(grid)
    row_value = check_row(grid)
    diag_value = check_diag(grid)

    if col_value != 0:
        return col_value
    elif row_value != 0:
        return row_value
    elif diag_value != 0:
        return diag_value

    return 0

# displays message box if win or draw is detected
def display_win(grid):

    win = check_win(grid)

    if win == 1:
        ai_wins()
    elif win == -1:
        human_wins()
    elif win == 0 and check_terminal(grid):
        player_draw()

# checks if the board is full (terminal node)
def check_terminal(grid):
    for row in grid:
        if None in row:
            return False
    return True

# formats and prints the grid in the terminal
def print_grid(grid):

    for i in range(len(grid)):
        for j in range(len(grid)):
            if grid[i][j] is None:
                print("|", " ", end=" ")
            else:
                print("|", grid[i][j], end=" ")
        print("|")
    print("\n")

# performs the minimax algorithm and returns best possible move
def minimax(current_grid, ai_turn, alpha, beta):

    current_ai_turn = ai_turn  # flagger for current player
    best_move = {
        "x": None,  # x-coordinate of move
        "y": None,  # y-coordinate of move
        "utility": None,  # utility value
    }

    # if max_value: m = neg_inf
    if ai_turn:
        best_move["utility"] = -inf
    # if min_value: m = pos_inf
    else:
        best_move["utility"] = +inf

    # if s is terminal: return utility(s)
    if check_win(current_grid) != 0 or check_terminal(current_grid):
        best_move["utility"] = check_win(current_grid)
        return best_move

    # traverses through all cells in the grid
    for i in range(len(current_grid)):
        for j in range(len(current_grid)):

            # checks for empty cell in the grid
            if current_grid[i][j] is None:

                # creates a copy of the grid with the move generated
                temp_grid = deepcopy(current_grid)

                # adds the generated move to the temporary grid
                if ai_turn:
                    temp_grid[i][j] = ai_player
                else:
                    temp_grid[i][j] = human_player

                # v = value(s, a, b)
                value = minimax(temp_grid, not current_ai_turn, alpha, beta)
                value["x"] = i
                value["y"] = j

                # maxValue(s, a, b)
                if ai_turn:
                    # m = max(m,v)
                    if value["utility"] > best_move["utility"]:
                        best_move = value
                    # if v >= b: return m
                    if value["utility"] >= beta:
                        return best_move
                    # a = max(a, m)
                    if value["utility"] > alpha:
                        alpha = best_move["utility"]

                # minNode(s, a, b)
                else:
                    # m = min(m, v)
                    if value["utility"] < best_move["utility"]:
                        best_move = value
                    # if v <= a
                    if value["utility"] <= alpha:
                        return best_move
                    # b = min(b, m)
                    if value["utility"] < beta:
                        beta = best_move["utility"]

    return best_move

# holds the game grid and buttons
class grid_frame(Frame):

    def __init__(self):
        Frame.__init__(self)
        self.master.title("Tic-tac-toe")
        self.create_board()
    
    def ai_random_turn(self):

        # for testing the algorithm, the ai can be assigned a random first move

        coordinates = [0, 1, 2]
        current_player = ai_player # sets the current player as the ai
        x = choice(coordinates)
        y = choice(coordinates)

        # updates the GUI and the grid list
        buttons[x][y].configure(text=current_player,
                                disabledforeground="red", state=DISABLED)
        game_grid[x][y] = ai_player

    def ai_turn(self):
        current_player = ai_player # sets the current player as the ai
        best_move = minimax(game_grid, True, alpha = -inf, beta = +inf)
        
        # retrieves the coordinates returned by minimax
        x = best_move["x"]
        y = best_move["y"]

        # updates the GUI and the grid list
        buttons[x][y].configure(text=current_player,
                                disabledforeground="red", state=DISABLED)
        game_grid[x][y] = ai_player

    def clicked(self, row, col):

        # checks if grid is still playable before allowing clicks
        if not check_win(game_grid) and not check_terminal(game_grid):
            
            current_player = human_player # sets the current player as the human
            
            # updates the GUI and the grid list
            buttons[row][col].configure(
                text=current_player, disabledforeground="blue", state=DISABLED)
            game_grid[row][col] = current_player
            
            display_win(game_grid) # displays prompt if win is detected

            # checks if grid is still playable before allowing clicks
            if not check_win(game_grid) and not check_terminal(game_grid):
                
                current_player = ai_player # sets the current player as the ai                
                self.ai_turn() # after human, ai will generate a move
                display_win(game_grid) # displays prompt if win is detected

    def create_board(self):

        # generates an empty, clickable button in a 3x3 grid format
        for row in range(3):
            for col in range(3):
                buttons[row][col] = Button(
                    height=2,
                    width=5,
                    font=("Arial Rounded MT Bold", 35),
                    command=lambda r=row, c=col: self.clicked(r, c)
                )
                buttons[row][col].grid(row=row, column=col)

        # if ai is "X", ai will be called to generate a move
        if not human_turn:
            # self.ai_turn()
            self.ai_random_turn()

# holds the starting prompt for player to pick between "X" and "O"
class start_frame(Frame):
    def __init__(self):
        Frame.__init__(self)
        self.master.title("Start")
        self.player_prompt()

    def set_human(self, state):

        global human_player, ai_player, human_turn
        human_player = state

        if human_player == "O":
            ai_player = "X"
            human_turn = False
        else:
            ai_player = "O"
            human_turn = True

        print("\nYou are:", human_player)
        print("AI is:", ai_player)

        # after selection, the game frame is called
        self.destroy()
        root = grid_frame()
        root.mainloop()

    def player_prompt(self):

        font_style = "Verdana"

        text = Label(self, text="Select your player:", height=3,
                     font=(font_style, 12))
        x_btn = Button(self, text="X", font=(
            font_style, 12), command=lambda: self.set_human("X"))
        exit_btn = Button(self, text="Exit", font=(
            font_style, 12), command=lambda: self.quit())
        o_btn = Button(self, text="O", font=(
            font_style, 12), command=lambda: self.set_human("O"))

        text.pack()
        x_btn.pack(side=LEFT)
        exit_btn.pack(side=RIGHT)
        o_btn.pack(pady=5)

def start_game():
    if __name__ == "__main__":
        start = start_frame()
        start.pack(padx=50, pady=10)
        start.mainloop()

start_game()
