import pygame

class SimpleObject(pygame.sprite.Sprite):
    def __init__(self, surface, position, group):
        super().__init__(group)
        self.image = surface
        self.rect = self.image.get_rect(topleft = position)
        self.hitbox = self.rect.inflate(0, -self.rect.height / 2)

class LongObject(pygame.sprite.Sprite):
    def __init__(self, surface, position, group):
        super().__init__(group)
        self.image = surface
        self.rect = self.image.get_rect(topleft = position)
        self.hitbox = self.rect.inflate(-self.rect.width * 0.9, -self.rect.height / 2)
        # hitbox um 10 pixel nach unten shiften
        self.hitbox.bottom = self.rect.bottom - 20
