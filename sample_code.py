SHIP_INFO = [
    ("Aircraft Carrier", 5),
    ("Battleship", 4),
    ("Submarine", 3),
    ("Cruiser", 3),
    ("Patrol Boat", 2)
]

def ask_ship():
    for ship, size in SHIP_INFO:
        while True:
            ask = input("Where do you want the ship?")

            if len(ask) not in range(2, 4):
                print("Sorry the Grid is a 10x10 square you must enter a valid position.  Try again...")
                continue
            else:
                return ask

def overlap():
    if guess in ask:
        print("you hit my ship")
    else:
        print("sorry try again")

# ask_ship()
# guess = input("Guess a location:")
# overlap()

tries = 0
while tries < 6:

    guess = input("Guess a spot on the grid (example A10:")

    if guess == '':  # checking for empty entry
        print("Misfire ey?")
        tries = tries + 1