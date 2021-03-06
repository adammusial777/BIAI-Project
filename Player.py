import pygame
from DeltaTime import DeltaTime
from GameObject import GameObject
from Chromosome import Chromosome


class Player(GameObject):

    width = 25
    height = 25
    speed = 6
    isFinishAreaReached = False

    def __init__(self, color, x, y, width, height):
        self.chromosome = Chromosome()
        self.coins = 0
        self.isDied = False
        super(Player, self).__init__(color, x, y, width, height)
        self.startPosition = (x, y)
        self.previousPosition = self.startPosition

    def Movement(self, collidingObjects):
        keys = pygame.key.get_pressed()
        speedByTime = self.speed * DeltaTime.GetDeltaTime()

        if keys[pygame.K_LEFT]:
            self.rect.x -= speedByTime
        if keys[pygame.K_RIGHT]:
            self.rect.x += speedByTime
        self.ResolveCollisions(collidingObjects)
        prevPos = (self.rect.x, self.rect.y)
        self.previousPosition = prevPos
        if keys[pygame.K_UP]:
            self.rect.y -= speedByTime
        if keys[pygame.K_DOWN]:
            self.rect.y += speedByTime
        self.ResolveCollisions(collidingObjects)

    def ResolveCollisions(self, colliders):
        for obj in colliders:
            if(self.rect.colliderect(obj.rect)):
                tag = obj.collider.tag
                if(tag == "Enemy"):
                    self.Kill()
                if(tag == "FinishArea"):
                    self.isFinishAreaReached = True
                if(tag == "Wall"):
                    self.rect.x = self.previousPosition[0]
                    self.rect.y = self.previousPosition[1]

    def Render(self, surface):
        pygame.draw.rect(surface, self.color, self.rect)

    def Kill(self):
        self.ResetPosition()

    def ResetPosition(self):
        self.rect.x = self.startPosition[0]
        self.rect.y = self.startPosition[1]

    def OnUpdate(self, collidingObjects):
        self.Movement(collidingObjects)

    def CheckFinishAreaReached(self):
        return self.isFinishAreaReached
