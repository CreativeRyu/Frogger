import pygame
from os import walk

class Player(pygame.sprite.Sprite):
    def __init__(self, position, group):
        super().__init__(group)
        self.import_assets()
        self.frame_index = 0
        self.status = "down"
        # self.image = self.animation[self.frame_index]
        self.image = self.animations[self.status][self.frame_index]
        self.rect = self.image.get_rect(center = position)
        
        # Float Based Position
        self.position = pygame.math.Vector2(self.rect.center)
        self.direction = pygame.math.Vector2()
        self.speed = 200
    
    def import_assets(self): 
        self.animations = {}
        for index, folder in enumerate(walk("graphix/Player/Walk/")):
            if index == 0:
                for name in folder[1]:
                    self.animations[name] = []
            else:
                for file_name in folder[2]:
                    path = folder[0].replace("\\", "/") + "/" + file_name
                    image = pygame.image.load(path).convert_alpha()
                    image_size = pygame.math.Vector2(image.get_size()) * 3
                    scaled_image = pygame.transform.scale(image, (image_size))
                    key = folder[0].split("/")[3]
                    self.animations[key].append(scaled_image)
    
    # Basic Animation without any Controls
    # geht durch die Bilder unter dem status und iteriert sie durch
    def animate(self, delta_time):
        current_animation = self.animations[self.status]
        if self.direction.magnitude() != 0: # Somit muss eine Bewegung vorhanden sein
            self.frame_index += 15 * delta_time
            if self.frame_index >= len(current_animation):
                self.frame_index = 0
        else:
            self.frame_index = 0
        self.image = current_animation[int(self.frame_index)]
    
    def handle_inputs(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_UP]:
            self.direction.y = -1
            self.status = "up"
        elif keys[pygame.K_DOWN]:
            self.direction.y = 1
            self.status = "down"
        else: self.direction.y = 0
        
        if keys[pygame.K_RIGHT]:
            self.direction.x = 1
            self.status = "right"
        elif keys[pygame.K_LEFT]:
            self.status = "left"
            self.direction.x = -1
        else: 
            self.direction.x = 0
    
    def move(self, delta_time):
        if self.direction.magnitude() != 0:
            self.direction = self.direction.normalize()
        self.position += self.direction * self.speed * delta_time
        self.rect.center = round(self.position.x), round(self.position.y)
    
    def update(self, delta_time):
        self.handle_inputs()
        self.move(delta_time)
        self.animate(delta_time)