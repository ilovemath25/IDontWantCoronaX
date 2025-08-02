# the one that eat the bat
import pygame
class Enemy(pygame.sprite.Sprite):
    def __init__(self, pos):
        super().__init__()
        self.image = pygame.Surface((30, 30))
        self.image.fill((255, 0, 0))
        self.rect = self.image.get_rect(topleft=pos)
        self.speed = 2

    def update(self):
        self.rect.y += self.speed
