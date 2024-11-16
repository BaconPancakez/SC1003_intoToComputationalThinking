board_size = 10
# Get the start position for the Carrier
print("Please enter start_position of Carrier in the following format (row,col). E.g. 6,4")
# TODO : 1. Split the string at the comma and convert to a tuple of integers
user_input_c = input("Enter coordinates: ")

# Add you code of TODO 1 here
x_carrier, y_carrier = map(int, user_input_c.split(','))
# Get the start position for the Submarine print("Please enter start_position of Submarine in the following format (row,col). E.g. 6,4")
user_input_s = input("Enter coordinates: ")

# TODO : 2. Split the string at the comma and convert to a tuple of integers
# Add you code of TODO 2 here
x_sub, y_sub = map(int, user_input_s.split(','))

# TODO : 3. Dictionary to store ship details (name, length, and starting coordinates)
# Add you code of TODO 3 here


def createShip(name, length, x, y):
    return {"name": name, "length": length, "coord_x": x, "coord_y": y}


ships = []
name = ('Carrier', 'Submarine')
length = (5, 3)
ships.append(createShip(name[0], length[0], x_carrier, y_carrier))
ships.append(createShip(name[1], length[1], x_sub, y_sub))


# code from lab4
# Initialize a board_size x board_size game board with all cells set to 0 (empty)
cells = [[0 for i in range(board_size)]for j in range(board_size)]


def place_ship(ship_name):
    # TODO : 4.Function to place ships on the board based on their start position and length
    # Add you code of TODO 4 here
    for ship in ships:
        if ship["name"] == ship_name:
            length = ship["length"]
            row = ship["coord_x"]
            col = ship["coord_y"]
            for x in range(length):
                cells[row][col + x] = 'S'


# Place the ships on the board
place_ship("Carrier")
place_ship("Submarine")
# code from lab4

# While loop to repeatedly ask for valid attack coordinates
# code from lab4
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

# For loop to iterate through each row and column of the board
for i in range(board_size):
    for j in range(board_size):
        cells[x][y] = '1'

for i in range(board_size):
    for j in range(board_size):
        print(cells[i][j], end=' ')
    print('')
