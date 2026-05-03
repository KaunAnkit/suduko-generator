from solution_counter import solution_counter

from sudoku_solver import board_filler
from sudoku_solver import number_placer
from sudoku_solver import position_finder


 

def empty_board_generator():

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





        


def generate_full_board():
    
    board = empty_board_generator()
    board_filler(board)
    
    return board




import random

def count_clues(board):
    cnt = 0
    for x in range(9):
        for y in range(9):
            if board[x][y] != -1:
                cnt += 1
    return cnt


def remove_numbers(board):

    choice = int(input("Press (1) Easy (2) Medium (3) Hard: "))

    if choice == 1:
        target_clues = random.randint(36, 45)
    elif choice == 2:
        target_clues = random.randint(30, 35)
    else:
        target_clues = random.randint(22, 28)

    copyboard = [row[:] for row in board]

    while count_clues(copyboard) > target_clues:

        row = random.randint(0, 8)
        col = random.randint(0, 8)

        if copyboard[row][col] == -1:
            continue

        backup = copyboard[row][col]
        copyboard[row][col] = -1


        board_copy = [r[:] for r in copyboard]
        if solution_counter(board_copy) != 1:
            copyboard[row][col] = backup  

    return copyboard






    


    
          
              


