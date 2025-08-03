from src.Scene.scene import Scene
from settings import *
from src.Core.slideSprite import SlideSprite
import pygame
import os
"""
video (transition scene)
- the character is in a classroom, taking an exam
- suddenly, character feel dizzy and falls asleep
- the character wake up in the past and see the world before covid-19
- the character decides to prevent it
"""
class Scene2(Scene):
    def __init__(self):
        super().__init__()
        self.slides = []
        self.current_index = 0
        self.current_y = 0

    def start(self, app):
        print("Scene2 started")
        slide_images = [pygame.image.load(os.path.join("assets", "scene2", "scene2-"+str(i)+".png")).convert_alpha() for i in range(1, 6)]
        for image in slide_images:
            surf = pygame.Surface((SCREEN_WIDTH, SCREEN_HEIGHT)).convert_alpha()
            surf.blit(image, (0, 0))
            slide = SlideSprite(surf, duration=5)
            self.slides.append(slide)
        if self.slides:
            app.group.add(self.slides[0])
        self.current_y = 0
        self.scene_state = "UPDATE"

    def update(self, app):
        if not self.slides:
            self.scene_state = "END"
            return

        current_slide = self.slides[self.current_index]

        if current_slide.state == "done":
            app.group.remove(current_slide)
            self.current_index += 1

            if self.current_index < len(self.slides):
                app.group.add(self.slides[self.current_index])
            else:
                self.scene_state = "END"
        else:
            current_slide.rect.y -= self.current_y % 1
            self.current_y += 0.5

    def end(self, app):
        print("Scene2 ended")

        for slide in self.slides:
            app.group.remove(slide)

        self.scene_state = "END"
        app.GameState = "SCENE3"
        app.AppState = "START"
