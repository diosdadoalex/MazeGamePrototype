# This is a sample Python script.
import pygame, random, time, math
import Block, Player

# Sets the size of the screen
import Ground

SCREEN_WIDTH = 700
SCREEN_HEIGHT = 500

# Reminder - set up some colors
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)
BLACK = (0, 0, 0)

PLAYER_X = 50
PLAYER_Y = 50

PLAYER_LAYER = 3
BLOCK_LAYER = 2
GROUND_LAYER = 1

tilemap = [
    'BBBBBBBBBBBBBBBBBBBB',
    'B..................B',
    'B..................B',
    'B..........BBB.....B',
    'B..................B',
    'B........P.........B',
    'B..................B',
    'B..................B',
    'B..................B',
    'B....B.............B',
    'B....B.............B',
    'B....BBB...........B',
    'B..................B',
    'B..................B',
    'BBBBBBBBBBBBBBBBBBBB',
]

block_list = pygame.sprite.Group()
all_sprite_list = pygame.sprite.Group()

def game_test():
    # initialize pygame
    pygame.init()
    size = (SCREEN_WIDTH, SCREEN_HEIGHT)

    # Sets up the screen display
    screen = pygame.display.set_mode(size)

    # Optional - can add a title to the window
    pygame.display.set_caption("This is a screen test")

    # joystick_count = pygame.joystick.get_count()
    # if joystick_count == 0:
    #     print("I couldn't find a joystick")
    # else:
    #     my_joystick = pygame.joystick.Joystick(0)
    #     my_joystick.init()
    #
    # background_image = pygame.image.load("GrassyField.jpg").convert()
    # player_image = pygame.image.load("test_knight.png").convert()
    # font = pygame.font.SysFont("Calibri", 40, True, False)

    clock = pygame.time.Clock()

    player = create_Tilemap()


    old_x = player.rect.x
    old_y = player.rect.y


    done = False
    while not done:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    player.change_speed(-3, 0)
                elif event.key == pygame.K_RIGHT:
                    player.change_speed(3, 0)
                elif event.key == pygame.K_UP:
                    player.change_speed(0, -3)
                elif event.key == pygame.K_DOWN:
                    player.change_speed(0, 3)
            elif event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT:
                    player.change_speed(3, 0)
                elif event.key == pygame.K_RIGHT:
                    player.change_speed(-3, 0)
                elif event.key == pygame.K_UP:
                    player.change_speed(0, 3)
                elif event.key == pygame.K_DOWN:
                    player.change_speed(0, -3)
        count = 2000

        # if joystick_count != 0:
        #     horiz_axis_pos = my_joystick.get_axis(0)
        #     vert_axis_pos = my_joystick.get_axis(1)
        #
        #     x = x + (horiz_axis_pos * 3)
        #     y = y + (vert_axis_pos * 3)

        all_sprite_list.update()

        screen.fill(BLACK)

        all_sprite_list.draw(screen)

        ### This is some basic code for a random battle
        #old_x, old_y = player.check_battle(screen, old_x, old_y)

        pygame.display.flip()

        clock.tick(60)


def create_Tilemap():
    for i, row in enumerate(tilemap):
        for j, column in enumerate(row):
            ground = Ground.Ground(j, i)
            all_sprite_list.add(ground)
            if column == "B":
                block = Block.Block(BLUE, j, i)
                block_list.add(block)
                all_sprite_list.add(block)
            if column == "P":
                player = Player.Player(BLUE, j, i)
                all_sprite_list.add(player)

    player.walls = block_list
    return player

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    game_test()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
