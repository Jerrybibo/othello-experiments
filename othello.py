# Othello game functions.

from settings import *
import random
from helpers import *


def othello(board, player):
    """
    Helper function to pass the game between players.
    :param board: The current board state, a 2d-List
    :param player: Player to go next, 0 = black, 1 = white
    """
    if not player:
        board = get_black_move(board)
    else:
        board = get_white_move(board)
    return board


def get_black_move(board):
    print("It is black's turn.")
    legal_moves = get_legal_moves(board, player=BLACK)
    if PLAYER == BLACK:
        print_board(board, legal_moves)
        move = ask_move(legal_moves)
    else:
        print_board(board)
        # todo AI is random right now
        move = random.choice(legal_moves)
        print("Computer plays", move)
    board[move[0]][move[1]] = BLACK
    board = update_board(board, move[0], move[1])
    return board


def get_white_move(board):
    print("It is white's turn.")
    legal_moves = get_legal_moves(board, player=WHITE)
    if PLAYER == WHITE:
        print_board(board, legal_moves)
        move = ask_move(legal_moves)
    else:
        print_board(board)
        # todo AI is random right now
        move = random.choice(legal_moves)
        print("Computer plays", move)
    board[move[0]][move[1]] = WHITE
    board = update_board(board, move[0], move[1])
    return board


def update_board(board, row_index, col_index):
    board_width, board_height = len(board), len(board[1])
    color = board[row_index][col_index]
    for move in MOVES_DELTA:
        traversed = []
        new_row, new_col = row_index, col_index
        while 1:
            new_row += move[0]
            new_col += move[1]
            if board[new_row][new_col] == EMPTY or \
                    new_row not in range(board_width) or new_col not in range(board_height):
                break
            elif board[new_row][new_col] == color:
                for traversed_pos in traversed:
                    board[traversed_pos[0]][traversed_pos[1]] = color
                break
            traversed.append((new_row, new_col))
    return board




def get_legal_moves(board, player):
    """
    Helper function to get a list of index 2-tuples that are valid moves for the current player.
    :param board: The current board state, a 2d-list
    :param player: The current player to place the next piece, 0 = black, 1 = white
    """
    board_width, board_height = len(board), len(board[1])
    valid_moves = set()
    for row_index, row in enumerate(board):
        for col_index, pos in enumerate(row):
            # The current position must be of the opposite color
            if pos != WHITE - player:
                continue
            for move in MOVES_DELTA:
                new_row, new_col = row_index + move[0], col_index + move[1]
                # For a move to be legal, it must be:
                # 1. On a position that is actually on the board and empty
                if new_row not in range(board_width) or new_col not in range(board_height) or \
                        board[new_row][new_col] != EMPTY:
                    continue
                # 2. Traverse the opposite direction: must be a piece of the player's color
                search_row, search_col = row_index - move[0], col_index - move[1]
                while search_row in range(board_width) and search_col in range(board_width):
                    if board[search_row][search_col] == player:
                        valid_moves.add((new_row, new_col))
                        break
                    search_row -= move[0]
                    search_col -= move[1]
    return list(valid_moves)


def main():
    board = parse_board('sample.board')
    while True:
        board = othello(board, player=PLAYER)
        board = othello(board, player=COMPUTER)


if __name__ == '__main__':
    main()
