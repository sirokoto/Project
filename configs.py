from pygame import time, display, font, event, image
LOGO=image.load("favicon.ico")
running = True
SCREEN_WIDTH=512
SCREEN_HEIGHT=768
FPS=60
SCREEN = display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
display.set_caption("Попробуй увернись!")
display.set_icon(LOGO)
CLOCK = time.Clock()
font.init()
FONT = "assets\\fonts\\pixelcyr_normal.ttf"
last_speed_increase_time = time.get_ticks()
event_list = event.get()
MIN_VERT_SPACING = 250
NUM_SPIKES = 5
SPACING = SCREEN_HEIGHT // NUM_SPIKES