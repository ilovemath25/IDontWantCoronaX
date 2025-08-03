import pygame
from src.Object.Equipment.baseEquip import BaseEquip

class Gun(BaseEquip):
    def __init__(self, pos):
        image = pygame.image.load("assets/equipment/gun.png").convert_alpha()
        super().__init__(pos, image)
        
        w, h = image.get_size()
        self.image = pygame.transform.smoothscale(image, (w // 2, h // 2))
        
        self.rect = self.image.get_rect(center=pos)