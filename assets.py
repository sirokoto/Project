import os
import pygame

class Sprite():

    def __init__(self, screen, path):
        self.screen = screen
        self.image = pygame.image.load(path)
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom

    def draw(self):
        self.screen.blit(self.image, self.rect)
