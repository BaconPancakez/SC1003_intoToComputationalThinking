# TODO : 1. There are two players in the game. Initialize their names as string
# Add you code of TODO 1 here

player1 = 'Computer'
player2 = 'User'

# TODO : 2. There are two layers in the sea. Initialize the integer variable layer
# Add you code of TODO 2 here
layer = 2

# TODO : 3. The battleship board is 10 by 10 dimension. Initialize the integer variables
# width and height
# Add you code of TODO 3 here
width, height = 10, 10

# TODO : 4. Initialize a boolean variable that will be used to indicate
# whether user input is valid or not, two boolean variables hit and miss that indicate
# whether the ship is hit or missed
# Add you code of TODO 4 here
valid, hit, miss = False, False, False

# TODO : 5. The ships have only two orientation, either vertical or horizontal.
# Initialize a variable as ship orientation
# Add you code of TODO 5 here
ori = 'v'

# TODO : 6. The coordinates of where to put ship or where to hit on the board have a
# specific format. Create a string variable as coordinates
# Add you code of TODO 6 here
coor = 'A,4,1'
# TODO : 7. There are only two types of ships. Initialize two string variables as ship names
# Add you code of TODO 7 here
ship1 = 'submarine'
ship2 = 'carrier'

# TODO : 8. Initialize a string variable holding a welcome message that can be displayed to user
# Add you code of TODO 8 here
welmes = (f'Welcome to Battleships! Hit ENTER to continue. \n\
Please enter coordinate of the attack center point in following this format (row,col,depth). E.g. {coor} \n\
Note: depth = 0 represents the subsea layer, and depth = 1 represents the surface level.)')

print(player1, player2)
print(layer)
print(width, height)
print(valid, hit, miss)
print(ori)
print(coor)
print(ship1, ship2)
print(welmes)

# TODO : 9. Take user input for attack coordinates and display the result.
# Add you code of TODO 9 here
userinput = input('Enter Coordinates: ')
print(f'Hit at area centering {userinput}')
