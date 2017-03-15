from .board import Board
from .player import Player
from .ship import Ship

import copy

class Game:

    SHIP_INFO = [
        ("Aircraft Carrier", 5),
        ("Battleship", 4),
        ("Submarine", 3),
        ("Cruiser", 3),
        ("Patrol Boat", 2)
    ]

    BOARD_SIZE = 10

    VERTICAL_SHIP = '|'
    HORIZONTAL_SHIP = '-'
    EMPTY = 'O'
    MISS = '.'
    HIT = '*'
    SUNK = '#'

    def __init__(self):
        pass

    def clear_screen(self):
        print("\n" * 10)
        print("\033c")

    def validate_guess(self,player):
        while True:
            guess = input("Please guess a location {}: ".format(player))
            if guess == "":
                print("Sorry not a valid entry.  Please try again")
                continue
            else:
                guess = guess.strip()
                guess = guess[0].lower() + guess[1:]
                if len(guess) in range(2, 4):
                    if guess[0] not in 'abcdefghij' or guess[1:] not in '1,2,3,4,5,6,7,8,9,10':
                        print("Sorry the Grid is a 10x10 square you must enter a valid position.  Try again...")
                        continue

                    else:
                        return guess

                else:
                    if len(guess) < 2 or len(guess) > 3:
                        print("Oops!  That's too not the right amount of characters. Please try again...")
                        continue

    def check_if_sunk(self,ship):
        if not ship:
            print("YOU SUNK MY BATTLESHIP!!")

    def play_one_win_check(self,player):
        for ship in Board.play_two_board:
            win = 0
            if len(ship) == 0:
                print("{} YOU ARE THE WINNER! CONGRATULATIONS!".format(player))
                win = 1
                return win
                break
            else:
                continue

    def play_two_win_check(self,player):
        for ship in Board.play_one_board:
            if len(ship) == 0:
                print("{} YOU ARE THE WINNER! CONGRATULATIONS!".format(player))
                return True
                break
            else:
                return False
                continue

    def run(self):
        BOARD_SIZE = 10

        """Main Game Loop"""
        # create player instances
        player1 = Player()
        player2 = Player()

        # set grid to be blank
        grid = [['O'] * BOARD_SIZE for _ in range(BOARD_SIZE)]

        # create board instances for each player
        grid1 = Board()
        grid2 = Board()


        # print a blank board
        print("\n" * 3)
        grid1.print_board()

        # loop function to get, create and display player one's ships

        for ship_name, ship_size in Game.SHIP_INFO:
            # create ship instance
            ship1 = Ship(player1, ship_name, ship_size)
            # ask user for starting coordinate for ship in form "A1" and split into x,y variables
            x, y = ship1.split_coordinates(ship_name,player1.player)
            # ask user for ship's position --horizontal or vertical
            direction = ship1.ask_ship_location()
            # create all coordinates for ship based on size of ship and location
            created_coords = ship1.create_ship_coordinates(x, y, ship_size,direction)
            # add coordinates to player's grid
            grid1.play_one_board.append(created_coords)
            # loop through coords for ship to print out on displayed grid
            grid1.print_ship_coordinates(created_coords,direction)

        print("Great work {}!  Now it's time for {} to place their ships!".format(player1.player, player2.player))
        print("\n")

        # print a blank board
        grid2.print_board()

        # loop function to get, create and display player two's ships

        for ship_name, ship_size in Game.SHIP_INFO:
            # create ship instance
            ship2 = Ship(player2, ship_name, ship_size)
            # ask user for starting coordinate for ship in form "A1" and split into x,y variables
            x, y = ship2.split_coordinates(ship_name,player2.player)
            # ask user for ship's position --horizontal or vertical
            direction = ship2.ask_ship_location()
            # create all coordinates for ship based on size of ship and location
            created_coords_2 = ship2.create_ship_coordinates(x, y, ship_size,direction)
            # add coordinates to player's grid
            grid2.play_two_board.append(created_coords_2)
            # loop through coords for ship to print out on displayed grid
            grid2.print_ship_coordinates(created_coords_2, direction)

        print("\n")
        print("AWESOME---ships placed! Thanks {}!  Let's play battleship! Good Luck!".format(player2.player))
        print("\n")

        # creating copies of grid instances these to get ships--will overlap guesses with methods from Board class
        play_one_ships = copy.deepcopy(grid1)
        play_two_ships = copy.deepcopy(grid2)

        # clear each of the users's grids
        grid1.clear_grid()
        grid2.clear_grid()

        guesses = 0

        while True:
            print("\n")
            #print updated guess board before player one takes a guess
            print("{}'s GUESSS BOARD".format(player1.player))
            grid2.print_board()
            print("\n" * 3)

            # get guess from player one in coordinate form (example: a10)
            # validate the guess
            guess = self.validate_guess(player1.player)
            # append the guess to a list for player 1
            player1.guesses.append(guess)
            # break down the coordinates into x and y variables
            x, y = ship1.split_guess(guess)
            # increment guesses
            guesses += 1
            # loop to assess whether, hit, miss or a won game
            if any(guess in ship for ship in grid2.play_two_board):
                print("SWEET That's a HIT")
                print("\n" * 4)
                #print updated guess board to reflect the hit
                grid2.print_guess_board(x, y, "h",player1.player)
                play_two_ships.update_my_ship_board(x,y,"h")
                print("\n" * 3)
                play_one_ships.print_my_ship_board(player1.player)
                print("\n" * 3)
                for ship in grid2.play_two_board:
                    try:
                        # remove correct guesses from list of ships
                        ship.remove(guess)
                        # check if any ships are sunk
                        self.check_if_sunk(ship)
                        # check if player one is winner
                        win = self.play_one_win_check(player1.player)
                        if win == 1:
                            print ("GAVE OVER!")
                            break
                    except ValueError:
                        pass
            else:
                print("\n" * 2)
                print("SORRY THAT's a Miss!")
                print("\n" * 2)
                play_two_ships.update_my_ship_board(x, y, "m")
                # print updated guess board to reflect the miss
                grid2.print_guess_board(x, y, "m",player1.player)
                print("\n" * 2)
                play_one_ships.print_my_ship_board(player1.player)

            print("\n" * 2)
            input("Press Enter to continue...")
            print("\n")

            # print updated guess board before player two takes a guess
            print("{}'s GUESSS BOARD".format(player2.player))
            grid1.print_board()

            print("\n")
            print("\n")

            # get guess from player two in coordinate form (example: a10)
            # validate the guess
            guess2 = self.validate_guess(player2.player)
            # append the guess to a list for player 1
            player2.guesses.append(guess2)
            # break down the coordinates into r and c variables
            r, c = ship2.split_guess(guess2)
            # increment guesses
            guesses += 1
            # loop to assess whether, hit, miss or a won game
            if any(guess2 in ship for ship in grid1.play_one_board):
                print("SWEET That's a HIT")
                print("\n" * 5)
                # print updated guess board to reflect the hit
                grid1.print_guess_board(r, c, "h", player2.player)
                play_one_ships.update_my_ship_board(x, y, "h")
                print("\n" * 3)
                play_two_ships.print_my_ship_board(player2.player)
                for ship in grid1.play_one_board:
                    try:
                        # remove correct guesses from list of ships
                        ship.remove(guess2)
                        # check if any ships are sunk
                        self.check_if_sunk(ship)
                        # check if player two is winner
                        win = self.play_two_win_check(player2.player)
                        if win == 1:
                            print("GAVE OVER!")
                            break
                    except ValueError:
                        pass
            else:
                print("\n" * 2)
                print("SORRY THAT's a Miss!")
                print("\n" * 2)
                play_one_ships.update_my_ship_board(x, y, "m")
                # print updated guess board to reflect the miss
                grid1.print_guess_board(r, c, "m",player2.player)
                print("\n" * 2)
                play_two_ships.print_my_ship_board(player2.player)

            print("\n" * 2)
            input("Press Enter to continue...")
            print("\n")


