import PlayerController
from DeltaTime import *
from Chromosome import Chromosome

class PlayerComputer(PlayerController.PlayerController):
    def __init__(self, color, startPosition, collider):
        PlayerController.PlayerController.__init__(self, color, startPosition, collider)

    def __Movement(self):
       # print(self.chromosome.genes[Chromosome.genesIterator].x)
        speedByTime=self.speed* deltaTime.deltaTime
        self.position.x+=speedByTime*self.chromosome.genes[Chromosome.genesIterator].x
        self.position.y+=speedByTime*self.chromosome.genes[Chromosome.genesIterator].y
        



    def OnUpdate(self):
        self.__Movement()
        self.collider.position=self.position