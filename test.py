
board_size = 10
# TODO : 1. Initialize a board_sizexboard_size game board with allncells set to 0 (empty)
# Add you code of TODO 1 here
board = [[0 for i in range(board_size)] for j in range(board_size)]



#4 – Iteration
# TODO : 3. For loop to iterate through each row and column of the board
# Add you code of TODO 3 here
for r in range(board_size):
    for c in range(board_size):
        print(board[r][c], end=" ")
    print() 
