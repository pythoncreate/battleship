from game.board import Board
from game.player import Player
from game.ship import Ship
from game.game import Game

from itertools import cycle

SHIP_INFO = [
    ("Aircraft Carrier", 5),
    ("Battleship", 4),
    # ("Submarine", 3),
    # ("Cruiser", 3),
    # ("Patrol Boat", 2)
]

BOARD_SIZE = 10

VERTICAL_SHIP = '|'
HORIZONTAL_SHIP = '-'
EMPTY = 'O'
MISS = '.'
HIT = '*'
SUNK = '#'


#
# def print_board_heading():
#     print("   " + " ".join([chr(c) for c in range(ord('A'), ord('A') + BOARD_SIZE)]))
#
#
# def print_board():
#     board = [['O']*BOARD_SIZE for _ in range(BOARD_SIZE)]
#     print_board_heading()
#     row_num = 1
#     for row in board:
#         print(str(row_num).rjust(2) + " " + (" ".join(row)))
#         row_num += 1
#
# def print_updated_board(coords, direction,board):
#     # create an empty board
#     # board = [['O']*BOARD_SIZE for _ in range(BOARD_SIZE)]
#     # at each coordinate, draw a ship
#
#     for coord in coords:
#         # convert string like "a1" to x,y coordinates
#         y = ord(coord[0])-ord('a')
#         x = int(coord[1:])-1
#         # update the board at this position
#         board[x][y] = '|' if direction == 'v' else '-'
#     print_board_heading()
#     row_num = 1
#     for row in board:
#         print(str(row_num).rjust(2) + " " + (" ".join(row)))
#         row_num += 1
#
#
# def clear_screen():
#     print("\033c", end="")
#
#
# # def get_coordinates(ship):
#     while True:
#         print("\n")
#         coordinate = input("Where do you want the " + ship + "(example: A1)?: ")
#         coords_strip = coordinate.strip()
#         coords_lower = coords_strip.lower()
#         x = coords_lower[0]
#         y = coords_lower[1:]
#
#         if (len(x)+len(y)) in range(2,4):
#             if x not in 'abcdefghij' or y not in '1,2,3,4,5,6,7,8,9,10':
#                 print("Oops!  That was not a valid entry.  Try again...")
#                 continue
#
#             else:
#                 return x, y
#
#         else:
#             if len(coords_lower) < 2 or len(coords_lower) > 3:
#                 print("Oops!  That's too not the right amount of characters. Please try again...")
#                 continue
#
#
# def get_direction():
#     while True:
#         dir = input("[H]orizontal or [V]ertical?: ")
#         dir_strip = dir.strip()
#         direction = dir_strip.lower()
#
#         if direction not in 'hv':
#             print("Oops!  That was not a valid entry.  Try again...")
#             continue
#
#         else:
#             return direction
#
#
# def create_ship_coordinates(x, y, size, direction):
#     ship_col = ord(x)
#     ship_row = int(y)
#     if direction == 'v':
#         # ship runs vertically DOWN from coordinate
#         coords = [chr(ship_col) + str(r) for r in range(ship_row, ship_row + size)]
#         return coords
#     else:
#         # ship runs horizontally RIGHT from coordinate
#         coords = [chr(col) + str(ship_row) for col in range(ship_col, ship_col + size)]
#         return coords
#
#
# def place_user_ships(player):
#     ships = []
#     print_board()
#     print("\n")
#     print("Let's go " + player + " !")
#     for ship, size in SHIP_INFO:
#
#         while True:
#             # ask for starting coordinate
#             x, y = get_coordinates(ship)
#             # ask for vertical or horizontal direction
#             direction = get_direction()
#             # create the coordinates for the ship placement
#             coords = create_ship_coordinates(x, y, size, direction)
#             # validate the
#             # new_ship = Board().add_ship(ship, size, coords, direction, player)
#             # update = Board.print_updated_board(coords,direction,board,player)
#             break
#         # create ship from data
#         # add the ship from above to a player list
#         # player = Player(board)
#         # place the ship on the game board
#         # print out the board to reflect the shp placement
#     clear_screen()
#     print("\n")
#     input("All ships placed for {}. Please hit ENTER to continue....".format(player))
#
# # player1 = input("What's Player 1's Name? ")
# # player2 = input("What's Player 2's Name? ")
#
# # # define player one's fleet
# # place_user_ships(player1)
# # place_user_ships(player2)

