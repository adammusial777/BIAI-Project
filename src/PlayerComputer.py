import Player
from DeltaTime import *
from Chromosome import Chromosome


class PlayerComputer(Player.Player):

    def __init__(self, color, x, y, width, height):
        super(PlayerComputer, self).__init__(color, x, y, width, height)

    def Kill(self):
        self.chromosome.killed = True

    def Movement(self, collidingObjects):
        speedByTime = self.speed
        self.rect.x += speedByTime * \
            self.chromosome.genes[Chromosome.genesIterator][0]
        self.ResolveCollisions(collidingObjects)
        prevPos = (self.rect.x, self.rect.y)
        self.previousPosition = prevPos
        self.rect.y += speedByTime * \
            self.chromosome.genes[Chromosome.genesIterator][1]
        self.ResolveCollisions(collidingObjects)

    def OnUpdate(self, collidingObjects):
        self.Movement(collidingObjects)
