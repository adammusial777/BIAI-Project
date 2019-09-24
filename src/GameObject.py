import pygame


class GameObject:

    def __init__(self, color, x, y, width, height):
        self.color = color
        self.rect = pygame.rect.Rect(x, y, width, height)
