from random import random
from configs import SCREEN_WIDTH, SCREEN_HEIGHT
import pygame

class Spike:
    def __init__(self, screen, position="left"):
        self.screen = screen
        self.image = pygame.image.load(".\\assets\\sprites\\spike.png")
        self.flipped_image = pygame.transform.flip(self.image, True, False)
        self.rect = self.image.get_rect()
        # Шипы должны быть по центру столба (совпадает с центром экрана)
        self.rect.centerx = SCREEN_WIDTH // 2
        self.rect.y = -self.rect.height  # Стартовое положение шипов сверху
        self.base_speed_y = 10
        self.speed_y = self.base_speed_y  # Скорость движения шипов
        self.position = position
        self.is_active = False
        self.base_speed_increment = 1
        self.speed_increment = self.base_speed_increment

        if position == 'left':
            self.rect.centerx -= 40
            self.image_to_draw = self.image
        elif position == 'right':
            self.rect.centerx += 40
            self.image_to_draw = self.flipped_image

    def spawn(self):
        self.is_active = True
        self.rect.y = -self.rect.height

    def update(self, other_spike):
        if not self.is_active and not other_spike.is_active and random() < 0.5:
            self.is_active = True

        if self.is_active:
            self.rect.y += self.speed_y
            if self.rect.top > SCREEN_HEIGHT:
                self.rect.y = -self.rect.height
                self.is_active = False
    def draw(self):
        if self.is_active:
            self.screen.blit(self.image_to_draw, self.rect)

    def check_collision(self, player_rect):
        return self.is_active and self.rect.colliderect(player_rect)  # Проверка столкновения с игроком

    def increase_speed_by_time(self):
        self.speed_y += self.speed_increment
