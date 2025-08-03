import pygame
import math
import os

class Character(pygame.sprite.Sprite):
    def __init__(self, pos):
        super().__init__()
        
        self.walk_images = []
        for i in range(1, 8):
            img = pygame.image.load(os.path.join("assets", "character", f"walk-{i}.png")).convert_alpha()
            w, h = img.get_size()
            img = pygame.transform.smoothscale(img, (w // 2, h // 2))
            self.walk_images.append(img)
        
        idle_img = pygame.image.load(os.path.join("assets", "character", "idle.png")).convert_alpha()
        w, h = idle_img.get_size()
        self.idle_image = pygame.transform.smoothscale(idle_img, (w // 2, h // 2))

        self.current_frame = 0
        self.animation_speed = 0.2
        self.image = self.idle_image
        self.rect = self.image.get_rect(center=pos)
        self.speed = 4
        self.frame_counter = 0
        self.is_idle = True
        self.facing_left = True
        
    def key(self, blocks):
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

        # Flip logic
        if dx < 0:
            self.facing_left = True
        elif dx > 0:
            self.facing_left = False

        # Normalize diagonal movement
        if dx != 0 and dy != 0:
            norm = 1 / math.sqrt(2)
            dx *= norm
            dy *= norm

        # Animation logic (no rect movement here)
        if dx == 0 and dy == 0:
            self.is_idle = True
            img = self.idle_image
            self.current_frame = 0
            self.frame_counter = 0
        else:
            self.is_idle = False
            self.frame_counter += self.animation_speed
            if self.frame_counter >= 1:
                self.current_frame = (self.current_frame + 1) % len(self.walk_images)
                self.frame_counter = 0
            img = self.walk_images[self.current_frame]

        # Apply flip if needed
        if self.facing_left:
            self.image = img
        else:
            self.image = pygame.transform.flip(img, True, False)

        # Return movement vector for moving the world
        return dx * self.speed, dy * self.speed