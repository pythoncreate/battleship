BOARD_SIZE = 10

class Board:
    play_one_board = []
    play_two_board = []

    def __init__(self):
        self.grid = self.initalize_board()
        self.play_board = [['O']*BOARD_SIZE for _ in range(BOARD_SIZE)]

    def print_board(self):
        print("   " + " ".join([chr(c) for c in range(ord('A'), ord('A') + BOARD_SIZE)]))
        row_num = 1
        for row in self.grid:
            print(str(row_num).rjust(2) + " " + (" ".join(row)))
            row_num += 1

    def initalize_board(self):
        return [['O']*BOARD_SIZE for _ in range(BOARD_SIZE)]

    def clear_grid(self):
        self.grid = [['O']*BOARD_SIZE for _ in range(BOARD_SIZE)]

    def _set_index_coords(self,x,y):
        col = ord(x[0]) - ord('a')
        row = int(y) - 1
        return [col, row]

    def create_grid_markers(self, c, x, y, row, col):
        if c == "m":
            self.grid[row][col] = "."
        elif c == 'h':
            self.grid[row][col] = "*"
        elif c == 's':
            self.grid[row][col] = "!"

    def print_ship_coordinates(self,created_coords,direction):
        # convert string like "a1" to x,y coordinates
        for coord in created_coords:
            y = ord(coord[0]) - ord('a')
            x = int(coord[1:]) - 1
            # update the board at this position
            self.grid[x][y] = '|' if direction == 'v' else '-'
        print("   " + " ".join([chr(c) for c in range(ord('A'), ord('A') + BOARD_SIZE)]))
        row_num = 1
        for row in self.grid:
            print(str(row_num).rjust(2) + " " + (" ".join(row)))
            row_num += 1

    def create_grid_markers_for_my_board(self, c, x, y, row, col):
        if c == "m":
            self.grid[row][col] = "."
        elif c == 'h':
            self.grid[row][col] = "*"
        elif c == 's':
            self.grid[row][col] = "!"

    def update_my_ship_board(self, x, y, c):
        # self.grid= [['O'] * BOARD_SIZE for _ in range(BOARD_SIZE)]
        col, row = self._set_index_coords(x,y)
        self.create_grid_markers_for_my_board(c,x,y,row,col)

    def print_my_ship_board(self,player):
        print("{}'s SHIP BOARD".format(player))
        print("   " + " ".join([chr(c) for c in range(ord('A'), ord('A') + BOARD_SIZE)]))
        row_num = 1
        for row in self.grid:
            print(str(row_num).rjust(2) + " " + (" ".join(row)))
            row_num += 1

    def print_guess_board(self, x, y, c,player):
        # self.grid= [['O'] * BOARD_SIZE for _ in range(BOARD_SIZE)]
        col, row = self._set_index_coords(x,y)
        self.create_grid_markers(c,x,y,row,col)
        print("{}'s GUESS BOARD".format(player))
        print("   " + " ".join([chr(c) for c in range(ord('A'), ord('A') + BOARD_SIZE)]))
        row_num = 1
        for row in self.grid:
            print(str(row_num).rjust(2) + " " + (" ".join(row)))
            row_num += 1

    def verify_empty(self, coords):
        """Verify all coordinates are clear of ships"""
        result = True
        for coord in coords:
            col = ord(coord[0]) - ord('A')
            row = int(coord[1:]) - 1
            return (row, col)
            if self.grid[row][col].ship:
                    result = False
        return result
