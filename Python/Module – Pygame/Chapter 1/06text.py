import sys
import pygame
from pygame.locals import *
import pylette_web as clr


pygame.init()
DISPLAYSURF = pygame.display.set_mode((400, 300))
pygame.display.set_caption('Hello, World!')

# Creates a Font Object (font file, font size (pt/pixels))
fontObj = pygame.font.Font('freesansbold.ttf', 32)

# Creates a surface object with text drawn on it by the Font object's render()
# method. Arguments: text, anti-aliasing (Boolean), font color, background color
textSurfaceObj = fontObj.render('Hello, world!', True, clr.Green, clr.Blue)


textRectObj = textSurfaceObj.get_rect()
textRectObj.center = (200, 150)

while True:  # Main Game Loop
    DISPLAYSURF.fill(clr.White)
    DISPLAYSURF.blit(textSurfaceObj, textRectObj)
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit(0)
    pygame.display.update()

# Notes:
# Anti aliasing is a technique for making objects look less blocky by adding
# a bit of blur to their edges. This takes more computation and makes the
# computer slightly slower than without anti-aliasing

# aliased == blocky
# anti-aliased == blurred == smooth

# When rendering font objects, pass "True" for anti-aliasing.
# For lines, pygame.draw.aaline is the anti-aliased version of pygame.draw.line
# they take the same parameters.
