import unittest

from connect_four import Board

import ai


class TestAddPiece(unittest.TestCase):

    def test_numeric(self):
        board = Board()

        move = ai.choose_move(board, "B")

        self.assertTrue(move <= 6)
        self.assertTrue(move >= 0)


if __name__ == '__main__':
    unittest.main(exit = False)