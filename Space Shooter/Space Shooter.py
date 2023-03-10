#! /usr/bin/env python

#Space Shooter.
#A scrolling arcade shooter.

#
#   Copyright (C) 2009  Tyler Gray, Chad Haley 
#
#   This program is free software: you can redistribute it and/or modify
#   it under the terms of the GNU General Public License as published by
#   the Free Software Foundation, either version 3 of the License, or
#   (at your option) any later version.
#
#   This program is distributed in the hope that it will be useful,
#   but WITHOUT ANY WARRANTY; without even the implied warranty of
#   MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#   GNU General Public License for more details.
#
#   You should have received a copy of the GNU General Public License
#   along with this program.  If not, see <http://www.gnu.org/licenses/>.




#Import
import os, sys, pygame, random
from pygame.locals import *
os.environ['SDL_VIDEO_CENTERED'] = "1"
pygame.init()
pygame.display.set_caption("Space Shooter")
icon = pygame.image.load("Space Shooter.png")
icon = pygame.display.set_icon(icon)
screen = pygame.display.set_mode((800, 600))
pygame.mouse.set_visible(0)

#Background
background = pygame.Surface(screen.get_size())
background = background.convert()
background.fill((0,0,0))
    
#Music
music = pygame.mixer.music.load ("data/music/blassic.ogg") #lost.ogg
pygame.mixer.music.play(-1)


#Load Images
def load_image(name, colorkey=None):
    fullname = os.path.join('data', name)
#   try:
    image = pygame.image.load(fullname)
##    except pygame.error(
##        print 'Cannot load image:', fullname
##        raise SystemExit, message
##    image = image.convert()
    if colorkey is not None:
        if colorkey is -1:
            colorkey = image.get_at((0,0))
        image.set_colorkey(colorkey, RLEACCEL)
    return image, image.get_rect()

#Load Sounds
def load_sound(name):
    class NoneSound:
        def play(self): pass
    if not pygame.mixer or not pygame.mixer.get_init():
        return NoneSound()
    fullname = os.path.join('data', name)
##    try:
    sound = pygame.mixer.Sound(fullname)
##    except pygame.error, message:
##        print 'Cannot load sound:', fullname
##        raise SystemExit, message
    return sound



#Sprites

