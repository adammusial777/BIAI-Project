import pygame

class DeltaTime:
    def __init__(self):
        self.ticksLastFrame=0
        self.deltaTime=0

    def __call__(self):
        t = pygame.time.get_ticks()
        # deltaTime in seconds.
        self.deltaTime = (t - self.ticksLastFrame) / 1000.0
        self.ticksLastFrame = t
        #return deltaTime

deltaTime= DeltaTime() 