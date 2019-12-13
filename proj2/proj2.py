#File: proj2.py
#Author: Matthew Yoon
#Section: 10
#Date: 11/6/2018
#Email: matt45@umbc.edu
#Description: play connect 4 with a computer or 2 players.

from random import randint, seed
seed(100)

#minimun value for width and height
MIN_VAL = 5


#asks for what column to put in
def choose(put):
    place = int(input("Enter a column to place your piece in (1 - " + str(put) + "): "))
    return place

#makes the board
def board(width, height):
    build = []
    high = height
    wide = width
    count = 0
    index = 0
    symbol = "_"
    while count < high:
        build.append([])
        index = 0
        while index < wide:
            build[count].append(symbol)
            index += 1
        count += 1
    return build

#checks for win conditions
def win(board):
    win = False
    index = 0
    height = len(board) - 1
    width = len(board[index]) - 1
    while index < height - 3:
        count = 0
        #checking veritcally
        while count < width:
            if board[index][count] != "_":
                if board[index][count] == board[index + 1][count]:
                    if board[index][count] == board[index + 2][count]:
                        if board[index][count] == board[index + 3][count]:
                            win = True
                            return win
            index += 1
            count += 1
    index = 0
    while index < height:
        count = 0
        #checking horizontally
        while count < width - 3:
            if board[index][count] != "_":
                if board[index][count] == board[index][count + 1]:
                    if board[index][count] == board[index][count + 2]:
                        if board[index][count] == board[index][count + 3]:
                            win = True
                            return win
            index += 1
            count += 1
    index = 0
    while  index < height - 3:
        count = 0
        #check diagonally from top left
        while count < width - 3:
            if board[index][count] != "_":
                if board[index][count] == board[index + 1][count + 1]:
                    if board[index][count] == board[index + 2][count + 2]:
                        if board[index][count] == board[index + 3][count + 3]:
                            win = True
                            return win
            index += 1
            count += 1

    index = 0
    while index < height - 3:
        count = 3
        #check diagnolly from top right
        while count < width:
            if board[index][count] != "_":
                if board[index][count] == board[index + 1][count + 1]:
                    if board[index][count] == board[index + 2][count + 2]:
                        if board[index][count] == board[index + 3][count + 3]:
                            win = True
                            return win
            count += 1
            index += 1


#prints the board
def printBoard(create, row, column):
    count = 0
    while count < column:
        index = 0
        while index < row:
            print(create[count][index], end = " ")
            index +=1
        count += 1
        print()
#puts the piece in the column
def moveBoard(board, column, row, piece, choice):
    playerChoice = choice - 1
    index = column - 1
    while index >= 0:
        #if the space is open, put the piece in
        if board[index][playerChoice] == "_":
            board[index][playerChoice] = piece
            return board
        else:
            index -= 1

#gets a random column and puts it in if there is space
def compBoard(board, column, row, compChoice):
    print("its the computer's turn")
    choice = compChoice - 1
    print("The computer chose column: ", compChoice)
    index = column - 1
    while index >= 0:
    #if the space is open, put it in
        if board[index][choice] == "_":
            board[index][choice] = "O"
            return board
        else:
            index -= 1

def main():
    flag = False
    while not flag:
        flag = True
        #asks for the size of the board
        width = int(input("Width: "))
        height = int(input("Height: "))
        #board must be at least 5x5
        if(width < MIN_VAL or height < MIN_VAL):
            print("Width and height must be at least 5")
            flag = False

    playComp = input("Play against the computer? (y/n): ")
    while(playComp != "y" and playComp != "n"):
        print("Answer y or n")
        playComp = input("Play against the computer? (y/n): ")

    #prints the empty board
    make = board(width, height)
    printBoard(make, width, height)

    flagFirst = False
    while not flagFirst:
        flagFirst = True
        #player 1 choice
        print("Player 1 what is your choice?")
        play = choose(width)
        while(play < 1 or play > width):
            print("Choose again.")
            play = choose(width)
        #if the top of the column is full, the whole column must be full
        if(make[0][play - 1] != "_"):
            print("Column is full, choose another.")
            flagFirst = False
        #if the bottom of the column is filled, but the top is open
        else:
            newBoard = moveBoard(make, height, width, "X", play)
            make = newBoard
        printBoard(make, width, height)
        winner = win(make)
        if winner == True:
            print("Player 1 won.")
            flagFirst = True
        else:
            #if playing against a comp
            if(playComp == "y"):
                compChose = randint(0, width)
                while make[0][compChose - 1] != "_":
                    compChose = randint(0, width)
                compTurn = compBoard(make, height, width, compChose)
                make = compTurn
                printBoard(make, width, height)
                winComp = win(make)
                if winComp == True:
                    print("The computer won.")
                    flagFisrt = True
                else:
                    flagFirst = False

            #if playing against another player
            if(playComp == "n"):
                flagSec = False
                while not flagSec:
                    flagSec = True
                    print("Player 2 what is your choice?")
                    play2 = choose(width)
                    while(play2 < 1 or play2 > width):
                        print("Choose again.")
                        play2 = choose(width)
                    #if the top of the column is full, the whole column must be full
                    if(make[0][play2 - 1] != "_"):
                        print("Column is full, choose another.")
                        flagSec = False
                    #if the bottom of the column is filled, but the top is open
                    else:
                        newBoard = moveBoard(make, height, width, "O", play2)
                        make = newBoard
                        printBoard(make, width, height)
                        winSecond = win(make)
                        if winSecond == True:
                            print("Player 2 won.")
                            flagFirst = True
                        else:
                            flagFirst = False

    if flagFirst == True:
        playAgain = input("Would you like to play again? (y/n): ")
        if playAgain == "y":
            flag = False
        else:
            print("ok")
main()
