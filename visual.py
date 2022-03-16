"""
GUI through Pygame for Othello game
Written by Jerrybibo 3/16/2022.
"""
# Only designed for 8x8 boards.

import pygame as p
from pygame.locals import *
from settings import *
from othello import *

WINDOW_SIZE = (680, 680)
BOARD_SIZE = (640, 640)


p.init()
# Each slot is 80x80 with border width of 20
window_surface = p.display.set_mode((680, 680), 0, 32)
p.display.set_caption("Othello")
background = p.image.load('./background.png')


def click(mouse_pos):
    """
    Return the indices for the game board to update, if the position is part of the board
    Note that board is assumed to be 680px*680px and 8x8.
    :param mouse_pos: 2-tuple representing the current mouse position relative to window
    """
    x, y = mouse_pos
    x = (x - 20) // 80 if 20 <= x <= 660 else -1
    y = (y - 20) // 80 if 20 <= y <= 660 else -1
    return x, y


def main():
    board = parse_board(BOARD)
    active_game = True
    while active_game:
        legal_moves = get_legal_moves(board, player=PLAYER)
        for e in p.event.get():
            if e.type == QUIT:
                p.quit()
                exit(0)
            if e.type == MOUSEBUTTONDOWN:
                move = click(p.mouse.get_pos())
                if move not in legal_moves:
                    print("Illegal move.")
                    break
                board = play_and_update(board, move, PLAYER)
                print_board(board)
                if check_board(board):
                    active_game = False
                move = calculate_move(board, 1-PLAYER)
                board = play_and_update(board, move, 1-PLAYER)
                print_board(board)
                if check_board(board):
                    active_game = False

        window_surface.blit(background, (0, 0))
        p.draw.rect(window_surface, (0,) * 3, (20, 20, 640, 640), 3)
        for x in range(8):
            for y in range(8):
                p.draw.rect(window_surface, (0,) * 3, (20 + x * 80, 20 + y * 80, 80, 80), 1)
        for row_index, row in enumerate(board):
            for col_index, pos in enumerate(row):
                if pos == WHITE:
                    p.draw.circle(window_surface, (255,) * 3, (60 + 80 * row_index, 60 + 80 * col_index), 35)
                    pass
                elif pos == BLACK:
                    p.draw.circle(window_surface, (0,) * 3, (60 + 80 * row_index, 60 + 80 * col_index), 35)
                    pass
                if (row_index, col_index) in legal_moves:
                    p.draw.circle(window_surface, (120,) * 3, (60 + 80 * row_index, 60 + 80 * col_index), 35, 4)
        p.display.update()

    stats = calculate_heuristics(board, PLAYER)
    player_count, opponent_count = stats['player_count'], stats['opponent_count']
    if player_count > opponent_count:
        print('Congratulations!', PLAYER, 'won!')
    elif player_count < opponent_count:
        print(COMPUTER, 'won.')
    else:
        print('It\'s a tie.')



if __name__ == "__main__":
    main()
