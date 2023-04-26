import pygame
import sys
import game_settings as gs
from player import Player
from car import Car
from random import choice, randint
from levelobjects import SpriteObject

class AllSprites(pygame.sprite.Group):
    def __init__(self):
        super().__init__()
        self.offset = pygame.math.Vector2()
        self.background = pygame.image.load("graphix/level/map.png").convert()
        self.foreground = pygame.image.load("graphix/level/overlay.png").convert_alpha()

    def custom_draw(self):
        # Camera Movement
        # change the offsetvector for camera movement
        self.offset.x = player.rect.centerx - gs.WINDOW_WIDTH / 2
        self.offset.y = player.rect.centery - gs.WINDOW_HEIGHT / 2
        
        # draw background
        display.blit(self.background, -self.offset)
        
        # draw player sprites and objects
        for sprite in sorted(self.sprites(), key = lambda sprite: sprite.rect.centery):
            offset_position = sprite.rect.topleft - self.offset
            display.blit(sprite.image, offset_position)
        
        # draw foreground
        display.blit(self.foreground, -self.offset)

# Erstellung der Levelobjekte auf der Karte zu Beginn es Spiels
def init_level_objects(sprite_dictionary, path):
    for file_name, position_list in sprite_dictionary.items():
        surface = pygame.image.load(f"{path}{file_name}.png").convert_alpha()
        for position in position_list:
            SpriteObject(surface, position, all_sprites)

# Basic Setup # # # # # # # # # # # # # 
pygame.init()
display = pygame.display.set_mode((gs.WINDOW_WIDTH, gs.WINDOW_HEIGHT))
pygame.display.set_caption("Frogger")
clock = pygame.time.Clock()

# Sprite Groups # # # # # # # # # # # #
all_sprites = AllSprites()

# Object Declaration
player = Player((2062, 3274), all_sprites)

# Object Sprite Init Level Creation
init_level_objects(gs.SIMPLE_OBJECTS, gs.SIMPLE_OBJECTS_PATH)
init_level_objects(gs.LONG_OBJECTS, gs.LONG_OBJECTS_PATH)

# Timer
car_timer = pygame.event.custom_type()
pygame.time.set_timer(car_timer, 100)
car_position_list = []

# Game Loop # # # # # # # # # # # # # # # #
while True:
    # Event Loop # # # # # # # # # # # # # #
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
            
        if event.type == car_timer:
            random_position = choice(gs.CAR_START_POSITIONS)
            if random_position not in car_position_list:
                car_position_list.append(random_position)
                current_position = (random_position[0], random_position[1] + randint(-8, 8))
                car = Car(current_position, all_sprites)
            if len(car_position_list) > 5:
                del car_position_list[0]
        
    delta_time = clock.tick() / 1000
    
    # Draw Background
    # display.fill("blue")

    all_sprites.update(delta_time)
    
    # Draw Graphix
    # all_sprites.draw(display)
    all_sprites.custom_draw()
    
    pygame.display.update()