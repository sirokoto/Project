import pygame

class Tileset:
    def __init__(self, file):
        self.image = pygame.image.load(file)
        self.rect = self.image.get_rect()
