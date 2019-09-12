import pygame
from DeltaTime import DeltaTime
from GameObject import GameObject
from Chromosome import Chromosome


class Player(GameObject):

    width = 25
    height = 25
    speed = 200

    def __init__(self, color, x, y, width, height):
        self.chromosome = Chromosome()
        self.coins = 0
        self.isDied = False
        super(Player, self).__init__(color, x, y, width, height)

    def Movement(self):
        keys = pygame.key.get_pressed()
        speedByTime = self.speed * DeltaTime.GetDeltaTime()
        if keys[pygame.K_LEFT]:
            self.rect.x -= speedByTime
        if keys[pygame.K_RIGHT]:
            self.rect.x += speedByTime
        if keys[pygame.K_UP]:
            self.rect.y -= speedByTime
        if keys[pygame.K_DOWN]:
            self.rect.y += speedByTime

    def ResolveCollisions(self, colliders):
        for obj in colliders:
            if(self.rect.colliderect(obj.rect)):
                tag = obj.collider.tag
                if(tag == "Enemy"):
                    pass
                if(tag == "FinishArea"):
                    pass
                if(tag == "Wall"):
                    if self.rect.left < obj.rect.right and self.rect.left > obj.rect.left and self.rect.top < obj.rect.bottom and self.rect.top > obj.rect.top:
                        self.rect.left = obj.rect.right
                        self.rect.top = obj.rect.bottom
                        break
                    elif self.rect.right > obj.rect.left and self.rect.right < obj.rect.right and self.rect.top < obj.rect.bottom and self.rect.top > obj.rect.top:
                        self.rect.right = obj.rect.left
                        self.rect.top = obj.rect.bottom
                        break
                    elif self.rect.left < obj.rect.right and self.rect.left > obj.rect.left and self.rect.bottom > obj.rect.top and self.rect.bottom < obj.rect.bottom:
                        self.rect.left = obj.rect.right
                        self.rect.bottom = obj.rect.top
                        break
                    elif self.rect.right > obj.rect.left and self.rect.right < obj.rect.right and self.rect.bottom > obj.rect.top and self.rect.bottom < obj.rect.bottom:
                        self.rect.right = obj.rect.left
                        self.rect.bottom = obj.rect.top
                        break
                    elif self.rect.left < obj.rect.right and self.rect.left > obj.rect.left:
                        self.rect.left = obj.rect.right
                        break
                    elif self.rect.right > obj.rect.left and self.rect.right < obj.rect.right:
                        self.rect.right = obj.rect.left
                        break
                    elif self.rect.top < obj.rect.bottom and self.rect.top > obj.rect.top:
                        self.rect.top = obj.rect.bottom
                        break
                    elif self.rect.bottom > obj.rect.top and self.rect.bottom < obj.rect.bottom:
                        self.rect.bottom = obj.rect.top
                        break

    # if collider.tag == "Wall":
    #     if player_transform.rect.left < transform.rect.right and player_transform.rect.left > transform.rect.left:
    #         player_transform.rect.left = transform.rect.right
    #     elif player_transform.rect.right > transform.rect.left and player_transform.rect.right < transform.rect.right:
    #         player_transform.rect.right = transform.rect.left

    def Render(self, surface):
        pygame.draw.rect(surface, self.color, self.rect)

    def EndOfPlayer(self):
        pass
        # return True if self.movementIterator==self.chromosome.genes.count or self.isDied else False

    def OnUpdate(self):
        self.Movement()
