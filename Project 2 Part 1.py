import pygame

SCR_WID, SCR_HEI = 640, 480
screen = pygame.display.set_mode((SCR_WID, SCR_HEI))
pygame.display.set_caption("Pong")
pygame.font.init()
clock = pygame.time.Clock()
FPS = 60

class Player():
        def __init__(self, player, screen, SCR_WID, SCR_HEI):

                self.player = player
                self.screen = screen
                self.SCR_WID = SCR_WID
                self.SCR_HEI = SCR_HEI

                self.speed = 3
                self.padWid, self.padHei = 8, 64
                self.score = 0
                self.scoreFont = pygame.font.Font("imagine_font.ttf", 64)

                if self.player == "1":
                        self.x, self.y = 16, self.SCR_HEI/2
                else:
                        # 16 + padWid(8) = 24, but original code isn't symeterical so I will leave it as is (16)
                        self.x, self.y = self.SCR_WID-16, self.SCR_HEI/2
       

        def scoring(self):
                scoreBlit = self.scoreFont.render(str(self.score), 1, (255, 255, 255))
                if self.player == "1":
                        self.screen.blit(scoreBlit, (32, 16))
                else:
                        self.screen.blit(scoreBlit, (self.SCR_HEI+92, 16))
                
                if self.score == 10:
                        print ("Player " + self.player + " wins!")
                        exit()
        
       
        def movement(self):
                keys = pygame.key.get_pressed()
                if self.player == "1":
                        if keys[pygame.K_w]:
                                self.y -= self.speed
                        elif keys[pygame.K_s]:
                                self.y += self.speed
                else:
                        keys = pygame.key.get_pressed()
                        if keys[pygame.K_UP]:
                                self.y -= self.speed
                        elif keys[pygame.K_DOWN]:
                                self.y += self.speed
            
                if self.y <= 0:
                        self.y = 0
                elif self.y >= self.SCR_HEI-64:
                        self.y = self.SCR_HEI-64

       
        def draw(self):
                pygame.draw.rect(self.screen, (255, 255, 255), (self.x, self.y, self.padWid, self.padHei))

 
class Ball():
        def __init__(self, player1, player2, screen, SCR_WID, SCR_HEI):

                self.player1 = player1
                self.player2 = player2
                self.screen = screen
                self.SCR_WID= SCR_WID
                self.SCR_HEI = SCR_HEI                
                
                self.x, self.y = self.SCR_WID/2, self.SCR_HEI/2
                self.speed_x = -3
                self.speed_y = 3
                self.size = 8


        def movement(self):
                self.x += self.speed_x
                self.y += self.speed_y
                
                #wall col
                if self.y <= 0:
                        self.speed_y *= -1
                elif self.y >= self.SCR_HEI-self.size:
                        self.speed_y *= -1
 
                if self.x <= 0:
                        self.x, self.y = self.SCR_WID/2, self.SCR_HEI/2
                        self.speed_y = 3
                        self.speed_x *= 1
                        self.player2.score += 1

                elif self.x >= self.SCR_WID-self.size:
                        self.x, self.y = self.SCR_WID/2, self.SCR_HEI/2
                        self.speed_y = 3
                        self.speed_x *= 1
                        self.player1.score += 1

                ##wall col
                #paddle col
                #player
                for n in range(-self.size, self.player1.padHei):
                        if self.y == self.player1.y + n:
                                if self.x <= self.player1.x + self.player1.padWid:
                                        self.speed_x *= -1
                                        break
                        n += 1
                #player2
                for n in range(-self.size, self.player2.padHei):
                        if self.y == self.player2.y + n:
                                if self.x >= self.player2.x - self.player2.padWid:
                                        self.speed_x *= -1
                                        break
                        n += 1
                ##paddle col
 

        def draw(self):
                pygame.draw.rect(self.screen, (255, 255, 255), (self.x, self.y, 8, 8))


def main():
        player1 = Player("1", screen, SCR_WID, SCR_HEI) 
        player2 = Player("2", screen, SCR_WID, SCR_HEI)
        ball = Ball(player1, player2, screen, SCR_WID, SCR_HEI)

        while True:
                #process
                for event in pygame.event.get():
                                if event.type == pygame.QUIT:
                                        print ("Game exited by user")
                                        exit()
                ##process
                #logic
                ball.movement()
                player1.movement()
                player2.movement()
                ##logic
                #draw
                screen.fill((0, 0, 0))
                ball.draw()
                player1.draw()
                player1.scoring()
                player2.draw()
                player2.scoring()
                ##draw
                #_______
                pygame.display.flip()
                clock.tick(FPS)
main()