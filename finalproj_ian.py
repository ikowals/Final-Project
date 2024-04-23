# -*- coding: utf-8 -*-
"""
Created on Mon Apr 15 09:02:10 2024

@author: ikowa
"""

"""
Created on Tue Mar 26 10:24:19 2024

@author: ikowa
"""
import simpleGE, pygame, random, math, time

class Knight(simpleGE.Sprite):
    def __init__(self, scene):
        super().__init__(scene)
        self.setImage("Mug.png")
        self.setSize(25,25)
        self.position = (320,400)
        self.moveSpeed = .1
    
    def process(self):
        keepGoing = True
        self.correction = (0, 0)
        if self.isKeyPressed(pygame.K_UP):
            """
            if self.isKeyPressed(pygame.K_LEFT):
                self.moveAngle = 180
                self.speed += .1
                keepGoing = False
            """
            # come back to 145 degree movement if you have time. IDK why it wasn't working with walls earlier
            self.moveAngle = 90
            self.speed += .1
            #self.speed += .1
            keepGoing = False
        elif self.isKeyPressed(pygame.K_DOWN):
            self.moveAngle = 270
            self.speed += .1
            keepGoing = False
        elif self.isKeyPressed(pygame.K_LEFT):
            #self.moveAngle = 90
            self.moveAngle = 180
            self.speed += .1
          
            keepGoing = False
        elif self.isKeyPressed(pygame.K_RIGHT):
            #self.moveAngle -= 40
            self.moveAngle = 0
            self.speed += .1
            keepGoing = False
 
        if self.speed > 5:
            self.speed = 5
        if keepGoing == True:
            self.speed = 0
        for barrier in self.scene.walls:
            if self.collidesWith(barrier):
                self.x -= self.dx
                self.y -= self.dy
                self.speed = 0
       
class Wall(simpleGE.Sprite):
    def __init__(self, scene):
        super().__init__(scene)
        self.visible = True
        self.setImage("Mug.png")
        self.setSize(25,25)
        self.position = (300,300)
        self.moveSpeed = .1
        self.colorRect("green",(50,50))

    def reset(self):
        self.x = 0
        self.y = 0
class Coin(simpleGE.Sprite):
    def __init__(self, scene):
        super().__init__(scene)
        self.setImage("Orange.png")
        self.setSize(25,25)
        self.minSpeed= 3
        self.maxSpeed = 8
        self.minNegative = -3
        self.maxNegative = -8
        self.reset()
        
    def reset(self):
        
            self.y = random.randint(0, self.screenHeight)
            self.x = random.randint(0, self.screenWidth)
        
            
      
    def checkBounds(self):
        if self.bottom > self.screenHeight:
            self.reset() 
        elif self.y < 0:
            self.reset()
        elif self.x > 640:
            self.reset()
        elif self.x < 0:
            self.reset()
"""
    def process(self):
        for hurtz in self.scene.hurts:
             if hurtz.collidesWith(self):
                 print("b")
                 self.x -= self.dx
                 self.y -= self.dy
                 self.speed = 0
                 self.reset()
                 #print("aaaaaaaaaaaa")
"""            
            
            
                
   

    
class Placer(simpleGE.Sprite):
    def __init__(self, scene):
        super().__init__(scene)
        self.colorRect("Red", (20, 20))
    def process(self):
           keepGoing = True
           self.correction = (0, 0)
           if self.isKeyPressed(pygame.K_w):
               """
               if self.isKeyPressed(pygame.K_LEFT):
                   self.moveAngle = 180
                   self.speed += .1
                   keepGoing = False
               """
               # come back to 145 degree movement if you have time. IDK why it wasn't working with walls earlier
               self.moveAngle = 90
               self.speed += .1
               #self.speed += .1
               keepGoing = False
           elif self.isKeyPressed(pygame.K_s):
               self.moveAngle = 270
               self.speed += .1
               keepGoing = False
           elif self.isKeyPressed(pygame.K_a):
               #self.moveAngle = 90
               self.moveAngle = 180
               self.speed += .1
             
               keepGoing = False
           elif self.isKeyPressed(pygame.K_d):
               #self.moveAngle -= 40
               self.moveAngle = 0
               self.speed += .1
               keepGoing = False
    
           if self.speed > 5:
               self.speed = 5
           if keepGoing == True:
               self.speed = 0
           for barrier in self.scene.walls:
                if self.isKeyPressed(pygame.K_q):
                    print("a")
                    barrier.x = self.x 
                    barrier.y = self.y 
                

            
    
class Hurt(simpleGE.Sprite):
    def __init__(self, scene):
        super().__init__(scene)
        self.setImage("Spider.png")
        self.setSize(25,25)
        self.minSpeed= 5
        self.maxSpeed = 8
        self.minNegative = -3
        self.maxNegative = -8
        self.reset()
        
    def reset(self):
        
        chooseSpot = random.randint(1,4)
        if chooseSpot == int(1):
            #top
            self.y = 10
            self.x = random.randint(0, self.screenWidth)
            #self.dy = random.randint(self.minSpeed,self.maxSpeed)
        if chooseSpot == int(2):
            #right
            self.y = random.randint(0, self.screenHeight)
            self.x = 640
            #self.dx = random.randint(self.maxNegative, self.minNegative)
        if chooseSpot == int(3):
            #bottom
            self.y = 450
            self.x = random.randint(0, self.screenWidth)
            #self.dy = random.randint(self.maxNegative, self.minNegative)
        if chooseSpot == int(4):
            #left, i' do this first cause  I knwo y = 0
            self.y = random.randint(0, self.screenHeight)
            self.x = 0
            #self.dx = random.randint(self.minSpeed,self.maxSpeed)
        
    def checkBounds(self):
        if self.bottom > self.screenHeight:
            self.reset()
        
        elif self.y < 0:
            self.reset()
        elif self.x > 640:
            self.reset()
        elif self.x < 0:
            self.reset()

    def process(self):
       
        for barrier in self.scene.walls:
            if self.collidesWith(barrier):
                self.x -= self.dx
                self.y -= self.dy
                self.speed = 0
                self.reset()
                #print("aaaaaaaaaaaa")
    
                
                
            
                
