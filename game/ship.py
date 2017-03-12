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

    def split_guess(self, guess):
        guess_strip = guess.strip()
        guess_lower = guess_strip.lower()
        x = guess_lower[0]
        y = guess_lower[1:]
        return x,y

    def split_coordinates(self,ship_name):
        while True:
            print("\n")
            coordinate = input("Where do you want the " + ship_name + "(example: A1)?: ")
            coords_strip = coordinate.strip()
            coords_lower = coords_strip.lower()
            x = coords_lower[0]
            y = coords_lower[1:]

            if (len(x) + len(y)) in range(2, 4):
                if x not in 'abcdefghij' or y not in '1,2,3,4,5,6,7,8,9,10':
                    print("Sorry the Grid is a 10x10 square you must enter a valid position.  Try again...")
                    continue

                else:
                    return x, y

            else:
                if len(coords_lower) < 2 or len(coords_lower) > 3:
                    print("Oops!  That's too not the right amount of characters. Please try again...")
                    continue

    def create_ship_coordinates(self, x, y, ship_size, direction,grid):
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
