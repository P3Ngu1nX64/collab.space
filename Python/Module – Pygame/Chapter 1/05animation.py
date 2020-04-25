import sys
import pygame
from pygame.locals import *
import pylette_web as clr

pygame.init()

FPS = 30  # frames per second setting
fpsClock = pygame.time.Clock()
# A clock object prevents the game from running too fast by setting a maximum
# FPS at which the game is allowed to run.


# window setup
DISPLAYSURF = pygame.display.set_mode((400, 300), 0, 32)
pygame.display.set_caption('Animation')

catImg = pygame.image.load('cat.png')
# An image is loaded and another surface object is returned.
# catImg must to then blitted (copied) to DISPLAYSURF for the image to display.
catx = 10
caty = 10
direction = 'right'

# Main Loop
while True:
    DISPLAYSURF.fill(clr.White)
    if direction == 'right':
        catx += 5
        if catx >= 280:
            direction = 'down'
    elif direction == 'down':
        caty += 5
        if caty >= 220:
            direction = 'left'
    elif direction == 'left':
        catx -= 5
        if catx <= 10:
            direction = 'up'
    elif direction == 'up':
        caty -= 5
        if caty <= 10:
            direction = 'right'

    DISPLAYSURF.blit(catImg, (catx, caty))
    # The surface object catImg is copied/blitted to DIPLAYSURF.

    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit(0)

    pygame.display.update()
    fpsClock.tick(FPS)
    # Ticks the clock and adds little pauses to keep the game under max FPS.

# Notes:

# when manipulating blitted/image surface objects, the sprite is referred to
# by it's top left coordinate.

# cannot blit to a surface that is locked (e.g. from a PixelArray that is yet
# to be deleted.)

# Pygame can load PNG, JPG, GIF, and BMP format image files as sprites/surface objects.
