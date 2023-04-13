import pygame

class Player(pygame.sprite.Sprite):
    def __init__(self, position, group):
        super().__init__(group)
        self.import_assets()
        self.frame_index = 0
        self.image = self.animation[self.frame_index]
        self.rect = self.image.get_rect(center = position)
        
        # Float Based Position
        self.position = pygame.math.Vector2(self.rect.center)
        self.direction = pygame.math.Vector2()
        self.speed = 200
    
    def import_assets(self):
        path = "Player/Sidewalk/Walking Side_Animation 1_"
        self.animation = [pygame.image.load(f"{path}{frame}.png").convert_alpha() for frame in range(10)]
        
    def move(self, delta_time):
        if self.direction.magnitude() != 0:
            self.direction = self.direction.normalize()
        self.position += self.direction * self.speed * delta_time
        self.rect.center = round(self.position.x), round(self.position.y)
    
    def animate(self, delta_time):
        self.frame_index += 10 * delta_time
        if self.frame_index >= len(self.animation):
            self.frame_index = 0
        self.image = self.animation[int(self.frame_index)]
    
    def handle_inputs(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_UP]:
            self.direction.y = -1
        elif keys[pygame.K_DOWN]:
            self.direction.y = 1
        else: self.direction.y = 0

        if keys[pygame.K_RIGHT]:
            self.direction.x = 1
        elif keys[pygame.K_LEFT]:
            self.direction.x = -1
        else: 
            self.direction.x = 0
    
    def update(self, delta_time):
        self.handle_inputs()
        self.move(delta_time)
        self.animate(delta_time)