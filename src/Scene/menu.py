from src.Scene.scene import Scene
from settings import *
import pygame
import os
"""
menu (start)
- title screen with options to start the game or exit
"""

class Menu(Scene):
    def __init__(self):
        super().__init__()
        self.background_imgs = [pygame.image.load(os.path.join("assets", "menu", "menu-1.png")), pygame.image.load(os.path.join("assets", "menu", "menu-2.png"))]
        self.background_index = 0
        self.background_timer = 0
        self.background_interval = 500
        self.background_sprite = None

        self.start_imgs = [pygame.image.load(os.path.join("assets", "menu", "start-1.png")), pygame.image.load(os.path.join("assets", "menu", "start-2.png"))]
        self.exit_imgs = [pygame.image.load(os.path.join("assets", "menu", "exit-1.png")), pygame.image.load(os.path.join("assets", "menu", "exit-2.png"))]

        self.start_sprite = None
        self.exit_sprite = None

        self.start_pos = (SCREEN_WIDTH // 2, 400)
        self.exit_pos = (SCREEN_WIDTH // 2, 530)
        self.end_time = 0
        
    def start(self, app):
        print("Menu started")
        self.scene_state = "UPDATE"

        self.background_sprite = pygame.sprite.Sprite()
        self.background_sprite.image = self.background_imgs[self.background_index]
        self.background_sprite.rect = self.background_sprite.image.get_rect(topleft=(0, 0))
        app.group.add(self.background_sprite, layer=0)

        self.start_sprite = pygame.sprite.Sprite()
        self.start_sprite.image = self.start_imgs[0]
        self.start_sprite.rect = self.start_sprite.image.get_rect(center=self.start_pos)
        app.group.add(self.start_sprite, layer=1)

        self.exit_sprite = pygame.sprite.Sprite()
        self.exit_sprite.image = self.exit_imgs[0]
        self.exit_sprite.rect = self.exit_sprite.image.get_rect(center=self.exit_pos)
        app.group.add(self.exit_sprite, layer=1)

        self.last_update = pygame.time.get_ticks()

    def update(self, app):
        print("Menu updated")
        # Animate background
        now = pygame.time.get_ticks()
        if now - self.last_update > self.background_interval:
            self.background_index = (self.background_index + 1) % 2
            self.background_sprite.image = self.background_imgs[self.background_index]
            self.last_update = now

        # Handle mouse interaction
        mouse_pos = pygame.mouse.get_pos()
        mouse_click = pygame.mouse.get_pressed()

        # Hover effects
        if self.start_sprite.rect.collidepoint(mouse_pos):
            self.start_sprite.image = self.start_imgs[1]
            if mouse_click[0]:
                self.scene_state = "END"
                self.end_time = pygame.time.get_ticks()
        else:
            self.start_sprite.image = self.start_imgs[0]

        if self.exit_sprite.rect.collidepoint(mouse_pos):
            self.exit_sprite.image = self.exit_imgs[1]
            if mouse_click[0]:
                app.AppState = "END"
        else:
            self.exit_sprite.image = self.exit_imgs[0]

    def end(self, app):
        print("Menu ended")
        if pygame.time.get_ticks() - self.end_time > 3000:
            app.GameState = "SCENE1"
            app.AppState = "START"

        app.group.remove(self.background_sprite)
        app.group.remove(self.start_sprite)
        app.group.remove(self.exit_sprite)