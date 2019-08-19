import pygame
from DeltaTime import *
from GenericAlghoritm import *


class PlayerController:
    def __init__(self,speed, isComputer):
        self.speed=speed
        self.isComputer=isComputer
        self.chromosome=Chromosome()
        self.movementIterator=0
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

    def __MovementComputer(self, gameObject, offsetVector):
        pass

    def __EndOfPlayer(self):
        return True if self.movementIterator==self.chromosome.genes.count or self.isDied else False

    def OnUpdate(self, gameObject):
        if self.isComputer:
            self.__MovementComputer(gameObject,2)
        else:
            self.__Movement(gameObject)