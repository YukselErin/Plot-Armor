from random import randint
import pygame
from numpy import random
class Game(object):
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
    

    player = Player
    enemies = []
    gameDelay = 100
    defeated = 0

    def __init__(self, agro, number, health, power):
        self.agro = agro
        self.number = number
        self.health = health
        self.power = power


    def enemyActivity(self,window):
        if pygame.time.get_ticks()%10 != 0:
            return
        for enemy in self.enemies:
            randd = random.randint(50)
            print(randd)
            if randd < self.agro:
                shotX = (enemy + random.randint(20) - 10)
                pygame.draw.line(window,(255,0,0), (enemy,20), (shotX, 600))
                if( 20 > abs(shotX - self.player.coords[0])):
                    print(shotX," " ,self.player.coords[0])
                    self.health -=1
                

    def createEnemy(self):
        gap = (self.width - 20) / self.number
        for i in range(0,self.number):
            self.enemies.append(i*gap + 10)
    
    def drawEnemy(self,window):
        for enemy in self.enemies:
            pygame.draw.circle(window, (255,0,0), (enemy,20), 20)

    def playerActivity(self,window):
        min =801
        cord = -1
        for i in self.enemies:
            if abs(self.player.coords[0] -i )< min:
                min = abs(self.player.coords[0] -i )
                cord = i
        pygame.draw.line(window,(0,255,0),(self.player.coords), (cord,0))
        

    def startGame(self):
        window = pygame.display.set_mode((self.width,self.height))
        window.fill((220,243,255))
        self.createEnemy()
        time = 0
        while True:
            if time >1500 +pygame.time.get_ticks():
                self.playerActivity(window)
                time = pygame.time.get_ticks()
                print(time)
            pygame.event.get()
            self.drawEnemy(window)
            print("health",self.health)
            if self.health == 0:
                print("gameover")
                break
            self.enemyActivity(window) 
            pygame.display.update()
            pygame.time.delay(self.gameDelay)
            window.fill((220,243,255))
            pygame.draw.circle(window, (0,255,0),(self.player.coords),20)
            self.player.move(self.player)

    


game1 = Game(5,10,10,10)
game1.startGame()

