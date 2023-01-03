# References:
# itertools - https://docs.python.org/3/library/itertools.html

from copy import *
from tkinter import *
from tkinter import messagebox

buttons = [
    [None, None, None],
    [None, None, None],
    [None, None, None]
]

grid = [
    [None, None, None],
    [None, None, None],
    [None, None, None]
]

human_player = None
ai_player = None
players = ["O", "X"]

def check_draw(grid):
    for row in grid:
        if None in row:
            return False
    return True

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
                    return -1
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
                    return -1
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
                return -1

    # checks for the right diagonal
    elif right_diag[0] in players:
        match = all(cell == right_diag[0] for cell in right_diag)
        if match:
            if right_diag[0] == ai_player:
                print("AI wins!")
                return 1
            elif right_diag[0] == human_player:
                print("You win!")
                return -1
    
    return 0

def check_win(grid):

    # checks if either player has won:
        # AI = 1
        # human = -1
        # neither (or draw) = 0

    if not check_draw(grid):
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

def calculate_score(all_grids):

    for grid in all_grids:
        grid_info = {}
        grid_info["grid"] = grid

        # if check_col(grid) or check_row(grid) or check_row(grid):
        #     pass

    pass

class grid_frame(Frame):

    def __init__(self):
        Frame.__init__(self)
        self.master.title("Tic-tac-toe")
        self.create_board()

    def clicked(self, row, col):

        buttons[row][col].configure(text = human_player)
        grid[row][col] = human_player
        check_win(grid)

    def create_board(self):

        for row in range(3):
            for col in range(3):
                buttons[row][col] = Button(
                    height=5,
                    width=10,
                    font=("Arial Rounded MT Bold", 10),
                    command=lambda r=row, c=col: self.clicked(r, c)
                )
                buttons[row][col].grid(row=row, column=col)

class start_frame(Frame):
    def __init__(self):
        Frame.__init__(self)
        self.master.title("Start")
        self.player_prompt()

    def set_human(self, state):

        global human_player, ai_player
        human_player = state
        print("You are playing as", human_player)

        if human_player == "O":
            ai_player = "X"
        else:
            ai_player = "O"


        self.destroy()
        root = grid_frame()
        root.mainloop()   

    def player_prompt(self):
        
        text = Label(self, text = "Select your player:", height = 3)
        x_btn = Button(self, text = "X", command = lambda:self.set_human("X"))
        exit_btn = Button(self, text = "Exit")
        o_btn = Button(self, text = "O", command = lambda:self.set_human("O"))
        
        text.pack()
        x_btn.pack(side = LEFT)
        exit_btn.pack(side = RIGHT)
        o_btn.pack(pady = 5)

def start_game():
    if __name__ == "__main__":

        start = start_frame()
        start.pack(padx = 50, pady = 10)
        start.mainloop()    

start_game()
