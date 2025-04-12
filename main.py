"""
Pygame base template for opening a window

Sample Python/Pygame Programs
Simpson College Computer Science
http://programarcadegames.com/
http://simpson.edu/computer-science/

Explanation video: http://youtu.be/vRB_983kUMc
"""

import pygame
from rectangle import Rectangle
from grid import Grid

# Define some colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
WIDTH = 20
HEIGHT = 20
MARGIN = 5

pygame.init()

# Set the width and height of the screen [width, height]
size = (804, 804)
screen = pygame.display.set_mode(size)

pygame.display.set_caption("My Game")

# Loop until the user clicks the close button.
done = False

# Used to manage how fast the screen updates
clock = pygame.time.Clock()

# -------- Main Program Loop -----------
while not done:
    # --- Main event loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                print("Left mouse button clicked at", event.pos)
                print("row, column:", grid.compute_clicked_field(event.pos))

    # --- Game logic should go here
    grid = Grid(screen, 10, 10, 1)
    # grid = Grid(screen, 20, 20, 5)

    # --- Screen-clearing code goes here

    # Here, we clear the screen to white. Don't put other drawing commands
    # above this, or they will be erased with this command.

    # If you want a background image, replace this clear with blit'ing the
    # background image.
    screen.fill(BLACK)

    # --- Drawing code should go here
    grid.draw()

    # --- Go ahead and update the screen with what we've drawn.
    pygame.display.flip()

    # --- Limit to 60 frames per second
    clock.tick(20)

# Close the window and quit.
pygame.quit()
