import pygame
from pygame import KEYDOWN

from configs import SCREEN_HEIGHT, SCREEN_WIDTH, event_list

class Player:
    def __init__(self, screen):
        self.screen = screen
        pygame.mixer.init()
        self.jump_sound = pygame.mixer.Sound('assets\\sounds\\jump.wav')
        self.jump_sound.set_volume(0.25)
        self.image = pygame.image.load("assets\\sprites\\player.png")
        self.image = pygame.transform.scale(
            self.image, (self.image.get_width() * 2, self.image.get_height() * 2)
        )
        self.flipped_image = pygame.transform.flip(self.image, True, False)
        self.rect = self.image.get_rect()
        self.rect.centerx = SCREEN_WIDTH // 2 - 40
        self.rect.bottom = SCREEN_HEIGHT // 2 + 250

        self.offset_x = 40
        self.on_left_side = True

    def draw(self):
        """Draws the player at its current position."""
        if self.on_left_side:
            self.screen.blit(self.image, self.rect)
        else:
            self.screen.blit(self.flipped_image, self.rect)

    def toggle_side(self):
        """Toggles the player's position between the left and right sides."""
        self.on_left_side = not self.on_left_side
        self.jump_sound.play()
        if self.on_left_side:
            self.rect.centerx = SCREEN_WIDTH // 2 - self.offset_x
        else:
            self.rect.centerx = SCREEN_WIDTH // 2 + self.offset_x

    def update(self):
        """
        Updates the player state. Listens for input
        and toggles side when the spacebar is pressed.
        """
        for e in event_list:
            if e.type == pygame.KEYDOWN:
                if e.key == pygame.K_SPACE:
                    self.toggle_side()

        # Draw the player in the updated position
        self.draw()

    def check_collision(self, spike_rect):
        """Checks if the player collides with the given spike rect."""
        return pygame.rect.Rect.colliderect(self.rect, spike_rect)

    def reset_position(self):
        """Reset the player's position to its starting point."""
        self.rect.center = (SCREEN_WIDTH // 2 - 40, SCREEN_HEIGHT // 2 + 250)
        self.on_left_side = True