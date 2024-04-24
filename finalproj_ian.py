# -*- coding: utf-8 -*-
"""
Created on Mon Apr 15 09:02:10 2024

@author: ikowa
"""

"""
Created on Tue Mar 26 10:24:19 2024

@author: ikowa
"""
import simpleGE, pygame, random, math

class Knight(simpleGE.Sprite):
    def __init__(self, scene):
        super().__init__(scene)
        self.setImage("knight.png")
        self.setSize(25,25)
        self.position = (320,300)
        self.moveSpeed = .1
    
    def process(self):
        keepGoing = True
        if self.isKeyPressed(pygame.K_UP):
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
        #self.visible = True
        self.setImage("Wall.png")
        self.setSize(25,25)
        self.position = (-10,-10)
        
        #self.colorRect("green",(30,30))


class Coin(simpleGE.Sprite):
    def __init__(self, scene):
        super().__init__(scene)
        self.setImage("Coin.png")
        self.setSize(25,25)
        self.reset()
        
    def reset(self):
        
            self.y = random.randint(0, self.screenHeight)
            self.x = random.randint(0, self.screenWidth)
        
            
      

                
   

    
class Placer(simpleGE.Sprite):
    def __init__(self, scene):
        super().__init__(scene)
        self.colorRect("Red", (20, 20))
    def process(self):
           keepGoing = True
           
           if self.isKeyPressed(pygame.K_w):
               # come back to 145 degree movement if you have time. IDK why it wasn't working with walls earlier
               self.moveAngle = 90
               self.speed += .4
               #self.speed += .1
               keepGoing = False
           elif self.isKeyPressed(pygame.K_s):
               self.moveAngle = 270
               self.speed += .4
               keepGoing = False
           elif self.isKeyPressed(pygame.K_a):
               #self.moveAngle = 90
               self.moveAngle = 180
               self.speed += .4
             
               keepGoing = False
           elif self.isKeyPressed(pygame.K_d):
               #self.moveAngle -= 40
               self.moveAngle = 0
               self.speed += .4
               keepGoing = False
    
           if self.speed > 5:
               self.speed = 5
           if keepGoing == True:
               self.speed = 0

  
    
class Hurt(simpleGE.Sprite):
    def __init__(self, scene):
        super().__init__(scene)
        self.setImage("goblin.png")
        self.setSize(25,25)
      
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
class LblTime(simpleGE.Label):
    def __init__(self):
        super().__init__()
        self.text = "Time Left: 10"
        self.center = (500, 30)
class LblLives(simpleGE.Label):
    def __init__(self):
        super().__init__()
        self.text = "Lives Left: 3"
        self.center = (300, 30)

