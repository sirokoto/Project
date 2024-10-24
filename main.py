import pygame
from spike import Spike
from configs import *
from player import Player
from tileset import Tileset
from tilemap import Tilemap
from random import random
from pygame.locals import *
pygame.init()

def load_high_score():
    try:
        with open('highscore.txt', 'r') as file:
            high_score = int(file.read())
    except Exception:
        high_score = 0
    return high_score

def save_high_score(high_score):
    with open('highscore.txt', 'w') as file:
        file.write(str(high_score))


pygame.display.set_caption(SCREEN_NAME, logo)
player = Player(SCREEN)
eventList = pygame.event.get()
spikeL = Spike(SCREEN, 'left')
spikeR = Spike(SCREEN, 'right')
tset = Tileset(".\\assets\\sprites\\tile\\log.png")
tmap = Tilemap(tset)
font = pygame.font.Font("assets\\fonts\\JetBrainsMono-SemiBold.ttf", 30)
score = 0
speed_increase_interval = 5000
last_speed_increase_time = pygame.time.get_ticks()
spawned = False
game_over = False
high_score = load_high_score()

def events(player):
    global eventList
    for event in eventList:
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                player.toggle_side()

def game_loop():
    last_speed_increase_time = pygame.time.get_ticks()
    global score, high_score, game_over
    if random() < 0.5:
        spikeL.spawn()
    else:
        spikeR.spawn()

    while running:
        current_time = pygame.time.get_ticks()

        if current_time - last_speed_increase_time > speed_increase_interval:
            spikeL.increase_speed_by_time()
            spikeR.increase_speed_by_time()
            last_speed_increase_time = current_time

        events(player)

        spikeL.update(spikeR)
        spikeR.update(spikeL)

        if not spikeL.is_active and not spikeR.is_active and not game_over and not spawned:
            if random() < 0.5:
                spikeL.spawn()
            if random() < 0.5:
                spikeR.spawn()
        if score > high_score:
            high_score = score

        SCREEN.fill((36, 186, 140))
        tmap.render()

        spikeL.draw()
        spikeR.draw()
        player.draw()
        if not game_over:
            score += 1

        if (spikeL.check_collision(player.rect) or spikeR.check_collision(player.rect)) and not game_over:
            game_over_screen()

            save_high_score(high_score)
        pygame.display.flip()
        pygame.display.update()
        CLOCK.tick(FPS)

    pygame.quit()

