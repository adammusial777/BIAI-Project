import Player
from DeltaTime import *
from Chromosome import Chromosome

class PlayerComputer(Player.Player):
    def __init__(self, color, startPosition, collider):
        Player.Player.__init__(self, color, startPosition, collider)

    def __Movement(self):
       # print(self.chromosome.genes[Chromosome.genesIterator].x)
        speedByTime=self.speed* deltaTime.deltaTime
        self.position.x+=speedByTime*self.chromosome.genes[Chromosome.genesIterator].x
        self.position.y+=speedByTime*self.chromosome.genes[Chromosome.genesIterator].y
        



    def OnUpdate(self):
        self.__Movement()
        self.collider.position=self.position