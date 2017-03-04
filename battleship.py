from ship import Ship, Player

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


def print_board(board):
    print_board_heading()

    row_num = 1
    for row in board:
        print(str(row_num).rjust(2) + " " + (" ".join(row)))
        row_num += 1


def get_coordinates(ship):
    while True:
        coordinate = input("Where do you want the " + ship + "(example: A1)?: ")
        coords_strip = coordinate.strip()
        coords_lower = coords_strip.lower()
        x = coords_lower[0]
        y = coords_lower[1:]

        if (len(x)+len(y)) in range(2,4):
            if x not in 'abcdefghij' or y not in '1,2,3,4,5,6,7,8,9,10':
                print("Oops!  That was not a valid entry.  Try again...")
                continue

            else:
                return x, y

        else:
            if len(coords_lower) < 2 or len(coords_lower) > 3:
                print("Oops!  That's too not the right amount of characters. Please try again...")
                continue


def get_direction():
    while True:
        dir = input("[H]orizontal or [V]ertical?: ")
        dir_strip = dir.strip()
        direction = dir_strip.lower()

        if direction not in 'hv':
            print("Oops!  That was not a valid entry.  Try again...")
            continue

        else:
            return direction


def create_ship_coordinates(x, y, size, direction):
    ship_col = int(y)
    ship_row = ord(x)
    if direction == 'v':
        # ship runs vertically DOWN from coordinate
        coords = [chr(ship_col) + str(r) for r in range(ship_row, ship_row + size)]
        return coords
    else:
        # ship runs horizontally RIGHT from coordinate
        coords = [chr(col) + str(ship_row) for col in range(ship_col, ship_col + size)]
        return coords



def place_user_ships(player):
    ships = []
    for ship, size in SHIP_INFO:
        print_board(board)

        while True:
            print("Placing the " + ship)
            # ask for starting coordinate
            x, y = get_coordinates(ship)
            # ask for vertical or horizontal direction
            direction = get_direction()
            # create the coordinates for the ship placement
            coords = create_ship_coordinates(x, y, size, direction)
            print(coords)
            # validate the placement
            break
        # create ship from data
        ship = Ship(ship, size, coords, direction)
        # add the ship from above to a player list
        # place the ship on the game board
        # print out the board to reflect the shp placement
    clear_screen()
    print("Placing ships for {}:\n".format(player))
    input("All ships placed for {}. Please hit ENTER to continue....".format(player))
    clear_screen()

player1 = input("What's Player 1's Name? ")
player2 = input("What's Player 2's Name? ")

# define player one's fleet
place_user_ships(player1)

