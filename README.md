-----------------------------To run the game-------------------------------
please run the file "driver.py", use command
"python driver.py"

the game will prompt to input size and number of color (I have tested it for size between 2 and 10 , color between 2 and 5)
the game will initialise with a random state based on the user input

the game has option to play
1.manually 2. simple bot 3. an adv bot (slightly better, nothing perfect. but reduced random picking from average 60 steps to 15 step for size 10 and color 5)

the use can also play the game manually step by step
or chose one of the 2 bots

the game shows step by step, the board status, chosen color
also the game saves the steps into a png, "GamePlay.png"
show all the steps till the finish of the game, a primitive way to see the result :)
the png my cause error during run time, this can be corrected by visiting line 15 in driver.py file
"pltRow, pltCol = 7, 7", this only allow 49 images to display.

---

---

------------------------------Test case implementation------------------------------------

----------Unit test - tests a particular fuction code-----
But i have impletemented one unit test case for "advance bot color choosing" - function

to run it use the command "python -m unittest test_getNextColorAdvBot.py"

this has 2 test files impletemented, more test cases can be added just by adding more files "Testx.csv"

-----------Game test - tests the game board code as a system------------
to Run, use the command "python TestCase.py"
this also takes the inputs and the correct output from csv file
hence more tests can be added

this test first sets the board to a particular configuration
then picks a particular color to play and test if the "board" reacts correctly
this is repeated till the game is completed

---

---

------------------------------Future addtions------------------------------------
---test----
I can add unit test for other fuctions, such as "get neightbour", "get boundary" , "switch color"etc
Also I would like to add more system test for the board and bot
-----corner case testing, coverage testing are warranted---

---bot algoritm---
the bot can be improved,
if time complexity is not a concern then i would continue doing the same idea but go deper for 2 levels of
longest chain detection in my bot
to reduce the complexity, then i would try to implemnet a graph based method

-----interface, and graphic output---

---

---

------------------------------Know Bugs------------------------------------
the gameplay.png, changes the color mapping from step to step
the advanced bot, has corner case bugs, not a big error but still bug - this will be testing in the unit test planed for future
