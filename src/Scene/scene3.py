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
    def __init__(self):
        super().__init__()
        self.backgrounds = []
        self.background_index = 0
        self.character = Character((SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2))
        self.blocks = pygame.sprite.Group()
        self.equipments = pygame.sprite.Group()
        
    def start(self, app):
        print("Scene3 started")
        for i in range(1, 4):
            img = pygame.image.load(os.path.join("assets", "scene3", f"bg-1.png")).convert_alpha()
            sprite = pygame.sprite.Sprite()
            sprite.image = img
            sprite.rect = img.get_rect(center=(1675, 255))
            self.backgrounds.append(sprite)
            self.background_index = 0

        app.group.add(self.backgrounds[self.background_index], layer=0)
        app.group.add(self.character, layer=5)
        self.scene_state = "UPDATE"
        self.equipments.add(
            Grenade((300, 200)),
            Gun((600, 400)),
        )
        for equipment in self.equipments:
            app.group.add(equipment, layer=3)
    
    def update(self, app):
        print("Scene3 updating")
        dx, dy = self.character.key(app, self.blocks, self.equipments)
        self.backgrounds[self.background_index].rect.x -= dx
        self.backgrounds[self.background_index].rect.y -= dy
        for spr in list(self.blocks) + list(self.equipments):
            spr.rect.x -= dx
            spr.rect.y -= dy
        if False:
            self.scene_state = "END"
            
    def end(self, app):
        print("Scene3 ended")
        self.scene_state = "END"
        app.GameState = "SCENE4"
        app.AppState = "START"