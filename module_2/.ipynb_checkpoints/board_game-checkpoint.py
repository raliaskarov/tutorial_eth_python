import numpy as np
import matplotlib as plt
import os

# game
board = np.array([[3, 4, 8], [7, ' ', 5], [2, 1, 6]],str)
"""
target output
     C 1 2 3
   R  ------
   1 | 3 4 8 
   2 | 7 0 5 
   3 | 2 1 6 
"""
def output(v):
    print("  C 1 2 3")
    print("R  -------")
    for i in range (0,3):
        print(i+1, "|", end = " ")
        for j in range (0,3):
            print(v[i][j], end=" ")
        print()
def locate_value(matrix, value):
    v = str(value)
    coord  = np.where(matrix == v )
    i, j = coord[0][0], coord[1][0]
    return i, j
def adjacent(p, q):
    return abs(p[0]-q[0]) + abs(p[1]-q[1]) == 1

def board_game(board):


    # user selects tile to move 
    input_number_to_move = input('Number to move: ')
    
    # find coordinates
    coord_of_number_to_move = locate_value(board, input_number_to_move)
    coord_blank = locate_value(matrix=board, value=" ")
    
    # move
    if adjacent(coord_of_number_to_move, coord_blank):
        board[coord_blank] = board[coord_of_number_to_move]
        board[coord_of_number_to_move] = " "
    else:
        print("Only tiles adjacent to blank can be moved\n\n")
    
    # show board
    output(board)

# initial board
board = np.array([[3, 4, 8], [7, ' ', 5], [2, 1, 6]],str)

# display initial board
output(board)
attempts = int(input("Provide number of attempts: "))


for i in range(attempts):
    board_game(board)
    print(f"Remaining steps: {(attempts-1-i)}")
print("Game Over!")