import math
import pygame
from GameObject import GameObject

class TargetArea(GameObject):
    def __init__(self, color, x, y, width, height):
            super(TargetArea, self).__init__(color, x, y, width, height)

    def IsAreaReached(self, rect):
        return self.rect.colliderect(rect)
  #      if not self.gameObject.rect.colliderect(other.rect):
 #           self.areaReached=True

    def CalculateDistance(self, rect):
        return math.hypot(rect.x - self.rect.x, rect.y-self.rect.y)

    def Render(self, surface):
        pygame.draw.rect(surface, self.color, self.rect)