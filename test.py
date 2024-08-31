board_size = 10
# TODO : 1. Initialize a board_sizexboard_size game board with allncells set to 0 (empty)
# Add you code of TODO 1 here
board = [[0 for i in range(board_size)] for j in range(3)]
print(board)
for r in range(3):
    for c in range(board_size):
        print(board[r][c], end=" ")
    print() 
