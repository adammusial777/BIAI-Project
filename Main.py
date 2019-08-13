import pygame
from pygame.locals import *
import GenericAlghoritm as GA

class Point:
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



class Bound:
    pass


class Level:
    pass

class GameObject:
    def __init__(self):
        self.componentsList=[]
        self.position=Position()
        self.collider=Collider(0,0, self.position)
        #print(self.position)

    def Update(self, DISPLAY_SURFACE):
        for component in self.componentsList:
            component.OnUpdate(self)
        self.collider.position=self.position
        for gameObject in gameObjects:
            if self.collider.CheckCollision(gameObject.collider):
                self.Draw(DISPLAY_SURFACE, 255,0,0)
            else:
                self.Draw(DISPLAY_SURFACE, 0,255,0)


    def AddComponent(self, newComponent):
        self.componentsList.append(newComponent)

    def GetComponent(self, component):
        pass

    def SetCollider(self, collider):
        self.collider=collider

    def OnCollision(self):
        pass

    def Draw(self, DISPLAY_SURFACE, r, g, b):
        pygame.draw.rect(DISPLAY_SURFACE,(r,g,b), (self.position.x,self.position.y,40,40))






class Position:
    def __init__(self):
        self.x=0.0
        self.y=0.0





class Collider:
    def __init__(self, width, height, position):
        self.position=position
        self.width=width
        self.height=height

    def CheckCollision(self, other):
        return not (other.position.x + other.width< self.position.x or other.position.x > self.position.x+ self.width or other.position.y - other.height> self.position.y   or other.position.y< self.position.y-self.height)


    


    
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

    def __MovementComputer(self, gameObject, offsetVector):
        pass

    def OnUpdate(self, gameObject):
        if self.isComputer:
            self.__MovementComputer(gameObject,2)
        else:
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






gameObjects=[]
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
        global gameObjects

        player=GameObject()
        player.AddComponent(PlayerController(100, False))
        enemy=GameObject()
        enemy.AddComponent(EnemyController())
        
        player.SetCollider(Collider(width, height, player.position))
        enemy.SetCollider(Collider(width, height, enemy.position))

        gameObjects.append(player)
        gameObjects.append(enemy)
        while True:
            for event in pygame.event.get():
                if event.type == QUIT:
                    pygame.quit()
                    sys.exit()

            deltaTime=DeltaTime()        
            DISPLAY_SURFACE.fill((0,0,0))
            player.Update(DISPLAY_SURFACE)
            enemy.Update(DISPLAY_SURFACE)
              #  pygame.draw.rect(DISPLAY_SURFACE,(255,0,0), (player.position.x,player.position.y,width,height))
           # pygame.draw.rect(DISPLAY_SURFACE,(0,255,0), (enemy.position.x,enemy.position.y,width,height))
            pygame.display.update()

    
game=GameManager()
game.Start()