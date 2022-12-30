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

player = "O"
win = False

class Puzzle(Frame):

    def __init__(self):

        Frame.__init__(self)
        self.master.title("Tic-tac-toe")
        self.createBoard() 
    
    def check_col(self):
        pass        
    
    def check_row(self):
        for row in states:
            print(row)
            match = all(state == row[0] for state in row)
            print(match)
            if match:
                return True
        return False

    def check_diag(self):
        pass

    def check_win(self):
        if self.check_col() or self.check_row():
            print("You win!")

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