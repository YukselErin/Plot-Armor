from random import randint
import pygame
from numpy import random

class Game(object):
    enemyTotalHealth = 10
    currentEnemyHealth = 10
    laserduration = 500
    width = 800
    height = 600
    class Player(object):
        health = 10
        coords = [400,590]
        left = True
        def move(self):
            if self.coords[0] == 790 or self.coords[0] == 10:
                self.left = not self.left
            if self.left:
                self.coords[0] -=1
            else:
                self.coords[0] +=1

    """"This object is used to keep track of laser shots that need to be drawn for multiple frames"""
    class Laser(object):
        start, finish, color, duration = (0,0),(0,0),(0,0,0),0
        def __init__(self,start, finish, color, duration ) :
            self.start, self.finish, self.color, self.duration = start, finish, color, duration 

    player = Player
    enemies = []
    gameDelay = 100
    defeated = 0
    shots = []

    def __init__(self, agro, health, power):
        self.agro = agro
        self.health = health
        self.power = power
        self.window = pygame.display.set_mode((self.width,self.height))
    
    """This function draws a laser from the list and decrements its duration variable, which allows us to control for how many frames a line is drawn."""
    def drawShot(self,laser):
        pygame.draw.line(self.window, laser.color, laser.start, laser.finish)
        laser.duration -= 1
        return laser

    """"This function uses (shots) list to draw all the necessary lines on the screen for each frame."""
    def drawAllShots (self):
        for laser in self.shots:
            laser = self.drawShot(laser)
            if laser.duration == 0:
                self.shots.remove(laser)

    """This function calculates coordinates for every enemy laser and puts them in a list. Also if the player is hit by the laser the player loses health."""
    def enemyActivity(self):
        for enemy in self.enemies:
            shotX = (enemy + random.randint(300) - 150)
            pygame.draw.line(self.window,(255,0,0), (enemy,20), (shotX, 600))
            laser = self.Laser((enemy,20), (shotX, 600), (255, 0,0), self.laserduration)
            self.shots.append(laser)
            if( 20 > abs(shotX - self.player.coords[0])):
                self.health -=1
                
    """"Creates a set number of enemy circles and keeps them in a list."""
    def createEnemy(self):
        gap = (self.width - 20) /5
        self.enemies.append(70)
        for i in range(1,5):
            self.enemies.append(i*gap + 70 )
    
    def drawEnemy(self):
        for enemy in self.enemies:
            pygame.draw.circle(self.window, (255,0,0), (enemy,20), 20)

    """The player shoots its laser at the closest target with perfect accuracy. Also by every shot the enemy loses health. Although there are multiple enemies represented in the visual they all share one health pool."""
    def playerActivity(self):
        min =801
        cord = -1
        for i in self.enemies:
            if abs(self.player.coords[0] -i )< min:
                min = abs(self.player.coords[0] -i )
                cord = i
        laser = self.Laser(self.player.coords, (cord,20), (0,255,0), self.laserduration)
        self.shots.append(laser)
        self.currentEnemyHealth -= self.power
        if self.currentEnemyHealth == 0:
            self.enemies.pop()
            self.currentEnemyHealth = self.enemyTotalHealth


    def startGame(self):       
        enemyEvent = pygame.USEREVENT+1
        playerEvent= pygame.USEREVENT+2
        pygame.time.set_timer(enemyEvent, 1000)
        pygame.time.set_timer(playerEvent, 1000)
        self.window.fill((220,243,255))
        self.createEnemy()
        pygame.time.delay(self.gameDelay)
        gameover = False        
        while not gameover:
            self.window.fill((220,243,255))
            self.drawAllShots()
            self.player.move(self.player)
            pygame.draw.circle(self.window, (0,255,0),(self.player.coords),20)
            self.drawEnemy()
            for event in pygame.event.get():
                if event.type == enemyEvent:
                    self.enemyActivity() 
                if event.type == playerEvent:
                    self.playerActivity()
                if (self.health == 0) or (not self.enemies):
                    print("gameover")
                    gameover = True
            pygame.display.update()

            


game1 = Game(5,10,1)
game1.startGame()

