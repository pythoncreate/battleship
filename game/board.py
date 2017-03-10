BOARD_SIZE = 10

class Board:
    board = []

    def __init__(self, grid):
        self.grid = [['O']*BOARD_SIZE for _ in range(BOARD_SIZE)]

    def print_board(self):
        print("   " + " ".join([chr(c) for c in range(ord('A'), ord('A') + BOARD_SIZE)]))
        row_num = 1
        for row in self.grid:
            print(str(row_num).rjust(2) + " " + (" ".join(row)))
            row_num += 1

    def print_ship_coordinates(self,created_coords,direction,grid):
        self.grid = []
        # convert string like "a1" to x,y coordinates
        for coord in created_coords:
            y = ord(coord[0]) - ord('a')
            x = int(coord[1:]) - 1
            # update the board at this position
            grid[x][y] = '|' if direction == 'v' else '-'
        print("   " + " ".join([chr(c) for c in range(ord('A'), ord('A') + BOARD_SIZE)]))
        row_num = 1
        for row in grid:
            print(str(row_num).rjust(2) + " " + (" ".join(row)))
            row_num += 1

    def verify_empty(self, coords):
        """Verify all coordinates are clear of ships"""
        result = True
        for coord in coords:
            col = ord(coord[0]) - ord('A')
            row = int(coord[1:]) - 1
            return (row, col)
            if grid[row][col].ship:
                    result = False
        return result
