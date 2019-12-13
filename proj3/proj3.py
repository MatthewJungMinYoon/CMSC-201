# File:    proj3.py
# Author:  Matthew Yoon
# Date:    12/5/2018
# Section: 10
# Email:   matt45@umbc.edu
# Description: This program is a text-based version of Sudoku. The user can play the puzzle
# or see the solved puzzle at the start. The game is won once the user finds the unique
# combination of the digit placements.

#The max and min choices of rows, columns, and numbers that the user can choose and the
#other numbers in between
MAX = 8

MIN = 0

TWO = 1

THREE = 2

FOUR = 3

FIVE = 4

SIX = 5

SEVEN = 6

EIGHT = 7

#Yes or no when asking the user if they want correctness check
YES = "y"

NO = "n"

#An empty space in the puzzle
EMPTY_SPACE = 0

#Solution to use in any function
SOLUTION = []

#Strings for play, save, undo, quit, and solve
PLAY = "p"

SAVE = "s"

SOLVE = "s"

UNDO = "u"

QUIT = "q"

# solvePuzzle() uses recursion to find solution to the puzzle
# Input:        row;     the row that the function is checking
#               col;     the column the function is checking
#               board;   function file that the function is using
# Output        solve;   makes a deep copy of the board and stores it to a lit to use later
def solvePuzzle(row, col, board):
    #make a deep copy of the board for the solution
    solve = list(board)
    #a list of filled numbers in the row and column
    filledRowAndCol = []
    #Base Case
    if(EMPTY_SPACE not in solve):
        return solve

    #Recursive Cases
    if solve[row][col] == EMPTY_SPACE:

        #Goes through the row and appends any present number into filledRowAndCol list
        for i in range(len(solve[row])):
            solve[row][i]
            if solve[row][i] != EMPTY_SPACE:
                filledRowAndCol.append(solve[row][i])
        #Goes through the column and appends any present number into filledRowAndCol list
        for o in range(len(solve)):
            solve[o][col]
            if solve[o][col] != EMPTY_SPACE:
                filledRowAndCol.append(solve[o][col])
        #These conditions find the filled numbers in the nonet and puts them in a list
        #Left nonets going top to bottom
        if row >= MIN and row <= THREE and col >= MIN and col <= THREE:
            filled = nonet(MIN, THREE, MIN, THREE, solve)
        if row >= FOUR and row <= SIX and col >= MIN and col <= THREE:
            filled = nonet(FOUR, SIX, MIN, THREE, solve)
        if row >= SEVEN and row <= MAX and col >= MIN and col <= THREE:
            filled = nonet(SEVEN, MAX, MIN, THREE, solve)
        #Middle nonets going top to bottom
        if row >= MIN and row <= THREE and col >= FOUR and col <= SIX:
            filled = nonet(MIN, THREE, FOUR, SIX, solve)
        if row >= FOUR and row <= SIX and col >= FOUR and col <= SIX:
            filled = nonet(FOUR, SIX, FOUR, SIX, solve)
        if row >= SEVEN and row <= MAX and col >= FOUR and col <= SIX:
            filled = nonet(SEVEN, MAX, FOUR, SIX, solve)
        #Right nonets going top to bottom
        if row >= MIN and row <= THREE and col >= SEVEN and col <= MAX:
            filled = nonet(MIN, THREE, SEVEN, MAX, solve)
        if row >= FOUR and row <= SIX and col >= SEVEN and col <= MAX:
            filled = nonet(FOUR, SIX, SEVEN, MAX, solve)
        if row >= SEVEN and row <= MAX and col >= SEVEN and col <= MAX:
            filled = nonet(SEVEN, MAX, SEVEN, MAX, solve)

        #Goes through 1-9 and compares sees if they are also in the 2 lists of already filled numbers, if not in both lists, set the cell equal to x
        for x in range(MIN + 1, MAX + 1):
            #sets the current cell as x for the answer
            if fineAns(x, filledRowAndCol, filled):
                solve[row][col] = x
            #backtracks if there is no possible answer
            else:
                solve[row][col] = EMPTY_SPACE
                return solvePuzzle(row, col, solve)

    #If the position is not at the end of the row yet
    if col < MAX:
        return solvePuzzle(row, col + 1, solve)
    #If the position has reached the end of a row, move on to the next row
    if col == MAX:
        return solvePuzzle(row + 1, MIN, solve)

# fineAns() sees if a number is in the 2 lists of impossible answers. If there is a good answer, return True, return False if not
# Input:    x; the current number to check
#           filledRowAndCol; the list of impossible numbers in current  row and column
#           filled; list of impossible numbers in current nonet
# Output:   True or False to put in the right answer if True or backtrack if False
def fineAns(x, filledRowAndCol, filled):
    #If the number is not in the lists of impossible answers
    if x not in filledRowAndCol and x not in filled:
        return True
    #If the number is in the list of already filled numbers, return False and move on to the next number
    else:
        return False

