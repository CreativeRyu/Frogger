import pygame
from os import walk

class Car(pygame.sprite.Sprite):
    def __init__(self, position, group):
        super().__init__(group)
        self.image = "bla" # pic a random car from the cars folder
        self.rect = self.image.get_rect(center = position)