EMPTY = -1
BLACK = 0
WHITE = 1

FLIP_COORDS = False

CONVERSION_DICT = {
    '.': EMPTY,
    'B': BLACK,
    'W': WHITE
}

CONVERSION_LIST = ['B', 'W', ' ']

MOVES_DELTA = [(-1, -1), (-1, 0), (-1, 1),
               (0, -1),           (0, 1),
               (1, -1),  (1, 0),  (1, 1)]

PLAYER = BLACK
COMPUTER = 1 - PLAYER
