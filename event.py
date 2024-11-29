import sys
from pygame import QUIT, quit, KEYDOWN, K_SPACE, event

def events(player):
    for e in event.get():
        if e.type == QUIT:
            sys.exit()
        if e.type == KEYDOWN:
            if e.key == K_SPACE:
                player.toggle_side()
