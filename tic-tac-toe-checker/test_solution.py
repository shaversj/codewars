import unittest
from solution import is_solved


class MyTestCase(unittest.TestCase):

    def test_is_not_finished(self):
        # not yet finished
        board = [[0, 0, 1],
                 [0, 1, 2],
                 [2, 1, 0]]
        self.assertEqual(is_solved(board), -1)

    def test_found_winning_row(self):
        # winning row
        board = [[1, 1, 1],
                 [0, 2, 2],
                 [0, 0, 0]]
        self.assertEqual(is_solved(board), 1)

    def test_found_winning_column(self):

        # winning column
        board = [[2, 1, 2],
                 [2, 1, 1],
                 [1, 1, 2]]
        self.assertEqual(is_solved(board), 1)

    def test_found_diagonal_winner(self):
        board = [[2, 1, 2],
                 [2, 2, 1],
                 [1, 1, 2]]

        self.assertEqual(is_solved(board), 2)

    def test_draw(self):

        # draw
        board = [[2, 1, 2],
                 [2, 1, 1],
                 [1, 2, 1]]
        self.assertEqual(is_solved(board), 0)


if __name__ == '__main__':
    unittest.main()
