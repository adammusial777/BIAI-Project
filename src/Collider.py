from pygame.rect import Rect


class Collider:

    def __init__(self, gameObject, tag):
        from GameManager import GameManager
        self.gameObject = gameObject
        self.tag = tag
        GameManager.collidingObjects.append(self.gameObject)

    def CheckCollision(self, other):
        return not self.gameObject.rect.colliderect(other.rect)
        # return not (other.position.x + other.width < self.position.x or other.position.x > self.position.x + self.width or other.position.y - other.height > self.position.y or other.position.y < self.position.y - self.height)

    def OnCollision(self, gameObject, other):
        return self.CheckCollision(other)