# nonet() for loop that goes through each nonet checking if the current number repeats in
#         its nonet
# Input:  minRow; top boundary of the nonet
#         maxRow; bottom boundary of the nonet
#         minCol; left boundary of the nonet
#         maxCol; right boundary of the nonet
#         solved; current board
# Output: i; the number that is missing from the nonet
def nonet(minRow, maxRow, minCol, maxCol, solved):
    solve = solved
    index = minRow
    filled = []
    #Checks the nonet the current cell is in and appends all numbers already in it to the list "filled"
    for i in range(maxCol):
        solve[index][i]
        #If there is a number at the current position
        if solve[index][i] != EMPTY_SPACE:
            filled.append(solve[index][i])
        #Moves on to next row and resets column number
        if i == maxCol and index < maxRow:
            index += 1
            i = 0
    return filled

#playSaveUndoQuit() asks the user if they want to play a number, save, undo, or quit
#Input:             None
#Output:            playerChoice: a string of their choice, returns to the either
#                   correctMove() or regMove() functions
def playSaveUndoQuit():
    #Asks the user if they want to play, save, undo, or quit
    playerChoice = input("play number (p), save (s), undo (u), quit (q): ")
    #Validation checks to make sure they choose a possible options and not some other letter
    while playerChoice != "p" or playerChoice != "s" or playerChoice != "u" or playerChoice != "q":
        print("Choose one of the given options.")
        playerChoice = input("play number (p), save (s), undo (u), quit (q): ")
    return playerChoice

#enterRow() asks the user for the row they want to put their number in
#Input:     none
#Output:    rowChoice; number of the row the user chose
def enterRow():
    #Asks for the row they want to put their number in
    rowChoice = int(input("Enter a row number (1-9): "))
    #Validation checks to make sure it is in the range of the board
    while rowChoice < MIN + 1 or rowChoice > MAX + 1:
        print("Must be between 1-9")
        rowChoice = int(input("Enter a row number (1-9): "))
    return rowChoice

#enterCol () asks user for the column the want to put their number in
#Input:      None
#Output      colChoice; number of the column the user chose
def enterCol():
    #Asks for the col they want to put their number in
    colChoice = int(input("Enter a column number (1-9): "))
    #Validation checks to make sure it is in the range of the board
    while colChoice < MIN + 1 or colChoice > MAX + 1:
        print("Must be between 1-9")
        colChoice = int(input("Enter a column number (1-9): "))
    return colChoice

#enterNum(row, col) asks the user what number they want to put in
#Input:             row; the row they want their number in
#                   col; the column they want their number in
#Output             numChoice; the number the user chose
def enterNum(row, col):
    #Asks for the number they want to put into the chosen cell
    numChoice = int(input("Enter a number to put in cell (", row, ", ", col, "): "))
    #Validation checks to make sure it is between 1-9
    while numChoice < MIN + 1 or numChoice > MAX + 1:
        numChoice = int(input("Enter a number to put in cell (", row, ", ", col, "): "))

#undo(row, col, num, curBoard) undos the last move of the user
#Input:                   row; the row they chose last
#                         col; the column they chose last
#                         curBoard; the current board
#                         num; number that the user put in
#Output:                  newBoard; new board after undoing a move
def undo(row, col, num, curBoard):
    newBoard = list(curBoard)
    #Sets the position they chose before as and empty space
    newBoard[row][column] = EMPTY_SPACE
    print("Removed the ", num, "you played at position (", row, ", ", col, ").")
    return newBoard

# correctMove() correctness chekcing version of the regMove function
#               doesn't allow player to make a move if number doesn't match
#               the one in SOLUTION.
# Input:        board; the board of the puzzle
#               solvedKey: SOLUTION, to compare the player's numbers to
# Output:       playerBoard; a version of the board with player inputs
def correctMove(board, solvedKey):
    playerBoard = list(board)
    flag = False
    while not flag:
        flag = True
        prettyPrint(playerBoard)
        #If they player board matches the solution, they win
        if playerBoard == solvedKey:
            print("You win!")
            flag = True
        #Keeps asking if they want to play, save, undo, or quit each turn
        choose = playSaveUndoQuit()
        #Asks for row, col, and number they want to put in
        if choose == PLAY:
            row = enterRow()
            col = enterCol()
            num = enterNum(row, col)
            #If they space is filled already, doesn't les the user put it in
            if playerBoard[row][col] != EMPTY_SPACE or board[row][col] != EMPTY_SPACE:
                print()
                print("There is already a number there")
                flag = False
            #Correctness checking. If their number doesn't match what is on the solution, tells them it is wrong
            if solvedKey[row][col] != num:
                print()
                print(num, "does not belong in position (", row, ", ", col, ")")
                flag = False
            else:
                playerBoard[row][col] = num
        #Asks what they want to name their file and calls save function
        if choose == SAVE:
            fileSave = input("Enter the filename you want to save to: ")
            savePuzzle(playerBoard, fileSave)
            flag = False
        #Calls undo function if they want to undo
        if choose == UNDO:
            undoBoard = undoMove(row, col, num, playerBoard)
            playerBoard = undoBoard
            flag = False
        #Breaks out of Boolean flag loop and prints final board and goes back to main
        if choose == QUIT:
            print("Good bye! Here is the final board:")
            prettyPrint(playerBoard)
            flag = True
    return None

