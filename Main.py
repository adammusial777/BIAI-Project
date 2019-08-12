import pygame
from pygame.locals import *
import GenericAlghoritm as GA

class Point:
    pass



class Bound:
    pass

class Board:
    pass

class GreenField:
    pass

class Coin:
    pass



class ScoreCounter:
    pass

class UI:
    pass

class FileReader:
    pass



class GameObject:
    def __init__(self):
        self.componentsList=[]
        self.position=Position()

    def Update(self):
        for component in self.componentsList:
            component.OnUpdate(self)

    def AddComponent(self, newComponent):
        self.componentsList.append(newComponent)

    def OnCollision(self):
        pass

    def Draw(self):
        pass

class Position:
    def __init__(self):
        self.x=0.0
        self.y=0.0

class Collider:
    def __init__(self, width, height):
        self.width=width
        self.height=height

    def CheckCollision(self):
        pass

    


    
ticksLastFrame=0.0
deltaTime=0.0
def DeltaTime():
    global ticksLastFrame
    t = pygame.time.get_ticks()
    # deltaTime in seconds.
    deltaTime = (t - ticksLastFrame) / 1000.0
    ticksLastFrame = t
    return deltaTime

        
class PlayerController:
    def __init__(self,speed, isComputer):
        self.speed=speed
        self.isComputer=isComputer

    def __Movement(self, gameObject):
        keys = pygame.key.get_pressed()
        speedByTime=self.speed*deltaTime
        if keys[pygame.K_LEFT]:
            gameObject.position.x-=speedByTime
        if keys[pygame.K_RIGHT]:
            gameObject.position.x+=speedByTime
        if keys[pygame.K_UP]:
            gameObject.position.y-=speedByTime
        if keys[pygame.K_DOWN]:
            gameObject.position.y+=speedByTime


    def OnUpdate(self, gameObject):
        self.__Movement(gameObject)


class EnemyController:
    def __init__(self):
        self.speed=200
        self.leftDirection=False

    def __Movement(self, gameObject):
        if gameObject.position.x>=100 and not self.leftDirection:
            self.speed*=-1
            self.leftDirection=True
        elif gameObject.position.x<=0 and self.leftDirection:
            self.speed*=-1
            self.leftDirection=False
        speedByTime=self.speed*deltaTime
        gameObject.position.x+=speedByTime

    def OnUpdate(self, gameObject):
        self.__Movement(gameObject)


class GameManager:
    def __init__(self):
        pass

    #grid

    def Start(self):
        pygame.init()
        DISPLAY_SURFACE = pygame.display.set_mode((500, 500))
        pygame.display.set_caption('The worlds hardest game GA edition')
        width=40
        height=40
        global deltaTime

        player=GameObject()
        player.AddComponent(PlayerController(100, False))
        enemy=GameObject()
        enemy.AddComponent(EnemyController())
        while True:
            for event in pygame.event.get():
                if event.type == QUIT:
                    pygame.quit()
                    sys.exit()

            deltaTime=DeltaTime()        

            player.Update()
            enemy.Update()
            DISPLAY_SURFACE.fill((0,0,0))
            pygame.draw.rect(DISPLAY_SURFACE,(255,0,0), (player.position.x,player.position.y,width,height))
            pygame.draw.rect(DISPLAY_SURFACE,(0,255,0), (enemy.position.x,enemy.position.y,width,height))
            pygame.display.update()

    
game=GameManager()
game.Start()