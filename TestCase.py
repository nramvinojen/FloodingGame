import csv
import numpy as np
from FloodBoard import FloodBoard
from FloodBoardBot import FloodBoardBot


class Testcase:

    def __init__(self, testfile):
        self.debug = False

        with open(testfile, 'r') as csvfile:
            raw_data = csv.reader(csvfile, delimiter=',',
                                  quoting=csv.QUOTE_NONNUMERIC)
            csv_data = []
            for row in raw_data:
                csv_data.append(row)

        if self.debug is True:
            print("csv data :", csv_data[:])

        self.size = int(csv_data[0][0])
        self.numColor = int(csv_data[0][1])
        self.steps = csv_data[1]
        self.numSteps = len(csv_data[1])

        if self.debug is True:
            print("size :", self.size)
            print("Steps :", self.steps)
            print("num Steps :", self.numSteps)

        self.matrices = np.zeros((self.numSteps+1, self.size, self.size))
        if self.debug is True:
            print(self.matrices)
        for i in range(2, len(csv_data)):
            self.matrices[i-2][:][:] = \
                np.asarray(csv_data[i]).reshape(self.size, self.size)

        if self.debug is True:
            for matrix in self.matrices:
                print(matrix, "\n")


def main():
    testFile = ["Test1.csv", "Test2.csv", "Test3.csv", "Test4.csv"]
    fileCounter = 0
    for file in testFile:
        print(file)
        gameTest = Testcase(file)

        board = FloodBoard(gameTest.size, gameTest.numColor)
        board.setPanel(gameTest.matrices[0])

        bot1 = FloodBoardBot(board)
        boundary = bot1.getboundary([(0, 0)])

        testPass = True
        for i in range(0, gameTest.numSteps):
            newColor = gameTest.steps[i]
            board.switchcolor(boundary, newColor)
            boundary = bot1.getboundary(boundary)

            if ((board.panel == gameTest.matrices[i+1]).all() is False):
                print("error found")
                print("step, selected color", i, newColor)
                print("\ngame board :\n", board.panel)
                print("\ntest board :\n", gameTest.matrices[i+1])
                testPass = False
                break
        if testPass is True:
            print("Test Passed")

        fileCounter = fileCounter+1
        del gameTest
        del board
        del bot1
        del boundary


if __name__ == "__main__":
    main()
