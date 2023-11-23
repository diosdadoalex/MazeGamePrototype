import pygame.sprite, Spritesheet
TILE_SIZE = 35

class Block(pygame.sprite.Sprite):
    def __init__(self, color, x, y):
        super().__init__()

        self.block_spritesheet = Spritesheet.Spritesheet("img/brick_texture.png")
        self.x = x * TILE_SIZE
        self.y = y * TILE_SIZE

        self.width = TILE_SIZE
        self.height = TILE_SIZE

        self.image = self.block_spritesheet.get_sprite(0, 0, TILE_SIZE, TILE_SIZE)

        self.rect = self.image.get_rect()
        self.rect.x = self.x
        self.rect.y = self.y