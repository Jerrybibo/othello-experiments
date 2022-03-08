from settings import *
import traceback


def parse_board(file):
    """
    Parses a board layout file, then returns a 2d-list representation of the board state.
    :param file: Path to the file that contains the board layout
    :return: A 2d-list of the board state
    """
    try:
        with open(file, 'r') as board_file:
            file_contents = [line.strip() for line in board_file.readlines()]
    except IOError:
        print("An IOError has occurred. Details:")
        print(traceback.format_exc())
    else:
        board_width, board_height = [int(i) for i in file_contents[0].split()]
        board = [[EMPTY] * board_height for _ in range(board_width)]
        file_contents = [list(row) for row in file_contents[1:]]
        for row_index, row in enumerate(file_contents):
            for col_index, pos in enumerate(row):
                board[row_index][col_index] = CONVERSION_DICT[pos]
        return board


def print_board(board, legal_moves=None):
    """
    Prints the board prettily. If legal_moves is specified, overlays the legal moves on top of the display.
    :param legal_moves: A list of 2-tuples, specifying the legal moves.
    :param board: The current game board state
    """
    print('   ', end='')
    for col_index in range(0, len(board[0])):
        print(' %2d ' % col_index, end='')
    print()
    for row_index, row in enumerate(board):
        print('   +' + '---+' * len(row) + "\n%2d |" % row_index, end='')
        for col_index, pos in enumerate(row):
            if legal_moves and (row_index, col_index) in legal_moves:
                print(' ? |', end='')
            else:
                print(' ' + CONVERSION_LIST[pos] + ' |', end='')
        print()
    print('   +' + '---+' * len(board[0]))


def ask_move(legal_moves):
    while 1:
        raw_move = input('>> ')
        try:
            move = tuple([int(pos) for pos in raw_move.split()])
            if move not in legal_moves:
                raise IndexError
        except ValueError:
            print("Incorrect format. Please enter desired moves as a space-delimited pair of 0-indexed row and column.")
            print("Example: '2 3' (3rd row, 4th column) or '6 0' (7th row, 1st column)")
        except IndexError:
            print("That's an invalid move.")
        else:
            return move

