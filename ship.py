class Ship():

    def __init__ (self, ship_name, size, player):
        self.ship_name = ship_name
        self.size =size
        self.player = player

    def get_ship_location(self):
        while True:
            ship_location = input(" please place your" + self.ship_name + "("+ self.size + " spaces--example (A2): ")
            ship_location_strip = ship_location.strip()
            lower_ship_location = ship_location_strip.lower()

            if len(lower_ship_location) in (2,3):
                if lower_ship_location[0] not in 'abcdefghij' or lower_ship_location[1:] not in '1,2,3,4,5,6,7,8,9,10':
                    print("Oops!  That was not a valid entry.  Try again...")
                    continue

            else:
                print("Success!")
                break

        else:
            print("Oops!  That's too many characters. Please try again...")

