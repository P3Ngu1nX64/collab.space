# Here is a basic game loop.

import sys
import pygame
from pygame.locals import *
# Imports constant variables, we know that these won't clash with other
# variables or functions so we can import them this way.
# E.g. QUIT is a constant imported from python.locals.QUIT

pygame.init()  # Initializes the Pygame package
# Needs to be called before any other pygame function

DISPLAYSURF = pygame.display.set_mode((400, 300))
# Input is a Tuple (400, 300) in pixles
# Returns a pygame.Surface object to variable DISPLAYSURF

pygame.display.set_caption("Hello, world!")
# Sets the caption

# Main loop - This is a forever loop.
while True:  # main game loop
    for event in pygame.event.get():
        # pygame.event.get() gets all NEW pygame.event.Event objects
        # such as player pressing a key.
        # The loop iterates over the list of events received.
        if event.type == QUIT:
            # Event object has .type attribute
            pygame.quit()
            # Deactivates the pygame library before exiting the program.
            sys.exit(0)
    pygame.display.update()

# What the main game loop does:
# 1: Handles Events
# 2: Updates the game state (variables).
# 3: Draws the game state to the screen

# Extra Notes:

# A constructor function (ctor "see-tor") is a function that returns a new
# Object, or a new instance of a Class.

# Computer Memory is faster than Updating Pixles so Pygame stores changes to
# the display in the pygame.Surface (DISPLAYSURF) object. Multiple actions
# could be performed on the pygame.Surface object simultaneously.
