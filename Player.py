import math

import pygame.sprite
import random, time, Spritesheet

BLACK = (0, 0, 0)

TILE_WIDTH = 40
TILE_HEIGHT = 60

PLAYER_SPEED = 3

class Player(pygame.sprite.Sprite):
    def __init__(self, color, x, y):
        super().__init__()

        self.character_spritesheet = Spritesheet.Spritesheet("img/player_sprite.png")
        self.x = x * TILE_WIDTH
        self.y = y * TILE_HEIGHT
        self.width = TILE_WIDTH
        self.height = TILE_HEIGHT

        self.facing = "down"
        self.animation_loop = 1
        self.image = self.character_spritesheet.get_sprite(3, 2, self.width, self.height)

        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

        self.change_x = 0
        self.change_y = 0
        self.walls = None

    def change_speed(self, x, y):
        self.change_x += x
        self.change_y += y

    def update(self):
        self.movement()
        self.animate()

        self.rect.x += self.change_x

        block_hit_list = pygame.sprite.spritecollide(self, self.walls, False)
        for block in block_hit_list:
            if self.change_x > 0:
                self.rect.right = block.rect.left
            else:
                self.rect.left = block.rect.right

        self.rect.y += self.change_y

        block_hit_list = pygame.sprite.spritecollide(self, self.walls, False)
        for block in block_hit_list:

            # Reset our position based on the top/bottom of the object.
            if self.change_y > 0:
                self.rect.bottom = block.rect.top
            else:
                self.rect.top = block.rect.bottom

    def movement(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_DOWN]:
            self.facing = "down"
        if keys[pygame.K_UP]:
            self.facing = "up"
        if keys[pygame.K_LEFT]:
            self.facing = "left"
        if keys[pygame.K_RIGHT]:
            self.facing = "right"

    def animate(self):
        down_animations = [self.character_spritesheet.get_sprite(3, 2, self.width, self.height),
                           self.character_spritesheet.get_sprite(53, 2, self.width, self.height),
                           self.character_spritesheet.get_sprite(96, 2, self.width, self.height),
                           self.character_spritesheet.get_sprite(135, 2, self.width, self.height)]
        up_animations = [self.character_spritesheet.get_sprite(3, 70, self.width, self.height),
                           self.character_spritesheet.get_sprite(53, 70, self.width, self.height),
                           self.character_spritesheet.get_sprite(96, 70, self.width, self.height),
                           self.character_spritesheet.get_sprite(135, 70, self.width, self.height)]
        left_animations = [self.character_spritesheet.get_sprite(3, 140, self.width, self.height),
                         self.character_spritesheet.get_sprite(53, 140, self.width, self.height),
                         self.character_spritesheet.get_sprite(96, 140, self.width, self.height),
                         self.character_spritesheet.get_sprite(135, 140, self.width, self.height)]
        right_animations = [self.character_spritesheet.get_sprite(3, 210, self.width, self.height),
                           self.character_spritesheet.get_sprite(53, 210, self.width, self.height),
                           self.character_spritesheet.get_sprite(96, 210, self.width, self.height),
                           self.character_spritesheet.get_sprite(135, 210, self.width, self.height)]
        if self.facing == "down":
            if self.change_y == 0:
                self.image = self.character_spritesheet.get_sprite(3, 2, self.width, self.height)
            else:
                self.image = down_animations[math.floor(self.animation_loop)]
                self.animation_loop += 0.1
                if self.animation_loop >= 4:
                    self.animation_loop = 1
        if self.facing == "up":
            if self.change_y == 0:
                self.image = self.character_spritesheet.get_sprite(3, 70, self.width, self.height)
            else:
                self.image = up_animations[math.floor(self.animation_loop)]
                self.animation_loop += 0.1
                if self.animation_loop >= 4:
                    self.animation_loop = 1
        if self.facing == "left":
            if self.change_x == 0:
                self.image = self.character_spritesheet.get_sprite(3, 140, self.width, self.height)
            else:
                self.image = left_animations[math.floor(self.animation_loop)]
                self.animation_loop += 0.1
                if self.animation_loop >= 4:
                    self.animation_loop = 1
        if self.facing == "right":
            if self.change_x == 0:
                self.image = self.character_spritesheet.get_sprite(3, 210, self.width, self.height)
            else:
                self.image = right_animations[math.floor(self.animation_loop)]
                self.animation_loop += 0.1
                if self.animation_loop >= 4:
                    self.animation_loop = 1
    def check_battle(self, screen, old_x, old_y):
        battle_chance = random.randint(0, 100)
        if old_x != self.rect.x and old_y != self.rect.y:
            if battle_chance > 89:
                old_x = self.rect.x
                old_y = self.rect.y
                screen.fill(BLACK)
                pygame.display.flip()
                time.sleep(3)
        return old_x, old_y
