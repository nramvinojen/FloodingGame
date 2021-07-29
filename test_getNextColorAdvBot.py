import unittest
from FloodBoardBot import FloodBoardBot
from FloodBoard import FloodBoard
import numpy as np
import csv


class test_getnextColorAdvBot(unittest.TestCase):
    """checks the advnced bot, asserts a board situation
    and expects the correct color choice from the bot
    """
    def read_testFile(self, testfile):
        with open(testfile, 'r') as csvfile:
            raw_data = csv.reader(csvfile, delimiter=',',
                                  quoting=csv.QUOTE_NONNUMERIC)
            csv_data = []
            for row in raw_data:
                csv_data.append(row)

        self.size = int(csv_data[0][0])
        self.correctColor = int(csv_data[1][0])

        self.matrices = np.asarray(csv_data[2]).reshape(self.size, self.size)

    def test_getnextColorAdvBot(self):
        testFile = ["Test5.csv", "Test6.csv"]

        fileCounter = 0
        for file in testFile:
            print("Sub test:", fileCounter, file)
            self.read_testFile(file)
            board = FloodBoard(self.size, self.size)
            bot1 = FloodBoardBot(board)

            board.setPanel(self.matrices)
            print(self.matrices)
            boundary = bot1.getboundary([(0, 0)])
            self.assertEqual(bot1.getNextColorAdvBot(boundary),
                             self.correctColor)
            self.assertNotEqual(bot1.getNextColorAdvBot(boundary),
                                self.correctColor+1)

            del board
            del bot1
            del boundary
            fileCounter = fileCounter+1
