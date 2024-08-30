board_size = 10
# TODO : 1. Initialize a board_sizexboard_size game board with allncells set to 0 (empty)
# Add you code of TODO 1 here
board = [[0 for i in range(board_size)] for j in range(board_size)]

# TODO : 2.While loop to repeatedly ask for valid attack coordinates
# Add you code of TODO 2 here
valid_input = False
while not valid_input:
    row = int(input(f"Enter attack row (0-{board_size-1}): "))
    col = int(input(f"Enter attack column (0-{board_size-1}): "))
    
    # Validate the coordinates
    if 0 <= row < board_size and 0 <= col < board_size:
        valid_input = True
        print(f"Coordinates ({row}, {col}) are valid: {valid_input}")
        board[row][col] = 1
    else:
        print(f"Coordinates ({row}, {col}) are valid: {valid_input}")
        print("Please enter again")

#4 – Iteration
# TODO : 3. For loop to iterate through each row and column of the board
# Add you code of TODO 3 here
for r in range(board_size):
    for c in range(board_size):
        print(board[r][c], end=" ")
    print() 
