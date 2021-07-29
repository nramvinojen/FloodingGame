import matplotlib.pyplot as plt
from matplotlib import colors
import numpy as np
import random
from FloodBoard import FloodBoard
from FloodBoardBot import FloodBoardBot


def main():
    print("\n\n------------Flooding Tiles -the Game-------------")
    userInpPanelSize = input("\nEnter panel size : ")
    userInpColorsize = input("\nEnter number of diffenrt colors in play : ")
    print("\n\nThe Game is starting up...")
    a = FloodBoard(int(userInpPanelSize), int(userInpColorsize))
    pltRow, pltCol = 7, 7
    fig, axes = plt.subplots(nrows=pltRow, ncols=pltCol)
    customcmap = 'GnBu'
    counter = 0

    a.randomColor()
    a.savePanel2File(fig, axes, counter, pltCol, customcmap)
    print("Root color :", a.panel[0][0])
    print("game status :" + str(a.getGameScore()))

    bot1 = FloodBoardBot(a)
    boundary = bot1.getboundary()
    print("boundary :", boundary)
    print("\n")

    player = input("\n1.Bot \n2.User Input  \n3.Advanced Bot \nPlease choose:")

    while(a.getGameScore() != 0):
        counter = counter+1
        rootColor = a.panel[0][0]

        print("counter", counter)
        print("Root color :", rootColor)

        if player == "1":
            newColor = bot1.getNextColor()
        elif player == "2":
            userColorIdx = input("chose color: ")
            newColor = int(userColorIdx)
        elif player == "3":
            newColor = bot1.getNextColorAdvBot(boundary)
        else:
            print("incorrect input")

        a.switchcolor(boundary, newColor)

        print("selected color:", newColor)
        print("game status :" + str(a.getGameScore()))

        a.savePanel2File(fig, axes, counter, pltCol, customcmap)
        boundary = bot1.getboundary()

        print("boundary :", boundary)
        print("\n")


if __name__ == "__main__":
    main()
