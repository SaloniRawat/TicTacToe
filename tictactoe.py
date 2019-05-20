# -*- coding: utf-8 -*-
"""
Created on Wed Apr 10 12:14:54 2019

@author: Saloni Rawat
"""

'''row and columns for the board'''
ROWS       = 3
COLUMNS    = 3

''' board pieces for both players'''
PIECE_ONE  = 'x'
PIECE_TWO  = 'o'

'''mapping pieces to the players'''
PIECE_COLOR_MAP = {
    PIECE_ONE  : 'Player 1',
    PIECE_TWO  : 'Player 2',
}

def create_board(rows=ROWS, columns=COLUMNS):
    ''' Creates empty tic tac toe board '''
    board = []
    PIECE_NONE = 0
    for row in range(rows):
        
        board_row = []
        for column in range(columns):
            board_row.append(PIECE_NONE)
            PIECE_NONE +=1
        board.append(board_row)

    return board

def print_board(board):
    ''' Prints tic tac toe board '''
    for row in board:
        for column in row:
            print ('|' + '|'.join(str(column)) + '|', end =""),
        print("")
        
        
def check_full_board (board):
    '''check if the board is full'''
    for row in board:
            for column in row:
                    if column != "x" :
                        if column != "o":
                            return False
    
    return True
    
    
    
def make_move(board, move, piece):
    ''' make a move'''
    '''To identify the row and column from the move, we will divide the 
    move by 3, the quotient will be the row #, and the remainder will be the 
    column #'''
    
    row = move// 3
    column = move%3
    
   # print("Row", row, "Column", column)
    if check_piece(board, row, column):
        board[row][column]= piece
        return True
        
    else:
        print("The square is already occupied");
        return False
        
def find_winner(board):
    ''' Return whether or not the board has a winner '''

    rows    = len(board)
    columns = len(board[0])

    for row in range(rows):
        if check_row(board, row):
            #print("won row", row)
            return board[row][0]
    for col in range(columns):
        if check_column(board, col):
            #print("won col", col)
            return board[0][col]
    
    if check_diagonal1(board):
        return board[0][0]
    
    if check_diagonal2(board):
        return board[0][2]
        
    return None

def check_row(board, row):
    '''checks the squares for a particular row'''
    flag = False
    piece = board[row][0]
    for col in range(0,3):
        if board[row][col]== piece:
            flag = True
        else:
            flag = False
            break;
            
    return flag
  
def check_column(board, col):
    '''checks the squares for a particular column'''
    flag = False
    piece = board[0][col]
    for row in range(0,3):
        if board[row][col]== piece:
            flag = True
        else:
            flag = False
            break;
            
    return flag      

def check_diagonal1(board):
    '''checks the diagnols of the board'''
    flag = False
    piece= board[0][0]
    
    for i in range(3):
        #print(i, board[i][i])
        if board[i][i]== piece:
            flag= True
        else:
            flag= False
            break;

    return flag

def check_diagonal2(board):
    '''checks the other diagonal of the board'''
    flag = False
    piece = board[0][2]
    
    if board[1][1]== piece:
    
        if board[2][0] == piece:
            flag= True
    else:
        flag = False
        
    return flag   
   
    
    
def check_piece(board, row, column):
    ''' returns true or false if the piece is present'''
    
    
    if board[row][column] != "x" :
        if board[row][column] != "o":
            return True;
    else:   
        return False


