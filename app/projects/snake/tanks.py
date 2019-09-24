# ====================================================================#
#                               TANKS
# ====================================================================#

import pygame
import time, random,math
from vector import *
from physics import *
from levels import *


class bullet(physics):
    def __init__(self,pos,state,host):
        
        super(bullet,self).__init__(pos)
        self.bulletDown = pygame.image.load('resources/images/bulletDown.png')
        self.bulletUp = pygame.image.load('resources/images/bulletUp.png')
        self.bulletLeft = pygame.image.load('resources/images/bulletLeft.png')
        self.bulletRight = pygame.image.load('resources/images/bulletRight.png')
        self.activeState = state
        self.velocity.z = 0
        self.display = True
        self.belong = host
        if host == 'player':
            if state == 'up':
                self.pos[0] += 14+11/2;self.pos[1]-=11
            if state == 'down':
                self.pos[0] += 14+11/2;self.pos[1]+=51
            if state == 'left':
                self.pos[0] -=20;self.pos[1]+= 14+11/2
            if state == 'right':
                self.pos[0] +=51;self.pos[1]+= 14+11/2
        if host == 'enemy':
            if state == 'up':
                self.pos[0] += 14+11/2;self.pos[1]-=11
            if state == 'down':
                self.pos[0] += 14+11/2;self.pos[1]+=51
            if state == 'left':
                self.pos[0] -=20;self.pos[1]+= 14+11/2
            if state == 'right':
                self.pos[0] +=51;self.pos[1]+= 14+11/2
    def turnLeft(self):
        screen.blit(self.bulletLeft,(self.pos[0],self.pos[1]))
        self.velocity.x = -25
        self.velocity.y = 0
        self.updatePos()
    def turnRight(self):
        screen.blit(self.bulletRight,(self.pos[0],self.pos[1]))
        self.velocity.x = 25
        self.velocity.y = 0
        self.updatePos()
    def turnUp(self):
        screen.blit(self.bulletUp,(self.pos[0],self.pos[1]))
        self.velocity.x = 0
        self.velocity.y = -25
        self.updatePos()
    def turnDown(self):
        screen.blit(self.bulletDown,(self.pos[0],self.pos[1]))
        self.velocity.x = 0
        self.velocity.y = 25
        self.updatePos()
    
