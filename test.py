from helpers import *
from othello import *

board = parse_board('sample.board')
moves = get_legal_moves(board, BLACK)
print_board(board, legal_moves=moves)
ask_move(legal_moves=moves)

