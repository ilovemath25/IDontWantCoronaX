import pygame
import math
import os
from src.Object.Equipment import *

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
        
        self.equipment = None
        self.equip_icon = None

        self.is_using = False
        self.use_frames = []
        self.current_use_frame = 0
        self.use_frame_counter = 0

        self.nearby_item = None
        self.prompt_sprite = None
       
    def equip(self, item):
        """Pick up `item` and remember its half-size icon."""
        self.equipment = item
        w,h = item.image.get_size()
        self.equip_icon = pygame.transform.smoothscale(item.image, (w//2, h//2))

    def use_equipment(self):
        """Start the use-animation and immediately call its Use()."""
        if not self.equipment or self.is_using:
            return
        folder = type(self.equipment).__name__.lower()
        self.use_frames.clear()
        for i in range(1,6):
            fn = f"assets/character/{folder}-{i}.png"
            img = pygame.image.load(fn).convert_alpha()
            w,h = img.get_size()
            self.use_frames.append(pygame.transform.smoothscale(img,(w//2,h//2)))

        self.is_using = True
        self.equipment.is_used = True
        self.current_use_frame = 0
        self.use_frame_counter = 0

    def key(self, app, blocks, equipments):
        # equipment usage
        if self.equipment and self.equipment.is_used:
            self.equipment.Use(app, self)
        
        # using equipment
        if self.is_using:
            self.use_equipment()
            return 0,0
        # movement
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

        # diagonal movement
        if dx != 0 and dy != 0:
            norm = 1 / math.sqrt(2)
            dx *= norm
            dy *= norm

        # Animation logic
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

        # flip
        if self.facing_left:
            self.image = img
        else:
            self.image = pygame.transform.flip(img, True, False)
        
        # detect nearby equipment
        nearby = pygame.sprite.spritecollide(self, equipments, False)
        if nearby:
            self.nearby_item = nearby[0]
            if self.prompt_sprite is None:
                font = pygame.font.Font(None, 24)
                surf = font.render("Press K to pick up", True, (255, 255, 255))
                self.prompt_sprite = pygame.sprite.Sprite()
                self.prompt_sprite.image = surf
                self.prompt_sprite.rect = surf.get_rect(midbottom=(self.rect.centerx, self.rect.top - 5))
                app.group.add(self.prompt_sprite, layer=10)
            else:
                self.prompt_sprite.rect.midbottom = (
                    self.rect.centerx,
                    self.rect.top - 5
                )
        else:
            if self.prompt_sprite is not None:
                app.group.remove(self.prompt_sprite)
                self.prompt_sprite = None
                
        # pick up
        if self.nearby_item and keys[pygame.K_k]:
            item = self.nearby_item
            self.equip(item)
            equipments.remove(item)
            app.group.remove(item)

        # use equipment
        if keys[pygame.K_j]:
            self.use_equipment()
        
        # collision detection
        if pygame.sprite.spritecollideany(self, blocks):
            dx = 0
            dy = 0
        
        # Return movement vector for moving the world
        return dx * self.speed, dy * self.speed