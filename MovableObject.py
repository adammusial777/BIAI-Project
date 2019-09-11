import Collider

class MovableObject:
    def __init__(self, color, startPosition, collider):
        self.color=color
        self.position=startPosition
        self.collider=collider
        collider.position=startPosition

    def OnUpdate(self):
        pass

    
