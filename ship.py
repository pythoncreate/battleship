class Ship(object):

    def __init__ (self, name):
        self.name = ship

    def prompt(self,name):
        while True:
            aircraft_one = input(" please place your aircraft carrier (5 spaces)--example (A2): ")
            air_one_strip = aircraft_one.strip()
            lower_air_one = air_one_strip.lower()

            if len(lower_air_one) in (2,3):
                if lower_air_one[0] not in 'abcdefghij' or lower_air_one[1:] not in '1,2,3,4,5,6,7,8,9,10':
                    print("Oops!  That was not a valid entry.  Try again...")
                    continue

            else:
                print("Success!")
                break

        else:
            print("Oops!  That's too many characters. Please try again...")

