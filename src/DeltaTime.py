import pygame


class DeltaTime:

    framerate = 60

    clock = pygame.time.Clock()

    def GetDeltaTime():
        return DeltaTime.clock.get_time() / 1000.0
