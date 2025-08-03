import pygame

# transparent block for collision detection or visual effects
class Block(pygame.sprite.Sprite):
    def __init__(self, pos, size):
        super().__init__()
        self.image = pygame.Surface(size, pygame.SRCALPHA)
        self.image.fill((255, 0, 0))
        self.rect = self.image.get_rect(topleft=pos)
        self.rect.size = size