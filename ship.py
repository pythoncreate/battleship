BOARD_SIZE = 10

class Ship:

    def __init__(self, ship_name, size, coordinates, direction):
        self.ship_name = ship_name
        self.size = size
        self.coordinates = coordinates
        self.direction = direction


class Board:

    def __init__(self, board):
        self.size = size
        self.board = board

    def print_board_heading(self):
        print("   " + " ".join([chr(c) for c in range(ord('A'), ord('A') + BOARD_SIZE)]))


    def print_board(self):
        board = [['O']*BOARD_SIZE for _ in range(BOARD_SIZE)]
        print_board_heading()
        row_num = 1
        for row in board:
            print(str(row_num).rjust(2) + " " + (" ".join(row)))
            row_num += 1

    def print_updated_board(self, coords, direction, board):
        # create an empty board
        # board = [['O']*BOARD_SIZE for _ in range(BOARD_SIZE)]
        # at each coordinate, draw a ship
        board = []
        for coord in coords:
            # convert string like "a1" to x,y coordinates
            y = ord(coord[0])-ord('a')
            x = int(coord[1:])-1
            # update the board at this position
            board[x][y] = '|' if direction == 'v' else '-'
        print_board_heading()
        row_num = 1
        for row in board:
            print(str(row_num).rjust(2) + " " + (" ".join(row)))
            row_num += 1





class Player:

    def __init__(self, name):
        """Define player's name, board, ships, guesses"""
        self.name = name
        # create dict of player's ships
        self.board = Board()
        self.ships = []
        self.guesses = []

    def add_ship(self, ship):
        """add ship to current list of ships"""
        self.ships.append(ship)




    # def place_ship(self, x, y, size, dir_lower):
    #     ship_col = x
    #     ship_row = y
    #     if dir_lower == 'v':
    #         # ship runs vertically DOWN from coordinate
    #         placement = [chr(ship_col) + str(row) for row in range(ship_row, ship_row + size)]
    #         print(placement)
    #     else:
    #         # ship runs horizontally RIGHT from coordinate
    #         placement = [chr(col) + str(ship_row) for col in range(ship_col, ship_col + size)]
    #         print(placement)


    def update_board(self, coords, direction):
        if direction == 'v':
             print_board_heading()
             row_num = 1
             for row in board:
                print(str(row_num).rjust(2) + " " + (" ".join(row)))
                row_num += 1


    # def get_ship_coordinates(self):
    #     while True:
    #         ship_coords = input('Please place your ' + self.ship_name + '('
    #                         + str(self.size) + ' spaces--example (A2)): ')
    #         ship_coords_strip = str(ship_coords).strip()
    #         coordinates = str(ship_coords_strip.lower())
    #
    #         if len(coordinates) in range(2,4):
    #             if coordinates[0] not in 'abcdefghij' or \
    #                coordinates[1:] not in '1,2,3,4,5,6,7,8,9,10':
    #                 print("Oops!  That was not a valid entry.  Try again...")
    #                 continue
    #
    #             else:
    #                 print("Success!")
    #                 break
    #
    #         else:
    #             if len(coordinates) < 2 or len(lower_ship_location) > 3:
    #                 print("Oops!  That's too not the right amount of characters. Please try again...")
    #                 continue
    #
    # def get_ship_direction(self):
    #     while True:
    #         ship_direction = input("Is it Horizontal(Y/N?): ")
    #         ship_direction_strip = ship_direction.strip()
    #         lower_ship_direction = ship_direction_strip.lower()
    #
    #         if lower_ship_direction not in 'ny':
    #             print("Oops!  That was not a valid entry.  Try again...")
    #             continue
    #
    #         else:
    #             break
    #
    # def place_fleet(self, player):
    #     coord = get_ship_coordinates()
    #     position = get_ship_direction()
