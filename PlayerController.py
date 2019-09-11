from pygame import *
from DeltaTime import *
from MovableObject import *
from Chromosome import Chromosome


class PlayerController(MovableObject):
    speed=100

    def __init__(self, color ,startPosition, collider):
        self.chromosome=Chromosome()
        self.coins=0
        self.isDied=False
        MovableObject.__init__(self, color, startPosition, collider)

    def __Movement(self):
        keys = pygame.key.get_pressed()
        speedByTime=self.speed* deltaTime.deltaTime
        if keys[pygame.K_LEFT]:
            self.position.x-=speedByTime
        if keys[pygame.K_RIGHT]:
            self.position.x+=speedByTime
        if keys[pygame.K_UP]:
            self.position.y-=speedByTime
        if keys[pygame.K_DOWN]:
            self.position.y+=speedByTime


    def __EndOfPlayer(self):
        pass
        #return True if self.movementIterator==self.chromosome.genes.count or self.isDied else False

    def OnUpdate(self):
            self.__Movement()
            self.collider.position=self.position