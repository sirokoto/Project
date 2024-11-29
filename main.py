import sys
import pygame
from spike import Spike
from configs import *
from PlayerPrefs import *
from player import Player
from tileset import Tileset
from tilemap import Tilemap
from event import events
from game_over_screen_render import game_over_screen

# Initialize game objects
pygame.mixer.init()
player = Player(SCREEN)
spike = Spike(SCREEN)
tset = Tileset("sprites\\log.png")
tmap = Tilemap(tset)

# Game variables
score = 0
speed_increase_interval = 5000
last_speed_increase_time = time.get_ticks()
spawned = False
game_over = False
high_score = load_high_score()
death_sound = pygame.mixer.Sound('sounds\\death.wav')
death_sound.set_volume(0.25)
bg = pygame.image.load('a637b614-12f0-44cb-bf16-7b13f1e98472.png')
#pygame.transform.smoothscale(bg, (SCREEN_WIDTH, SCREEN_HEIGHT))


def main():
    global score, high_score, last_speed_increase_time, game_over, running

    while running:
        current_time = time.get_ticks()

        # Handle events
        events(player)

        # Clear the screen
        SCREEN.blit(bg, (0,0))

        # Increase spike speed periodically
        if current_time - last_speed_increase_time > speed_increase_interval:
            spike.increase_speed()
            last_speed_increase_time = current_time

        # Spawn spike if not active and game is running

        # Update high score
        if score > high_score:
            high_score = score

        # Increment score if game is running
        if game_over is False:
            spike.update()
            player.update()
            score += 1

        # Check for game over and display game over screen
        if player.check_collision(spike.rect) and not game_over:
            game_over = False
            save_high_score(high_score)
            spike.is_active = False
            death_sound.play()

        if game_over is True:
            game_over_screen(spike, player, score, high_score, FONT)
            # Reset variables (e.g., player position) if restarting

        spike.update()

        spike.draw()

        # Render tilemap and update player
        tmap.render()
        player.update()

        # Update the display
        display.update()
        CLOCK.tick(FPS)
        pygame.time.delay(23)

    sys.exit()

if __name__ == '__main__':
    main()