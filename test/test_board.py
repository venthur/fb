import unittest

from game import Board


class TestBoard(unittest.TestCase):

    def test_init(self):
        data = [[0, 0], [0, 0]]
        board = Board(data)
        self.assertEquals(board.n, 2)

    def test_init_value_error(self):
        """Board raises ValueError on non square input matrix."""
        data = [[0, 0], [0, 0], [0, 0]]
        with self.assertRaises(ValueError):
            Board(data)

    def test_copy(self):
        """Board generates a deep copy of itself."""
        data = [[0, 1], [1, 0]]
        b1 = Board(data)
        b2 = b1.copy()
        # test if proper copy
        self.assertListEqual(b1.data, b2.data)
        # teset if not just a shallow copy
        b1.data[0][0] = 1
        self.assertNotEqual(b1.data[0][0], b2.data[0][0])

    def test_set_color(self):
        """Board colorizes properly."""
        data = [[0, 1, 0],
                [1, 0, 0],
                [0, 0, 1]]
        board = Board(data)
        # no change expected
        board.set_color(0)
        self.assertListEqual(data, board.data)
        # step 1
        board.set_color(1)
        data = [[1, 1, 0],
                [1, 0, 0],
                [0, 0, 1]]
        self.assertListEqual(data, board.data)
        # step 2
        board.set_color(0)
        data = [[0, 0, 0],
                [0, 0, 0],
                [0, 0, 1]]
        self.assertListEqual(data, board.data)
        # step 3
        board.set_color(1)
        data = [[1, 1, 1],
                [1, 1, 1],
                [1, 1, 1]]
        self.assertListEqual(data, board.data)

    def test_count_connected(self):
        """Board must count number of connections to origin properly."""
        data = [[0, 1, 0],
                [1, 0, 0],
                [0, 0, 1]]
        board = Board(data)
        self.assertEquals(board.count_connected(), 1)

        data = [[1, 1, 0],
                [1, 0, 0],
                [0, 0, 1]]
        board = Board(data)
        self.assertEquals(board.count_connected(), 3)

        data = [[0, 0, 0],
                [0, 0, 0],
                [0, 0, 1]]
        board = Board(data)
        self.assertEquals(board.count_connected(), 8)

        data = [[1, 1, 1],
                [1, 1, 1],
                [1, 1, 1]]
        board = Board(data)
        self.assertEquals(board.count_connected(), 9)

    def test_get_neighbours(self):
        """Properly calculate number of neighbours."""
        data = [[0, 0, 0],
                [0, 0, 0],
                [0, 0, 0]]
        board = Board(data)

        # [pos(x, y), #neighbours]
        posx_posy_n = [[0, 0, 2], [0, 1, 3], [0, 2, 2],
                       [1, 0, 3], [1, 1, 4], [1, 2, 3],
                       [2, 0, 2], [2, 1, 3], [2, 2, 2]]
        for x, y, n in posx_posy_n:
            neighbours = [i for i in board.get_neighbours(x, y)]
            self.assertEquals(len(neighbours), n)

    def test_play_example(self):
        """Play the example from the exercise sheet."""
        data = [[0, 1, 0, 2, 0, 1],
                [2, 0, 2, 1, 2, 1],
                [2, 2, 1, 2, 2, 2],
                [2, 1, 0, 2, 0, 1],
                [2, 1, 0, 1, 1, 1],
                [0, 2, 0, 1, 2, 0]]
        board = Board(data)
        board.set_color(2)
        board.set_color(1)
        board.set_color(0)
        board.set_color(2)
        data_end = [[2, 2, 2, 2, 0, 1],
                    [2, 2, 2, 1, 2, 1],
                    [2, 2, 2, 2, 2, 2],
                    [2, 2, 2, 2, 0, 1],
                    [2, 2, 2, 1, 1, 1],
                    [2, 2, 2, 1, 2, 0]]
        self.assertListEqual(board.data, data_end)

    #def test_regresssion_infinite_loop(self):
    #    """Test case to reproduce a bug."""
    #    data = [[0, 1, 0, 2, 0, 1],
    #            [2, 0, 2, 1, 2, 1],
    #            [2, 2, 1, 2, 2, 2],
    #            [2, 1, 0, 2, 0, 1],
    #            [2, 1, 0, 1, 1, 1],
    #            [0, 2, 0, 1, 2, 0]]
    #    board = Board(data)
    #    board.set_color(2)
    #    # this causes an infinite loop
    #    board.set_color(2)

if __name__ == "__main__":
    unittest.main()