#
#
if __name__ == '__main__':
    grid = [['O']*BOARD_SIZE for _ in range(BOARD_SIZE)]
    player1 = Player()
    player2 = Player()
    grid1 = Board()
    grid2 = Board()
    grid1.print_board()
    chris =[]

    for ship_name, ship_size in SHIP_INFO:
        ship1 = Ship(player1,ship_name,ship_size,grid1) #create ship instance
        # ask_coords = ship1.ask_ship_coords(ship_name) #ask user for starting coordinate for ship in form "A1"
        x,y = ship1.split_coordinates(ship_name) #split coordinate from above into x, y variables and check if valid
        direction = ship1.ask_ship_location() # ask for ship's postion --horizontal or vertical
        created_coords = ship1.create_ship_coordinates(x, y, ship_size, direction,grid) # create all coordinates for ship based on size of ship and locatio
        #add coordinates to player's grid
        grid1.board.append(created_coords)
#
        grid1.print_ship_coordinates(created_coords, direction,grid) #loop through coords for ship to print out on displayed grid


    print("Great work {}!  Now it's time for {} to place their ships!".format(player1.player,player2.player))
    print("\n")
    grid = [['O'] * BOARD_SIZE for _ in range(BOARD_SIZE)]
    grid1.print_board()

    for ship_name, ship_size in SHIP_INFO:
        ship2 = Ship(player2,ship_name,ship_size,grid2) #create ship instance
        # ask_coords = ship2.ask_ship_coords(ship_name) #ask user for starting coordinate for ship in form "A1"
        x,y = ship2.split_coordinates(ship_name) #split coordinate from above into x, y variables and check if valid
        direction = ship2.ask_ship_location() # ask for ship's postion --horizontal or vertical
        created_coords = ship2.create_ship_coordinates(x, y, ship_size, direction,grid) # create all coordinates for ship based on size of ship and location
        grid2.board.append(created_coords) #add coords to list to test out --not part of final code
        grid2.print_ship_coordinates(created_coords, direction, grid) #loop through coords for ship to print out on displayed grid

    print("great thanks {}!  Let's play battleship!".format(player2.player))



def check_if_sunk():
    if not ship:
        print("YOU SUNK MY BATTLESHIP!!")

guesses = 0

while len(grid1.board) and len(grid2.board) > 0:
    guess = input("{}'s turn to guess".format(player1.player))
    player1.guesses.append(guess)
    x, y = ship1.split_guess(guess)
    guesses += 1
    if any(guess in ship for ship in grid2.board):
        print("HIT")
        grid1.guess_board(x, y)
        for ship in grid2.board:
            try:
                ship.remove(guess)
                print(grid2.board)
                check_if_sunk()
            except ValueError:
                pass
    else:
        print("Miss!")

    guess2 = input("{}'s turn to guess".format(player2.player))
    player2.guesses.append(guess2)
    x, y = ship2.split_guess(guess2)
    guesses += 1
    if any(guess2 in ship for ship in grid1.board):
        print("HIT")
        grid2.guess_board(x, y)
        for ship in grid1.board:
            try:
                ship.remove(guess2)
                print(grid1.board)
                check_if_sunk()
            except ValueError:
                pass
    else:
        print("Miss!")

else:
    if (len(grid1.board) == 0):
        print("{} YOU ARE THE WINNER! CONGRATULATIONS!".format(player1.player))

    elif (len(grid2.board) == 0):
        print("{} YOU ARE THE WINNER! CONGRATULATIONS!".format(player2.player))
