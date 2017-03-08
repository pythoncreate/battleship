BOARD_SIZE = 10

class Ship:

    def __init__(self,player,ship_name,ship_size,grid):
        self.player = player
        self.ship_name = ship_name
        self.ship_size = ship_size

    def ask_ship_coords(self,ship_name):
        print("\n")
        coords = input("Place your " + ship_name + ": ")
        return coords

    def ask_ship_location(self):
        direction = input("[H]orizontal or [V]ertical?: ")
        return direction

    def guess_ship(self,guesses,ship):
        location = input("Guess a location: ")
        return location

    def split_coordinates(self, coords):
        while True:
            coord_strip = coords.strip()
            coord_lower = coord_strip.lower()
            x = coord_lower[0]
            y = coord_lower[1:]

            if (len(x) + len(y)) in range(2, 4):
                if x not in 'abcdefghij' or y not in '1,2,3,4,5,6,7,8,9,10':
                    print("Oops!  That was not a valid entry.  Try again...")
                    continue

                else:
                    return x, y

            else:
                if len(coord_lower) < 2 or len(coord_lower) > 3:
                    print("Oops!  That's too not the right amount of characters. Please try again...")
                    continue

    def create_ship_coordinates(self, x, y, ship_size, direction):
        grid = []
        ship_col = ord(x)
        ship_row = int(y)
        if direction == 'v':
            # ship runs vertically DOWN from coordinate
            coords = [chr(ship_col) + str(r) for r in range(ship_row, ship_row + ship_size)]
            return coords
        else:
            # ship runs horizontally RIGHT from coordinate
            coords = [chr(col) + str(ship_row) for col in range(ship_col, ship_col + ship_size)]
            return coords