class tank(physics):
    
    def __init__(self,pos):
        super(tank,self).__init__(pos)
        self.bullet = 8000
        self.health = 100
        self.fireRate = 6 # rate of fire of bullets
        self.damageRate = 5 
        self.damage = True
        self.fire = False   # True when tank fire a bullet
        self.bullet = pygame.image.load('resources/images/bulletDown.png')
        self.rest = False # defines when the tank is at rest or not
        # velocity of the tank
        self.velocity.x = 0
        self.velocity.y = random.uniform(2,5)
        self.velocity.z = 0
        self.timer = 0.0
        self.damage = 50 
        self.alive = True # false when health becomes zero
    def loadFiles(self,_type_):
        if _type_ == 'player':
            self.activeState = 'up'
            self.tankUp = pygame.image.load('resources/images/tankUp.png')
            self.tankDown = pygame.image.load('resources/images/tankDown.png')
            self.tankRight = pygame.image.load('resources/images/tankRight.png')
            self.tankLeft = pygame.image.load('resources/images/tankLeft.png')
            self.health = 200
            self.damage = 50 
        elif _type_ == 'enemy':
            self.activeState = 'down'
            self.tankUp = pygame.image.load('resources/images/enemyUp.png')
            self.tankDown = pygame.image.load('resources/images/enemyDown.png')
            self.tankRight = pygame.image.load('resources/images/enemyRight.png')
            self.tankLeft = pygame.image.load('resources/images/enemyLeft.png')
            self.health = 100
            self.damage = 25
            #self.fire = True
    def turnLeft(self):
        screen.blit(self.tankLeft,(self.pos[0],self.pos[1]))
    def turnRight(self):
        screen.blit(self.tankRight,(self.pos[0],self.pos[1]))
    def turnUp(self):
        screen.blit(self.tankUp,(self.pos[0],self.pos[1]))
    def turnDown(self):
        screen.blit(self.tankDown,(self.pos[0],self.pos[1]))
    def fireBullet(self):
        screen.blit(self.bullet,(0,0))
    def controlTimer(self,host):
        
        if host == 'player':
            if self.timer > 0 :
                self.timer -= 5
                            
        if host == 'enemy':
            if self.timer > 0 :
                self.timer -= 3
   
        if self.timer <= 0 :
            self.timer = 0
    def isalive(self):
        if self.health > 0:
            self.alive = True
        else :
            self.alive = False
            self.fire = False
            self.velocity.asign(0,0,0)
            self.health = 0
    def enemyAI(self):
        self.controlTimer('enemy')
        if self.rest == True:
             
                           
               if self.activeState == 'down':
                   p = random.uniform(0,20)
                   if p <= 5:
                       self.activeState = 'left'
                       self.velocity.asign(-2,0,0)
                   if p > 5 and p <= 10:
                       self.activeState = 'up'
                       self.velocity.asign(0,-2,0)
                   if p > 10 and p <= 15:
                       self.activeState = 'right'
                       self.velocity.asign(2,0,0)
                   if p > 15 and p <= 20:
                       self.activeState = 'down'
                       self.velocity.asign(0,2,0)
               if self.activeState == 'up':
                   p = random.uniform(0,20)
                   if p <= 5:
                       self.activeState = 'left'
                       self.velocity.asign(-2,0,0)
                   if p > 5 and p <= 10:
                       self.activeState = 'up'
                       self.velocity.asign(0,-2,0)
                   if p > 10 and p <= 15:
                       self.activeState = 'right'
                       self.velocity.asign(2,0,0)
                   if p > 15 and p <= 20:
                       self.activeState = 'down'
                       self.velocity.asign(0,2,0)
               if self.activeState == 'left':
                   p = random.uniform(0,20)
                   if p <= 5:
                       self.activeState = 'left'
                       self.velocity.asign(-2,0,0)
                   if p > 5 and p <= 10:
                       self.activeState = 'up'
                       self.velocity.asign(0,-2,0)
                   if p > 10 and p <= 15:
                       self.activeState = 'right'
                       self.velocity.asign(2,0,0)
                   if p > 15 and p <= 20:
                       self.activeState = 'down'
                       self.velocity.asign(0,2,0)
               if self.activeState == 'right':
                   p = random.uniform(0,20)
                   if p <= 5:
                       self.activeState = 'left'
                       self.velocity.asign(-2,0,0)
                   if p > 5 and p <= 10:
                       self.activeState = 'up'
                       self.velocity.asign(0,-2,0)
                   if p > 10 and p <= 15:
                       self.activeState = 'right'
                       self.velocity.asign(2,0,0)
                   if p > 15 and p <= 20:
                       self.activeState = 'down'
                       self.velocity.asign(0,2,0)
               self.rest = False
        if random.uniform(0,100) < 2:
            if self.timer == 0:
                  self.fire =True
                  self.timer = 100
    def bound(self,window = []):
        # right
        if self.pos[0] >= window[0]-160 :
            self.pos[0] =window[0]-160-1
            self.rest = True # tank come to rest
        #left    
        if self.pos[0] < 10 :
            self.pos[0] = 10+0.001
            self.rest = True # tank come to rest
        #bottom    
        if self.pos[1] >= window[1]-60 :
            self.pos[1] = window[1]-60-1
            self.rest = True # tank come to rest
        #top    
        if self.pos[1] < 10 :
            self.pos[1] = 10+1
            self.rest = True # tank come to rest
    def restControl(self):

        if self.rest == True:
            self.velocity.asign(0,0,0)
            self.rest = False
    def getHitBrick(self,pos,w,h):
        if self.activeState == 'left':
                self.pos[0] = pos[0]+w+1
        if self.activeState == 'right':
                self.pos[0] = pos[0]-1
        if self.activeState == 'up':
                self.pos[1] = pos[1]+h+1
        if self.activeState == 'down':
                self.pos[1] = pos[1]-1

