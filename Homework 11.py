import pygame, sys, random
from pygame.locals import *

# Set up pygame.
pygame.init()
mainClock = pygame.time.Clock()

# Set up the window.
WINDOWWIDTH = 400
WINDOWHEIGHT = 400
windowSurface = pygame.display.set_mode((WINDOWWIDTH, WINDOWHEIGHT), 0, 32)
pygame.display.set_caption('Input')

# Set up the colors.
BLACK = (0, 0, 0)
GREEN = (0, 255, 0)
WHITE = (255, 255, 255)
CYAN = (19, 139, 143)

# Set up the player and food data structure.
foodCounter = 0
NEWFOOD = 40
FOODSIZE = 20
player1 = pygame.Rect(300, 100, 50, 50)
player2 = pygame.Rect(50, 250, 50, 50)
foods = []
for i in range(20):
    foods.append(pygame.Rect(random.randint(0, WINDOWWIDTH - FOODSIZE), random.randint(0, WINDOWHEIGHT - FOODSIZE), FOODSIZE, FOODSIZE))

# Set up player 1 movement variables.
p1moveLeft = False
p1moveRight = False
p1moveUp = False
p1moveDown = False

# Set up player 2 movement variables
p2moveLeft = False
p2moveRight = False
p2moveUp = False
p2moveDown = False


MOVESPEED = 6


# Run the game loop.
while True:
    # Check for events.
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

        # Player 1 controls
        if event.type == KEYDOWN:
            # Change the keyboard variables.
            if event.key == K_LEFT:
                p1moveRight = False
                p1moveLeft = True
            if event.key == K_RIGHT:
                p1moveLeft = False
                p1moveRight = True
            if event.key == K_UP:
                p1moveDown = False
                p1moveUp = True
            if event.key == K_DOWN:
                p1moveUp = False
                p1moveDown = True
        if event.type == KEYUP:
            if event.key == K_LEFT:
                p1moveLeft = False
            if event.key == K_RIGHT:
                p1moveRight = False
            if event.key == K_UP:
                p1moveUp = False
            if event.key == K_DOWN:
                p1moveDown = False
            if event.key == K_x:
                player1.top = random.randint(0, WINDOWHEIGHT - player1.height)
                player1.left = random.randint(0, WINDOWWIDTH - player1.width)
    
        # Player 2 controls
        if event.type == KEYDOWN:
            # Change the keyboard variables.
            if event.key == K_a:
                p2moveRight = False
                p2moveLeft = True
            if event.key == K_d:
                p2moveLeft = False
                p2moveRight = True
            if event.key == K_w:
                p2moveDown = False
                p2moveUp = True
            if event.key == K_s:
                p2moveUp = False
                p2moveDown = True
        if event.type == KEYUP:
            if event.key == K_a:
                p2moveLeft = False
            if event.key == K_d:
                p2moveRight = False
            if event.key == K_w:
                p2moveUp = False
            if event.key == K_s:
                p2moveDown = False
            if event.key == K_z:
                player2.top = random.randint(0, WINDOWHEIGHT - player2.height)
                player2.left = random.randint(0, WINDOWWIDTH - player2.width)

        if event.type == KEYUP:
            if event.key == K_ESCAPE:
                pygame.quit()
                sys.exit()

        if event.type == MOUSEBUTTONUP:
            foods.append(pygame.Rect(event.pos[0], event.pos[1], FOODSIZE, FOODSIZE))

    foodCounter += 1
    if foodCounter >= NEWFOOD:
        # Add new food.
        foodCounter = 0
        foods.append(pygame.Rect(random.randint(0, WINDOWWIDTH - FOODSIZE), random.randint(0, WINDOWHEIGHT - FOODSIZE), FOODSIZE, FOODSIZE))

    # Draw the white background onto the surface.
    windowSurface.fill(WHITE)

    # Move player 1
    if p1moveDown and player1.bottom < WINDOWHEIGHT:
        player1.top += MOVESPEED
    if p1moveUp and player1.top > 0:
        player1.top -= MOVESPEED
    if p1moveLeft and player1.left > 0:
        player1.left -= MOVESPEED
    if p1moveRight and player1.right < WINDOWWIDTH:
        player1.right += MOVESPEED

    # Move player 2
    if p2moveDown and player2.bottom < WINDOWHEIGHT:
        player2.top += MOVESPEED
    if p2moveUp and player2.top > 0:
        player2.top -= MOVESPEED
    if p2moveLeft and player2.left > 0:
        player2.left -= MOVESPEED
    if p2moveRight and player2.right < WINDOWWIDTH:
        player2.right += MOVESPEED


    # Draw the player onto the surface.
    pygame.draw.rect(windowSurface, BLACK, player1)
    pygame.draw.rect(windowSurface, CYAN, player2)

    # Check if the player has intersected with any food squares.
    for food in foods[:]:
        if player1.colliderect(food) or player2.colliderect(food):
            foods.remove(food)
        

    # Draw the food.
    for i in range(len(foods)):
        pygame.draw.rect(windowSurface, GREEN, foods[i])

    # Draw the window onto the screen.
    pygame.display.update()
    mainClock.tick(40)