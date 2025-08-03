from src.Scene.scene import Scene
from settings import SCREEN_WIDTH, SCREEN_HEIGHT
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
        self.slides = []       # List of SlideSprite
        self.current_index = 0

    def start(self, app):
        print("Scene1 started")
        slide_images = [pygame.image.load(os.path.join("assets", "scene1", "scene1-"+str(i)+".png")).convert_alpha() for i in range(1, 4)]
        for image in slide_images:
            surf = pygame.Surface((SCREEN_WIDTH, SCREEN_HEIGHT)).convert_alpha()
            surf.blit(image, (0, 0))
            slide = SlideSprite(surf, screen_size=(SCREEN_WIDTH, SCREEN_HEIGHT), duration=3)
            self.slides.append(slide)
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
        

    def end(self, app):
        print("Scene1 ended")

        for slide in self.slides:
            app.group.remove(slide)

        self.scene_state = "END"
        app.GameState = "SCENE2"
        app.AppState = "START"

class SlideSprite(pygame.sprite.Sprite):
    def __init__(self, image, screen_size, duration=2.0, fps=60):
        super().__init__()
        self.original_image = image.convert_alpha()
        self.image = self.original_image.copy()
        self.rect = self.image.get_rect(topleft=(0, 0))
        self.screen_size = screen_size
        self.duration = duration
        self.fps = fps
        self.state = "fade_in"
        self.timer = 0
        self.fade_steps = int(fps * 0.5)
        self.hold_steps = int(fps * (duration - 1.0))
        self.current_step = 0

    def update(self):
        if self.state == "fade_in":
            alpha = int(255 * self.current_step / self.fade_steps)
            self.image = self.original_image.copy()
            self.image.set_alpha(alpha)
            self.current_step += 1
            if self.current_step >= self.fade_steps:
                self.state = "hold"
                self.current_step = 0
        elif self.state == "hold":
            self.image = self.original_image.copy()
            self.image.set_alpha(255)
            self.current_step += 1
            if self.current_step >= self.hold_steps:
                self.state = "fade_out"
                self.current_step = 0
        elif self.state == "fade_out":
            alpha = int(255 * (1 - self.current_step / self.fade_steps))
            self.image = self.original_image.copy()
            self.image.set_alpha(alpha)
            self.current_step += 1
            if self.current_step >= self.fade_steps:
                self.state = "done"