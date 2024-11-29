from configs import SCREEN
from pygame import QUIT, KEYDOWN, K_r, K_q, display, event

def game_over_screen(spike, player, score, high_score, font):
    """
    Render the game-over screen and handle input for restarting or quitting the game.
    """
    SCREEN.fill((200, 200, 200))  # Background color

    # Render game-over text
    game_over_text = font.render("Game Over!", True, (255, 255, 255))
    SCREEN.blit(game_over_text,
                (SCREEN.get_width() // 2 - game_over_text.get_width() // 2, 50))

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

    # Update display
    display.update()

    # Wait for user input
    waiting = True
    while waiting:
        for e in event.get():
            if e.type == QUIT:
                quit()  # Terminate program
            if e.type == KEYDOWN:
                if e.key == K_r:  # Restart game
                    score = 0
                    spike.speed_y = spike.base_speed_y
                    spike.is_active = False
                    waiting = False  # Exit the waiting loop to restart the game
                elif e.key == K_q:  # Quit game
                    quit()
