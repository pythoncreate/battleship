
class Ship:

    def __init__(self, name, size):
        self.name = name
        self.size = size


class Board:

    def __init__(self, size=10):
        self.size = size
        self.grid = []

    def add_ship(self, ship):
        """Place ship on board"""
        self.grid.[row][col].ship

    def print_board(self):
        print(self.board)

    def validate_ships(self):
        pass

    def clear_board(self):
        pass


class Player:

    def __init__(self,player):
        self.player = player
        self.ships = []

    def store_ships(self,coords):
        ships = []
        ships.append(coords)

    def store_guesss(self,coords):
        self.guesses = []
        guesses.append(coords)