class Game(simpleGE.Scene):
    def __init__(self):
        super().__init__()
        self.setImage("field.png")
        self.knight = Knight(self)
        self.placer = Placer(self)
        self.timer = simpleGE.Timer()
        self.numCoins = 5
        self.score = 0
        self.timer.totalTime = 180
        self.lives = 3
        self.numHurt = 4
        self.numWall = 4
        self.wallsIndex = 0 
        self.lblTime = LblTime()
        self.lblLives= LblLives()
        self.lblscore = LblScore()
        self.walls = []
        self.hurts = []
        self.coins = []
        for i in range(self.numWall):
            self.walls.append(Wall(self))
        for i in range(self.numCoins):
            self.coins.append(Coin(self))
        for i in range(self.numHurt):
            self.hurts.append(Hurt(self))
     
        
        self.sprites = [self.knight,
                        self.placer,
                        self.walls,
                        self.hurts,
                        self.coins,
                        self.lblscore,
                        self.lblTime,
                        self.lblLives]
    def moveWall(self):
        for hurtz in self.hurts:
            if hurtz.collidesWith(self.walls):
                self.walls.reset()
    def setPrevScore(self, prevScore):
        self.prevScore = prevScore
        self.lblScore.text = f":Last score: {self.prevScore}"
        
        
    def process(self):
        self.lblTime.text = f"Time left: {self.timer.getTimeLeft():.2f}"
        if self.timer.getTimeLeft() < 0:
            print(f"Score: {self.score} ")
            self.stop()
        for coin in self.coins:
            if coin.collidesWith(self.knight):
                coin.reset()
                self.score += 1
                self.lblscore.text = f"Score = {self.score}"
                
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
        #divider
    
        for hurtz in self.hurts:
            dist = math.hypot(abs(hurtz.x-self.knight.x), abs(hurtz.y-self.knight.y))
            if dist < 5:
                self.lives -= 1
                self.lblLives.text = f"Lives Left = {self.lives}"
                hurtz.reset()
                print(f"{self.lives}")
                if self.lives < 1:
                    self.stop()
            if hurtz.x > abs(self.knight.x):
                keepGoing1 = True
                while keepGoing1:
                    hurtz.x -= 3
                    keepGoing1 = False
            if hurtz.x < abs(self.knight.x):
                keepGoing2 = True
                while keepGoing2:
                    hurtz.x += 3
                    keepGoing2 = False
            if hurtz.y > abs(self.knight.y):
                keepGoing3 = True
                while keepGoing3:
                    hurtz.y -= 3
                    keepGoing3 = False
            if hurtz.y < abs(self.knight.y):
                keepGoing4 = True
                while keepGoing4:
                    hurtz.y += 3
                    keepGoing4 = False 
       
     
    def processEvent(self, event):
          if event.type == pygame.KEYDOWN:
              if event.key == pygame.K_q:
                      self.walls[self.wallsIndex].position = (self.placer.x,self.placer.y) 
                      self.wallsIndex += 1
                      if self.wallsIndex > 3:
                          self.wallsIndex = 0 
class Instructions(simpleGE.Scene):
    def __init__(self, prevScore):
        super().__init__()
        self.prevScore = prevScore
        self.setImage("kingdom.png")
        self.response = "Quit"
        #self.prevScore = 0
        self.directions = simpleGE.MultiLabel()
        self.directions.textLines = [
            "Goblins are attacking! Defend yourself with walls!",
            "Use the directional arrows to move your Knight",
            "Use WASD keys to select where to place walls",
            "Collect coins to increase your score!",
            "Avoid goblins to protect your 3 lives!",
            "Hit q to place walls"]
        self.directions.center = (320,240)
        self.directions.size = (500,250)
        self.btnPlay = simpleGE.Button()
        self.btnPlay.text = "Play"
        self.btnPlay.fgColor = ("Purple")
        self.btnPlay.clearBack = True
        self.btnPlay.center = (100,400)
        self.btnQuit = simpleGE.Button()
        self.btnQuit.clearBack = True
        self.btnQuit.text = "Quit"
        self.btnQuit.fgColor = ("red")
        self.btnQuit.center = (540,400)
        self.lblScore = simpleGE.Label()
        
        self.lblScore.center = (320,400)
        self.lblScore.text = f"Last Score: {self.prevScore}"
        self.lblScore.clearBack = True
        self.sprites = [self.directions,
                        self.btnPlay,
                        self.btnQuit,
                        self.lblScore]
    def process(self):
        if self.btnPlay.clicked:
            self.response = "Play"
            self.stop()
        if self.btnQuit.clicked:
            self.response = "Quit"
            self.stop()
            
     
            
def main():
    keepGoingF = True
    lastScore = 0
    while keepGoingF:
        #lastScore = 0
        instructions = Instructions(lastScore)
        #instructions.setPrevScore(lastScore)
        instructions.start()
        #print(instructions.response)
        if instructions.response == "Play":
            game = Game()
            game.start()
            lastScore = game.score
        else:
            keepGoingF = False
    
    
if __name__ == "__main__":
    main()