# -*- coding: utf-8 -*-
"""
Created on Mon Apr 15 09:02:10 2024

@author: ikowa
"""

"""
Created on Tue Mar 26 10:24:19 2024

@author: ikowa
"""
import simpleGE, pygame, random, time

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
        for barrier in self.scene.wall:
            if self.collidesWith(barrier):
                self.x -= self.dx
                self.y -= self.dy
                self.speed = 0
       
class Wall(simpleGE.Sprite):
    def __init__(self, scene):
        super().__init__(scene)
        self.colorRect("green",(50,50))
    def process(self):
        for enemy in self.scene.hurts:
            if self.distanceTo((self.hurts.x,self.hurts.y)) >=1:
                print("work")
                self.timer = simpleGE.Timer()
                self.timer.totalTime = 8
                self.timer.start()
                if time == 3:
                   self.wall.color  = "blue"
                   
    
class Placer(simpleGE.Sprite):
    def __init__(self, scene):
        super().__init__(scene)
        self.colorRect("Blue", (50, 50))
    """   
    def process(self):
        self.distanceTo(4,20) == place
    """
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
            self.dy = random.randint(self.minSpeed,self.maxSpeed)
        if chooseSpot == int(2):
            #right
            self.y = random.randint(0, self.screenHeight)
            self.x = 640
            self.dx = random.randint(self.maxNegative, self.minNegative)
        if chooseSpot == int(3):
            #bottom
            self.y = 450
            self.x = random.randint(0, self.screenWidth)
            self.dy = random.randint(self.maxNegative, self.minNegative)
        if chooseSpot == int(4):
            #left, i' do this first cause  I knwo y = 0
            self.y = random.randint(0, self.screenHeight)
            self.x = 0
            self.dx = random.randint(self.minSpeed,self.maxSpeed)
        
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
        for barrier in self.scene.wall:
            if self.collidesWith(barrier):
                self.x -= self.dx
                self.y -= self.dy
                self.speed = 0

"""
class LblScore(simpleGE.Label):
    def __init__(self):
        super().__init__()
        self.text = "Score: 0"
        self.center =  (100,30)
"""
class Game(simpleGE.Scene):
    def __init__(self):
        super().__init__()
        self.setImage("mug.png")
        self.sndHurt = simpleGE.Sound("hurtNoise.wav")
        self.knight = Knight(self)
        self.placer = Placer(self)
        #self.lblscore = LblScore()
        self.numHurt = 4
        self.wall = []
        self.hurts = []
        for i in range(10):
            newWall = Wall(self)
            newWall.y= 300
            newWall.x= (i*50)+ 125
            self.wall.append(newWall)
        
        for i in range(self.numHurt):
            self.hurts.append(Hurt(self))
        #self.placer.distanceTo(Knight) == 0
        self.sprites = [self.knight,
                        self.placer,
                        self.wall,
                        self.hurts]

    #def process(self):
     #   for hurts in self.hurts:
      #      if hurts.collidesWith(self.wall):
          #      print("ouch")

        #for wallz in self.wall:
            #if wallz.distanceTo((self.hurts.x, self.hurts.y)) >= 1:
             #   print("howdy")
        
                #hurt.reset()
               
# hey here is a good idea. Have the enemies get faster every 30 seconds. Have an invisisble timeer, and whenever the time divided by something is three, increase enemy speed
        """
        def setPrevScore(self, prevScore):
            self.prevScore = prevScore
            self.lblScore.text = f":Last score: {self.prevScore}"
        """
       
        """
        def process(self):
            for placer in self.placer:
                if  placer.distanceTo(self.knight) >5:
                    placer.
        """
            
def main():
    game = Game()
    game.start()
    
if __name__ == "__main__":
    main()