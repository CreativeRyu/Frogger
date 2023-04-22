import pygame, sys
import game_settings as gs
from player import Player
from car import Car

# Basic Setup # # # # # # # # # # # # # 
pygame.init()
display = pygame.display.set_mode((gs.WINDOW_WIDTH, gs.WINDOW_HEIGHT))
pygame.display.set_caption("Frogger")
clock = pygame.time.Clock()

# Sprite Groups # # # # # # # # # # # #
player_group = pygame.sprite.Group()
all_sprites = pygame.sprite.Group()

# Object Declaration
player = Player((gs.WINDOW_WIDTH // 2, gs.WINDOW_HEIGHT // 2), player_group)
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
    display.fill("blue")
    
    player_group.update(delta_time)
    all_sprites.update(delta_time)
    
    # Draw Graphix
    all_sprites.draw(display)
    player_group.draw(display)
    
    pygame.display.update()