import random
from configs import SCREEN_WIDTH, SCREEN_HEIGHT
from pygame import image

class Spike:
    def __init__(self, screen):
        self.screen = screen
        self.image = image.load("sprites\\spike.png")
        self.rect = self.image.get_rect()
        self.rect.y = -self.rect.height  # Start off-screen
        self.spike_pos_options = ["left", "right"]
        self.spike_pos = self.spike_pos_options[0]
        self.choose_pos()  # Choose initial spike position
        self.base_speed_y = 10
        self.speed_y = self.base_speed_y
        self.is_active = False
        self.base_speed_increment = 1
        self.speed_increment = self.base_speed_increment

    def choose_pos(self):
        """Randomly choose the spike position (left or right) and set rect center accordingly."""
        self.spike_pos = random.choice(self.spike_pos_options)
        if self.spike_pos == 'left':
            self.rect.centerx = SCREEN_WIDTH // 2 - 40
        else:
            self.rect.centerx = SCREEN_WIDTH // 2 + 40

    def update(self):
        """Update the position of the spike and reset if it goes off-screen."""
        if not self.is_active:
            # Reactivate the spike with a 50% chance
            self.is_active = True
            self.choose_pos()  # Reposition the spike when it reactivates
            self.rect.y = -self.rect.height

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
        self.speed_y += self.speed_increment