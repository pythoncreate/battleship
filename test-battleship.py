from ship import Ship

ships = [
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

#setup a blank board 10x10
board = []
for row in range(10):
    board_row = []
    for j in range(10):
        board_row.append(EMPTY)
    board.append(board_row)


def clear_screen():
    print("\033c", end="")


def print_board_heading():
    print("   " + " ".join([chr(c) for c in range(ord('A'), ord('A') + BOARD_SIZE)]))




print_board(player, board)


def place_user_ships(board, ships):
    for ship, size in ships:
        while True:
            print_board("u", board)
            print ("Placing a ship")


place_user_ships(board,ships)

# MAIN EVENT RIGHT HERE
#
# ASK USER ONE FOR COORDINATES FOR ALL SHIPS
# VALIDATE THAT VIA LOOP THAT ALL PLACEMENT CAN BE MADE
# PRINT THE SHIP ON NEW BOARD_SIZE
# ASK USER TWO FOR COORDINATES
# VALIDATE THAT ALL PLACEMENT CAN BE MADE
# START GAME AND GUESSING
