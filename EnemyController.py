from DeltaTime import *


class EnemyController:
    def __init__(self):
        self.speed=200
        self.leftDirection=False

    def __Movement(self, gameObject):
        if gameObject.position.x>=450 and not self.leftDirection:
            self.speed*=-1
            self.leftDirection=True
        elif gameObject.position.x<=0 and self.leftDirection:
            self.speed*=-1
            self.leftDirection=False
        speedByTime=self.speed*deltaTime.deltaTime
        gameObject.position.x+=speedByTime

    def OnUpdate(self, gameObject):
        self.__Movement(gameObject)
