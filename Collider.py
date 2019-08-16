class Collider:
    def __init__(self, width, height, position):
        self.position=position
        self.width=width
        self.height=height

    def CheckCollision(self, other):
        return not (other.position.x + other.width< self.position.x or other.position.x > self.position.x+ self.width or other.position.y - other.height> self.position.y   or other.position.y< self.position.y-self.height)

    def OnCollision(self, gameObject, other):
            if self.CheckCollision(other):
                gameObject.Draw( 255,0,0)
            else:
                gameObject.Draw( 0,255,0)