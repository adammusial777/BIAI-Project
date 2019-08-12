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

class MovementObject:
    def movement(self):
        pass




        
class Player(MovementObject):
    pass

class Enemy(MovementObject):
    pass

class GameManager:
    def Start(self):
        pygame.init()
        DISPLAY_SURFACE = pygame.display.set_mode((500, 500))
        pygame.display.set_caption('Hello World!')
        x=50
        y=50
        width=40
        height=40
        speed=100
        getTicksLastFrame=0
        while True:
            for event in pygame.event.get():
                if event.type == QUIT:
                    pygame.quit()
                    sys.exit()
            keys = pygame.key.get_pressed()

            t = pygame.time.get_ticks()
            # deltaTime in seconds.
            deltaTime = (t - getTicksLastFrame) / 1000.0
            getTicksLastFrame = t
            speedByTime=speed*deltaTime
            print(deltaTime)
            if keys[pygame.K_LEFT]:
                x-=speedByTime
            if keys[pygame.K_RIGHT]:
                x+=speedByTime
            if keys[pygame.K_UP]:
                y-=speedByTime
            if keys[pygame.K_DOWN]:
                y+=speedByTime
            DISPLAY_SURFACE.fill((0,0,0))
            pygame.draw.rect(DISPLAY_SURFACE,(255,0,0), (x,y,width,height))
            pygame.display.update()
            
game=GameManager()
game.Start()