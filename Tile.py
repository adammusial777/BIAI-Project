import pygame
from GameObject import GameObject
from Collider import Collider


class Tile(GameObject):

    def __init__(self, color, x, y, width, height, tag):
        super(Tile, self).__init__(color, x, y, width, height)
        self.collider = Collider(self, tag)

    def Render(self, surface):
        pygame.draw.rect(surface, self.color, self.rect)
