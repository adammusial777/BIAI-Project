import Player
from DeltaTime import *
from Chromosome import Chromosome


class PlayerComputer(Player.Player):

    def __init__(self, color, startPosition, collider, surface):
        Player.Player.__init__(self, color, startPosition, collider, surface)

    def Movement(self):
       # print(self.chromosome.genes[Chromosome.genesIterator].x)
        speedByTime = self.speed * DeltaTime.GetDeltaTime()
        self.position.x += speedByTime * \
            self.chromosome.genes[Chromosome.genesIterator].x
        self.position.y += speedByTime * \
            self.chromosome.genes[Chromosome.genesIterator].y

    def OnUpdate(self):
        self.Movement()
        self.collider.position = self.position