def game_over_screen():
    SCREEN.fill((200, 200, 200))
    global score, high_score, game_over, font
    while running:
        for e in pygame.event.get():
            if e.type == pygame.QUIT:
                pygame.quit()

        gameOverText = font.render("Game Over!", 1, (255, 255, 255))
        SCREEN.blit(gameOverText, (SCREEN.get_width()//2 - gameOverText.get_width() // 2,
                                   0 + 50))

        score_text = font.render(f"Score: {score}", True, (255, 255, 255))
        SCREEN.blit(score_text, (SCREEN.get_width()//2 - score_text.get_width() // 2,
                                 SCREEN.get_height()//2 - 30))

        score_text = font.render(f"High Score: {high_score}", True, (255, 255, 255))
        SCREEN.blit(score_text, (SCREEN.get_width()//2 - score_text.get_width() // 2,
                                 SCREEN.get_height()//2))

        restart_button = font.render("R - Restart", 1, (255, 255, 255))
        SCREEN.blit(restart_button, (SCREEN.get_width()//2 - restart_button.get_width() // 2, SCREEN.get_height()//2 + 30))

        quit_button = font.render("Q - Quit", 1, (255, 255, 255))
        SCREEN.blit(quit_button, (SCREEN.get_width()//2 - restart_button.get_width() // 2, SCREEN.get_height()//2 + 60))

        for e in eventList:
            if e.type == pygame.KEYDOWN:
                if e.key == pygame.K_r:
                    if game_over:
                        score=0
                        player.on_left_side = True
                        spikeL.speed_y, spikeR.speed_y = spikeL.base_speed_y, spikeR.base_speed_y
                        spikeL.speed_increment, spikeR.speed_increment = spikeL.base_speed_increment, spikeR.base_speed_increment
                        game_over = False
                elif e.key == pygame.K_q:
                    pygame.quit()
        pygame.display.flip()
        pygame.display.update()
        CLOCK.tick(FPS)

def main():
    game_loop()
#
# def main():
#     global running
#     pygame.init()
#     pygame.display.set_caption(SCREEN_NAME)
#     player = Player(SCREEN)
#     spikeL = Spike(SCREEN, 'left')
#     spikeR = Spike(SCREEN, 'right')
#     tset = Tileset(".\\assets\\sprites\\tile\\log.png")
#     tmap = Tilemap(tset)
#     font = pygame.font.Font("assets\\fonts\\JetBrainsMono-SemiBold.ttf", 20)
#     score = 0
#     high_score = load_high_score()
#     speed_increase_interval = 5000
#     last_speed_increase_time = pygame.time.get_ticks()
#     SCREEN = pygame.rect.Rect((SCREEN_WIDTH // 2 - 130, SCREEN_HEIGHT // 2 - 100), (260, 200))
#     game_over = False
#     spawned = False  # Флаг для предотвращения двойного спавна
#     timer = 0 + (pygame.time.get_ticks()//1000)
#
#     # При первом запуске случайный спавн одного шипа
#     if random() < 0.5:
#         spikeL.spawn()
#     else:
#         spikeR.spawn()
#
#     while running:
#         current_time = pygame.time.get_ticks()
#
#         if current_time - last_speed_increase_time > speed_increase_interval:
#             spikeL.increase_speed_by_time()
#             spikeR.increase_speed_by_time()
#             last_speed_increase_time = current_time
#
#         events(player)
#
#         spikeL.update(spikeR)
#         spikeR.update(spikeL)
#
#         if not spikeL.is_active and not spikeR.is_active and not game_over and not spawned:
#             if timer > 1:
#                 if random() < 0.5:
#                     spikeL.spawn()
#                     timer=0
#                 else:
#                     spikeR.spawn()
#                     timer=0
#             spawned = True
#             timer = 0 + (pygame.time.get_ticks() // 1000)
#         if not game_over:
#             score += 1
#
#         # Проверка на столкновение
#         if spikeL.check_collision(player.rect) or spikeR.check_collision(player.rect):
#             game_over = True
#             spikeL.speed_y, spikeR.speed_y, spikeL.speed_increment, spikeR.speed_increment = 0, 0, 0, 0
#             pygame.draw.rect(SCREEN, (200, 200, 200), SCREEN)
#             gameOverText = font.render("Game Over!", 1, (255, 255, 255))
#             SCREEN.blit(gameOverText,
#                         (SCREEN.centerx - gameOverText.get_width() // 2, SCREEN.top + 10))
#
#             # Выводим счёт
#             score_text = font.render(f"Score: {score}", True, (255, 255, 255))
#             SCREEN.blit(score_text,
#                         (SCREEN.centerx - score_text.get_width() // 2, SCREEN.centery - 25))
#
#             score_text = font.render(f"High Score: {high_score}", True, (255, 255, 255))
#             SCREEN.blit(score_text,
#                         (SCREEN.centerx - score_text.get_width() // 2, SCREEN.centery + 10))
#
#             # Обрабатываем событие рестарта
#             for e in pygame.event.get():
#                 if e.type == pygame.KEYDOWN and e.key == pygame.K_r:
#                     # Сброс параметров игры
#                     score = 0
#                     game_over = False
#                     spawned = False  # Разрешаем новый спавн
#                     spikeL.speed_y, spikeR.speed_y = spikeL.base_speed_y, spikeR.base_speed_y
#                     spikeL.speed_increment, spikeR.speed_increment = Spike.__init__(spikeL, SCREEN).speed_increment, Spike.__init__(spikeR, SCREEN).speed_increment
#                     last_speed_increase_time = pygame.time.get_ticks()
#
#         # Рендер экрана
#         SCREEN.fill((36, 186, 140))
#         tmap.render()
#
#         spikeL.draw()
#         spikeR.draw()
#         player.draw()
#
#         pygame.display.flip()
#         pygame.display.update()
#         CLOCK.tick(FPS)
#
#     pygame.quit()


if __name__ == '__main__':
    main()

