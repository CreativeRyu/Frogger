import pygame
from random import randint

class Car(pygame.sprite.Sprite):
    def __init__(self, position, group):
        super().__init__(group)
        self.name = "car"
        self.coordinates = position
        self.frame_index = 0
        self.random_car = f"Car{randint(1,2)}"
        self.random_animation_import(self.random_car)
        self.image = self.animation[self.frame_index]
        self.rect = self.image.get_rect(center = position)
        
        # Float Based Position
        self.position = pygame.math.Vector2(self.rect.center)
        self.direction = pygame.math.Vector2(1,0)
        if position[0] < 200:       
            self.direction = pygame.math.Vector2(1,0)
        else:
            self.direction = pygame.math.Vector2(-1,0)
        self.speed = 300
        
        # Collision
        self.hitbox = self.rect.inflate(-self.rect.width * 0.3, -self.rect.height * 0.8)
    
    def random_animation_import(self, car):
        path = f"graphix/Car/Car_images/{car}/{car}_"
        self.animation = []
        
        for frame in range(4):
            surface = pygame.image.load(f"{path}{frame}.png")
            self.animation.append(surface)
    
    def animate(self, delta_time):
        self.frame_index += 10 * delta_time
        if self.frame_index >= len(self.animation):
            self.frame_index = 0
        self.image = self.animation[int(self.frame_index)]
        if self.coordinates[0] < 200:       
            self.image = pygame.transform.flip(self.image, True, False)

    def move(self, delta_time):
        self.position += self.direction * self.speed * delta_time
        self.hitbox.center = round(self.position.x), round(self.position.y)
        self.rect.center = self.hitbox.center
    
    def update(self, delta_time):
        self.move(delta_time)
        self.animate(delta_time)
        
        if not -200 < self.rect.x < 3400:
            self.kill()