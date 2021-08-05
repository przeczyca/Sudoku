from Board import *
from tkinter import *

myBoard = Board()
myBoard.createBoard("easy.txt")
#myBoard.printBoard()
myEntries = []

root = Tk()

#create entries and assign them a stringVar
for row in range(9):
    myEntries.append([])
    for col in range(9):
        entry = Entry(root, width = 2, justify = "center", font = "Helvetica 20 bold")

        entry.insert(END, str(myBoard.board[row][col]))
        if str(myBoard.board[row][col]) != '':
            entry.config(state = DISABLED)
        entry.grid(row = row, column = col, padx = 2, pady = 2)
        myEntries[row].append(entry)

#print(myEntries)

def submit():
    validValues = {"1", "2", "3", "4", "5", "6", "7", "8", "9"}
    for row in range(9):
        for col in range(9):
            entry = myEntries[row][col]
            if entry.get() in validValues:
                myBoard.board[row][col] = entry.get()
            else:
                Label(root, text = "Invalid Value").grid(row = 10, column = 0, columnspan=9)
                return
    
    if myBoard.isSolved():
        Label(root, text = "Solved!!").grid(row = 10, column = 0, columnspan=9)
    else:
        Label(root, text = "Wrong").grid(row = 10, column = 0, columnspan=9)

submitButton = Button(root, text = "Submit", command = submit)
submitButton.grid(row = 9, column = 3, columnspan=3)

def getEntry(row, col):
    entry = myEntries[row][col]
    return entry

root.mainloop()