from Position import *

class Collider:
    def __init__(self, width, height):
        self.position=Position(0,0)
        self.width=width
        self.height=height

    def CheckCollision(self, other):
        return not (other.position.x + other.width< self.position.x or other.position.x > self.position.x+ self.width or other.position.y - other.height> self.position.y   or other.position.y< self.position.y-self.height)

    def OnCollision(self, gameObject, other):
        return self.CheckCollision(other)