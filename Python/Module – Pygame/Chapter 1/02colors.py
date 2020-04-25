# Pygame uses 0-255 RGB sliders for colors, giving it 16777216 possible
# combinations. These values are stored inside tuples.
import pygame
from pygame.locals import *
import pylette_web as clr  # My own color pack, based on HTML colors.


aqua = (0, 255, 255)
black = (0, 0, 0)
blue = (0, 0, 255)
fuchsia = (255, 0, 255)
gray = (128, 128, 128)
green = (0, 128, 0)
lime = (0, 255, 0)
maroon = (128, 0, 0)
navy_blue = (0, 0, 128)
olive = (128, 128, 0)
purple = (128, 0, 128)
red = (255, 0, 0)
silver = (192, 192, 192)
teal = (0, 128, 128)
white = (255, 255, 255)
yellow = (255, 255, 0)

# a fourth value represents alpha, or transparency, where 255 is opaque and
# 0 is transparent

green_tint = (0, 128, 0, 128)

pygame.init()

DISPLAYSURF = pygame.display.set_mode((400, 300))

# A surface object called using .convert_alpha() is required to draw with
# transparent colors:

alt_surface = DISPLAYSURF.convert_alpha()

# After transparent objects are drawn to alt_surface, they can then be "blitted"
# back to DISPLAYSURF so it appears on the screen.

# pygame.image.load() and blits() mentioned later in the chapter.
