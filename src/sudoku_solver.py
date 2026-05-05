from utils import random_list_generator


board = [[-1,-1,-1,-1,-1,-1,-1,-1,-1],
         [-1,-1,-1,-1,-1,-1,-1,-1,-1],
         [-1,-1,-1,-1,-1,-1,-1,-1,-1],
         [-1,-1,-1,-1,-1,-1,-1,-1,-1],
         [-1,-1,-1,-1,-1,-1,-1,-1,-1],
         [-1,-1,-1,-1,-1,-1,-1,-1,-1],
         [-1,-1,-1,-1,-1,-1,-1,-1,-1],
         [-1,-1,-1,-1,-1,-1,-1,-1,-1],
         [-1,-1,-1,-1,-1,-1,-1,-1,-1],]

def position_finder(board):

    for x in range(9):
        for y in range(9):
            if  board[x][y] == -1:
                return [x,y]
            

    return None


def number_placer(board,Number,row,col):

    for x in range(9):
        if board[x][col] == Number:
            return False
        
    for y in range(9):
        if board[row][y] == Number:
            return False
        
    row_start  = (row // 3) * 3
    col_start  = (col // 3) * 3

    for x in range(row_start,row_start + 3):
        for y in range(col_start,col_start + 3):

            if board[x][y] == Number:
                return False
            
    return True

def board_filler(board):

    if position_finder(board) == None:
        return True

    row,col = position_finder(board)
    for x in random_list_generator():
        

        value = number_placer(board,x,row,col)
        if value == True:
            board[row][col] = x
            
            value2 = board_filler(board)

            if  value2 == True:
                return True

            if value2 == False:
                board[row][col] = -1
    
    return False
    


board2 = [
    [5, 3, -1, -1, 7, -1, -1, -1, -1],
    [6, -1, -1, 1, 9, 5, -1, -1, -1],
    [-1, 9, 8, -1, -1, -1, -1, 6, -1],
    [8, -1, -1, -1, 6, -1, -1, -1, 3],
    [4, -1, -1, 8, -1, 3, -1, -1, 1],
    [7, -1, -1, -1, 2, -1, -1, -1, 6],
    [-1, 6, -1, -1, -1, -1, 2, 8, -1], 
    [-1, -1, -1, 4, 1, 9, -1, -1, 5],
    [-1, -1, -1, -1, 8, -1, -1, 7, 9]
]

# board_filler(board2)


