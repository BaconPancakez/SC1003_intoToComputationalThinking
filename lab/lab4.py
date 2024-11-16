board_size = 10
# TODO : 1. Initialize a board_sizexboard_size game board with all cells set to 0 (empty)
# Add you code of TODO 1 here
cells = [[0 for i in range(board_size)]for j in range(board_size)]

# for i in range(0, board_size):
#     row = []
#     for j in range(0, board_size):
#         row.append('0')
#     cells.append(row)

# TODO : 2.While loop to repeatedly ask for valid attack coordinates
# Add you code of TODO 2 here
valid = False
while not valid:
    x = int(input('Enter attack row (0-9): '))
    y = int(input('Enter attack column (0-9): '))
    if (0 <= x < board_size) and (0 <= y < board_size):
        valid = True
        print(f'Coordinates ({x}, {y}) are valid: {valid}')
    else:
        print(f'Coordinates ({x}, {y}) are valid: {valid}')
        print('Pleaase enter again')


# TODO : 3. For loop to iterate through each row and column of the board
# Add you code of TODO 3 here
for i in range(board_size):
    for j in range(board_size):
        cells[x][y] = '1'

for i in range(board_size):
    for j in range(board_size):
        print(cells[i][j], end=' ')
    print('')
