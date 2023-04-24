import pygame, sys
import game_settings as gs
from player import Player
from car import Car

class AllSprites(pygame.sprite.Group):
    def __init__(self):
        super().__init__()
        self.offset = pygame.math.Vector2()
        self.background = pygame.image.load("graphix/level/map.png").convert()
        self.foreground = pygame.image.load("graphix/level/overlay.png").convert_alpha()

    def custom_draw(self):
        
        display.blit(self.background, (0,0))
        
        for sprite in self.sprites():
            offset_position = sprite.rect.topleft + self.offset
            display.blit(sprite.image, offset_position)
        
        display.blit(self.foreground, (0,0))

# Basic Setup # # # # # # # # # # # # # 
pygame.init()
display = pygame.display.set_mode((gs.WINDOW_WIDTH, gs.WINDOW_HEIGHT))
pygame.display.set_caption("Frogger")
clock = pygame.time.Clock()

# Sprite Groups # # # # # # # # # # # #
all_sprites = AllSprites()

# Object Declaration
player = Player((gs.WINDOW_WIDTH // 2, gs.WINDOW_HEIGHT // 2), all_sprites)
car = Car((100,200), all_sprites)

# Game Loop # # # # # # # # # # # # # # # #
while True:
    # Event Loop # # # # # # # # # # # # # #
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        
    delta_time = clock.tick() / 1000
    
    # Draw Background
    # display.fill("blue")

    all_sprites.update(delta_time)
    
    # Draw Graphix
    # all_sprites.draw(display)
    all_sprites.custom_draw()
    
    pygame.display.update()