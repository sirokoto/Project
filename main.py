from spike import Spike
from controls import events
from configs import *
from player import Player
from tileset import Tileset
from tilemap import Tilemap
from random import random

def load_high_score():
    try:
        with open('highscore.txt', 'r') as file:
            high_score = int(file.read())
    except FileNotFoundError:
        high_score = 0  # Если файл не найден, устанавливаем наивысший счёт в 0
    return high_score

def save_high_score(high_score):
    with open('highscore.txt', 'w') as file:
        file.write(str(high_score))

def main():
    global running
    pygame.init()
    pygame.display.set_caption(SCREEN_NAME)
    player = Player(SCREEN)
    spikeL = Spike(SCREEN, 'left')
    spikeR = Spike(SCREEN, 'right')
    tset = Tileset(".\\assets\\sprites\\tile\\log.png")
    tmap = Tilemap(tset)
    font = pygame.font.Font("assets\\fonts\\JetBrainsMono-SemiBold.ttf", 20)
    score = 0
    high_score = load_high_score()
    speed_increase_interval = 5000
    last_speed_increase_time = pygame.time.get_ticks()

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

        if not spikeL.is_active and not spikeR.is_active:
            if random() < 0.2:  # Вероятность спавна шипа
                spikeL.spawn()
            if random() < 0.2:  # Вероятность спавна шипа
                spikeR.spawn()

        score+=1

        if score>high_score:
            high_score=score

        SCREEN.fill((36, 186, 140))
        tmap.render()

        spikeL.draw()
        spikeR.draw()
        player.draw()

        if spikeL.check_collision(player.rect) or spikeR.check_collision(player.rect):
            save_high_score(high_score)
            pygame.quit()
            exit()

        score_text = font.render(f"Score: {score}", True, (255, 255, 255))
        SCREEN.blit(score_text, (10,10))

        score_text = font.render(f"High Score: {high_score}", True, (255, 255, 255))
        SCREEN.blit(score_text, (10,40))

        pygame.display.flip()
        pygame.display.update()
        CLOCK.tick(FPS)

    pygame.quit()

if __name__ == '__main__':
    main()