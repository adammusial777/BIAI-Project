import pygame
from DeltaTime import DeltaTime
from GameObject import GameObject
from Collider import Collider


class Enemy(GameObject):

    radius = 12

    def __init__(self, color, x, y, width, height, startDirection):
        self.speed = 8
        self.leftDirection = startDirection
        self.collider = Collider(self, "Enemy")
        super(Enemy, self).__init__(color, x, y, width, height)

    def Movement(self):
        if self.rect.x <= 220 and self.leftDirection:
            self.speed *= -1
            self.rect.x = 220
            self.leftDirection = False
        elif self.rect.x >= 580 and not self.leftDirection:
            self.speed *= -1
            self.rect.x = 580
            self.leftDirection = True
        speedByTime = self.speed #* DeltaTime.GetDeltaTime()
        self.rect.x += speedByTime

    def MoveLeft(self):
        if self.leftDirection:
            self.speed *= -1

    def Render(self, surface):
        pygame.draw.circle(surface, self.color, (
            self.rect.x, self.rect.y), self.radius)

    def OnUpdate(self):
        self.Movement()
