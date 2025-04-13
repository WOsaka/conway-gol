import pygame
from rectangle import Rectangle
from grid import Grid
from pattern import Pattern

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

pygame.display.set_caption("Conways Game of Life")

# Loop until the user clicks the close button.
done = False

# Used to manage how fast the screen updates
clock = pygame.time.Clock()

game_running = False

grid = Grid(screen, 10, 10, 1)
pattern = Pattern(grid)  

# -------- Main Program Loop -----------
while not done:
    # --- Main event loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                grid.change_fields_living_status(event)
            if event.button == 3:
                pattern.set_pattern_in_grid(event)

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                game_running = not game_running
            if event.key == pygame.K_q:
                done = True
            if event.key == pygame.K_RIGHT:
                pattern.set_next_pattern()
            if event.key == pygame.K_LEFT:
                pattern.set_prev_pattern()

    # --- Game logic should go here
    if game_running:
        grid.compute_next_generation()

    # --- Screen-clearing code goes here

    # Here, we clear the screen to white. Don't put other drawing commands
    # above this, or they will be erased with this command.

    # If you want a background image, replace this clear with blit'ing the
    # background image.
    screen.fill(BLACK)

    # --- Drawing code should go here
    grid.draw()

    x, y = pygame.mouse.get_pos()
    pattern.draw(x, y)

    # --- Go ahead and update the screen with what we've drawn.
    pygame.display.flip()

    # --- Limit to 60 frames per second
    clock.tick(20)

# Close the window and quit.
pygame.quit()
