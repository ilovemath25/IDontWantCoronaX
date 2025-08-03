from src.Scene.scene import Scene
from settings import *
from src.Core.slideSprite import SlideSprite
import pygame
import os
"""
video (opening scene)
- the character is in the future
- they are studying about covid-19
- the current date and time are shown
- the screen gradually gets darker as the character fall asleep
"""
class Scene1(Scene):
    def __init__(self):
        super().__init__()
        self.slides = []
        self.current_index = 0
        self.current_y = 0

    def start(self, app):
        print("Scene1 started")
        pygame.mixer.music.load(os.path.join("sound", "bgm", "scene1-2.mp3"))
        pygame.mixer.music.play(-1)
        slide_images = [pygame.image.load(os.path.join("assets", "scene1", "scene1-"+str(i)+".png")).convert_alpha() for i in range(1, 4)]
        for image in slide_images:
            surf = pygame.Surface((SCREEN_WIDTH, 1000)).convert_alpha()
            surf.blit(image, (0, 0))
            slide = SlideSprite(surf, duration=5)
            self.slides.append(slide)
        if self.slides:
            app.group.add(self.slides[0])
        self.current_y = 0
        self.scene_state = "UPDATE"

    def update(self, app):
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
        print("Scene1 ended")

        for slide in self.slides:
            app.group.remove(slide)

        self.scene_state = "END"
        app.GameState = "SCENE2"
        app.AppState = "START"