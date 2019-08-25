import PlayerController
from DeltaTime import *
from Chromosome import Chromosome

class PlayerComputer(PlayerController.PlayerController):
    def __init__(self):
        PlayerController.PlayerController.__init__(self)

    def __Movement(self, gameObject):
       # print(self.chromosome.genes[Chromosome.genesIterator].x)
        speedByTime=self.speed* deltaTime.deltaTime
        gameObject.position.x+=speedByTime*self.chromosome.genes[Chromosome.genesIterator].x
        gameObject.position.y+=speedByTime*self.chromosome.genes[Chromosome.genesIterator].y



    def OnUpdate(self, gameObject):
        self.__Movement(gameObject)