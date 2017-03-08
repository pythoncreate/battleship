BOARD_SIZE = 10


SHIP_INFO = [
    ("Aircraft Carrier", 5),
    ("Battleship", 4),
    ("Submarine", 3),
    ("Cruiser", 3),
    ("Patrol Boat", 2)
]

class Ship:

    def __init__(self, ship_name, size, coords, player, direction):
        self.ship_name = ship_name
        self.size = size
        self.player = player
        self.coords = coords
        self.direction = direction

class Board:
    def __init__(self):
        self.board = []
        self.guesses = []

    board = [['O']*BOARD_SIZE for _ in range(BOARD_SIZE)]

    def add_ship(self, name, size, player, coords, direction):
        for coord in coords:
            # convert string like "a1" to x,y coordinates
            y = ord(coord[0])-ord('a')
            x = int(coord[1:])-1
            # update the board at this position
            self.board = board[x][y]
        print("   " + " ".join([chr(c) for c in range(ord('A'), ord('A') + BOARD_SIZE)]))
        row_num = 1
        for row in board:
            print(str(row_num).rjust(2) + " " + (" ".join(row)))
            row_num += 1
        self.board.append(Ship(coords,player,name,size,direction))

    def print_board_heading(self):
        print("   " + " ".join([chr(c) for c in range(ord('A'), ord('A') + BOARD_SIZE)]))

    def print_board(self):
        board = [['O']*BOARD_SIZE for _ in range(BOARD_SIZE)]
        print_board_heading()
        row_num = 1
        for row in board:
            print(str(row_num).rjust(2) + " " + (" ".join(row)))
            row_num += 1



class Player():

    board = [['O']*BOARD_SIZE for _ in range(BOARD_SIZE)]

    def __init__(self,name,board):
        self.name = name
        self.board = board
        self.ships = []
        self.guesses = []

    def ask_ships(self,ship,player):
        self.ship = ship
        self.player=player
        while True:
            print("\n")
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

    def get_direction(self):
        while True:
            dir = input("[H]orizontal or [V]ertical?: ")
            dir_strip = dir.strip()
            direction = dir_strip.lower()

            if direction not in 'hv':
                print("Oops!  That was not a valid entry.  Try again...")
                continue
            else:
                return direction

    def create_ship_coordinates(self, x, y, size, direction):
        board = []
        ship_col = ord(x)
        ship_row = int(y)
        if direction == 'v':
            # ship runs vertically DOWN from coordinate
            coords = [chr(ship_col) + str(r) for r in range(ship_row, ship_row + size)]
            return coords
        else:
            # ship runs horizontally RIGHT from coordinate
            coords = [chr(col) + str(ship_row) for col in range(ship_col, ship_col + size)]
            return coords

    def add_ship_to_player_ships(self, coords):
        self.ships.append(coords)

    def print_updated_board(self,board,coords,direction):
        for coord in coords:
            # convert string like "a1" to x,y coordinates
            y = ord(coord[0])-ord('a')
            x = int(coord[1:])-1
            # update the board at this position
            board[x][y] = '|' if direction == 'v' else '-'
        print("   " + " ".join([chr(c) for c in range(ord('A'), ord('A') + BOARD_SIZE)]))
        row_num = 1
        for row in board:
            print(str(row_num).rjust(2) + " " + (" ".join(row)))
            row_num += 1

class Game():
    board = [['O']*BOARD_SIZE for _ in range(BOARD_SIZE)]
    name1 = input("What is Player 1's name? ")
    name2 = input("What is Player 2's name? ")
    player1 = Player(name1,board)
    player2 = Player(name2,board)
    print("Hi {}! Let's place your ships!".format(name1))
    for ship, size in SHIP_INFO:
        x,y = player1.ask_ships(ship,name1)
        direction = player1.get_direction()
        coords = player1.create_ship_coordinates(x,y,size,direction)
        player1.add_ship_to_player_ships(coords)
        player1.print_updated_board(board,coords,direction)

    print("Great now it's time for Player 2")
    print("Hi {}! Let's place your ships!".format(name2))

    for ship, size in SHIP_INFO:
        coords = []
        x,y = player2.ask_ships(ship,name2)
        direction = player2.get_direction()
        coords = player2.create_ship_coordinates(x,y,size,direction)
        player2.add_ship_to_player_ships(coords)
        player2.print_updated_board(board,coords,direction)

    print("Great thanks {}! Let's play battleship!".format(name2))

    print(player1.ships)
    print(player2.ships)

    battleship = Game()