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

class Puzzle(Frame):

    def __init__(self):

        Frame.__init__(self)
        self.master.title("Tic-tac-toe")
        self.createBoard() 
    
    def check_col(self, array):
        pass
    
    def check_row(self, array):
        pass

    def check_diag(self, array):
        pass

    def check_win(self):
        self.check_col(states)

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