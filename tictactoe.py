# from minmax import *
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
human_turn = True
ai_player = None
players = ["O", "X"]

# TIC-TAC-TOE LOGIC

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

# GUI

class grid_frame(Frame):

    def __init__(self):
        Frame.__init__(self)
        self.master.title("Tic-tac-toe")
        self.create_board()

    def clicked(self, row, col):
        global human_turn
        buttons[row][col].configure(text = human_player)
        grid[row][col] = human_player
        human_turn = False

        # print("\nYour move:")
        # print_grid(grid)
        # generate_moves(grid, ai_player)
        check_win(grid)
    
    def refresh_frame(self):
        for item in self.mainFrame.winfo_children():
            item.destroy()

    def create_board(self):

        for row in range(3):
            for col in range(3):
                buttons[row][col] = Button(
                    height=2,
                    width=5,
                    font=("Arial Rounded MT Bold", 35),
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
        
        text = Label(self, text = "Select your player:", height = 3, font=("Arial Rounded MT Bold", 12))
        x_btn = Button(self, text = "X", font=("Arial Rounded MT Bold", 12), command = lambda:self.set_human("X"))
        exit_btn = Button(self, text = "Exit", font=("Arial Rounded MT Bold", 12), command = lambda:self.quit())
        o_btn = Button(self, text = "O", font=("Arial Rounded MT Bold", 12), command = lambda:self.set_human("O"))
        
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
