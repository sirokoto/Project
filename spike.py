import random

import pygame

from configs import SCREEN_WIDTH, SCREEN_HEIGHT
from pygame import image

class Spike(pygame.sprite.Sprite):
    def __init__(self, screen):
        super().__init__()
        self.screen = screen
        self.image = image.load("assets\\sprites\\spike.png")
        self.rect = self.image.get_rect()
        self.rect.y = -self.rect.height  # Start off-screen
        self.base_speed_y = 10
        self.speed_y = self.base_speed_y
        self.is_active = False

    def choose_pos(self):
        """Randomly choose the spike position (left or right) and set rect center accordingly."""
        self.rect.centerx = random.choice([
            SCREEN_WIDTH // 2 - 40,
            SCREEN_WIDTH // 2 + 40
        ])
    def update(self):
        """Update the position of the spike and reset if it goes off-screen."""
        if self.is_active:
            self.rect.y += self.speed_y
            # If the spike moves off the bottom of the screen, deactivate it
            if self.rect.top > SCREEN_HEIGHT:
                self.is_active = False

    def draw(self):
        """Draw the spike on the screen if active."""
        if self.is_active:
            self.screen.blit(self.image, self.rect)

    def increase_speed(self):
        """Increase the speed of the spike's downward movement."""
        self.speed_y += 1

    def reset(self, y_offset=0, side=None):
        self.rect.y = y_offset
        if side: self.rect.centerx = SCREEN_WIDTH // 2 - 40 if side == 'left' else SCREEN_WIDTH // 2 + 40
        else: side = self.choose_pos()
        self.is_active = True