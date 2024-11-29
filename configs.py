from pygame import time, display, font, event, image
LOGO=image.load("favicon.ico")
running = True
SCREEN_WIDTH=512
SCREEN_HEIGHT=768
FPS=60
SCREEN = display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
display.set_caption("Ninja Flip")
display.set_icon(LOGO)
CLOCK = time.Clock()
font.init()
FONT = font.Font("fonts\\JetBrainsMono-SemiBold.ttf", 30)
last_speed_increase_time = time.get_ticks()
event_list = event.get()
