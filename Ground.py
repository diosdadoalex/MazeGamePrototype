import pygame.sprite, Spritesheet

TILE_SIZE = 100
class Ground(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.x = x * TILE_SIZE
        self.y = y * TILE_SIZE

        self.width = TILE_SIZE
        self.height = TILE_SIZE

        self.ground_spritesheet = Spritesheet.Spritesheet("img/GrassyField.jpg")
        self.image = self.ground_spritesheet.get_sprite(0, 0, self.width, self.height)

        self.rect = self.image.get_rect()
        self.rect.x = self.x
        self.rect.y = self.y