def _input_():
    global playerTank
    # loop through the events
    for event in pygame.event.get():
        #check if the event is the x button
        if event.type==pygame.QUIT:
            #if it is quit the game
            pygame.quit()
            exit(0)
        elif event.type == pygame.MOUSEBUTTONDOWN:
             if playerTank.timer == 0:  # check weather the bullet ca be fiered or not
                playerTank.fire = True
                playerTank.timer = 100  # start the timer for net bullet to be launch
        elif event.type == pygame.MOUSEBUTTONUP:
                playerTank.fire = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                playerTank.activeState = 'left'
                playerTank.velocity.y = 0  # palyer speed in y becomes zero
                playerTank.velocity.x = -20# palyer speed in x becomes 10
            if event.key == pygame.K_RIGHT:
                playerTank.activeState = 'right'
                playerTank.velocity.y = 0 # palyer speed in y becomes zero
                playerTank.velocity.x = 20# palyer speed in x becomes 10
            if event.key == pygame.K_UP:
                playerTank.activeState = 'up'
                playerTank.velocity.x = 0 # palyer speed in x becomes zero
                playerTank.velocity.y = -20 # palyer speed in y becomes 10
            if event.key == pygame.K_DOWN:
                playerTank.activeState = 'down'
                playerTank.velocity.x = 0 # palyer speed in x becomes zero
                playerTank.velocity.y = 20# palyer speed in y becomes 10
            if event.key == pygame.K_LCTRL:
                playerTank.fire = True    # palyer fires a bullet
            if event.key == pygame.K_r:
                pass
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT:
                playerTank.velocity.y = 0
                playerTank.velocity.x = 0
            if event.key == pygame.K_RIGHT:
                playerTank.velocity.y = 0
                playerTank.velocity.x = 0
            if event.key == pygame.K_UP:
                playerTank.velocity.y = 0
                playerTank.velocity.x = 0
            if event.key == pygame.K_DOWN:
                playerTank.velocity.y = 0
                playerTank.velocity.x = 0


    
def display(tank):
    # display the tank on the screen
    if tank.activeState == 'up':
        tank.turnUp()
    if tank.activeState == 'down':
        tank.turnDown()
    if tank.activeState == 'left':
        tank.turnLeft()
    if tank.activeState == 'right':
        tank.turnRight()
         
        
def bulletCollision():
    global l1,bullets,window,tanks,playerTank
    # collision of bullet with level walls
    for r in l1.level:
        for c in r:
            for b in bullets :
                if IsPointInside(b.pos[0],b.pos[1],c,50,50) == True:
                    if c[5] == True:
                        b.display = False
                        bullets.remove(b)
                        c[6] -= c[7]
                    if c[6] <=0 :
                        c[4] = False; c[5] = False
    # collision of tanks and bullet
    for t in tanks:
        for b in bullets :
                p = [t.pos[0],t.pos[1]]
                if IsPointInside(b.pos[0],b.pos[1],p,50,50) == True:
                     b.display = False
                     bullets.remove(b)
                     t.health -= t.damage
                if t.health <= 0 :
                    tanks.remove(t)
                    break
    # collision of bullet with boundary
    for b in bullets:
        # right
        if b.pos[0] >= window[0]-130 :
            bullets.remove(b)
        #left    
        if b.pos[0] < 10 :
            bullets.remove(b)
        #bottom    
        if b.pos[1] >= window[1]-30 :
            bullets.remove(b)
        if b.pos[1] < 10 :
           bullets.remove(b)
    # collision of bullet with player
    p = [playerTank.pos[0],playerTank.pos[1]]
    for b in bullets:
        if IsPointInside(b.pos[0],b.pos[1],p,50,50) == True:
            playerTank.health -= playerTank.damage
            if playerTank.health > 0:
               b.display = False
    # collision of tank with level bricks
    
    for r in l1.level:
        for c in r:
            if c[4] == True:
                if IsPointInside(playerTank.pos[0],playerTank.pos[1],c,50,50) == True:
                   print ('true')
                   playerTank.rest = True
                   p = [c[0],c[1]]
                   playerTank.getHitBrick(p,50,50) 

                
def fire():
    global bullets,playerTank,tanks
    if playerTank.fire == True :
        b = bullet(playerTank.pos,playerTank.activeState,'player')
        b.velocity.asign(playerTank.velocity.x,playerTank.velocity.y,0)
        bullets.append(b)
        playerTank.fire = False
    for t in tanks:
        if t.fire == True :
            
            b = bullet(t.pos,t.activeState,'enemy')
            b.velocity.asign(t.velocity.x,t.velocity.y,0)
            bullets.append(b)
            t.fire = False
