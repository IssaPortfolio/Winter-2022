import pygame
import random

pygame.init()

class Player():
        def __init__(self, name):
                if name == "hero":
                    self.x, self.y = 16, SCR_HEI/2
                else:
                    self.x, self.y = SCR_WID-24, SCR_HEI/2
                self.speed = 4
                self.padWid, self.padHei = 8, 64
                self.score = 0
                self.scoreFont = pygame.font.Font("imagine_font.ttf", 64)
       
        def scoring(self, name):
                scoreBlit = self.scoreFont.render(str(self.score), 1, (255, 255, 255))
                if name == "hero":
                    screen.blit(scoreBlit, (32, 16))
                    if self.score == 10:
                        print ("Player 1 wins!")
                        exit()
                else:
                    screen.blit(scoreBlit, (SCR_HEI+92, 16))
                    if self.score == 10:
                        print ("Player 2 wins!")
                        exit()
       
        def movement(self, name):
                keys = pygame.key.get_pressed()
                if name == "hero":
                    if keys[pygame.K_w]:
                            self.y -= self.speed
                    elif keys[pygame.K_s]:
                            self.y += self.speed
                    if self.y <= 0:
                            self.y = 0
                    elif self.y >= SCR_HEI-64:
                            self.y = SCR_HEI-64
                else:
                    if keys[pygame.K_UP]:
                            self.y -= self.speed
                    elif keys[pygame.K_DOWN]:
                            self.y += self.speed
       
                    if self.y <= 0:
                            self.y = 0
                    elif self.y >= SCR_HEI-64:
                            self.y = SCR_HEI-64
       
        def draw(self):
                pygame.draw.rect(screen, (255, 255, 255), (self.x, self.y, self.padWid, self.padHei))
 


class Ball():
        def __init__(self):
                self.x, self.y = SCR_WID/2, SCR_HEI/2
                self.speed_x = random.randint(-3,-2)
                self.speed_y = random.randint(2,5)
                self.size = 8
       
        def movement(self):
                self.x += self.speed_x
                self.y += self.speed_y

                #wall col
                if self.y <= 0:
                        self.speed_y *= -1
                        collisionSound = pygame.mixer.Sound('Bounce.wav')
                        collisionSound.play()
                elif self.y >= SCR_HEI-self.size:
                        self.speed_y *= -1
                        collisionSound = pygame.mixer.Sound('Bounce.wav')
                        collisionSound.play()
 
                if self.x <= 0:
                        self.__init__()
                        enemy.score += 1
                        edgeSound = pygame.mixer.Sound('Edge.wav')
                        edgeSound.play()
                elif self.x >= SCR_WID-self.size:
                        self.__init__()
                        self.speed_x = 3
                        player.score += 1
                        edgeSound = pygame.mixer.Sound('Edge.wav')
                        edgeSound.play()
                ##wall col
                #paddle col
                #player
                for n in range(-self.size, player.padHei):
                        if self.y == player.y + n:
                                if self.x <= player.x + player.padWid:
                                        self.speed_x *= -1
                                        collisionSound = pygame.mixer.Sound('Bounce.wav')
                                        collisionSound.play()
                                        break
                        n += 1
                #enemy
                for n in range(-self.size, enemy.padHei):
                        if self.y == enemy.y + n:
                                if self.x >= enemy.x - enemy.padWid:
                                        self.speed_x *= -1
                                        collisionSound = pygame.mixer.Sound('Bounce.wav')
                                        collisionSound.play()
                                        break
                        n += 1
                ##paddle col
 
        def draw(self):
                pygame.draw.rect(screen, (255, 255, 255), (self.x, self.y, 8, 8))



SCR_WID, SCR_HEI = 640, 480
pygame.font.init()

player = Player("hero") 
ball = Ball()
ball2 = Ball()
enemy = Player("enemy")

CYAN = (19, 139, 143)
ORANGE = (239, 111, 54)
screen = pygame.display.set_mode((SCR_WID, SCR_HEI))
clock = pygame.time.Clock()
FPS = 60

backgroundSound = pygame.mixer.Sound('BackgroundAudio.wav')
backgroundSound.play(-1, 0, 0)
backgroundSound.set_volume(0.15)

backgroundImage = pygame.image.load("court1.png")
backgroundImage2 = pygame.image.load("court2.png")

def main():
    while True:
        #process
        for event in pygame.event.get():
                        if event.type == pygame.QUIT:
                                print ("Game exited by user")
                                exit()
        ##process
        #logic
        ball.movement()
        player.movement("hero")
        enemy.movement("enemy")
        ##logic
        #draw
        #Changes background if the player or enemy reaches 5 and adds a new ball
        if player.score <= 5 and enemy.score <= 5:
                screen.blit(backgroundImage, (0, 0))
        else:
                screen.blit(backgroundImage2, (0, 0))
                ball2.draw()
                ball2.movement()
        
        ball.draw()
        player.draw()
        player.scoring("hero")
        enemy.draw()
        enemy.scoring("enemy")
        ##draw
        #_______
        pygame.display.flip()

        clock.tick(FPS)
main()
