from sudoku_solver import board_filler
from sudoku_solver import position_finder
from sudoku_solver import number_placer
from utils import random_list_generator

def solution_counter(board):

    cnt = 0

    pos = position_finder(board)
    
    if pos == None:
        return 1

    row,col =   pos
    for x in random_list_generator():
        

        value = number_placer(board,x,row,col)
        if value == True:
            board[row][col] = x

            cnt += solution_counter(board)    
            board[row][col] = -1

            if cnt > 1: return cnt
            
            
           
    
    return cnt
    
