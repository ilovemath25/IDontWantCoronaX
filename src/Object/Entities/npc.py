import pygame
import os

class Npc:
    def __init__(self, pos, index):
        if index==1: imgCount = 7
        else: imgCount = 8
        for i in range(1, imgCount + 1):
            img = pygame.image.load(os.path.join("assets", "npc", f"Npc{index}-{i}.png")).convert_alpha()
            w, h = img.get_size()
            img = pygame.transform.smoothscale(img, (w // 2, h // 2))
            self.walk_images.append(img)