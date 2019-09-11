from DeltaTime import *
from MovableObject import *

class Enemy(MovableObject):
    def __init__(self, color , startPosition, collider):
        self.speed=200
        self.leftDirection=False
        MovableObject.__init__(self,color, startPosition, collider)

    def __Movement(self):
        if self.position.x>=450 and not self.leftDirection:
            self.speed*=-1
            self.leftDirection=True
        elif self.position.x<=0 and self.leftDirection:
            self.speed*=-1
            self.leftDirection=False
        speedByTime=self.speed*deltaTime.deltaTime
        self.position.x+=speedByTime

    def OnUpdate(self):
        self.__Movement()
        self.collider.position=self.position
