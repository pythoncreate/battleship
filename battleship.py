from ship import Ship

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

# define player one's fleet

for ship, size in SHIP_INFO:
    ship = Ship(ship, size, coordinates, direction)
    place_fleet(player1)