#This class controls the arena background
class Arena(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image, self.rect = load_image("menu/arena.jpg", -1)
        self.dy = 5
        self.reset()
        
    def update(self):
        self.rect.bottom += self.dy
        if self.rect.bottom >= 1200:
            self.reset() 
    
    def reset(self):
        self.rect.top = -600
        

#Player
class Player(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image, self.rect = load_image("sprites/player.png", -1)
        self.rect.center = (400,500)
        self.dx = 0
        self.dy = 0
        self.reset()
        self.lasertimer = 0
        self.lasermax = 5
        self.bombamount = 1
        self.bombtimer = 0
        self.bombmax = 10
        
    def update(self):
        self.rect.move_ip((self.dx, self.dy))
        
        #Fire the laser
        key = pygame.key.get_pressed()
        if key[pygame.K_SPACE]:
            self.lasertimer = self.lasertimer + 1
            if self.lasertimer == self.lasermax:
                laserSprites.add(Laser(self.rect.midtop))
                fire.play()
                self.lasertimer = 0
                 
        #Fire the bomb          
        if key[pygame.K_LCTRL]:
            self.bombtimer = self.bombtimer + 1
            if  self.bombtimer == self.bombmax:
                self.bombtimer = 0
                if self.bombamount > 0:
                    self.bombamount = self.bombamount -1
                    score.bomb += -1
                    bombSprites.add(Bomb(self.rect.midtop))
                    torpedo.play()
                    
                                
        #Player Boundaries    
        if self.rect.left < 0:
          self.rect.left = 0
        elif self.rect.right > 800:
          self.rect.right = 800
         
        if self.rect.top <= 260:
          self.rect.top = 260
        elif self.rect.bottom >= 600:
          self.rect.bottom = 600
         
          
        
    def reset(self):
        self.rect.bottom = 600  




#Laser class
class Laser(pygame.sprite.Sprite):
    def __init__(self, pos):
        pygame.sprite.Sprite.__init__(self)
        self.image, self.rect = load_image("sprites/laser.png", -1)
        self.rect.center = pos

    
    def update(self):
        if self.rect.top < 0:
            self.kill()
        else:    
            self.rect.move_ip(0, -15)  
                

#Bomb class
class Bomb(pygame.sprite.Sprite):
    def __init__(self, pos):
        pygame.sprite.Sprite.__init__(self)
        self.image, self.rect = load_image("sprites/bomb.png", -1)
        self.rect.center = pos
    
    def update(self):
        if self.rect.top < 0:
            self.kill()
        else:    
            self.rect.move_ip(0, -5)
        if pygame.sprite.groupcollide(enemySprites, bombSprites, 1, 1):
               bombExplosionSprites.add(BombExplosion(self.rect.center))
               explode.play()

#Laser class
class EnemyLaser(pygame.sprite.Sprite):
    def __init__(self, pos):
        pygame.sprite.Sprite.__init__(self)
        self.image, self.rect = load_image("sprites/elaser.png", -1)
        self.rect.center = pos

    
    def update(self):
        if self.rect.bottom < 0:
            self.kill()
        else:    
            self.rect.move_ip(0, 15) 
   

#Enemy class
class Enemy(pygame.sprite.Sprite):
    def __init__(self, centerx):
        pygame.sprite.Sprite.__init__(self)
        self.image, self.rect = load_image("sprites/enemy.png", -1)
        self.rect = self.image.get_rect()
        self.dy = 8
        self.reset()
        
    def update(self):
        self.rect.centerx += self.dx
        self.rect.centery += self.dy
        if self.rect.top > screen.get_height():
            self.reset()
           
        #random 1 - 60 determines if firing
        efire = random.randint(1,60)
        if efire == 1:
            enemyLaserSprites.add(EnemyLaser(self.rect.midbottom))
            efire = load_sound("sounds/elaser.ogg")
            efire.play()
            
        #Laser Collisions    
        if pygame.sprite.groupcollide(enemySprites, laserSprites, 1, 1):
           explosionSprites.add(EnemyExplosion(self.rect.center))
           explode.play()
           score.score += 10
            
        #Bomb Collisions    
        if pygame.sprite.groupcollide(enemySprites, bombSprites, 1, 1):
           bombExplosionSprites.add(BombExplosion(self.rect.center))
           explode.play()
           score.score += 10
            
        #Bomb Explosion Collisions    
        if pygame.sprite.groupcollide(enemySprites, bombExplosionSprites, 1, 0):
           explosionSprites.add(EnemyExplosion(self.rect.center))
           explode.play()
           score.score += 10

    
    def reset(self):
        self.rect.bottom = 0
        self.rect.centerx = random.randrange(0, screen.get_width())
        self.dy = random.randrange(5, 10)
        self.dx = random.randrange(-2, 2)

#Banana enemy class
class EnemyBanana(pygame.sprite.Sprite):
    def __init__(self, centerx):
        pygame.sprite.Sprite.__init__(self)
        self.image, self.rect = load_image("sprites/Banana.png", -1)
        self.rect = self.image.get_rect()
        self.dy = 8
        self.reset()

        
        
    def update(self):
        self.rect.centerx += self.dx
        self.rect.centery += self.dy
        if self.rect.top > screen.get_height():
            self.reset()
           
            
        #Laser Collisions    
        if pygame.sprite.groupcollide(bananaSprites, laserSprites, 1, 1):
           explosionSprites.add(EnemyExplosion(self.rect.center))
           explode.play()
           score.score += 5
            
        #Bomb Collisions    
        if pygame.sprite.groupcollide(bananaSprites, bombSprites, 1, 1):
           bombExplosionSprites.add(BombExplosion(self.rect.center))
           explode.play()
           score.score += 5
            
        #Bomb Explosion Collisions    
        if pygame.sprite.groupcollide(enemySprites, bombExplosionSprites, 1, 0):
           explosionSprites.add(EnemyExplosion(self.rect.center))
           explode.play()
           score.score += 5

    
    def reset(self):
        self.rect.bottom = 0
        self.rect.centerx = random.randrange(0, screen.get_width())
        self.dy = random.randrange(5, 10)
        self.dx = random.randrange(-2, 2)



        
class Shield(pygame.sprite.Sprite):
    def __init__(self, pos):
        pygame.sprite.Sprite.__init__(self)
        self.image, self.rect = load_image("sprites/shield.png", -1)
        self.rect.center = pos
        self.counter = 0
        self.maxcount = 2
    def update(self):
        self.counter = self.counter + 1
        if self.counter == self.maxcount:
            self.kill()
            
class EnemyExplosion(pygame.sprite.Sprite):
    def __init__(self, pos):
        pygame.sprite.Sprite.__init__(self)
        self.image, self.rect = load_image("sprites/enemyexplosion.png", -1)
        self.rect.center = pos        
        self.counter = 0
        self.maxcount = 10
    def update(self):
        self.counter = self.counter + 1
        if self.counter == self.maxcount:
            self.kill()
            
class BombExplosion(pygame.sprite.Sprite):
    def __init__(self, pos):
        pygame.sprite.Sprite.__init__(self)
        self.image, self.rect = load_image("sprites/bombexplosion.png", -1)
        self.rect.center = pos        
        self.counter = 0
        self.maxcount = 5
    def update(self):
        self.counter = self.counter + 1
        if self.counter == self.maxcount:
            self.kill()
            
#Bomb Powerup
class BombPowerup(pygame.sprite.Sprite):
    def __init__(self, centerx):
        pygame.sprite.Sprite.__init__(self)
        self.image, self.rect = load_image("sprites/torpedopowerup.png", -1)
        self.rect = self.image.get_rect()
        self.rect.centerx = random.randrange(0, screen.get_width())
     
        
    def update(self):
        if self.rect.top > screen.get_height():
            self.kill
        else:    
            self.rect.move_ip(0, 6) 

#Shield Powerup
class ShieldPowerup(pygame.sprite.Sprite):
    def __init__(self, centerx):
        pygame.sprite.Sprite.__init__(self)
        self.image, self.rect = load_image("sprites/shieldpowerup.png", -1)
        self.rect = self.image.get_rect()
        self.rect.centerx = random.randrange(0, screen.get_width())
     
        
    def update(self):
        if self.rect.top > screen.get_height():
            self.kill
        else:    
            self.rect.move_ip(0, 6)         
        
class Score(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.shield = 100
        self.score = 0
        self.bomb = 1
        self.font = pygame.font.Font("data/fonts/arial.ttf", 28)
        
    def update(self):
        self.text = "Shield: %d                        Score: %d                        Torpedo: %d" % (self.shield, self.score, self.bomb)
        self.image = self.font.render(self.text, 1, (0, 255, 0))
        self.rect = self.image.get_rect()
        self.rect.center = (400,20)
        
class Gameover(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.font = pygame.font.Font("data/fonts/planet5.ttf", 48)
        
    def update(self):
        self.text = ("GAME OVER")
        self.image = self.font.render(self.text, 1, (0, 255, 0))
        self.rect = self.image.get_rect()
        self.rect.center = (400,300)
        
class Gameoveresc(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.font = pygame.font.Font("data/fonts/arial.ttf", 28)
        
    def update(self):
        self.text = "PRESS ESC TO RETURN"
        self.image = self.font.render(self.text, 1, (0, 255, 0))
        self.rect = self.image.get_rect()
        self.rect.center = (400,400)
                    
#Game Module    
def game():
 
    #Game Objects
    global player
    player = Player()
    global score
    score = Score()
    
    global fire
    fire = load_sound("sounds/laser.ogg")
    global explode
    explode = load_sound("sounds/explode.ogg")
    global torpedo
    torpedo = load_sound("sounds/torpedo.ogg")
    global powerup
    powerup = load_sound("sounds/powerup.ogg")
    
    #Game Groups
    
    #Player/Enemy
    playerSprite = pygame.sprite.RenderPlain((player))
    
    global enemySprites
    enemySprites = pygame.sprite.RenderPlain(())
    enemySprites.add(Enemy(200))
    enemySprites.add(Enemy(300))
    enemySprites.add(Enemy(400))

    #banana enemy 
    global bananaSprites
    bananaSprites = pygame.sprite.RenderPlain(())
    bananaSprites.add(EnemyBanana(200))
    bananaSprites.add(EnemyBanana(300))
    bananaSprites.add(EnemyBanana(400))
    
    #Projectiles
    global laserSprites
    laserSprites = pygame.sprite.RenderPlain(())
    
    global bombSprites
    bombSprites = pygame.sprite.RenderPlain(())
    global enemyLaserSprites
    enemyLaserSprites = pygame.sprite.RenderPlain(())
    
    #Powerups
    global bombPowerups
    bombPowerups = pygame.sprite.RenderPlain(())
    global shieldPowerups
    shieldPowerups = pygame.sprite.RenderPlain(())
    
    #Special FX
    shieldSprites = pygame.sprite.RenderPlain(())
    
    global explosionSprites
    explosionSprites = pygame.sprite.RenderPlain(())
    
    global bombExplosionSprites
    bombExplosionSprites = pygame.sprite.RenderPlain(())
    
    #Score/and game over
    scoreSprite = pygame.sprite.Group(score)
    gameOverSprite = pygame.sprite.RenderPlain(())
    
    #Arena
    arena = Arena()
    arena = pygame.sprite.RenderPlain((arena))
    
    
    #Set Clock
    clock = pygame.time.Clock()
    keepGoing = True
    counter = 0
  
    #Main Loop
    while keepGoing:
       clock.tick(30)
       #input
       for event in pygame.event.get():
            if event.type == pygame.QUIT:
                keepGoing = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    keepGoing = False
                elif event.key == pygame.K_LEFT:
                    player.dx = -10
                elif event.key == K_RIGHT:
                    player.dx = 10
                elif event.key == K_UP:
                    player.dy = -10
                elif event.key == K_DOWN:
                    player.dy = 10
            elif event.type == KEYUP:
                if event.key == K_LEFT:
                    player.dx = 0
                elif event.key == K_RIGHT:
                    player.dx = 0
                elif event.key == K_UP:
                    player.dy = 0
                elif event.key == K_DOWN:
                  player.dy = 0
                
             
             
       #Update and draw on the screen
       
       #Update     
       screen.blit(background, (0,0))     
       playerSprite.update()
       enemySprites.update()
       bananaSprites.update()
       laserSprites.update()
       bombSprites.update()
       enemyLaserSprites.update()
       bombPowerups.update()
       shieldPowerups.update()
       shieldSprites.update()
       explosionSprites.update()
       bombExplosionSprites.update()
       arena.update()
       scoreSprite.update()
       gameOverSprite.update()
       
       #Draw
       arena.draw(screen)
       playerSprite.draw(screen)
       enemySprites.draw(screen)
       bananaSprites.draw(screen)
       laserSprites.draw(screen)
       bombSprites.draw(screen)
       enemyLaserSprites.draw(screen)
       bombPowerups.draw(screen)
       shieldPowerups.draw(screen)
       shieldSprites.draw(screen)
       explosionSprites.draw(screen)
       bombExplosionSprites.draw(screen)
       scoreSprite.draw(screen)
       gameOverSprite.draw(screen)
       pygame.display.flip()
     
       #Spawn new enemies
       counter += 1
       if counter >= 20:
          enemySprites.add(Enemy(300))
          counter = 0

       randomBanana = random.randint(1,300)
       if randomBanana == 10:
          bananaSprites.add(EnemyBanana(300))

       
       #Spawn Shield Power up
       #shieldPowerupcounter += 1
       spawnShieldpowerup = random.randint(1,500)
       if spawnShieldpowerup == 1:
          shieldPowerups.add(ShieldPowerup(300))
          
        
       #Spawn Bomb Power up
       spawnBombpowerup = random.randint(1,500)
       if spawnBombpowerup == 1:
          bombPowerups.add(BombPowerup(300))
          bombPowerupcounter = 0
      
      
       #Check if enemy lasers hit player's ship   
       for hit in pygame.sprite.groupcollide(enemyLaserSprites, playerSprite, 1, 0):
           explode.play()
           explosionSprites.add(Shield(player.rect.center))
           score.shield -= 10
           if score.shield <= 0:
              gameOverSprite.add(Gameover())
              gameOverSprite.add(Gameoveresc())
              playerSprite.remove(player)

          
       #Check if enemy collides with player 
       for hit in pygame.sprite.groupcollide(enemySprites, playerSprite, 1, 0):
           explode.play()
           explosionSprites.add(Shield(player.rect.center))
           score.shield -= 10
           if score.shield <= 0:
              gameOverSprite.add(Gameover())
              gameOverSprite.add(Gameoveresc())
              playerSprite.remove(player)

       for hit in pygame.sprite.groupcollide(bananaSprites, playerSprite, 1, 0):
           explode.play()
           explosionSprites.add(Shield(player.rect.center))
           score.shield -= 5
           if score.shield <= 0:
              gameOverSprite.add(Gameover())
              gameOverSprite.add(Gameoveresc())
              playerSprite.remove(player)
              
       #Check if player collides with shield powerup       
       for hit in pygame.sprite.groupcollide(shieldPowerups, playerSprite, 1, 0):
            if score.shield < 100:
               powerup.play()
               score.shield += 10
             
       #Check if player collides with bomb powerup    
       for hit in pygame.sprite.groupcollide(bombPowerups, playerSprite, 1, 0):
           powerup.play()
           player.bombamount += 1
           score.bomb += 1
           
#Class Module
class SpaceMenu:

#Define the initalize self options
    def __init__(self, *options):

        self.options = options
        self.x = 0
        self.y = 0
        self.font = pygame.font.Font(None, 32)
        self.option = 0
        self.width = 1
        self.color = [0, 0, 0]
        self.hcolor = [0, 0, 0]
        self.height = len(self.options)*self.font.get_height()
        for o in self.options:
            text = o[0]
            ren = self.font.render(text, 1, (0, 0, 0))
            if ren.get_width() > self.width:
                self.width = ren.get_width()

#Draw the menu
    def draw(self, surface):
        i=0
        for o in self.options:
            if i==self.option:
                clr = self.hcolor
            else:
                clr = self.color
            text = o[0]
            ren = self.font.render(text, 1, clr)
            if ren.get_width() > self.width:
                self.width = ren.get_width()
            surface.blit(ren, (self.x, self.y + i*self.font.get_height()))
            i+=1

#Menu Input            
    def update(self, events):
        for e in events:
            if e.type == pygame.KEYDOWN:
                if e.key == pygame.K_DOWN:
                    self.option += 1
                if e.key == pygame.K_UP:
                    self.option -= 1
                if e.key == pygame.K_RETURN:
                    self.options[self.option][1]()
        if self.option > len(self.options)-1:
            self.option = 0
        if self.option < 0:
            self.option = len(self.options)-1

#Position Menu
    def set_pos(self, x, y):
        self.x = x
        self.y = y

#Font Style        
    def set_font(self, font):
        self.font = font

#Highlight Color        
    def set_highlight_color(self, color):
        self.hcolor = color

#Font Color        
    def set_normal_color(self, color):
        self.color = color

#Font position        
    def center_at(self, x, y):
        self.x = x-(self.width/2)
        self.y = y-(self.height/2)
        
        

def missionMenu():
    
    #Arena
    arena = Arena()
    arena = pygame.sprite.RenderPlain((arena))
    

    #Title for Option Menu
    menuTitle = SpaceMenu(
        ["Space Shooter"])

    #Option Menu Text
    instructions = SpaceMenu(
        [""], 
        ["Aliens from the planet Solaris have entered earth's sub"],
        [""],
        ["space and plan to destroy the Earth! You are our last hope!"],
        [""],
        ["Navigate your space cruiser with the arrow keys and use"],
        [""],
        ["the space bar to fire the proton laser. Use the left CTRL"],
        [""],
        ["key to shoot a torpedo. Be careful, you have a limited"],
        [""],
        ["supply. Kill as many enemies as you can!"],
        [""],
        [""],
        ["                   PRESS ESC TO RETURN                    "])

    #Title 
    menuTitle.center_at(150, 150)
    menuTitle.set_font(pygame.font.Font("data/fonts/planet5.ttf", 48))
    menuTitle.set_highlight_color((0, 255, 0))
        

    #Title Center
    instructions.center_at(440, 350)

    #Menu Font
    instructions.set_font(pygame.font.Font("data/fonts/arial.ttf", 22))

    #Highlight Color
    instructions.set_normal_color((0, 255, 0))


    #Set Clock
    clock = pygame.time.Clock()
    keepGoing = True

    while keepGoing:
           clock.tick(30)
           #input
           for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    keepGoing = False
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        keepGoing = False
           #Draw
           screen.blit(background, (0,0))    
           arena.update()
           arena.draw(screen)
           menuTitle.draw(screen)
           instructions.draw(screen)
           pygame.display.flip()




def aboutMenu():
 
    #Arena
    arena = Arena()
    arena = pygame.sprite.RenderPlain((arena))
    
    #About Menu Text
    #Title for Option Menu
    menuTitle = SpaceMenu(
        ["Space Shooter"])

    info = SpaceMenu(
        [""], 
        ["Space Shooter Beta"],
        [""],
        ["Devloped by the Monty Pythons."],
        [""],
        ["Student's from Mr. Raza's DPT 110 class"],
        [""],
        [""],
        ["      PRESS ESC TO RETURN            "])
        

    #About Title Font color, alignment, and font type
    menuTitle.center_at(150, 150)
    menuTitle.set_font(pygame.font.Font("data/fonts/planet5.ttf", 48))
    menuTitle.set_highlight_color((0, 255, 0))

    #About Menu Text Alignment
    info.center_at(400, 310)

    #About Menu Font
    info.set_font(pygame.font.Font("data/fonts/arial.ttf", 28))

    #About Menu Font Color
    info.set_normal_color((0, 255, 0))


    #Set Clock
    clock = pygame.time.Clock()
    keepGoing = True

    while keepGoing:
           clock.tick(30)
           #input
           for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    keepGoing = False
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        keepGoing = False
           #Draw
           screen.blit(background, (0,0))    
           arena.update()
           arena.draw(screen)
           menuTitle.draw(screen)
           info.draw(screen)
           pygame.display.flip()

#Functions

def option1():
    game()
def option2():
    missionMenu()
def option3():
    aboutMenu()   
def option4():
    pygame.quit()
    sys.exit()
    
        

#Main
def main():

    
    #Arena
    arena = Arena()
    arena = pygame.sprite.RenderPlain((arena))

   
    #Defines menu, option functions, and option display. For example,
    #Changing "Start" to "Begin" will display Begin, instead of start. 
    menuTitle = SpaceMenu(
        ["Space Shooter"])
        
    menu = SpaceMenu(
        ["Start", option1],
        ["Misson", option2],
        ["About", option3],
        ["Quit", option4])
        
        

    #Title
    menuTitle.center_at(150, 150)
    menuTitle.set_font(pygame.font.Font("data/fonts/planet5.ttf", 48))
    menuTitle.set_highlight_color((0, 255, 0))
    
    #Menu settings
    menu.center_at(400, 320)
    menu.set_font(pygame.font.Font("data/fonts/arial.ttf", 32))
    menu.set_highlight_color((0, 255, 0))
    menu.set_normal_color((0, 85, 0))
    
    clock = pygame.time.Clock()
    keepGoing = True


    while 1:
        clock.tick(30)

        #Events
        events = pygame.event.get()

        #Update Menu
        menu.update(events)

        #Quit Event
        for e in events:
            if e.type == pygame.QUIT:
                pygame.quit()
                return

        #Draw
        screen.blit(background, (0,0))
        arena.update()
        arena.draw(screen)
        menu.draw(screen)
        menuTitle.draw(screen)
        pygame.display.flip()

if __name__ == "__main__":
   main()