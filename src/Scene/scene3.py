import pygame
import os
from src.Scene.scene import Scene
from settings import *
from src.Object.Equipment import *
from src.Object.Entities.character import Character
"""
gameplay (main loop)
- the player is in the past
- in each time loop, the character collects different equipment
- the goal is to find and defeat the people that ate the bat
- the character fails each time and loops back to the beginning
- this continue until the character finds the final equipment which is bat
- the character gave up and eats the bat, and the covid-19 still exists
"""
class Scene3(Scene):
    BG_LAYER, EQ_LAYER, CH_LAYER = 0, 3, 5

    def __init__(self):
        super().__init__()
        self.bg_imgs = [pygame.image.load(os.path.join("assets", "scene3", f"bg-{i}.png")).convert_alpha() for i in range(1, 4)]
        self.bg_idx = 0
        self.bg = pygame.sprite.Sprite()
        self.bg._layer = self.BG_LAYER
        self.bg.image = self.bg_imgs[0]
        self.bg.rect = self.bg.image.get_rect(center=(1675,255))

        self.character = Character((SCREEN_WIDTH//2, SCREEN_HEIGHT//2))
        self.character._layer = self.CH_LAYER

        self.equipments = pygame.sprite.Group(
            Grenade((300,200)),
            Gun((600,400)),
        )
        for e in self.equipments: e._layer = self.EQ_LAYER

        self.blocks = pygame.sprite.Group()
        self.bg_interval = 10

    def start(self, app):
        for spr in (self.bg, self.character, *self.equipments):
            app.group.add(spr, layer=spr._layer)
        self.scene_state = "UPDATE"

    def update(self, app):
        t = pygame.time.get_ticks() // self.bg_interval
        self.bg_idx = t % len(self.bg_imgs)
        self.bg.image = self.bg_imgs[self.bg_idx]

        dx, dy = self.character.key(app, self.blocks, self.equipments)
        for spr in (self.bg, *self.blocks, *self.equipments):
            spr.rect.move_ip(-dx, -dy)
