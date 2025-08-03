from src.Scene.scene import Scene
from settings import *
import pygame
import os
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
        # self.background = pygame.image.load(os.path.join("assets", "scene3", "background.png")).convert_alpha()
        self.character = Character((SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2))
        self.blocks = pygame.sprite.Group()
        
    def start(self, app):
        print("Scene3 started")
        app.group.add(self.character)
        self.scene_state = "UPDATE"
        
    def update(self, app):
        print("Scene3 updating")
        dx, dy = self.character.key(self.blocks)
        for block in self.blocks:
            # move all blocks
            block.rect.x -= dx
            block.rect.y -= dy
        if False:
            self.scene_state = "END"
            
    def end(self, app):
        print("Scene3 ended")
        self.scene_state = "END"
        app.GameState = "SCENE4"
        app.AppState = "START"