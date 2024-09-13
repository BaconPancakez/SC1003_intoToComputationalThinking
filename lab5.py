#SC1003 - Week 6 Lab

board_size = 10
# Get the start position for the Carrier
print("Please enter start_position of Carrier in the following format (row,col). E.g. 6,4")

user_input_c = input("Enter coordinates: ") 
# TODO : 1. Split the string at the comma and convert to a tuple of integers
# Add you code of TODO 1 here
valid_input = False
while valid_input == False:
    array_c = user_input_c.split(',')
    if(len(array_c)==2):
        try:
            row_c = int(array_c[0])
            col_c = int(array_c[1])
            print(f"Carrier - Row: {row_c}, Column: {col_c}")
            valid_input = True
        except ValueError:
            print("Invalid input! Try again")
            user_input_c = input("Enter coordinates: ") 

    else:
        print("Invalid input! Try again")
        user_input_c = input("Enter coordinates: ") 

# Get the start position for the Submarine
print("Please enter start_position of Submarine in the following format (row,col). E.g. 6,4")
user_input_s = input("Enter coordinates: ")

# TODO : 2. Split the string at the comma and convert to a tuple of integers
# Add you code of TODO 2 here
valid_input = False
while valid_input == False:
    array= user_input_s.split(',')
    if(len(array)==2):
        try:
            row_s = int(array[0])
            col_s = int(array[1])
            print(f"Submarine - Row: {row_s}, Column: {col_s}")
            valid_input = True
        except ValueError:
            print("Invalid input! Try again")
            user_input_c = input("Enter coordinates: ") 

    else:
        print("Invalid input! Try again")
        user_input_s = input("Enter coordinates: ") 


# TODO : 3. Dictionary to store ship details (name, length, and starting coordinates)
# Add you code of TODO 3 here
# Function to create a ship and add it to the ships list
def create_ship(name, length, row, col):
    return {"name": name, "length": length, "coord_x": row, "coord_y": col}
name = ("Submarine","Carrier")
size = (3,4)
ships = []
ships.append(create_ship(name[0], size[0], row_s, col_s))
ships.append(create_ship(name[1], size[1], row_c, col_c))

#print(ships)

#code from lab4
# Initialize a board_size x board_size game board with all cells set to 0 (empty)
board = [[0 for i in range(board_size)] for j in range(board_size)]
def place_ship(ship_name):
    for ship in ships:
        if ship["name"] == ship_name:
            length = ship["length"]
            row = ship["coord_x"]
            col = ship["coord_y"]
            if col + length <= board_size:
                for i in range(length):
                    board[row][col+i] = ship_name[0]
            else:
                print(f"{ship_name} unable to placed at the given position")
            
# TODO : 4.Function to place ships on the board based on their start position and length
# Add you code of TODO 4 here
# Place the ships on the board
place_ship("Carrier")
place_ship("Submarine")
#code from lab4

# While loop to repeatedly ask for valid attack coordinates
#code from lab4
valid_input = False
while valid_input == False:
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

# For loop to iterate through each row and column of the board
for r in range(board_size):
    for c in range(board_size):
        print(board[r][c], end=" ")
    print() 
