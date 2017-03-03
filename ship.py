class Ship():

    def __init__(self, ship_name, size, coordinates, direction):
        self.ship_name = ship_name
        self.size = size
        self.coordinates = coordinates
        self.direction = direction

    def get_ship_coordinates(self):
        while True:
            ship_coords = input('Please place your ' + self.ship_name + '('
                            + str(self.size) + ' spaces--example (A2)): ')
            ship_coords_strip = str(ship_coords).strip()
            coordinates = str(ship_coords_strip.lower())

            if len(coordinates) in range(2,4):
                if coordinates[0] not in 'abcdefghij' or \
                   coordinates[1:] not in '1,2,3,4,5,6,7,8,9,10':
                    print("Oops!  That was not a valid entry.  Try again...")
                    continue

                else:
                    print("Success!")
                    break

            else:
                if len(coordinates) < 2 or len(lower_ship_location) > 3:
                    print("Oops!  That's too not the right amount of characters. Please try again...")
                    continue

    def get_ship_direction(self):
        while True:
            ship_direction = input("Is it Horizontal(Y/N?): ")
            ship_direction_strip = ship_direction.strip()
            lower_ship_direction = ship_direction_strip.lower()

            if lower_ship_direction not in 'ny':
                print("Oops!  That was not a valid entry.  Try again...")
                continue

            else:
                break

    def place_fleet(self, player):
        coord = get_ship_coordinates()
        position = get_ship_direction()
