# Assignment 5

## Requirements

1. When the application is started, the player may choose to (1) Play a word game, (2) View statistics, or (3) Adjust the game settings.  

    To realize 1, I create a ```MainMenu``` class and 3 methods, i.e., ```MainMenu.playGame()```, ```MainMenu.viewStatistics()```, ```MainMenu.adjustSettings()``` corresponding to the 3 options in 1. When the player choose any option, it will switch to the corresponding scene.

2. When choosing to adjust the game settings, the player (1) may choose for the game to end after a certain number of minutes, from 1 to 5, defaulting to 3, (2) may adjust the size of the square board, between 4(x4) and 8(x8), defaulting to 4, and (3) may adjust the weights of the letters of the alphabet between 1 and 5, defaulting to 1.

    To implement 2, I created a ```Settings``` class. There are 3 instance variables, i.e., ```time_limit``` with defaut value 3, ```board_size``` with defaut value 4, and ```weight[26]```, which is an int array representing the weight from a-z, whose defaut value is 1 for all entries, which means all letters have equal weights. When players choose their own time limit from 1-5, the ```time_limit``` can be changed through ```setTimeLimit()``` , after prompts/options are handled within the GUI. In the same manner, the ```board_size``` from 4-8 and ```weight```1-5 can also be changed by ```setBoardSize()``` and ```setWeight()``` methods.
    
3. When choosing to play a word game, a player will:
    1. Be shown a ’board’ of randomly generated letters.
    2. Be shown a timer counting down the number of minutes available for the game, as set in the settings.
    3. Start with 0 points, which is not required to be displayed during the game.
    4. Until the game timer counts to zero and the game ends:
        1. Enter a unique word made up of two or more letters on the board. The word must contain only letters from the board  that are each adjacent to the next (horizontally, vertically, or diagonally) and a single letter on the board may not be used twice.  The word does not need to be checked against a dictionary (for simplicity, we will assume the player enters only real words that are spelled correctly). or
        2. Choose to re-roll the board at a cost of 5 points.  The board will be re-created in the same way it is generated at the start of each game, replacing each letter. The timer will not be reset or paused.  The player’s score may go into negative values. or
        3. Choose to exit the game early.
    5. At the end of the game, when the timer has run out or the player chooses to exit, the final score for the game will be displayed.
    6. Each word will score 1 point per letter (‘Qu’ will count as 2 letters), and the cost for each board reset will be subtracted.
    7. After the player views the score, they will continue back to the main menu.
    
    To implement i, I created a ```Board``` class, including 2 instance variables. ```Board.cells``` is a two-dimentional string array consisting of all letters randomly generated. ```Board.settings``` is a Setting class. ```Board.generateBoard()``` can generate random letters based on the rules in the requirements(*detailed implementations are not interested in the UML design*). To implement ii, ```Board.showLeftTime()``` can update the ```Board.left_time``` and show the rest time in minutes. ```Game``` is the class to handle more requirements in the game. To implement iii, ```Game.score``` records the points the player get so far. (a) can be implemented in ```Game.calculatePoints()```, which is also used to calculate the points so far and update the ```Game.score``` variable ```Game.words_dict```, which is the dictionary storing the frequency of each word in each game. (b) can be implemented through ```Game.rerollBoard()```, which will reset a new ```board``` and also update the ```score``` as well as ```reset_times```. (c) can be implemented ```Game.exit()``` in the conditions when the program exit(1. time is run out;2. player choose to exit early). v can also implemented in ```Game.exit()```, which will show the ```Game.score```. vi can be implemented in ```Game.calculatePoints()```. vii can be implemented in ```Game.exit()```, after display the score, it returns the ```MainMenu```. So ```MainMenu``` uses Game and vice versa.
    
4. Whenever the board is generated, or re-generated it will meet the following criteria:
    1. The board will consist of a square full of letters.  The square should have the number of letters, both horizontally and vertically, indicated by the size of the square board from the game settings (4x4, 5x5, 6x6, 7x7, or 8x8).  
    2. ⅕ (rounded up) of the letters will be vowels (a,e,i,o,u). ⅘ will be consonants.
    3. The letter Q will be displayed as ‘Qu’ (so that Q never appears alone).  
    4. The location and particular letters should be randomly selected from a distribution of letters reflecting the weights of letters from the settings.  A letter with a weight of 5 should be 5 times as likely to be chosen as a letter with a weight of 1 (assuming both are consonants or both are vowels).  In this way, more common letters can be set to appear more often.
    5. A letter may appear on the board more than once.
    
    All requirments in 4 can be implemented through ```Board.generateBoard()```, the input will be ```Board.setting```. board size and weights can be get through ```setting.getBoardSize()``` and ```setting.getWeight()```. The 5 requirments belong to implementation details which will not be shown in this UML design.
    
5. When choosing to view statistics, the player may view (1) game score statistics, or (2) word statistics.
    
    To implement 5, I create a class ```Statistics```. ```Statistics.showStasMenu()``` can be used to diaplay the menu. Moreover, ```Statistics.displayWordsStats()``` can be used to show (1) and ```Statistics.displayScoreStats()``` can be used to show (2).
    
6. For game score statistics, the player will view the list of scores, in descending order by final game score, displaying:
The final game score
    1. The number of times the board was reset.
    2. The number of words entered in the game.
    3. The player may select any of the game scores from this list to view the settings for that game’s board size, number of minutes, and the highest scoring word played in the game (if multiple words score an equal number of points, the first played will be displayed).

   To implement 6, ```Statistics``` class is created, and ```Statistics.games``` is a game array which includes all historical games. ```Statistics.words_dict``` is a dictionary which includes the frequences of all words in the past. ```Statistics.addGame()``` can add the last game into ```Statistics.games``` array and also update the ```Statistics.words_dict```. Each entry in ```Statistics.games``` has ```Game.getScore()```, ```Game.getResetTimes()```, and , corresponding to i, ii, and iii. ```Game.getBoard().getSettings()``` and ```Game.getHighestScoreWord()``` can implement iii. The ```Statistics.sortFinalScore()``` will return a sorted game array in descending order of ```Game.score```.
   

7. For the word statistics, the player will view the list of words used, starting from the most frequently played, displaying:
    1. The word
    2. The number of times the word has been played, across all games
    
    To implement7, ```Statistics.sortWordFreq()``` is used to sort the ```Statistics.words_dict``` according to the frequences of all words stored in the ```words_dict```, which stores the words's frequency by ```Game.getWordsDict()``` of all Games.  
    
8. The user interface must be intuitive and responsive.

    This is not represented in my design, as it will be handled entirely within the GUI implementation.

9. The performance of the game should be such that students do not experience any considerable lag between their actions and the response of the application.

    This is not represented in my design, as it will be handled entirely within the GUI implementation.

10. For simplicity, you may assume there is a single system running the application.
    
    The UML design just use a single system.

## Relationships

* ```MainMenu``` has an association relationship with ```Settings```, ```Game```, and ```Statistics```.
