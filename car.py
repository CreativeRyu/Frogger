import pygame
from os import walk
from random import choice

class Car(pygame.sprite.Sprite):
    def __init__(self, position, group):
        super().__init__(group)
        self.image = self.random_image_import()
        self.rect = self.image.get_rect(center = position)
        
        # Float Based Position
        self.position = pygame.math.Vector2(self.rect.center)
        if position[0] < 200:       
            self.direction = pygame.math.Vector2(1,0)
            self.image = pygame.transform.flip(self.image, True, False)
        else:
            self.direction = pygame.math.Vector2(-1,0)
        self.speed = 300
    
    def random_image_import(self):
        path = "Car/Car_images/"
        for _, _, image_list in walk(path):
            file_name = choice(image_list)
        image = pygame.image.load(path + file_name).convert_alpha()
        image_size = pygame.math.Vector2(image.get_size()) * 1.5
        scaled_image = pygame.transform.scale(image, (image_size))
        return scaled_image

    def move(self, delta_time):
        self.position += self.direction * self.speed * delta_time
        self.rect.center = round(self.position.x), round(self.position.y)
    
    def update(self, delta_time):
        self.move(delta_time)
        
        if not -200 < self.rect.x < 3400:
            self.kill()