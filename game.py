#!/usr/bin/env python

import copy

class Board(object):
    """The board class.

    The board is a nxn matrix of integers. Each inteter represents a
    color. The board has no knowledge about the available colors of the
    game.

    """

    def __init__(self, data):
        """Initialize the board.

        Parameters
        ----------
        data : list of lists of ints
            the initial data

        Raises
        ------
        ValueError : if the board is not square

        """
        self.data = data[:]
        self.n = len(self.data)
        for row in data:
            if len(row) != self.n:
                raise ValueError("Data is not a square matrix!")

    def __str__(self):
        """Return a string representation of the board.

        Returns
        -------
        s : str
            representation of the board

        """
        s = ""
        for row in self.data:
            s = s + str(row) + "\n"
        return s

    def copy(self):
        """Returns a (deep) copy of this board.

        Use this method if you want to test a coloring and keep the old
        board as a backup.

        Returns
        -------
        b : Board
            a deep copy of this board

        """
        return Board(copy.deepcopy(self.data))

    def set_color(self, c):
        """Colorize the board starting vom origin.

        This will change the board *in place*.

        Parameters
        ----------
        c : int
            the new color for origin

        """
        # we color the board using simple flooding. Instead of using a
        # recursion and rising to hit Pythons recursion-limit, we use a
        # stack to keep track of the tiles left to colorize
        c_orig = self.data[0][0]
        self.data[0][0] = c
        stack = [(0, 0)]
        visited = set()
        while stack:
            x, y = stack.pop()
            if (x, y) in visited:
                continue
            visited.add((x, y))
            for xn, yn in self.get_neighbours(x, y):
                if self.data[xn][yn] == c_orig:
                    stack.append((xn, yn))
            self.data[x][y] = c

    def count_connected(self):
        """Count the number of connected tiles.

        Returns
        -------
        c : int
            number of connected tiles

        """
        # this works similar to the `set_color` above
        c = 0
        stack = [(0, 0)]
        visited = set()
        while stack:
            x, y = stack.pop()
            if (x, y) in visited:
                continue
            visited.add((x, y))
            c += 1
            for xn, yn in self.get_neighbours(x, y):
                if self.data[xn][yn] == self.data[x][y]:
                    stack.append((xn, yn))
        return c

    def get_neighbours(self, x, y):
        """Generate the the valid neighbours for position (x, y).

        Returns
        -------
        generator object with (x, y) positions

        """
        if (0 <= x < self.n) and (0 <= y < self.n):
            if x-1 >= 0:
                yield x-1, y
            if x+1 < self.n:
                yield x+1, y
            if y-1 >= 0:
                yield x, y-1
            if y+1 < self.n:
                yield x, y+1



def play(board, colors):
    """Play the board given the available colors.

    THIS METHOD IS NOT FINISHED YET :(

    """
    # Haven't finished here... should run until the end
    for i in range(3):
        # try all colorings
        connected_color_map = []
        for c in colors:
            board_copy = board.copy()
            board_copy.set_color(c)
            connected = board_copy.count_connected()
            connected_color_map.append((connected, c))
        # take the color resulting in max connections
        connected_color_map.sort()
        c_win = connected_color_map[-1][1]
        board.set_color(c_win)


if __name__ ==  "__main__":
    # initialize
    data = [[0, 1, 0, 2, 0, 1],
            [2, 0, 2, 1, 2, 1],
            [2, 2, 1, 2, 2, 2],
            [2, 1, 0, 2, 0, 1],
            [2, 1, 0, 1, 1, 1],
            [0, 2, 0, 1, 2, 0]]
    board = Board(data)
    colors = [0, 1, 2]
    play(board, colors)
