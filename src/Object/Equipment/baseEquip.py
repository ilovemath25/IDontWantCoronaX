import pygame

class BaseEquip(pygame.sprite.Sprite):
    def __init__(self, pos, image):
        super().__init__()
        self.original_image = image
        size = image.get_size()
        self.image = pygame.Surface(size, pygame.SRCALPHA)
        self.image.blit(image, (0, 0))
        self.rect = self.image.get_rect(topleft=pos)

    def Use(self):
        print(f"{self.__class__.__name__} used!")
