
import pygame
import sys
import ai


class Board():

    def __init__(self):
        self.spots = [None]*7

        for col in xrange(0, 7):
            self.spots[col] = [None]*6

    def get_spot_status(self, col, row):
        return self.spots[col][row]

    def add_piece(self, col, player):
        """
        Add a piece to the correct row in the column. If there are no spaces
        left in the column return False. If the piece is added return True
        """
        pass

    def get_game_result(self):
        """
        If there is currently a winner, return "R" or "B" depending on who 
        won the game. Otherwise return None
        """
        pass


def draw_board(b):
    screen.fill((0, 0, 0))

    pygame.draw.rect(screen, (255, 255, 0), (50, 50, 700, 600), 0)

    for row in xrange(0, 6):
        for col in xrange(0, 7):
            x = (col * 100) + 100
            y = 700 - ((row * 100) + 100)

            if b.get_spot_status(col, row) == "R":
                pygame.draw.circle(screen, (255, 0, 0), (x, y), 50)
            elif b.get_spot_status(col, row) == "B":
                pygame.draw.circle(screen, (0, 0, 0), (x, y), 50)
            else:
                pygame.draw.circle(screen, (255, 255, 255), (x, y), 50)


if __name__ == '__main__':
    screen = pygame.display.set_mode((800, 700))

    board = Board()
    move = "R"

    while True:

        change_move = False

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if move == "R":
                    valid = False
                    if event.key == pygame.K_1:
                        valid = board.add_piece(0, "R")
                    elif event.key == pygame.K_2:
                        valid = board.add_piece(1, "R")
                    elif event.key == pygame.K_3:
                        valid = board.add_piece(2, "R")
                    elif event.key == pygame.K_4:
                        valid = board.add_piece(3, "R")
                    elif event.key == pygame.K_5:
                        valid = board.add_piece(4, "R")
                    elif event.key == pygame.K_6:
                        valid = board.add_piece(5, "R")
                    elif event.key == pygame.K_7:
                        valid = board.add_piece(6, "R")

                    if valid:
                        change_move = True

        if move == "B":
            valid = False

            ai_col = ai.choose_move(board, "B")
            valid = board.add_piece(ai_col, "B")

            if valid:
                change_move = True

        if change_move:
            if move == "B":
                move = "R"
            elif move == "R":
                move = "B"

        if board.get_game_result() == "R":
            exit("Red Wins!")
        elif board.get_game_result() == "B":
            exit("Black Wins!")

        draw_board(board)
        pygame.display.flip()





