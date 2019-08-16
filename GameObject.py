import pygame
import Collider


class GameObject:
    def __init__(self, position,  DISPLAY_SURFACE):
        self.componentsList=[]
        self.position=position
        self.collider=Collider.Collider(0,0, self.position)
        self.screen= DISPLAY_SURFACE
        #print(self.position)

    def Update(self, DISPLAY_SURFACE):
        for component in self.componentsList:
            component.OnUpdate(self)
        self.collider.position=self.position

    def AddComponent(self, newComponent):
        self.componentsList.append(newComponent)

    def GetComponent(self, component):
        pass

    def SetCollider(self, collider):
        self.collider=collider

    def Draw(self, r, g, b):
        pygame.draw.rect(self.screen,(r,g,b), (self.position.x,self.position.y,40,40))