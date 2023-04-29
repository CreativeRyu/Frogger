import pygame

class SpriteObject(pygame.sprite.Sprite):
    def __init__(self, surface, position, group):
        super().__init__(group)
        self.image = surface
        self.rect = self.image.get_rect(topleft = position)