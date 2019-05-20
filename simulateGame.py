# -*- coding: utf-8 -*-
"""
Created on Wed Apr 10 12:22:40 2019

@author: Saloni Rawat
"""

import tictactoe
import gamePlay

Players = (tictactoe.PIECE_ONE, tictactoe.PIECE_TWO)
History = []
Board   = tictactoe.create_board()
Winner  = None
Tries   = 0
Draw = None


def writeToFile():
    '''write history to file'''
    f = open("history.txt", "w")
    for i in History:
        f.write(str(i))
    f.close
    
    
# Game Loop
'''choose vs Player or vs Computer''' 
Mode = input("Do you want to play against another (P)layer or against the (C)omputer: ")
#print("mode", Mode)

'''if no valid choice is made, default is vs player'''
if Mode == "C" or Mode == "P":
    History.append(Mode)
else:
    print ("Invalid mode. Default player vs player")
    Mode = "P"
    History.append(Mode)
    
'''game continues till a winner is found or a draw'''
while not Winner and not Draw:
    turn = len(History) - 1
    #print(turn)
    if turn % 2 == 0:
        print ("Player 1 turn")
        move = gamePlay.HumanPlayer(Board, History, Players)   # Player One
        
        #drop piece to column
        
    else:
        print("Player 2 turn")
        #print ("move", move)
        #connect4.print_board(Board)
        if Mode == "C":
            move = gamePlay.ComputerPlayer(Board, History, Players )
        elif Mode == "P":
            move = gamePlay.HumanPlayer(Board, History, Players)  # Player Two

    #1print ("Piece", Players[turn % 2])
    '''check if the move is valid and add to the history'''
    if tictactoe.make_move(Board, move, Players[turn % 2]):
       # print ("drop piece")
        Tries = 0
        History.append(move)
        
    '''if players makes more than 3 invalid moves, the game is stuck'''
    if Tries > 3:
        print ('Player {} is stuck!'.format((turn % 2) + 1))
        break

    
    '''prints the updated board'''
    tictactoe.print_board(Board)
    print()
    print()

    '''check for winner after the move'''
    Winner = tictactoe.find_winner(Board)
    
    '''checks for a draw board'''
    Draw = tictactoe.check_full_board(Board)
    #print (Winner)
 
if Winner:
    print ('The Winner is {}'.format(tictactoe.PIECE_COLOR_MAP[Winner]))
elif Draw:
    print('It is a draw')

writeToFile()
