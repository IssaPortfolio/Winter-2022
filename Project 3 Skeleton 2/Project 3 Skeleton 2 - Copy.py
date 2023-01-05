
from turtle import width
import pygame, sys, time, random
from pygame.locals import *

SCR_WID, SCR_HEI = 1280, 720
screen = pygame.display.set_mode((SCR_WID, SCR_HEI))
clock = pygame.time.Clock()
FPS = 120
WHITE = (255,255,255)
BLACK = (0,0,0)
CYAN = (0, 234, 255)
DARKERCYAN = (0, 94, 102)
ORANGE = (255, 151, 23)
DARKERORANGE = (135, 62, 30)
GREY = (62, 62, 62)

pygame.font.init()
pygame.init()
pygame.mixer.init()
pygame.display.set_caption("Corona Mutated")

#images
icon = pygame.image.load("IMAGES/zombieIcon.jpg")
icon = pygame.display.set_icon(icon)
menuBackground = pygame.image.load("IMAGES/MenuBackground.png")
bed = pygame.image.load("IMAGES/BED.png")
bedScaled = pygame.transform.scale(bed, (SCR_WID, SCR_HEI))
next = pygame.image.load("IMAGES/transparentNext.png")
nextScaled = pygame.transform.scale(next, (170, 120))
player = pygame.image.load("IMAGES/player.png")

zombie = pygame.image.load("IMAGES/zombie.png")
flipZombie = pygame.transform.flip(zombie, 90, 0)

room = pygame.image.load("IMAGES/room.png")
roomScaled = pygame.transform.scale(room, (SCR_WID, SCR_HEI))
door = pygame.image.load("IMAGES/door.png")
doorScaled = pygame.transform.scale(door, (60, 120))
grey = pygame.image.load("IMAGES/grey.png")
greyScaled = pygame.transform.scale(grey, (SCR_WID, SCR_HEI))

#audio
ambient = pygame.mixer.Sound('SOUNDS/ZombieDistant.wav')
zombieSound = pygame.mixer.Sound('SOUNDS/ZombieSound.wav')
zombieSound2 = pygame.mixer.Sound('SOUNDS/ZombieSound2.wav')
menuAudio = pygame.mixer.Sound('SOUNDS/menuAudio.flac')

#fonts
titleFont = pygame.font.Font("FONTS/ZombieFont.ttf", 80)
menuFont = pygame.font.SysFont("Arial", 70)
gameFont= pygame.font.SysFont("Arial", 35)
doorRect = doorScaled.get_rect()

class Player(pygame.sprite.Sprite):
    roomEdgeOffset = SCR_HEI/6.5
    def __init__(self, WIDTH, HEIGHT, x, y, speed):
        super().__init__()
        self.image = pygame.Surface([WIDTH,HEIGHT])
        self.image.fill(player)
        self.rect = self.image.get_rect()
        self.speed = speed
        self.x = x
        self.y = y


    def movement(self):
        movementKeys = pygame.key.get_pressed()
        if movementKeys[pygame.K_UP] or movementKeys[pygame.K_w]:
            if self.y > self.roomEdgeOffset:
                self.y -= self.speed
        elif movementKeys[pygame.K_DOWN] or movementKeys[pygame.K_s]:
            if self.y < SCR_HEI - self.HEIGHT:
                self.y += self.speed
        elif movementKeys[pygame.K_LEFT] or movementKeys[pygame.K_a]:
            if self.x > 0:
                self.x -= self.speed
        elif movementKeys[pygame.K_RIGHT] or movementKeys[pygame.K_d]:
            if self.x < SCR_WID - self.WIDTH:
                self.x += self.speed

    def draw(self):
        movementKeys = pygame.key.get_pressed()
        if movementKeys[pygame.K_LEFT] or movementKeys[pygame.K_a]:
            flip = pygame.transform.flip(player, 90, 0)
            playerScaled = pygame.transform.scale(flip, (self.WIDTH, self.HEIGHT))
            screen.blit(playerScaled, (self.x,self.y))
        else:
            playerScaled = pygame.transform.scale(player, (self.WIDTH, self.HEIGHT))
            screen.blit(playerScaled, (self.x,self.y))


class Zombies():
    roomEdgeOffset = SCR_HEI/6.5
    def __init__(self):
        self.WIDTH, self.HEIGHT = 50, 50
        self.speed = 14
        self.x, self.y = random.randint(200,SCR_WID - self.WIDTH), random.randint(100, SCR_HEI - self.HEIGHT)
        zombieRect = flipZombie.get_rect()

        
    def movement(self):
        movementKeys = pygame.key.get_pressed()
        randomMovement = random.randint(0,300)
        if randomMovement == 1:
            if self.y > self.roomEdgeOffset:
                self.y -= self.speed
        elif randomMovement == 2:
            if self.y < SCR_HEI - self.HEIGHT:
                self.y += self.speed
        elif randomMovement == 3:
            if self.x > 0:
                self.x -= self.speed
        elif randomMovement == 4:
            if self.x < SCR_WID - self.WIDTH:
                self.x += self.speed

    def draw(self):
        movementKeys = pygame.key.get_pressed()
        zombieScaled = pygame.transform.scale(flipZombie, (self.WIDTH, self.HEIGHT))
        screen.blit(zombieScaled, (self.x,self.y))


