"""
GUI through Pygame for Othello game
Written by Jerrybibo 3/16/2022.
"""
# Only designed for 8x8 boards.

import pygame as p
from pygame.locals import *
from settings import *
from othello import *

p.init()
# Each slot is 80x80 with border width of 20
window_surface = p.display.set_mode((680, 680), 0, 32)
p.display.set_caption("Othello")
background = p.image.load('./background.png')


def click(x, y, player):
    """
    Return the indices for the game board to update, if the position is part of the board
    Note that board is assumed to be 680px*680px and 8x8.
    :param x: The x-position of the mouse relative to the window
    :param y: The y-position of the mouse relative to the window
    :param player: The current player
    """
    # TODO
    pass


def main():
    while 1:
        for e in p.event.get():
            if e.type == QUIT:
                p.quit()
                exit(0)
        window_surface.blit(background, (0, 0))
        p.display.update()


if __name__ == "__main__":
    main()
