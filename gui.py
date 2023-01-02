from minmax import *
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

players = ["O", "X"]
player = players[1]


class Puzzle(Frame):

    def __init__(self):
        Frame.__init__(self)
        self.master.title("Tic-tac-toe")
        self.createBoard()

    def check_win(self):
        check_col(grid)
        check_row(grid)
        check_diag(grid)

    def clicked(self, row, col):
        buttons[row][col].configure(text=player)
        grid[row][col] = player
        self.check_win()

    def createBoard(self):

        for row in range(3):
            for col in range(3):
                buttons[row][col] = Button(
                    height=5,
                    width=10,
                    font=("Arial Rounded MT Bold", 10),
                    command=lambda r=row, c=col: self.clicked(r, c)
                )
                buttons[row][col].grid(row=row, column=col)

def startGame():
    if __name__ == "__main__":
        root = Puzzle()
        root.mainloop()


startGame()
