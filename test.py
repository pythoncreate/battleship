SHIP_INFO = [
    ("Aircraft Carrier", 5),
    ("Battleship", 4),
    ("Submarine", 3),
    ("Cruiser", 3),
    ("Patrol Boat", 2)
]

for ship, size in SHIP_INFO:
    while True:
        coords = input("Where do you want the " + ship + "(example: A1)?: ")
        coords_strip = coords.strip()
        coords_lower = coords_strip.lower()
        x = coords_lower[0]
        y = coords_lower[1:]

        if (len(x)+len(y)) in range(2,4):
            if x not in 'abcdefghij' or y not in '1,2,3,4,5,6,7,8,9,10':
                print("Oops!  That was not a valid entry.  Try again...")
                continue

            else:
                break

        else:
            if len(coords_lower) < 2 or len(coords_lower) > 3:
                print("Oops!  That's too not the right amount of characters. Please try again...")
                continue
