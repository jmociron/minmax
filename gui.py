from tkinter import *
from tkinter import messagebox

buttons = [
    [0, 0, 0],
    [0, 0, 0],
    [0, 0, 0]
]

states = [
    [0, 0, 0],
    [0, 0, 0],
    [0, 0, 0]
]

players = ["O", "X"]
player = players[1]

class Puzzle(Frame):

    def __init__(self):

        Frame.__init__(self)
        self.master.title("Tic-tac-toe")
        self.createBoard() 
    
    def check_col(self):
        for i in range(len(states)):
            col = list(map(lambda row: row[i], states))
            if col[0] in players:
                match = all(state == col[0] for state in col)
                if match:
                    print(col[0], "wins!")
                    return True
        return False
        
    def check_row(self):

        for row in states:
            if row[0] in players:
                match = all(state == row[0] for state in row)
                if match:
                    print(row[0], "wins!")
                    return True
        return False

    def check_diag(self):
        
        left_diag = []
        right_diag = []

        # retrieves states in both possible diagonals
        for i in range(len(states)):
            left_diag.append(states[i][i])
            for j in range(len(states)):
                if i+j == len(states)-1:
                    right_diag.append(states[i][j])

        # checks for the left diagonal
        if left_diag[0] in players:
            match = all(state == left_diag[0] for state in left_diag)
            if match:
                print(left_diag[0], "wins!")
                return True

        # checks for the right diagonal
        elif right_diag[0] in players:
            match = all(state == right_diag[0] for state in right_diag)
            if match:
                print(right_diag[0], "wins!")
                return True
        return False

    def check_win(self):
        self.check_col()
        # self.check_row()
        # self.check_diag()

    def clicked(self, row, col):
        buttons[row][col].configure(text = player)
        states[row][col] = player
        self.check_win()

    def createBoard(self):

        for row in range(3):
            for col in range(3):
                buttons[row][col] = Button(
                    height = 5,
                    width = 10,
                    font = ("Arial Rounded MT Bold", 10),
                    command = lambda r = row, c = col: self.clicked(r, c)
                )
                buttons[row][col].grid(row = row, column = col)

def startGame(): 
    if __name__ == "__main__":
        root = Puzzle()
        root.mainloop()

startGame()