SHIP_INFO = [
    ("Aircraft Carrier", 5),
    ("Battleship", 4),
    ("Submarine", 3),
    ("Cruiser", 3),
    ("Patrol Boat", 2)
]

BOARD_SIZE = 10

VERTICAL_SHIP = '|'
HORIZONTAL_SHIP = '-'
EMPTY = 'O'
MISS = '.'
HIT = '*'
SUNK = '#'

board=[]
for row in range(10):
    board.append('O'*10)

def clear_screen():
    print("\033c", end="")

def print_board_heading():
    print("   " + " ".join([chr(c) for c in range(ord('A'), ord('A') + BOARD_SIZE)]))

def print_board(board):
    print_board_heading()
    row_num = 1
    for row in board:
        print(str(row_num).rjust(2) + " " + (" ".join(row)))
        row_num += 1

player1 = input("What's Player 1's Name? ")
player2 = input("What's Player 2's Name? ")
print("\n")
print_board(board)
print("\n")

#prompt user one for aircraft carrier coordinates and position

while True:
    aircraft_one = input(player1.title() + " please place your aircraft carrier (5 spaces)"
                                                                 "--example (1E): ")
    air_one_strip = aircraft_one.strip()
    lower_air_one = air_one_strip.lower()
       
    if lower_air_one[0] not in '1234567890' or lower_air_one[1] not in 'abcdefghij':
        print("Oops!  That was not a valid entry.  Try again...")
        continue

    else:
        break

while True:    
    aircraft_one_position = input("Is it Horizontal(Y/N?): ")
    air_one_position_strip = aircraft_one_position.strip()
    lower_air_one_position = air_one_position_strip.lower()

    if lower_air_one_position not in 'ny':
        print("Oops!  That was not a valid entry.  Try again...")
        continue

    else:
        break
   
print("\n")
clear_screen()
print_board(board)

#prompt user one for battleship coordinates and position

while True:
    battleship_one = input(player1.title() + " please place your battleship (4 spaces)"
                                                                 "--example (1E): ")
    battleship_one_strip = battleship_one.strip()
    lower_battleship_one = battleship_one_strip.lower()
        
    if lower_battleship_one[0] not in '1,2,3,4,5,6,7,8,9,10' or lower_battleship_one[1] not in 'abcdefghij':
        print("Oops!  That was not a valid entry.  Try again...")
        continue

    else:
        break

while True:    
    battleship_one_position = input("Is it Horizontal(Y/N?): ")
    battle_one_position = battleship_one_position.strip()
    lower_battleship_one_position = battle_one_position.lower()

    if lower_battleship_one_position not in 'ny':
        print("Oops!  That was not a valid entry.  Try again...")
        continue

    else:
        break


print("\n")
clear_screen()
print_board(board)

# prompt user one for submarine coordinates and position

while True:
    submarine_one = input(player1.title() + " please place your submarine (3 spaces)"
                                                                 "--example (1E): ")
    sub_one_strip = submarine_one.strip()
    lower_submarine_one = sub_one_strip.lower()
        
    if lower_submarine_one[0] not in '1,2,3,4,5,6,7,8,9,10' or lower_submarine_one[1] not in 'abcdefghij':
        print("Oops!  That was not a valid entry.  Try again...")
        continue

    else:
        break

while True:    
    submarine_one_position = input("Is it Horizontal(Y/N?): ")
    sub_one_position = submarine_one_position.strip()
    lower_submarine_one_position = sub_one_position.lower()

    if lower_submarine_one_position not in 'ny':
        print("Oops!  That was not a valid entry.  Try again...")
        continue

    else:
        break


print("\n")
clear_screen()
print_board(board)

# prompt user one for cruiser coordinates and position

while True:
    cruiser_one = input(player1.title() + " please place your cruiser (3 spaces)"
                                                                 "--example (1E): ")
    cruiser_one_strip = cruiser_one.strip()
    lower_cruiser_one = cruiser_one_strip.lower()
        
    if lower_cruiser_one[0] not in '1,2,3,4,5,6,7,8,9,10' or lower_cruiser_one[1] not in 'abcdefghij':
        print("Oops!  That was not a valid entry.  Try again...")
        continue

    else:
        break

while True:    
    cruiser_one_position = input("Is it Horizontal(Y/N?): ")
    cruise_one_position = cruiser_one_position.strip()
    lower_cruiser_one_position = cruise_one_position.lower()

    if lower_cruiser_one_position not in 'ny':
        print("Oops!  That was not a valid entry.  Try again...")
        continue

    else:
        break

print("\n")
clear_screen()
print_board(board)

# prompt user one for patrol boat coordinates and position

while True:
    patrol_one = input(player1.title() + " please place your patrol (2 spaces)"
                                                                 "--example (1E): ")
    patrol_one_strip = patrol_one.strip()
    lower_patrol_one = patrol_one_strip.lower()
        
    if lower_patrol_one[0] not in '1,2,3,4,5,6,7,8,9,10' or lower_patrol_one[1] not in 'abcdefghij':
        print("Oops!  That was not a valid entry.  Try again...")
        continue

    else:
        break

while True:    
    patrol_one_position = input("Is it Horizontal(Y/N?): ")
    pat_one_position = patrol_one_position.strip()
    lower_patrol_one_position = pat_one_position.lower()

    if lower_patrol_one_position not in 'ny':
        print("Oops!  That was not a valid entry.  Try again...")
        continue

    else:
        break


