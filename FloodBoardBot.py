import matplotlib.pyplot as plt
from matplotlib import colors
import numpy as np
import random


class FloodBoardBot:
    """the game bot is separated as diffent entity
    every gam bot will be attached to a board entity
    the fuctions are the interaction and the calculation done by a bot
    """
    def __init__(self, board):
        self.board = board

    def getNextColor(self):
        """returns the  next color that needs to be chosen
        randomly picks a color, which is not the root color
        primitive method to find next color
        """
        return(random.choice([i for i in range(1, self.board.nColor+1)
                             if i != self.board.panel[0][0]]))

    def getNextColorAdvBot(self, boundary):
        """returns the  next color that needs to be chosen
        checks the neighbours, which has the longest chain
        and compares with all neigbours chain
        finds the maximum, returns the color
        """
        maxConnection = 0
        maxConnectionCell = (0, 0)
        maxConnecitonCellColor = 0
        rootColor = self.board.panel[0][0]
        if self.board.debug is True:
            print("adv bot boundary :", boundary)
        for cell in boundary:
            neighbourofBoundrayCell = self.getNeighbour(cell)
            if self.board.debug is True:
                print("adv bot cell :", cell)
                print("adv bot neighbourofBoundrayCell :",
                      neighbourofBoundrayCell)
            for neighbourCell in neighbourofBoundrayCell:
                if self.board.panel[neighbourCell[0]][neighbourCell[1]] != rootColor:
                    if self.board.debug is True:
                        print("adv bot neighbourCell :", neighbourCell)
                    neighbourCellBoundary = self.getboundary([neighbourCell])
                    if self.board.debug is True:
                        print("adv bot neighbourCellBoundary :",
                              neighbourCellBoundary)

                    if len(neighbourCellBoundary) > maxConnection:
                        if self.board.debug is True:
                            print("adv bot length neighbourCellBoundary :",
                                  len(neighbourCellBoundary))
                        maxConnection = len(neighbourCellBoundary)
                        maxConnectionCell = neighbourCell

        maxConnecitonCellColor = self.board.panel[maxConnectionCell[0]][maxConnectionCell[1]] 

        return(maxConnecitonCellColor)

    def getGameScore(self):
        """returns a int value, representing game status
        when value is 0, the game is completed
        a very primitive impurity check fuction
        """
        result = self.board.nSize*self.board.nSize

        for i in range(0, self.board.nSize):
            for j in range(0, self.board.nSize):
                if self.board.panel[i][j] == self.board.panel[0][0]:
                    result = result-1

        return(result)

    def getNeighbour(self, *xytuple):
        """returns a list of tupeles
        finds the neighbour for th given tuple
        this can be extended if the diagonals need to be 
        described as neigbours in the future
        helper function
        """
        neighbour = []
        currentx = xytuple[0][0]
        currenty = xytuple[0][1]

        neighbourVals = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        for cell in neighbourVals:
            tempNeighbour = (currentx+cell[0], currenty+cell[1])
            if(tempNeighbour[0] > -1 and tempNeighbour[1] > -1 and
               tempNeighbour[0] < self.board.nSize and
               tempNeighbour[1] < self.board.nSize):
                neighbour.append(tempNeighbour)

        return(neighbour)

    def isBoundTuplePresent(self, boundTuplesLst, neighbour):
        """returns true or false, 
        checks if the tuple is present in the given list of tuple
        helper function, this is to make sure only unique tuples are
        added in the getboundary function
        """
        for boundCell in boundTuplesLst:
            if(boundCell == neighbour):
                return(True)

        return (False)

    def getboundary(self, boundry=[(0, 0)]):
        """returns a list of tupes the flooding boundary for the given boundary
        for instance, when the game starts, it returs the indices
        connected with the root, ie. with same color
        iteratevely finds the neighbours and checks if its the
        same color as the root
        """
        boundTuplesLst = boundry
        rootcolor = self.board.panel[boundTuplesLst[0][0]][boundTuplesLst[0][1]]
        for boundCell in boundTuplesLst:
            neighbours = self.getNeighbour(boundCell)

            if self.board.debug is True:
                print("Boundry/root :", boundTuplesLst)
                print("Neighbours:", neighbours)

            for neighbour in neighbours:
                if self.board.debug is True:
                    print("neightbour, color", neighbour,
                          self.board.panel[neighbour[0]][neighbour[1]])
                if self.board.panel[neighbour[0]][neighbour[1]] == rootcolor:
                    if self.board.debug is True:
                        print("same color")
                    if self.isBoundTuplePresent(boundTuplesLst, neighbour) is False:
                        boundTuplesLst.append(neighbour)

        return(boundTuplesLst)
