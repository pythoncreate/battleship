BOARD_SIZE = 10

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

    def print_updated_board(coords, direction, board, player):
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


class Player():
    def __init__(self,name):
        self.name = name
        self.board = Board()
        self.ships = []
        self.guesses = []
