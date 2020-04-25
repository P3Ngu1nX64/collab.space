import sys
import pygame
from pygame.locals import *
import pylette_web as clr

pygame.init()

# set up the window
DISPLAYSURF = pygame.display.set_mode((500, 400), 0, 32)
pygame.display.set_caption('Drawing')

# draw on the surface object
DISPLAYSURF.fill(clr.White)
pygame.draw.polygon(DISPLAYSURF, clr.Green,
                    ((146, 0), (291, 106), (236, 277), (56, 288), (0, 106)))
pygame.draw.line(DISPLAYSURF, clr.Blue, (60, 60), (120, 120), 4)
pygame.draw.line(DISPLAYSURF, clr.Blue, (120, 60), (60, 120))
pygame.draw.line(DISPLAYSURF, clr.Blue, (60, 120), (120, 120), 4)
pygame.draw.circle(DISPLAYSURF, clr.Blue, (300, 50), 20, 0)
pygame.draw.ellipse(DISPLAYSURF, clr.Red, (300, 250, 40, 80), 1)
pygame.draw.rect(DISPLAYSURF, clr.Red, (200, 150, 100, 50))

pixObj = pygame.PixelArray(DISPLAYSURF)
pixObj[480][380] = clr.Black
pixObj[482][382] = clr.Black
pixObj[484][384] = clr.Black
pixObj[486][386] = clr.Black
pixObj[488][388] = clr.Black

# run the game loop
while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit(0)
    pygame.display.update()

# Notes:

# fill (color): Method of pygame.Surface objects, fills entire surface object
# with a certain given color

# pygame.draw.polygon(surface, color, pointlist, width)
# pointlist is a tuple of x-y coordinate tuples (double tuple)
# If width is left default, or 0, polygon (and other shapes) will be filled in
# If width is a value, the polygon will be a line tracing the edges with the
# specified width or thickness. Width is optional.

# pygame.draw.line(surface, color, start_point, end_point, width)
# draws a line between startpoint and endpoint with thickness of width.

# pygame.draw.lines(surface, color, closed, pointlist, width)
# similar to the polygon, but if the boolean closed is False, the first point
# and last point won't connect.

# pygame.draw.circle(surface, color, center_point, radius, width)
# the circle will be located at center_point (x, y tuple) radius sets the size
# of the circle. radius MUST be INT, use ellipse instead if a float is needed.

# pygame.draw.ellipse(surface, color, bounding_rectangle, width)
# a bounding_rectangle can be a pygame.Rect object or a tuple of four integers:
# (x, y, w, h). A centerpoint is not needed.

# pygame.draw.rect(surface, color, rectangle_tuple, width)
# rectangle_tuple can either be (x, y, w, h) or another pygame.Rect object.

# pygame.PixelArray Objects
# It is not possible to directly draw pixles onto the screen
# Pixle arrays are much slower than normal drawing
# When drawing pixle arrays, the surface object is locked, shapes could still
# be drawn but images can't be blitted using the .blit() method
# to check if locked, use the .get_locked() method that returns a boolean.

# pygame.display.update
# Push changes to the user's moniter by updating the display.
