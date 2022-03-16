# Othello game functions.

from settings import *
import random
from helpers import *


def get_move(board, current_player):
    """
    Helper function to pass the game between players.
    :param board: The current board state, a 2d-List
    :param current_player: Player to go next, 0 = black, 1 = white
    """
    print('It is', NAME_LIST[current_player] + '\'s turn.')
    legal_moves = get_legal_moves(board, player=current_player)
    # No legal moves!
    if len(legal_moves) == 0:
        return board
    if current_player == PLAYER:
        print_board(board, legal_moves)
        move = ask_move(legal_moves)
    else:
        print_board(board, legal_moves)
        # move = random.choice(legal_moves)
        move = calculate_move(board, current_player, legal_moves)
        print("Computer played", move[::-1])
    board = play_and_update(board, move, current_player)

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
            if new_row not in range(board_width) or new_col not in range(board_height) or \
                    board[new_row][new_col] == EMPTY:
                break
            elif board[new_row][new_col] == color:
                for traversed_pos in traversed:
                    board[traversed_pos[0]][traversed_pos[1]] = color
                break
            traversed.append((new_row, new_col))
    return board


def check_board(board):
    """
    Checks the board for whether the game has finished or not.
    :param board: Current board state
    :returns: True if game has ended, False if not
    """
    # Terminate if there are no legal moves for either player
    return True if len(get_legal_moves(board, PLAYER)) == 0 and len(get_legal_moves(board, COMPUTER)) == 0 else False


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
            if pos != 1 - player:
                continue
            # Then we search in all adjacent positions
            for move in MOVES_DELTA:
                new_row, new_col = row_index + move[0], col_index + move[1]
                # For a move to be legal, it must be:
                # 1. On a position that is actually on the board and empty
                if new_row not in range(board_width) or new_col not in range(board_height) or \
                        board[new_row][new_col] != EMPTY:
                    continue
                # 2. Traverse in the opposite direction; there must be a piece of the player's color
                search_row, search_col = row_index - move[0], col_index - move[1]
                while search_row in range(board_width) and search_col in range(board_width):
                    if board[search_row][search_col] == player:
                        valid_moves.add((new_row, new_col))
                        break
                    elif board[search_row][search_col] == EMPTY:
                        break
                    search_row -= move[0]
                    search_col -= move[1]
    return list(valid_moves)


def calculate_move(board, player, legal_moves=None):
    """
    Evaluate, then returns the most optimal move for the current player.
    :param board: Current board state, a 2d-list
    :param player: The current player
    :param legal_moves: A list of legal moves
    """
    opponent = 1 - player
    if legal_moves is None:
        legal_moves = get_legal_moves(board, player)
    moves = []
    for move in legal_moves:
        player_board = [row[:] for row in board]
        player_board = play_and_update(player_board, move, player)
        opponent_legal_moves = get_legal_moves(player_board, opponent)
        h_sum = 0
        for opponent_move in opponent_legal_moves:
            opponent_board = [row[:] for row in player_board]
            opponent_board = play_and_update(opponent_board, opponent_move, opponent)
            h_sum += calculate_heuristics(opponent_board, opponent)['h']
        moves.append([(move[0], move[1]), h_sum])
    if len(moves) > 0:
        return sorted(moves, key=lambda x: x[1])[0][0]
    else:
        return tuple()


def play_and_update(board, move, player):
    board[move[0]][move[1]] = player
    return update_board(board, move[0], move[1])


def calculate_heuristics(board, player):
    """
    Calculate the heuristic value given current board state and player.
    :param board: Current board state, a 2d-list
    :param player: The current player
    """
    # First, get a bunch of useful information
    opponent = 1 - player
    total_board_space = len(board) * len(board[0])
    # count: range(0, 64)
    player_count, opponent_count = 0, 0
    # corners: range(0, 5)
    player_corners, opponent_corners = 0, 0
    # weight: around range(-160, 520)
    weight = 0
    for row_index, row in enumerate(board):
        for col_index, pos in enumerate(row):
            if pos == player:
                player_count += 1
                if (row_index, col_index) in CORNERS:
                    player_corners += 1
                weight += WEIGHTS[row_index][col_index]
            elif pos == opponent:
                opponent_count += 1
                if (row_index, col_index) in CORNERS:
                    opponent_corners += 1
                weight -= WEIGHTS[row_index][col_index]
    # Calculate mobility
    mobility = len(get_legal_moves(board, player))
    empty_count = total_board_space - player_count - opponent_count

    return {
        'h': weight + mobility * 8,
        'player_count': player_count,
        'opponent_count': opponent_count
    }  # for now - todo h-value is tentative


def ask_move(legal_moves):
    while 1:
        raw_move = input('>> ')
        try:
            move = tuple([int(pos) for pos in raw_move.split()])
            if not FLIP_COORDS:
                move = move[::-1]
            if move not in legal_moves:
                raise IndexError
        except ValueError:
            if FLIP_COORDS:
                print("Incorrect format. "
                      "Please enter desired moves as a space-delimited pair of 0-indexed row and column.\n"
                      "Example: '2 3' (3rd row, 4th column) or '6 0' (7th row, 1st column)")
            else:
                print("Incorrect format."
                      "Please enter desired moves as a space-delimited pair of 0-indexed column and row.\n"
                      "Example: '2 3' (3rd column, 4th row) or '6 0' (7th column, 1st row)")
        except IndexError:
            print("That's an invalid move.")
        else:
            return move


def conclude_game(board):
    stats = calculate_heuristics(board, PLAYER)
    player_count, opponent_count = stats['player_count'], stats['opponent_count']
    if player_count > opponent_count:
        print('Congratulations!', PLAYER, 'won!')
    elif player_count < opponent_count:
        print(COMPUTER, 'won.')
    else:
        print('It\'s a tie.')


def main():
    board = parse_board(BOARD)
    while True:
        board = get_move(board, current_player=BLACK)
        if check_board(board):
            break
        board = get_move(board, current_player=WHITE)
        if check_board(board):
            break
    conclude_game(board)


if __name__ == '__main__':
    main()
