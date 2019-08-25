import pygame
from DeltaTime import *
from Chromosome import Chromosome


class PlayerController:
    speed=100

    def __init__(self):
        self.chromosome=Chromosome()
        self.coins=0
        self.isDied=False

    def __Movement(self, gameObject):
        keys = pygame.key.get_pressed()
        speedByTime=self.speed* deltaTime.deltaTime
        if keys[pygame.K_LEFT]:
            gameObject.position.x-=speedByTime
        if keys[pygame.K_RIGHT]:
            gameObject.position.x+=speedByTime
        if keys[pygame.K_UP]:
            gameObject.position.y-=speedByTime
        if keys[pygame.K_DOWN]:
            gameObject.position.y+=speedByTime

    def __EndOfPlayer(self):
        pass
        #return True if self.movementIterator==self.chromosome.genes.count or self.isDied else False

    def OnUpdate(self, gameObject):
            self.__Movement(gameObject)