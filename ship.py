class Ship():

    def __init__(self, ship_name, size, player):
        self.ship_name = ship_name
        self.size = size
        self.player = player

    def get_ship_location(self):
        while True:
            ship_location = input('Please place your ' + self.ship_name + '('
                            + str(self.size) + ' spaces--example (A2)): ')
            ship_location_strip = str(ship_location).strip()
            lower_ship_location = str(ship_location_strip.lower())

            if len(lower_ship_location) in range(2,4):
                if lower_ship_location[0] not in 'abcdefghij' or \
                   lower_ship_location[1:] not in '1,2,3,4,5,6,7,8,9,10':
                    print("Oops!  That was not a valid entry.  Try again...")
                    continue

                else:
                    print("Success!")
                    break

            else:
                if len(lower_ship_location) < 2 or len(lower_ship_location) > 3:
                    print("Oops!  That's too not the right amount of characters. Please try again...")
                    continue




