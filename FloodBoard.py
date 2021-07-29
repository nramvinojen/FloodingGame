import matplotlib.pyplot as plt
from matplotlib import colors
import numpy as np
import random


class FloodBoard:
    """the game board is separated as diffent entity
    every game bot will be attached to a board entity
    the fuctions are the interaction and the calculation done by a game
    """
    def __init__(self, nSize, nColor):
        """initialise the board with size """
        self.nSize = nSize
        self.nColor = nColor
        self.panel = np.full((self.nSize, self.nSize), 0)
        self.debug = False

    def sameColor(self, color):
        """primitive function to set the board to same color """
        for i in range(0, self.nSize):
            for j in range(0, self.nSize):
                self.panel[i][j] = color

    def randomColor(self):
        """function to set the board to random state """
        for i in range(0, self.nSize):
            for j in range(0, self.nSize):
                self.panel[i][j] = random.randint(1, self.nColor)

    def setPanel(self, matrix):
        """function to set the board to given state """
        self.panel = matrix

    def setPanelVal(self, row, col, coloridx):
        """function to set individual board points to given color"""
        self.panel[row][col] = coloridx

    def savePanel2File(self, fig, axes, count, figCol, customcmap):
        """function to save individual steps in a image """
        print(self.panel)
        plt.setp(axes, xticks=range(0, self.nSize),
                 yticks=range(0, self.nSize))

        pltRow = int((count)/figCol)
        plotCol = (count) % figCol
        axes[pltRow, plotCol].imshow(self.panel, cmap=customcmap)
        plt.savefig('GamePlay.png')

    def getGameScore(self):
        """returns a int value, representing game status
        when value is 0, the game is completed
        a very primitive impurity check fuction,
        """
        result = self.nSize*self.nSize

        for i in range(0, self.nSize):
            for j in range(0, self.nSize):
                if self.panel[i][j] == self.panel[0][0]:
                    result = result-1

        return(result)

    def switchcolor(self, boundary, colorIdx):
        """the basic function of the game, to flood the board with a given color
        """
        for boundCell in boundary:
            self.panel[boundCell[0]][boundCell[1]] = colorIdx
