import random
import pygame
from pygame.examples.cursors import image

from button import Button
from spike import Spike
from configs import SCREEN,FPS, FONT, CLOCK, SCREEN_HEIGHT, NUM_SPIKES, MIN_VERT_SPACING, SCREEN_WIDTH
from PlayerPrefs import *
from player import Player
from tileset import Tileset
from tilemap import Tilemap
from event import events
from game_over_screen_render import game_over_screen


menu = ['main_menu', 'score_menu', 'game_menu']
# Initialize game objects
pygame.mixer.init()
player = Player(SCREEN)
tset = Tileset("assets\\sprites\\log.png")
tmap = Tilemap(tset)
spikes = [Spike(SCREEN) for _ in range(NUM_SPIKES)]

# Game variables
#pygame.mixer.music.load("assets\\sounds\\An Enigmatic Encounter.wav", "MemeMainGame")
score = 0
speed_increase_interval = 5000
last_speed_increase_time = pygame.time.get_ticks()
spawned = False
high_score = load_high_score()
death_sound = pygame.mixer.Sound('assets\\sounds\\death.wav')
death_sound.set_volume(0.25)
bg = pygame.image.load('assets\\a637b614-12f0-44cb-bf16-7b13f1e98472.png')
mmbg = pygame.transform.scale(pygame.image.load("assets\\sprites\\main_menu_bg.png"), (512, 768))
button_image = pygame.transform.scale(pygame.image.load("assets\\sprites\\button.png"), (192,64))
def get_font(size):
    return pygame.font.Font(FONT, size)

def main_menu():
    pygame.mixer.music.load("assets\\sounds\\MainMenu.wav", "MainMenu")
    pygame.mixer_music.play(-1)
    while True:
        SCREEN.blit(mmbg, (0,0))
        mmpos= pygame.mouse.get_pos()
        MENU_TEXT = get_font(48).render("Попробуй увернись!", 0, '#f63f11')
        MENU_RECT = MENU_TEXT.get_rect()

        START_BUTTON = Button(image=button_image, pos=(SCREEN_WIDTH//2, SCREEN_HEIGHT//3), text_input="START", font=get_font(30), base_color="#dfae23", hovering_color="#ffdd77")
        SCORE_BUTTON = Button(image=button_image, pos=(SCREEN_WIDTH//2, SCREEN_HEIGHT//2), text_input="SCORE", font=get_font(30), base_color="#dfae23", hovering_color="#ffdd77")
        QUIT_BUTTON = Button(image=button_image, pos=(SCREEN_WIDTH//2, SCREEN_HEIGHT//1.5), text_input="QUIT", font=get_font(30), base_color="#dfae23", hovering_color="#ffdd77")

        SCREEN.blit(MENU_TEXT, (SCREEN.get_rect().centerx-MENU_RECT.width//2, MENU_RECT.y+50))

        for button in [START_BUTTON, SCORE_BUTTON, QUIT_BUTTON]:
            button.changeColor(mmpos)
            button.update(SCREEN)

        for e in pygame.event.get():
            if e.type == pygame.QUIT:
                pygame.quit()
            if e.type == pygame.MOUSEBUTTONDOWN:
                if START_BUTTON.checkForInput(mmpos):
                    game()
                if SCORE_BUTTON.checkForInput(mmpos):
                    score_menu()
                if QUIT_BUTTON.checkForInput(mmpos):
                    pygame.quit()

        pygame.display.update()
def game():
    global last_speed_increase_time, score, high_score, game_over
    pygame.mixer.music.load("assets\\sounds\\Pixelated Dreams.wav", "MainGame")
    for i, spike in enumerate(spikes):
        side = 'left' if i % 2 == 0 else 'right'
        y_offset = -i * MIN_VERT_SPACING
        spike.reset(y_offset=y_offset, side=side)
    pygame.mixer_music.play(-1)
    while True:
        current_time = pygame.time.get_ticks()

        # Handle events
        events(player)

        # Clear the screen
        SCREEN.blit(bg, (0,0))

        # Increase spike speed periodically
        if current_time - last_speed_increase_time > speed_increase_interval:
            for spike in spikes:
                spike.increase_speed()
            last_speed_increase_time = current_time

        for i, spike in enumerate(spikes):
            if not spike.is_active:
                if random.random() < 0.01:
                    side = 'left' if i % 2 == 0 else 'right'
                    y_offset = -i * MIN_VERT_SPACING
                    spike.reset(y_offset=y_offset, side=side)
            spike.update()
            spike.draw()

            if spike.is_active and player.check_collision(spike.rect):
                game_over = True
                death_sound.play()
                spikes.remove(spike)
                save_high_score(high_score)

        if not game_over:
            score += 1
        #Update high score
        if score > high_score:
            high_score = score

        # Render tilemap and update player
        tmap.render()
        player.update()

        #Handle game over
        if game_over:
            pygame.mixer.music.pause()
            game_over_screen(spikes, player, score, high_score, get_font(30))
            score=0
            game_over=False
        pygame.mixer.music.unpause()
        # Update the display
        pygame.display.update()
        CLOCK.tick(FPS)
def score_menu():
    while True:
        SCREEN.blit(mmbg, (0,0))
        mmpos=pygame.mouse.get_pos()
        high_score = load_high_score()
        SCORE_AREA = get_font(75).render("SCORE:", 0, '#f63f11')
        SCREEN.blit(SCORE_AREA, (SCREEN.get_rect().centerx-SCORE_AREA.get_width()//2,20))
        BACK_BUTTON = Button(image=button_image, pos=(SCREEN_WIDTH-202, SCREEN_HEIGHT-74), text_input="BACK", font=get_font(24), base_color="#dfae23", hovering_color="#ffdd77")

        SCORE = get_font(75).render(str(high_score), 0, '#f63f11')
        SCREEN.blit(SCORE, (SCREEN.get_rect().centerx-SCORE_AREA.get_rect().centerx, SCORE_AREA.get_rect().y+SCORE_AREA.get_height()+50))

        for btn in [BACK_BUTTON]:
            btn.changeColor(mmpos)
            btn.update(SCREEN)
        for e in pygame.event.get():
            if e.type == pygame.QUIT:
                pygame.quit()
            if e.type == pygame.MOUSEBUTTONDOWN:
                if BACK_BUTTON.checkForInput(mmpos):
                    main_menu()
        pygame.display.update()
main_menu()