class LblScore(simpleGE.Label):
    def __init__(self):
        super().__init__()
        self.text = "Score: 0"
        self.center =  (100,30)

class Game(simpleGE.Scene):
    def __init__(self):
        super().__init__()
        self.setImage("mug.png")
        self.sndHurt = simpleGE.Sound("hurtNoise.wav")
        self.knight = Knight(self)
        self.placer = Placer(self)
        self.numCoins = 5
        #self.lblscore = LblScore()
        self.numHurt = 4
        self.numWall = 4
        self.walls = []
        self.hurts = []
        self.coins = []
        for i in range(self.numWall):
            #newWall = Wall(self)
            #newWall.y= 300
            #newWall.x= (i*50)+ 125
            self.walls.append(Wall(self))
        for i in range(self.numCoins):
            self.coins.append(Coin(self))
        for i in range(self.numHurt):
            self.hurts.append(Hurt(self))
     
        #self.placer.distanceTo(Knight) == 0
        self.sprites = [self.knight,
                        self.placer,
                        self.walls,
                        self.hurts,
                        self.coins]
    def moveWall(self):
        for hurtz in self.hurts:
            if hurtz.collidesWith(self.walls):
                self.walls.reset()
        
    def process(self):
        #dist = math.hypot(abs(self.placer.x-self.knight.x), abs(self.placer.y-self.knight.y))
        for coin in self.coins:
            """
            if self.charlie.collidesWith(self.coin):
                self.sndCoin.play()
                self.coin.reset()
            """
            if coin.collidesWith(self.knight):
                coin.reset()
                #self.sndCoin.play()
                #self.score += 1
                #self.lblscore.text = f"Score = {self.score}"
        if self.placer.x > abs(self.knight.x + 40):
            keepGoing1 = True
            while keepGoing1:
                self.placer.x -= 10
                #self.placer.y -= 5
                keepGoing1 = False
        if self.placer.x < abs(self.knight.x - 40):
            keepGoing2 = True
            while keepGoing2:
                #print("positive")
                self.placer.x += 10
                #self.placer.y += 5
                keepGoing2 = False
        if self.placer.y > abs(self.knight.y + 40):
            keepGoing3 = True
            while keepGoing3:
                self.placer.y -= 10
                #self.placer.y -= 5
                keepGoing3 = False
        if self.placer.y < abs(self.knight.y - 40):
            keepGoing4 = True
            while keepGoing4:
                #print("positive")
                self.placer.y += 10
                #self.placer.y += 5
                keepGoing4 = False
    def follow(self):
        if self.hurts.x > abs(self.knight.x+1):
            keepGoing1 = True
            while keepGoing1:
                self.hurts.x -= 10
                #self.placer.y -= 5
                keepGoing1 = False
        if self.hurts.x < abs(self.knight.x+1):
            keepGoing2 = True
            while keepGoing2:
                #print("positive")
                self.hurts.x += 10
                #self.placer.y += 5
                keepGoing2 = False
        if self.hurts.y > abs(self.knight.y+1):
            keepGoing3 = True
            while keepGoing3:
                self.hurts.y -= 10
                #self.placer.y -= 5
                keepGoing3 = False
        if self.hurts.y < abs(self.knight.y+1):
            keepGoing4 = True
            while keepGoing4:
                #print("positive")
                self.hurts.y += 10
                #self.placer.y += 5
                keepGoing4 = False
        
        """    
        else:
            self.placer.x = self.placer.x
            self.placer.y = self.placer.y
        """
            
        #else:
         #   keepGoing = False
        
        
   
        
    """
    def process(self):
         for enemy in self.hurts:
             dist = math.hypot(abs(self.x-enemy.x), abs(self.y-enemy.y))
             if dist <= 100:
                 #print("please I need this")
                 
                 self.timer = simpleGE.Timer()
                 self.timer.totalTime = 20
                 #self.timer.start()
                 print(f"{self.Timer.getTimeLeft}")
                 if self.timer.getTimeLeft() == 10:
                     print("clock checkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkk")
                     self.stop()
    """
                 
    """
    def process(self):
        for hurt in self.hurts:
            if hurt.collidesWith((self.walls)):
                #this is the "visible" one when activated
                print("BBBBB")
    """
    
   
    #def process(self):
     #   for hurts in self.hurts:
      #      if hurts.collidesWith(self.wall):
          #      print("ouch")

        #for wallz in self.wall:
            #if wallz.distanceTo((self.hurts.x, self.hurts.y)) >= 1:
             #   print("howdy")
        
                #hurt.reset()
               
# hey here is a good idea. Have the enemies get faster every 30 seconds. Have an invisisble timeer, and whenever the time divided by something is three, increase enemy speed
       
            
def main():
    game = Game()
    game.start()
    
if __name__ == "__main__":
    main()