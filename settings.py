EMPTY = -1
BLACK = 0
WHITE = 1
BOARD = 'default.board'
FLIP_COORDS = False
CONVERSION_DICT = {'.': EMPTY, 'B': BLACK, 'W': WHITE}
CONVERSION_LIST = ['B', 'W', ' ']
NAME_LIST = ['black', 'white']
MOVES_DELTA = [(-1, -1), (-1, 0), (-1, 1),
               (0, -1), (0, 1),
               (1, -1), (1, 0), (1, 1)]
CORNERS = [(0, 0), (0, -1), (-1, 0), (-1, -1)]
PLAYER = BLACK
COMPUTER = 1 - PLAYER
WEIGHTS = [[100, -10, 11, 6, 6, 11, -10, 100],
           [-10, -20, -1, -2, -2, -1, -20, -10],
           [11, -1, 5, 4, 4, 5, -1, 11],
           [6, -2, 4, 2, 2, 4, -2, 6],
           [6, -2, 4, 2, 2, 4, -2, 6],
           [11, -1, 5, 4, 4, 5, -1, 11],
           [-10, -20, -1, -2, -2, -1, -20, -10],
           [100, -10, 11, 6, 6, 11, -10, 100]]
