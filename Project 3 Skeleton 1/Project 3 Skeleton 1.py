import pygame, sys, time, random
from pygame.locals import *

SCR_WID, SCR_HEI = 1280, 720
screen = pygame.display.set_mode((SCR_WID, SCR_HEI))
clock = pygame.time.Clock()
FPS = 60

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
icon = pygame.image.load("IMAGES/zombieIcon.jpg")
icon = pygame.display.set_icon(icon)

title = pygame.font.Font("FONTS/ZombieFont.ttf", 80)
menuFont = pygame.font.SysFont("Arial", 70)
gameFont= pygame.font.SysFont("Arial", 35)


class Player():
    def __init__(self):
        self.x, self.y = SCR_WID/2, SCR_HEI/2
        self.speed = 30
        self.WIDTH, self.HEIGHT = 60, 60
        
    def movement(self):
        movementKeys = pygame.key.get_pressed()
        if movementKeys[pygame.K_UP] or movementKeys[pygame.K_w]:
            if self.y > 0:
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
        pygame.draw.rect(screen, CYAN, (self.x, self.y, self.WIDTH, self.HEIGHT))

def menu():
    menuAudio = pygame.mixer.Sound('SOUNDS/menuAudio.flac')
    menuAudio.play(-1, 0, 0)
    menuAudio.set_volume(0.10)

    menuBackground = pygame.image.load("IMAGES/MenuBackground.png")
    menuBackgroundScaled = pygame.transform.scale(menuBackground, (SCR_WID, SCR_HEI))

    mainMenuTitle = title.render("CORONA MUTATED!", False, WHITE,)
    play = menuFont.render("PLAY", False, CYAN, DARKERCYAN)
    exit = menuFont.render("EXIT", False, ORANGE, DARKERORANGE)
    screen.blit(menuBackgroundScaled, (0,0))
    screen.blit(mainMenuTitle,(SCR_WID/2 - mainMenuTitle.get_rect().width/2, SCR_HEI/5))
    screen.blit(play,(SCR_WID/2 - play.get_rect().width/2, SCR_HEI/2.2))
    screen.blit(exit,(SCR_WID/2 - exit.get_rect().width/1.8, SCR_HEI/1.5))

    while True:
        clock.tick(FPS)
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

    ambient = pygame.mixer.Sound('SOUNDS/ZombieDistant.wav')
    ambient.play(-1, 0, 0)
    ambient.set_volume(0.30)

    zombieSound = pygame.mixer.Sound('SOUNDS/ZombieSound.wav')
    zombieSound.set_volume(1.50)

    zombieSound2 = pygame.mixer.Sound('SOUNDS/ZombieSound2.wav')
    zombieSound.set_volume(1.50)

    bed = pygame.image.load("IMAGES/BED.png")
    bedScaled = pygame.transform.scale(bed, (SCR_WID, SCR_HEI))
    screen.blit(bedScaled, (0,0))
    story = gameFont.render("WAKE UP " + name + " ! THERE ARE ZOMBIES EVERYWHERE!", False, WHITE, GREY)
    screen.blit(story,(SCR_WID/2 - story.get_rect().width/3, SCR_HEI/6))

    next = pygame.image.load("IMAGES/transparentNext.png")
    nextScaled = pygame.transform.scale(next, (170, 120))
    screen.blit(nextScaled,(SCR_WID - 170, SCR_HEI - 120))

    nextRect= pygame.Rect(SCR_WID - 170, SCR_HEI - 120, nextScaled.get_rect().width, nextScaled.get_rect().height)

    while True:
        clock.tick(FPS)
        mouseXY = pygame.mouse.get_pos()
        randomZombieSound = random.randint(1,20000)
        if randomZombieSound == 1:
            zombieSound.play(0,0,0)

        randomZombieSound2 = random.randint(1,20000)
        if randomZombieSound2 == 1:
            zombieSound2.play(0,0,0)

        for event in pygame.event.get():
            if nextRect.collidepoint(mouseXY):
                if event.type == pygame.MOUSEBUTTONUP:
                    if event.button == 1:
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


def main():
    options = menu()
    if options == "PlayClicked":
        introScreen = intro(str.upper("Issa"))
        if introScreen == "NextClicked":
            player = Player()
            while True:
                screen.fill(BLACK)
                player.draw()
                player.movement()

                for event in pygame.event.get():
                    if event.type == QUIT:
                        pygame.quit()
                        sys.exit()
                
                pygame.display.update()
                clock.tick(FPS) 
main()