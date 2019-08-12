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

class Position:
    def __init__(self):
        self.x=0.0
        self.y=0.0


ticksLastFrame=0.0
def DeltaTime():
    global ticksLastFrame
    t = pygame.time.get_ticks()
    # deltaTime in seconds.
    deltaTime = (t - ticksLastFrame) / 1000.0
    ticksLastFrame = t
    return deltaTime

        
class PlayerController:
    def __init__(self):
        self.speed=100

    def OnUpdate(self, gameObject):
        keys = pygame.key.get_pressed()
        speedByTime=self.speed*DeltaTime()

        if keys[pygame.K_LEFT]:
            gameObject.position.x-=speedByTime
        if keys[pygame.K_RIGHT]:
            gameObject.position.x+=speedByTime
        if keys[pygame.K_UP]:
            gameObject.position.y-=speedByTime
        if keys[pygame.K_DOWN]:
            gameObject.position.y+=speedByTime


class EnemyController:
    pass

class GameManager:
    def Start(self):
        pygame.init()
        DISPLAY_SURFACE = pygame.display.set_mode((500, 500))
        pygame.display.set_caption('The worlds hardest game GA edition')
        x=50
        y=50
        width=40
        height=40
        speed=100

        player=GameObject()
        player.AddComponent(PlayerController())
        while True:
            for event in pygame.event.get():
                if event.type == QUIT:
                    pygame.quit()
                    sys.exit()
            player.Update()
            DISPLAY_SURFACE.fill((0,0,0))
            pygame.draw.rect(DISPLAY_SURFACE,(255,0,0), (player.position.x,player.position.y,width,height))
            pygame.display.update()

    
game=GameManager()
game.Start()