import pygame
from checker.board import Board
from checker.constants import *


class Game:
    previous_row = 0
    previous_column = 0

    def __init__(self, win):
        self._init()
        self.win = win

    # Start _init private method that initialize all properties for the game to start
    def _init(self):
        self.selected = None  # the piece is not selected
        self.board = Board()  # Board object creation
        self.turn = WHITE
        self.valid_moves = {}

    # End _init private method that initialize all properties for the game to start

    # Start winner method
    def winner(self):
        if self.board is not None:
            return self.board.winner()

    # End winner method

    # Start update method that draw the board and update it
    def update(self):
        self.board.draw(self.win)
        self.draw_valid_moves(self.valid_moves)
        pygame.display.update()

    # End update method that draw the board and update it

    # call it when you want to play again
    # def reset(self):
    #     self._init()

    # End reset method that reset the game

    # Start select method to try to move the selected piece
    def select(self, row, col):
        # if we already select a piece and the click is to move it
        if self.selected:
            result = self._move(row, col)
            # if the position that we try to move to is invalid
            if not result:
                self.selected = None
                # that means I don't move but select another piece or
                # go to invalid square
                self.select(row, col)  # recursively calling the select method
        # select a piece if not selected
        piece = self.board.get_piece(row, col)
        if piece != 0 and piece.color == self.turn:
            self.selected = piece
            self.valid_moves = self.board.get_valid_moves(piece)
            return True  # if the selected piece is valid
        # that will run if I already select the piece and tried to move it to invalid,
        # so I will let the same piece selected as we don't move
        piece = self.board.get_piece(Game.previous_row, Game.previous_column)
        if piece != 0 and piece.color == self.turn:
            self.selected = piece
            self.valid_moves = self.board.get_valid_moves(piece)
            return False
        return False  # if the selected piece is invalid or if I move the piece

    # End select method to try to move the selected piece

    # Start move method to handle the moving of the selected piece to the pos we choose
    def _move(self, row, col):
        piece = self.board.get_piece(row, col)
        # check if there is a selected piece and if the pos that we need to move to is = 0
        if self.selected and piece == 0 and (row, col) in self.valid_moves:
            self.board.move(self.selected, row, col)  # this functions draws the move
            skipped = self.valid_moves[(row, col)]
            if skipped:
                self.board.remove_piece(skipped)  # delete red (guide dots)
            self.change_turn()
        else:
            return False  # if the selection method is invalid(don't move)
        return True  # if the selection method is valid(move done)

    # End move method to handle the moving of the selected piece to the pos we choos e

    # Start draw_valid_moves method
    def draw_valid_moves(self, moves):  # moves is a dictionary of valid moves
        for move in moves:
            row, col = move  # row , col is the keys of the dictionary
            pygame.draw.circle(self.win, RED,  # it's the red guide when you select a piece
                               (col * SQUARE_SIZE + SQUARE_SIZE // 2, row * SQUARE_SIZE + SQUARE_SIZE // 2), 15)

    # End draw_valid_moves method

    # Start change_turn method
    def change_turn(self):
        self.valid_moves = {}  # make the valid_moves dictionary empty again
        if self.turn == WHITE:
            self.turn = ORANGE
        else:
            self.turn = WHITE

    # End change_turn method

    # Start get_board method
    def get_board(self):
        return self.board

    # End get_board method

    # Start ai_move method
    def ai_move(self, board):
        self.board = board
        self.change_turn()
    # End ai_move method
