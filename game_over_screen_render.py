import sys

import pygame
from configs import SCREEN, SCREEN_WIDTH, SCREEN_HEIGHT, MIN_VERT_SPACING
from pygame import QUIT, KEYDOWN, K_r, K_q, display, event


def game_over_screen(spikes, player, score, high_score, font):
    """
    Render the game-over screen and handle input for restarting or quitting the game.
    """
    global game_over
    SPLASHWIDTH, SPLASHHEIGHT = 300, 470
    splash = pygame.draw.rect(SCREEN, (200,200,200), (SCREEN_WIDTH//2-SPLASHWIDTH//2, SCREEN_HEIGHT//2-SPLASHHEIGHT//2, SPLASHWIDTH, SPLASHHEIGHT))

    # Render game-over text
    game_over_text = font.render("Game Over!", True, (255, 255, 255))

    SCREEN.blit(game_over_text,
                (SCREEN.get_width()//2 - game_over_text.get_width()//2, SCREEN_HEIGHT//2-SPLASHHEIGHT//2+50))

    # Render score and high score
    score_text = font.render(f"Score: {score}", True, (255, 255, 255))

    SCREEN.blit(score_text,
                (SCREEN.get_width() // 2 - score_text.get_width() // 2, SCREEN.get_height() // 2 - 30))

    high_score_text = font.render(f"High Score: {high_score}", True, (255, 255, 255))

    SCREEN.blit(high_score_text,
                (SCREEN.get_width() // 2 - high_score_text.get_width() // 2, SCREEN.get_height() // 2))

    # Render instructions
    restart_button = font.render("R - Restart", True, (255, 255, 255))

    SCREEN.blit(restart_button,
                (SCREEN.get_width() // 2 - restart_button.get_width() // 2, SCREEN.get_height() // 2 + 30))

    quit_button = font.render("Q - Quit", True, (255, 255, 255))

    SCREEN.blit(quit_button,
                (SCREEN.get_width() // 2 - quit_button.get_width() // 2, SCREEN.get_height() // 2 + 60))

    # Wait for user input
    display.update()

    wait=True
    while wait:
        for e in event.get():
            if e.type == QUIT:
                sys.exit()
            if e.type == KEYDOWN:
                if e.key == K_r:  # Restart game
                    player.reset_position()
                    for i, spike in enumerate(spikes):
                        side = 'left' if i % 2 == 0 else 'right'
                        y_offset = -i * MIN_VERT_SPACING
                        spike.reset(y_offset=y_offset, side=side)
                        spike.speed_y = spike.base_speed_y
                    game_over = False
                    wait=False
                elif e.key == K_q:  # Quit game
                    sys.exit()