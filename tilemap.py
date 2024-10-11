from configs import SCREEN, SCREEN_WIDTH, SCREEN_HEIGHT

class Tilemap:
    def __init__(self, tileset):
        self.tileset = tileset
        self.column_x = SCREEN_WIDTH // 2 - self.tileset.rect.width // 2
        self.column_y = 0

    def render(self):
        for y in range(0, SCREEN_HEIGHT, self.tileset.rect.height):
            SCREEN.blit(self.tileset.image, (self.column_x, y))