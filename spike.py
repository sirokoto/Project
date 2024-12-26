import random
import configs
import pygame

class Spike(pygame.sprite.Sprite):
    def __init__(self, screen):
        super().__init__()
        self.screen = screen
        self.image = pygame.image.load("assets\\sprites\\spike.png")
        self.rect = self.image.get_rect()
        self.rect.y = -self.rect.height  # Start off-screen
        self.base_speed_y = 10
        self.speed_y = self.base_speed_y
        self.is_active = False

    def reset(self, y_offset=0, side=None):
        self.rect.y = y_offset
        if side == 'left': self.rect.centerx = configs.SCREEN_WIDTH // 2 - 40
        elif side == 'right':  self.rect.centerx = configs.SCREEN_WIDTH // 2 + 40
        self.is_active = True

    def choose_pos(self):
        """Randomly choose the spike position (left or right) and set rect center accordingly."""
        self.rect.centerx = random.choice([
            configs.SCREEN_WIDTH // 2 - 40,
            configs.SCREEN_WIDTH // 2 + 40
        ])
        return self.rect.centerx
    def update(self):
        """Update the position of the spike and reset if it goes off-screen."""
        if self.is_active:
            self.rect.y += self.speed_y

    def draw(self):
        """Draw the spike on the screen if active."""
        if self.is_active:
            self.screen.blit(self.image, self.rect)
    def increase_speed(self): self.speed_y += .1

