class Board():
    def __init__(self):
        self.board = []
    
    def createBoard(self, fileName):
        file = open(fileName)

        for line in file.readlines():
            row = line.rstrip().split(",")
            self.board.append(row)

        file.close()
    
    def isSolved(self):
        #Check rows
        for row in range(9):
            rowSet = set()
            for value in self.board[row]:
                if value in rowSet:
                    return False
                rowSet.add(value)

        #Check column
        for col in range(9):
            colSet = set()
            for row in range(9):
                value = self.board[row][col]
                if value in colSet:
                    return False
                colSet.add(value)

        #Check 3x3 areas
        areaRow = 0
        while areaRow < 3:
            row = areaRow * 3
            areaCol = 0
            while areaCol < 3:
                col = areaCol * 3
                areaSet = set()
                areaSet.add(self.board[row][col])
                areaSet.add(self.board[row][col+1])
                areaSet.add(self.board[row][col+2])
                areaSet.add(self.board[row+1][col])
                areaSet.add(self.board[row+1][col+1])
                areaSet.add(self.board[row+1][col+2])
                areaSet.add(self.board[row+2][col])
                areaSet.add(self.board[row+2][col+1])
                areaSet.add(self.board[row+2][col+2])

                if len(areaSet) < 9:
                    return False

                areaCol += 1
            areaRow += 1

        return True

    def printBoard(self):
        for row in self.board:
            print(row)