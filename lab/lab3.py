# For beginners, all code in a single file without functions
board_size = 10
valid_orientations = ['horizontal', 'vertical']
status = False
# Exercise 1: Basic Conditional Statements
x, y = 5, 8

# TODO : 1. Check if coordinates are within the valid range
# Add you code of TODO 1 here
if (1 <= x <= board_size) and (1 <= y <= board_size):
    status = True
else:
    status = False

print(f'Coordinates ({x}, {y}) are valid: {status}')

# One more example
x, y = 10, -1
# TODO : 2. Check if coordinates are within the valid range
# Copy your code of TODO 1 here to test on x, y = 10, -1
if (1 <= x <= board_size) and (1 <= y <= board_size):
    status = True
else:
    status = False

print(f'Coordinates ({x}, {y}) are valid: {status}')

# Exercise 2: Conditional with Logical Operators

# TODO : 3. Validate user input for coordinates and orientation
# Add you code of TODO 3 here
x, y, orientation = 4, 6, 'horizontal'
if (1 <= x <= board_size) and (1 <= y <= board_size) and orientation in valid_orientations:
    status = True
else:
    status = False

print(f'Coordinates ({x}, {y}, {orientation}) are valid: {status}')

# One more example
x, y, orientation = 11, 3, 'diagonal'
# TODO : 4. Validate user input for coordinates and orientation
# Copy your code of TODO 3 here to test on x, y, orientation = 11, 3, 'diagonal'
if (1 <= x <= board_size) and (1 <= y <= board_size) and orientation in valid_orientations:
    status = True
else:
    status = False

print(f'Coordinates ({x}, {y}, {orientation}) are valid: {status}')

# Exercise 3: Nested Conditionals
# TODO : 5. Validate the placement of a ship
x, y, ship_length, orientation = 3, 5, 4, 'horizontal'
# Add you code of TODO 5 here

if orientation in valid_orientations:
    if orientation == 'horizontal':
        if (1 <= (x + ship_length) <= board_size) and (1 <= y <= board_size):
            status = True
        else:
            status = False
    else:
        if (1 <= (x) <= board_size) and (1 <= (y + ship_length) <= board_size):
            status = True
        else:
            status = False
else:
    status = False

print(f'Coordinates ({x}, {y}, {ship_length}, {
      orientation}) are valid: {status}')

# One more example
x, y, ship_length, orientation = 7, 7, 4, 'vertical'

# TODO : 6. Validate the placement of a ship
# Copy your code of TODO 5 here to test on x, y, ship_length, orientation = 7, 7, 4, 'vertical'
if orientation in valid_orientations:
    if orientation == 'horizontal':
        if (1 <= (x + ship_length) <= board_size) and (1 <= y <= board_size):
            status = True
        else:
            status = False
    else:
        if (1 <= (x) <= board_size) and (1 <= (y + ship_length) <= board_size):
            status = True
        else:
            status = False
else:
    status = False

print(f'Coordinates ({x}, {y}, {ship_length}, {
      orientation}) are valid: {status}')
