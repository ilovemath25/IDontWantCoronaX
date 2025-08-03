import pygame
import math
import os
class Character(pygame.sprite.Sprite):
    def __init__(self, pos):
        super().__init__()
        self.images = [pygame.image.load(os.path.join("assets", "character", "character"+str(i)+".png")).convert_alpha() for i in range(1, 8)]
        self.current_frame = 0
        self.animation_speed = 0.2
        self.image = self.images[self.current_frame]
        self.rect = self.image.get_rect(topleft=pos)
        self.speed = 2
        self.frame_counter = 0

    def key(self):
        keys = pygame.key.get_pressed()
        dx, dy = 0, 0
        if keys[pygame.K_LEFT] or keys[pygame.K_a]:
            dx -= 1
        if keys[pygame.K_RIGHT] or keys[pygame.K_d]:
            dx += 1
        if keys[pygame.K_UP] or keys[pygame.K_w]:
            dy -= 1
        if keys[pygame.K_DOWN] or keys[pygame.K_s]:
            dy += 1
        if dx != 0 and dy != 0:
            normal = 1 / math.sqrt(2)
            dx *= normal
            dy *= normal

        self.rect.x += int(dx * self.speed)
        self.rect.y += int(dy * self.speed)
        
        # animation logic
        self.frame_counter += self.animation_speed
        if self.frame_counter >= 1:
            self.current_frame = (self.current_frame + 1) % len(self.images)
            self.image = self.images[self.current_frame]
            self.frame_counter = 0