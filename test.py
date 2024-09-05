board_size = 5
a = 2
board = [[0 for i in range(board_size)] for j in range(a)]
for r in range(a):
    for c in range(board_size):
        print(board[r][c], end=" ")
    print() 

board[1][1] = 1
print("\n")

for r in range(a):
    for c in range(board_size):
        print(board[r][c], end=" ")
    print() 