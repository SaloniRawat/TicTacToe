# -*- coding: utf-8 -*-
"""
Created on Wed Apr 10 12:47:09 2019

@author: Saloni Rawat
"""

from numpy import random
import tictactoe


gameBoard = tictactoe.create_board()
tictactoe.print_board(gameBoard)
Players = (tictactoe.PIECE_ONE, tictactoe.PIECE_TWO)

def HumanPlayer(board, history, players):
    ''' Read move from human player '''
    moves = 9
    move  = -1
 

    while move not in range(0, moves):
        move = int(input('Which square? '))
        print()
        print()        
        #Handle the exception
        '''check if the value is in range'''
        if move not in range(0, moves):
            print ("invalid value")
        else: 
            break;

    return move


def ComputerPlayer(board, history, players):
    '''selects random move for the computer'''
    move = random.randint(0,8)
    flag = False
    
    
    
    while not flag:
        row = move// 3
        column = move%3  
        if tictactoe.check_piece(board, row, column):
            #print("Move", move)
            return move
        else:
            move = random.randint(0,8)
            
    return move
        



