import pygame
from checker.constants import *
from checker.game import Game
from alphabeta.algorithm import alphabeta

# To render the game in a fixed frames number per second
FPS = 170

WIN = pygame.display.set_mode((WIDTH, HEIGHT))

# Name of the game
pygame.display.set_caption('Checkers')


# Start get_row_col_from_mouse method to get the position of the piece that mouse clicked
def get_row_col_from_mouse(pos):
    x, y = pos
    row = y // SQUARE_SIZE
    col = x // SQUARE_SIZE
    return row, col


# End get_row_col_from_mouse method to get the position of the piece that mouse clicked

def main():
    run = True

    # To make the game run in fixed speed
    clock = pygame.time.Clock()

    # To create a board and start the game
    game = Game(WIN)

    # Event Loop
    while run:
        # To run the game in a fixed speed -> (f/s)
        clock.tick(FPS)

        # Start To make the AI play
        if game.turn == ORANGE:
            # The higher the number of depth, the higher the complexity of the AI
            # value, new_board = minimax(game.get_board(), 4, BLUE, game)
            value, new_board = alphabeta(game.get_board(), 4, float('-inf'), float('inf'), ORANGE, game)
            game.ai_move(new_board)

        # End To make the AI play

        if game.winner() is not None:
            if game.winner() == ORANGE:
                print("The computer wins the game")
                run = False
            else:
                print("You wins the game")
                run = False

            # run = False  # To quit the game if someone win

        # Start check if any event happen in the current time
        for event in pygame.event.get():
            # if I press the x in top right corner he will exit
            if event.type == pygame.QUIT:
                run = False

            if event.type == pygame.MOUSEBUTTONDOWN:  # condition when click the mouse
                pos = pygame.mouse.get_pos()  # return tuple
                row, col = get_row_col_from_mouse(pos)
                valid_select = game.select(row, col)
                # I want the selected piece row and column to return to it if he made
                # an invalid move
                if valid_select:
                    Game.previous_row = row
                    Game.previous_column = col

        # End check if any event happen in the current time

        game.update()  # To update any change that happens in the game board
    # Quit from the game
    pygame.quit()


# To call the main function and run the code inside it
main()