# regMove() asks what the player wants to do and put in a number if they want to play a
#           a number. Doesn't check correctness
# Input:    board; the board of the puzzle
#           solvedKey; SOLUTION, to compare the players board to and end the function
#           if the user finished the board correctly
# Output:   None
def regMove(board, solvedKey):
    playerBoard = list(board)
    flag = False
    while not flag:
        flag = True
        prettyPrint(playerBoard)
        #Base case: if they player board matches the solution they win and return to main and ends
        if playerBoard == solvedKey:
            print("You win!")
            flag = True
        #Asks if the user wants to play, save, undo, or quit each turn
        choose = playSaveUndoQuit()
        #Asks for row, col, and number if they want to play
        if choose == PLAY:
            row = enterRow()
            col = enterCol()
            num = enterNum(row, col)
            #If there is already a number present at the space, function doesn't let the user put a number in
            if playerBoard[row][col] != EMPTY_SPACE or board[row][col] != EMPTY_SPACE:
                print("There is already a number there.")
                flag = False
            #If the space is empty, sets the cell equal to the number they chose
            else:
                playerBoard[row][col] = num
        #Asks what they want to name their file and calls the save function
        if choose = SAVE:
            fileSave = input("Enter the filename you want to save to: ")
            savePuzzle(playerBoard, fileSave)
            flag = False
        #Calls the undo function if they want to undo
        if choose = UNDO:
            undoBoard = undoMove(row, col, num, playerBoard)
            playerBoard = undoBoard
            flag = False
        #Breaks out of the Boolean flag loop if they want to quit and prints the final board they end with
        if choose = QUIT:
            print("Good bye! Here is the final board: ")
            prettyPrint(playerBoard)
            flag = True
    return None

# prettyPrint() prints the board with row and column labels,
#               and spaces the board out so that it looks nice
# Input:        board;   the square 2d game board (of integers) to print
# Output:       None;    prints the board in a pretty way
def prettyPrint(board):
    # print column headings and top border
    print("\n    1 2 3 | 4 5 6 | 7 8 9 ")
    print("  +-------+-------+-------+")

    for i in range(len(board)):
        # convert "0" cells to underscores  (DEEP COPY!!!)
        boardRow = list(board[i])
        for j in range(len(boardRow)):
            if boardRow[j] == 0:
                boardRow[j] = "_"

        # fill in the row with the numbers from the board
        print( "{} | {} {} {} | {} {} {} | {} {} {} |".format(i + 1,
                boardRow[0], boardRow[1], boardRow[2],
                boardRow[3], boardRow[4], boardRow[5],
                boardRow[6], boardRow[7], boardRow[8]) )

        # the middle and last borders of the board
        if (i + 1) % 3 == 0:
            print("  +-------+-------+-------+")


# savePuzzle() writes the contents a sudoku puzzle out
#              to a file in comma separated format
# Input:       board;    the square 2d puzzle (of integers) to write to a file
#              fileName; the name of the file to use for writing to
def savePuzzle(board, fileName):
    ofp = open(fileName, "w")
    for i in range(len(board)):
        rowStr = ""
        for j in range(len(board[i])):
            rowStr += str(board[i][j]) + ","
        # don't write the last comma to the file
        ofp.write(rowStr[ : len(rowStr)-1] + "\n")
    ofp.close()

# boardList() makes the board into a 2d list of integers
# Input:      chosenFile;    the chosen text file
# Output:     board;   2d list of the file as integers instead of strings
def boardList(chosenFile):
    board = []
    read = chosenFile.readlines()
    chosenFile.close()
    #Strips the file of whitespace and commas
    for i in range(len(read)):
        clean = read[i].strip()
        cleaner = clean.split(",")
        board.append(cleaner)
    #Converts the strings to integers
    index = 0
    while(index < len(board)):
        count = 0
        while(count < len(board[index])):
            int(board[index][count])
            count += 1
        index += 1
    return board

def main():
    #Asks for filename of puzzle user wants
    chooseFile = input("Enter the filename of the puzzle: ")
    #Prints the board
    openFile = open(chooseFile)
    board = boardList(openFile)
    prettyPrint(board)
    #Finds solution and sets it equal to a constant to use to compare player's board as an answer key
    solved = solvePuzzle(MIN, MIN, board)
    SOLUTION = list(solved)
    #Asks if the player wants to play or see solution
    playOrSolve = input("play (p) or solve (s)?: ")
    #Prints the solution if they input "s"
    if playOrSolve == SOLVE:
        prettyPrint(SOLUTION)
    #Asks if they want to play with correctness checking
    else:
        checkCorrect = input("correctness checking? (y/n): ")
        #Runs play function with correctness checking
        if checkCorrect == YES:
            correctMove(board, SOLUTION)
        #Runs play function without correctness checking
        if checkCorrect == NO:
            regMove(board, SOLUTION)
main()
