# Othello game functions.

from settings import *


def othello(board, player):
    """
    Helper function to pass the game between players.
    :param board: The current board state, a 2d-List
    :param player: Player to go next, 0 = black, 1 = white
    """
    if not player:
        get_black_move(board)
    else:
        get_white_move(board)


def get_black_move(board):
    pass


def get_white_move(board):
    pass


def get_legal_moves(board, player):
    """
    Helper function to get a list of index 2-tuples that are valid moves for the current player.
    :param board: The current board state, a 2d-list
    :param player: The current player to place the next piece, 0 = black, 1 = white
    """
    moves_delta = [(-1, -1), (-1, 0), (-1, 1),
                   (0, -1), (0, 0), (0, 1),
                   (1, -1), (1, 0), (1, 1)]
    board_width, board_height = len(board), len(board[1])
    valid_moves = set()
    for row_index, row in enumerate(board):
        for col_index, pos in enumerate(row):
            # The current position must be of the opposite color
            if pos != WHITE - player:
                continue
            for move in moves_delta:
                new_row, new_col = row_index + move[0], col_index + move[1]
                # For a move to be legal, it must be:
                # 1. On a position that is actually on the board and empty
                if new_row not in range(0, board_width) or new_col not in range(0, board_height) or \
                        board[new_row][new_col] != EMPTY:
                    continue
                # 2. Traverse the opposite direction: must be a piece of the player's color
                search_row, search_col = row_index - move[0], col_index - move[1]
                while search_row in range(0, board_width) and search_col in range(0, board_width):
                    if board[search_row][search_col] == player:
                        valid_moves.add((new_row, new_col))
                        break
                    search_row -= move[0]
                    search_col -= move[1]
    return list(valid_moves)
