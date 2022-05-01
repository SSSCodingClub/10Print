import pygame
import random

# Dimensions of window to create, in pixels.
SCREEN_WIDTH = 720
SCREEN_HEIGHT = 720

# Creates the window, gives us a pygame.Surface object which can be drawn onto. When
# pygame.display.update() is called, the contents of the Surface object will be displayed to the 
# user in the window.
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

DRAWING_DELAY_MS = 10

NUM_COLUMNS = 20
NUM_ROWS = 20

CELL_WIDTH = SCREEN_WIDTH / NUM_COLUMNS
CELL_HEIGHT = SCREEN_HEIGHT / NUM_ROWS

current_column = 0
current_row = 0

DRAW_CELL_EVENT = pygame.USEREVENT
pygame.time.set_timer(DRAW_CELL_EVENT, DRAWING_DELAY_MS, NUM_COLUMNS * NUM_ROWS)

# Infinite loop until set to False
is_running = True
while is_running:
    
    # Gets all unprocessed events and loops over each one...
    for event in pygame.event.get():
        # If user pressed red X (wants to close the window)
        if event.type == pygame.QUIT:
            is_running = False # End the infinite loop

        # Add another cell to our "image"
        elif event.type == DRAW_CELL_EVENT:

            top = current_row * CELL_HEIGHT
            left = current_column * CELL_WIDTH
            bottom = top + CELL_HEIGHT
            right = left + CELL_WIDTH

            if random.random() < 0.5:
                point1 = (left, top)
                point2 = (right, bottom)
            else:
                point1 = (left, bottom)
                point2 = (right, top)

            pygame.draw.line(screen, (255, 255, 255), point1, point2, 3)

            current_column += 1
            if current_column >= NUM_COLUMNS:
                current_row += 1
                current_column = 0 

    # Updates window contents
    pygame.display.update()

pygame.quit()