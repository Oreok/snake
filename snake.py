import pygame
import random

# Set the window size
WINDOW_SIZE = (500, 500)

# Define some colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)

# Initialize the game
pygame.init()

# Create the screen
screen = pygame.display.set_mode(WINDOW_SIZE)

# Set the title of the window
pygame.display.set_caption('Snake')

# Set the initial position of the snake
snake_pos = [100, 50]
snake_body = [[100, 50], [90, 50], [80, 50]]

# Create a food block
food_pos = [random.randrange(1, (WINDOW_SIZE[0]//10)) * 10, random.randrange(1, (WINDOW_SIZE[1]//10)) * 10]
food_spawn = True

# Set the initial direction of the snake
direction = 'RIGHT'
changeto = direction

# Set the initial score
score = 0

# Initialize the clock
clock = pygame.time.Clock()

# Define a function to end the game
def game_over():
    # Stop the game loop
    pygame.quit()
    # Exit the program
    sys.exit()

# Game loop
while True:
    # Set the frame rate
    clock.tick(15)

    # Handle key events
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                changeto = 'UP'
            if event.key == pygame.K_DOWN:
                changeto = 'DOWN'
            if event.key == pygame.K_LEFT:
                changeto = 'LEFT'
            if event.key == pygame.K_RIGHT:
                changeto = 'RIGHT'
            if event.key == pygame.K_ESCAPE:
                game_over()

    # Verify that the direction is not opposite to the current direction
    if changeto == 'UP' and direction != 'DOWN':
        direction = 'UP'
    if changeto == 'DOWN' and direction != 'UP':
        direction = 'DOWN'
    if changeto == 'LEFT' and direction != 'RIGHT':
        direction = 'LEFT'
    if changeto == 'RIGHT' and direction != 'LEFT':
        direction = 'RIGHT'

    # Move the snake
    if direction == 'UP':
        snake_pos[1] -= 10
    if direction == 'DOWN':
        snake_pos[1] += 10
    if direction == 'LEFT':
        snake_pos[0] -= 10
    if direction == 'RIGHT':
        snake_pos[0] += 10

    # Snake body growing mechanism
    snake_body.insert(0, list(snake_pos))
    if snake_pos[0] == food_pos[0] and snake_pos[1] == food_pos[1]:
        score += 1
        food_spawn = False
    else:
        snake_body.pop()

    # Spawn food on the screen
    if not food_spawn:
        food_pos = [random.randrange(1, (WINDOW_SIZE[0]//10)) * 10, random.randrange(1, (WINDOW_SIZE[1]//10)) * 10]
        food_spawn = True

    # Draw the screen
    screen.fill(BLACK)

    # Draw the snake
    for pos in snake_body:
        pygame.draw.rect(screen, GREEN, pygame.Rect(pos[0], pos[1], 10, 10))

    # Draw the food
    pygame.draw.rect(screen, WHITE, pygame.Rect(food_pos[0], food_pos[1], 10, 10))

    # Update the display
    pygame.display.update()

    # Check for game over
    if snake_pos[0] < 0 or snake_pos[0] > WINDOW_SIZE[0] - 10:
        game_over()

    if snake_pos[1] < 0 or snake_pos[1] > WINDOW_SIZE[1] - 10:
        game_over()

    for block in snake_body[1:]:
        if snake_pos[0] == block[0] and snake_pos[1] == block[1]:
            game_over()
    
    # Set the title of the window

    pygame.display.set_caption('Snake | Score: ' + str(score))

    # End of the game loop

# End of the program


