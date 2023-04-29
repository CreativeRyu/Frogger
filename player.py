import pygame
from os import walk
import sys

class Player(pygame.sprite.Sprite):
    def __init__(self, position, group, collision_sprites):
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
        
        # Collisions
        self.collision_sprites = collision_sprites
        self.hitbox = self.rect.inflate(-self.rect.width * 0.4, -self.rect.height / 2)
    
    def car_collision(self, sprite):
        if hasattr(sprite, "name") and sprite.name == "car":
            pygame.quit()
            sys.exit()
    
    def collision(self, axis):
        if axis == "horizontal":
            for sprite in self.collision_sprites.sprites():
                if sprite.hitbox.colliderect(self.hitbox):
                    self.car_collision(sprite)
                    if self.direction.x > 0: # player moving right
                        self.hitbox.right = sprite.hitbox.left
                    if self.direction.x < 0: # player moving left
                        self.hitbox.left = sprite.hitbox.right
                    self.rect.centerx = self.hitbox.centerx
                    self.position.x = self.hitbox.centerx
        else:
            for sprite in self.collision_sprites.sprites():
                if sprite.hitbox.colliderect(self.hitbox):
                    self.car_collision(sprite)
                    if self.direction.y > 0: # player moving down
                        self.hitbox.bottom = sprite.hitbox.top
                    if self.direction.y < 0: # player moving up
                        self.hitbox.top = sprite.hitbox.bottom
                    self.rect.centery = self.hitbox.centery
                    self.position.y = self.hitbox.centery
    
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
        else: 
            self.direction.y = 0
        
        if keys[pygame.K_RIGHT]:
            self.direction.x = 1
            self.status = "right"
        elif keys[pygame.K_LEFT]:
            self.status = "left"
            self.direction.x = -1
        else: 
            self.direction.x = 0
    
    # Die unsichtbare Wand definieren
    # Der Bereich in dem sich der Player bewegen darf
    def restrict_player(self):
        if self.rect.left < 620:
            self.position.x = 620 + self.rect.width / 2
            self.rect.left = 620

        if self.rect.right > 2584:
            self.position.x = 2584 - self.rect.width / 2
            self.rect.right = 2584

        if self.rect.bottom > 3500:
            self.position.y = 3500 - self.rect.height / 2
            self.rect.bottom = 3500
        
        if self.rect.bottom > 3500:
            self.position.y = 3500 - self.rect.height / 2
            self.rect.bottom = 3500
            
        self.hitbox.center = self.rect.center
        
    def move(self, delta_time):
        if self.direction.magnitude() != 0:
            self.direction = self.direction.normalize()
        
        # horizontal movement + collision
        self.position.x += self.direction.x * self.speed * delta_time
        self.hitbox.centerx = round(self.position.x) # for collision
        self.rect.centerx = self.hitbox.centerx # for drawing
        self.collision("horizontal")
        
        # vertical movement + collision
        self.position.y += self.direction.y * self.speed * delta_time
        self.hitbox.centery = round(self.position.y)
        self.rect.centery = self.hitbox.centery
        self.collision("vertical")
    
    def update(self, delta_time):
        self.handle_inputs()
        self.move(delta_time)
        self.animate(delta_time)
        self.restrict_player()