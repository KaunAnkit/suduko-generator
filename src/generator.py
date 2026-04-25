from solution_counter import check_uniqueness

from sudoku_solver import board_filler
from sudoku_solver import number_placer
from sudoku_solver import position_finder


 

def empty_box_generator():

    # board = [[-1 for x in range(9)]-1 for y in range(9)]

    board = []
    for x in range(9):
        row = [-1]*9
        board.append(row)

    return  board


import random

def random_list_generator():

    list_suf = [1,2,3,4,5,6,7,8,9]
    
    random.shuffle(list_suf)

    return list_suf

def board_gen():

    

    # row_start  = (row // 3) * 3
    # col_start  = (col // 3) * 3

    # empty_box_generator() → creates an empty board 

    # random_list_generator() → creates a shuffled list 1–9 

    # number_placer() → checks validity 

    # board_filler() → backtracking solver 

    # check_uniqueness() → uniqueness checker 
                    
    board = empty_box_generator()

    for x in range(9):
        suffled = random_list_generator()
        for y in range(9):

          
              


