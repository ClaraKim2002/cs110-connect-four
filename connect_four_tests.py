import unittest

from connect_four import Board


class TestAddPiece(unittest.TestCase):

    def test_normal(self):
        board = Board()
        board.add_piece(3, "R")

        self.assertEqual(board.spots[3][0], "R",
                         "The first piece in the column is being added wrong!")

        for row in xrange(0, 6):
            for col in xrange(0, 7):
                if col == 3 and row == 0:
                    continue

                self.assertEqual(board.spots[col][row], None,
                                 "A piece has been added to the wrong spot.")

    def test_stack(self):
        board = Board()
        board.add_piece(3, "R")
        board.add_piece(3, "R")
        board.add_piece(3, "B")

        self.assertEqual(board.spots[3][0], "R",
                         "The first piece in the column is being added wrong!")
        self.assertEqual(board.spots[3][1], "R",
                         "The second piece is being added wrong!")
        self.assertEqual(board.spots[3][2], "B",
                         "The third piece is being added wrong!")

        for row in xrange(0, 6):
            for col in xrange(0, 7):
                if col == 3 and row == 0:
                    continue

                if col == 3 and row == 1:
                    continue

                if col == 3 and row == 2:
                    continue

                self.assertEqual(board.spots[col][row], None,
                                 "A piece has been added to the wrong spot.")

    def test_full_column(self):
        board = Board()
        self.assertTrue(board.add_piece(3, "R"),
                        "Your add_piece function must return True if a piece " +
                        "has been added to the board.")
        self.assertTrue(board.add_piece(3, "R"),
                        "Your add_piece function must return True if a piece " +
                        "has been added to the board.")
        self.assertTrue(board.add_piece(3, "R"),
                        "Your add_piece function must return True if a piece " +
                        "has been added to the board.")
        self.assertTrue(board.add_piece(3, "R"),
                        "Your add_piece function must return True if a piece " +
                        "has been added to the board.")
        self.assertTrue(board.add_piece(3, "R"),
                        "Your add_piece function must return True if a piece " +
                        "has been added to the board.")
        self.assertTrue(board.add_piece(3, "R"),
                        "Your add_piece function must return True if a piece " +
                        "has been added to the board.")
        self.assertFalse(board.add_piece(3, "R"),
                         "Your add_piece function must return False if a " +
                         "piece has not been added to the board.")


class TestGameResult(unittest.TestCase):

    def test_horizontal_first_row(self):
        board = Board()

        board.spots[2][0] = "R"
        board.spots[3][0] = "R"
        board.spots[4][0] = "R"
        board.spots[5][0] = "R"

        self.assertEqual(board.get_game_result(), "R",
                         "Horizontal wins are not being found correctly in " +
                         "the first row.")

    def test_horizontal_third_row(self):
        board = Board()

        board.spots[2][2] = "R"
        board.spots[3][2] = "R"
        board.spots[4][2] = "R"
        board.spots[5][2] = "R"

        self.assertEqual(board.get_game_result(), "R",
                         "Horizontal wins are not being found correctly in " +
                         "the third row.")

    def test_horizontal_black(self):
        board = Board()

        board.spots[2][0] = "B"
        board.spots[3][0] = "B"
        board.spots[4][0] = "B"
        board.spots[5][0] = "B"

        self.assertEqual(board.get_game_result(), "B",
                         "Horizontal black wins are not being found " +
                         "correctly in the first row.")

    def test_vertical(self):
        board = Board()

        board.spots[2][2] = "R"
        board.spots[2][3] = "R"
        board.spots[2][4] = "R"
        board.spots[2][5] = "R"

        self.assertEqual(board.get_game_result(), "R",
                         "Vertical wins are not being found correctly.")

    def test_diagonal_up_right(self):
        board = Board()

        board.spots[2][2] = "R"
        board.spots[3][3] = "R"
        board.spots[4][4] = "R"
        board.spots[5][5] = "R"

        self.assertEqual(board.get_game_result(), "R",
                         "Diagonal (/) wins are not being found correctly.")

    def test_diagonal_up_left(self):
        board = Board()

        board.spots[2][5] = "R"
        board.spots[3][4] = "R"
        board.spots[4][3] = "R"
        board.spots[5][2] = "R"

        self.assertEqual(board.get_game_result(), "R",
                         "Diagonal (\) wins are not being found correctly.")

if __name__ == '__main__':
    unittest.main(exit = False)