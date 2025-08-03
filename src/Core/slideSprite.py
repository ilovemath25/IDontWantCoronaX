import pygame
from settings import *
class SlideSprite(pygame.sprite.Sprite):
    def __init__(self, image, duration=2.0):
        super().__init__()
        self.original_image = image.convert_alpha()
        self.image = self.original_image.copy()
        self.rect = self.image.get_rect(topleft=(0, 0))
        self.screen_size = (SCREEN_WIDTH, SCREEN_HEIGHT)
        self.duration = duration
        self.state = "fade_in"
        self.timer = 0
        self.fade_steps = int(FPS * 0.5)
        self.hold_steps = int(FPS * (duration - 1.0))
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