import pygame
from settings import *
class Scene:
    def __init__(self):
        self.scene_state = "START"
        self.background = None
        self.temp_surface = pygame.Surface((SCREEN_WIDTH, SCREEN_HEIGHT)).convert_alpha()
        self.temp_surface.fill((0, 0, 0, 0))