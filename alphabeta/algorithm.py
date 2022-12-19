from copy import deepcopy
from checker.constants import ORANGE, WHITE


# WHITE = (255, 255, 255)
# BLUE = (255, 222, 173)


# start alpha beta depth first algo method
# this function use recursion

def alphabeta(position, depth, max_player, game, cond=float('inf')):
    if depth == 0 or position.winner(ORANGE) is not None:
        return position.evaluate(), position
    if max_player == ORANGE:
        max_eval = float('-inf')
        best_move = None
        for move in get_all_moves(position, ORANGE):
            evaluation = alphabeta(move, depth - 1, WHITE, game, max_eval)[0]
            if evaluation >= cond:
                break
            max_eval = max(max_eval, evaluation)
            if max_eval == evaluation:
                best_move = move
        return max_eval, best_move
    else:
        # if the AI don't checked anything in a specific position then it will be -inf
        min_eval = float('inf')
        best_move = None
        for move in get_all_moves(position, WHITE):

            evaluation = alphabeta(move, depth - 1, ORANGE, game, min_eval)[0]
            # To check if the new state evaluation is better than minEval that we have now
            if evaluation <= cond:
                break
            min_eval = min(min_eval, evaluation)

            if min_eval == evaluation:
                best_move = move
        return min_eval, best_move


# End alpha beta depth first algo method


# Start simulate method
def simulate_move(piece, move, board, skip):
    board.move(piece, move[0], move[1])
    if skip:
        board.remove_piece(skip)
    return board


# End simulate method

# Start get_all_moves method
# This function take the current shape of the board
# and test all valid moves and return the boards shape after these
# valid moves

def get_all_moves(board, color):
    is_skip = False
    moves = []
    all_pieces = board.get_all_pieces(color)
    # we loop to check if there is something I could eat
    for piece in all_pieces:
        valid_moves = board.get_valid_moves(piece)
        # check if there is a skip that could happen
        for move, skip in valid_moves.items():
            if skip:
                is_skip = True
                break
        if is_skip:
            break
    if not is_skip:
        for piece in board.get_all_pieces(color):
            valid_moves = board.get_valid_moves(piece)

            for move, skip in valid_moves.items():
                # draw_moves(game, board, piece)
                # copy the board to don't modify in the original board
                temp_board = deepcopy(board)
                temp_piece = temp_board.get_piece(piece.row, piece.col)
                # try to execute the move that AI select now and save the new board state that it will be returned
                new_board = simulate_move(temp_piece, move, temp_board, skip)
                moves.append(new_board)  # save the new board
        return moves
    else:
        for piece in all_pieces:
            valid_moves = board.get_valid_moves(piece)
            for move, skip in valid_moves.items():
                if skip:
                    temp_board = deepcopy(board)
                    temp_piece = temp_board.get_piece(piece.row, piece.col)
                    # try to execute the move that AI select now and save the new board state that it will be returned
                    new_board = simulate_move(temp_piece, move, temp_board, skip)
                    moves.append(new_board)
        return moves


# End get_all_moves method# Start get_all_moves method
# This function take the current shape of the board
# and test all valid moves and return the boards shape after these
# valid moves


def get_all_user_moves(board, color):
    is_skip = False
    moves = []
    all_pieces = board.get_all_pieces(WHITE)
    # we loop to check if there is something I could eat
    for piece in all_pieces:
        valid_moves = board.get_valid_moves(piece)
        # check if there is a skip that could happen
        for move, skip in valid_moves.items():
            if skip:
                is_skip = True
                break
        if is_skip:
            break

    # No skip could happen
    if not is_skip:
        for piece in all_pieces:
            valid_moves = board.get_valid_moves(piece)
            for move, skip in valid_moves.items():
                moves.append(move)
    # only skip moves
    else:
        for piece in all_pieces:
            valid_moves = board.get_valid_moves(piece)
            for move, skip in valid_moves.items():
                if skip:
                    moves.append(move)
    return moves

# End get_all_moves method