class Collision(Player, Zombies):
    def collision(self):
        if pygame.Rect.colliderect(player.get_rect(), zombie.get_rect()):
            print("collided")

def menu():
    menuAudio.play(-1, 0, 0)
    menuAudio.set_volume(0.10)
    menuBackgroundScaled = pygame.transform.scale(menuBackground, (SCR_WID, SCR_HEI))

    mainMenuTitle = titleFont.render("CORONA MUTATED!", False, WHITE,)
    play = menuFont.render("PLAY", False, CYAN, DARKERCYAN)
    exit = menuFont.render("EXIT", False, ORANGE, DARKERORANGE)
    screen.blit(menuBackgroundScaled, (0,0))
    screen.blit(mainMenuTitle,(SCR_WID/2 - mainMenuTitle.get_rect().width/2, SCR_HEI/5))
    screen.blit(play,(SCR_WID/2 - play.get_rect().width/2, SCR_HEI/2.2))
    screen.blit(exit,(SCR_WID/2 - exit.get_rect().width/1.8, SCR_HEI/1.5))

    while True:
        mouseXY = pygame.mouse.get_pos()

        playRect= pygame.Rect(SCR_WID/2 - play.get_rect().width/2, SCR_HEI/2.2, play.get_rect().width, play.get_rect().height) #x,y,width,height
        exitRect= pygame.Rect(SCR_WID/2 - exit.get_rect().width/1.8, SCR_HEI/1.5, exit.get_rect().width + 50, exit.get_rect().height)

        for event in pygame.event.get():
            if playRect.collidepoint(mouseXY):
                if event.type == pygame.MOUSEBUTTONUP:
                    if event.button == 1:
                        menuAudio.set_volume(0)           
                        #game(str.upper(input("Hello, what is your name?: ")))
                        return "PlayClicked"

            if exitRect.collidepoint(mouseXY):
                if event.type == pygame.MOUSEBUTTONUP:
                    if event.button == 1:
                        pygame.quit()
                        sys.exit()

            if event.type == KEYUP:
                if event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    sys.exit()

            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        pygame.display.update() 


def intro(name):
    print("Welcome, " + name + "!")
    ambient.play(-1, 0, 0)
    ambient.set_volume(0.30)
    zombieSound.set_volume(1.50)
    zombieSound2.set_volume(1.50)
    screen.blit(bedScaled, (0,0))
    story = gameFont.render("WAKE UP " + name + " ! THERE ARE ZOMBIES EVERYWHERE!", False, WHITE, GREY)
    screen.blit(story,(SCR_WID/2 - story.get_rect().width/3, SCR_HEI/6))
    screen.blit(nextScaled,(SCR_WID - 170, SCR_HEI - 120))
    nextRect= pygame.Rect(SCR_WID - 170, SCR_HEI - 120, nextScaled.get_rect().width, nextScaled.get_rect().height)



    while True:
        mouseXY = pygame.mouse.get_pos()
        randomZombieSound = random.randint(1,1200)
        if randomZombieSound == 1:
            zombieSound.play(0,0,0)

        randomZombieSound2 = random.randint(1,1200)
        if randomZombieSound2 == 2:
            zombieSound2.play(0,0,0)

        for event in pygame.event.get():
            if nextRect.collidepoint(mouseXY):
                if event.type == pygame.MOUSEBUTTONUP:
                    if event.button == 1:
                        ambient.set_volume(0)
                        return "NextClicked"

            if event.type == KEYUP:
                if event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    sys.exit()

            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
                    
        pygame.display.update()
        clock.tick(FPS)


def game():
    a = False
    player = Player(35, 55, 17.5, SCR_HEI/2 - 27.5, 2.5)
    zombies = []
    for amount in range(random.randint(20,30)):
        zombies.append(Zombies())
    timer = 100
    dead = False
    while True:
        timer -= 1/FPS

        screen.blit(roomScaled, (0,0))
        screen.blit(roomScaled, (0,0))
        timerRender = gameFont.render("MAKE IT TO THE AIRPORT: " + str(int(timer)) + "s", False, CYAN, GREY)
        screen.blit(timerRender, (0,0))
        screen.blit(doorScaled, (SCR_WID - doorScaled.get_rect().width, SCR_HEI/6))
        player.draw()
        player.movement()
        #player.collision()
        
        for zombie in zombies:
            zombie.draw()
            zombie.movement()
            #zombie.collision()

        collisiondetection = Collision()
        collisiondetection.collision()
        for event in pygame.event.get():
            if event.type == KEYUP:
                if event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    sys.exit()

            elif event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit() 
        if timer <= 0:
            dead = titleFont.render("TIMER RAN OUT, YOU DIED!", False, CYAN, BLACK)
            screen.blit(dead, (SCR_WID/2 - dead.get_rect().width/2, SCR_HEI/2 - dead.get_rect().height/2))
            dead = True
  
        pygame.display.update() 

        if dead == True:
            clock.tick(0.000001)
        if dead != True:
            clock.tick(FPS)


def main():
    options = menu()
    if options == "PlayClicked":
        introScreen = intro(str.upper("Issa"))
        if introScreen == "NextClicked":
            mainGame = game()

main()