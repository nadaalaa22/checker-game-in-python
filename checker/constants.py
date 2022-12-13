import pygame

#Size of board
WIDTH, HEIGHT = 600, 600 
ROWS, COLS = 8, 8

#Size of one square in the board
SQUARE_SIZE = WIDTH//COLS 

# RGB Color
WHITE = (255,255,255)
BLACK = (0,0,0)
BLUE  = (0,0,255)
RED   = (255, 0, 0)
GREY  = (128, 128, 128)

#Crown image
CROWN = pygame.transform.scale(pygame.image.load('assets/crown.png'), (44, 25))