def displayBullet(bullets):
    
    for b in bullets:
            if b.display == True:
                if b.activeState == 'up':
                    b.turnUp()
                if b.activeState == 'down':
                    b.turnDown()
                if b.activeState == 'left':
                    b.turnLeft()
                if b.activeState == 'right':
                    b.turnRight()
                
def initGame(width,height):
    global tanks,palyerTank
    
    for i in range(0,10):
        pos = (random.uniform(1,width-250),11,0)
        t = tank(pos)
        t.loadFiles('enemy')
        tanks.append(t)
    
def gameLogic():
    global palyerTank,tanks,window,bullets,gameOver
    
    # enemy logics
    for t in tanks:
        t.enemyAI()
        t.updatePos()
        t.bound(window)
        t.isalive()
        display(t)
        
    # player logics
    display(playerTank)
    playerTank.updatePos()
    playerTank.bound(window) # collision with boundary
    playerTank.isalive()
    playerTank.restControl()
    if playerTank.health <= 0:
        gameOver = True
    playerTank.controlTimer('player')
    # bullet logics
    fire()
    displayBullet(bullets)
    bulletCollision()
def drawEnv():
    global window,brick,l1
    pygame.draw.rect(screen,BLUE,[[0,0],[window[0]-100,window[1]]],5)
    pygame.draw.rect(screen,(78,47,41),[[0+10,0+10],[800-20,600-20]])
    # score board
    pygame.draw.rect(screen,BLUE,[[window[0]-100+1,0],[100,window[1]]],5)
    # draw the level
    dx,dy = 10,10

    for r in l1.level:
        for c in r:
            if c[4] == True :
              c[0],c[1] = 0+dx,0+dy
              screen.blit(brick,(c[0],c[1]))
            dx += 50      
        dy += 50
        dx = 10

def loadWall():
        global l1
        if l1._type_ == 'redbrick':
            brick = pygame.image.load('resources/images/redBrick.png')
            return brick
        elif l1._type_ == 'whiteWall':
            brick = pygame.image.load('resources/images/whiteWall.png')
            return brick
    
    
def main():
    global window,WHITE,tanks

    # init the game
    initGame(window[0],window[1])
    # main loop
    while(1):
        # load environment
        drawEnv()
        # input from all input devices
        _input_()
        # game logic
        gameLogic()
        # update the screen
        pygame.display.update()
        # clear the screen
        screen.fill(WHITE)
        # frame rate
        clock.tick(60)
        
        font = pygame.font.SysFont("calibri",40)
        textWin = font.render("You Win",True,(254,254,254))
        screen.blit(textWin,[window[0]/2-50,window[1]/2])
        if len(tanks) == 0:
            print ('+===================+')
            print ('|     you won       |')
            print ('+===================+')
            font = pygame.font.SysFont("calibri",40)
            textWin = font.render("You Win",True,(254,254,254))
            screen.blit(textWin,[window[0]/2-50,window[1]/2])
            initGame(window[0],window[1])
        if gameOver == True :
            break
        
# colors 
WHITE = (254,254,254)
RED = (254,0,0)
BLACK = (0,0,0)
BLUE = (0,0,254)
YELLOW = (254,254,0)

# init the pygame 
window = (900,600)
pygame.init()
screen = pygame.display.set_mode(window)
clock = pygame.time.Clock()

# global variables
gameOver = False  # game over 
tanks = list()      # enemy tanks
# init window size
pos = (window[0]/2,window[1]-200,0)
# init the player
playerTank = tank(pos) # player tank
playerTank.loadFiles('player')
# load the level
l1 = level('redBrick')
l1.fillSequence() # create random level
brick = pygame.image.load('resources/images/redBrick.png')

# init bullet stack
bullets = list()


main()
pygame.draw.rect(screen,BLUE,[[0,0],[window[0]-300,window[1]-200]])
pygame.draw.rect(screen,(78,47,41),[[0+10,0+10],[800-20,600-20]])
pygame.quit()
exit(0)
