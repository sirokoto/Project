import pygame
from configs import SCREEN_HEIGHT, SCREEN_WIDTH
class Player:
    def __init__(self, screen):
        self.screen = screen
        self.image = pygame.image.load(".\\assets\\sprites\\player.png")
        self.image = pygame.transform.scale(self.image, (self.image.get_width()*2, self.image.get_height()*2))
        self.rect = self.image.get_rect()
        self.rect.center = (SCREEN_WIDTH//2, SCREEN_HEIGHT//2)
        self.screen_rect = screen.get_rect()
        self.rect.centerx = SCREEN_WIDTH//2-40
        self.rect.bottom = SCREEN_HEIGHT//2+250
        self.flipped_image = pygame.transform.flip(self.image, True, False)
        self.offset_x=40
        self.width, self.height = self.image.get_size()
        self.centerx=self.width//2
        self.centery=self.height//2
        self.on_left_side = True  # Переменная для отслеживания стороны игрока

    def update_player(self):
        # Переключение стороны ниндзя
        keys = pygame.key.get_pressed()
        if keys[pygame.K_SPACE]:
            self.on_left_side = not self.on_left_side
            if self.on_left_side:
                self.rect.centerx = SCREEN_WIDTH // 2 - self.offset_x  # Перемещение на левую сторону
                self.image_to_draw = self.image  # Обычное изображение
            else:
                self.rect.centerx = SCREEN_WIDTH // 2 + self.offset_x  # Перемещение на правую сторону
                self.image_to_draw = self.flipped_image  # Отраженное изображение

    def draw(self):
        if not self.on_left_side:
            flipped_player = pygame.transform.flip(self.image, True, False)
            self.screen.blit(flipped_player, self.rect)
        else:
            self.screen.blit(self.image, self.rect)

    def toggle_side(self):
        self.on_left_side = not self.on_left_side

        if self.on_left_side:
            self.rect.centerx = SCREEN_WIDTH//2 - self.offset_x
        else:
            self.rect.centerx = SCREEN_WIDTH//2 + self.offset_x

    def check_collision(self, spike_rect):
        return self.rect.colliderect(spike_rect)