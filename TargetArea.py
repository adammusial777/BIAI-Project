import math

class TargetArea:
    def __init__(self, gameObject):
     #   self.areaReached=False
        self.distanceToEnd=0
        self.gameObject=gameObject

    def IsAreaReached(self, other):
        return not self.gameObject.rect.colliderect(other.rect)
  #      if not self.gameObject.rect.colliderect(other.rect):
 #           self.areaReached=True

    def CalculateDistance(self, gameObject):
        return math.hypot(gameObject.x - self.gameObject.x, gameObject.y-self.gameObject.y)