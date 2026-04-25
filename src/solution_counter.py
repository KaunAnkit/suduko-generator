from sudoku_solver import board_filler
from sudoku_solver import position_finder
from sudoku_solver import number_placer

def solution_counter(board):
    
    if solution_counter(board) > 1:
        return True

    row,col = position_finder(board)
    for x in range(1,10):
        

        value = number_placer(board,x,row,col)
        if value == True:
            board[row][col] = x
            
            value2 = board_filler(board)

            if  value2 == True:
                cnt = cnt + 1
                board[row][col] = -1

            if value2 == False:
                board[row][col] = -1
    
    return cnt
    
