import pygame
from src.Scene.scene1 import Scene1
from src.Scene.scene2 import Scene2
from src.Scene.scene3 import Scene3
from src.Scene.scene4 import Scene4

class App:
    def __init__(self):
        self.AppState = "START"
        self.GameState = "SCENE1"
        self.scene = None
        self.group = pygame.sprite.LayeredUpdates()

    @property
    def app_state(self):
        return self.AppState

    def start(self):
        if self.GameState == "SCENE1":
            self.scene = Scene1()
        elif self.GameState == "SCENE1":
            self.scene = Scene1()
        elif self.GameState == "SCENE2":
            self.scene = Scene2()
        elif self.GameState == "SCENE3":
            self.scene = Scene3()
        elif self.GameState == "SCENE4":
            self.scene = Scene4()
        self.AppState = "UPDATE"

    def update(self, screen):
        if self.scene:
            if self.scene.scene_state == "START":
                self.scene.start(self)
            elif self.scene.scene_state == "UPDATE":
                self.scene.update(self)
            elif self.scene.scene_state == "END":
                self.scene.end(self)
            self.group.update()
            self.group.draw(screen)

    def end(self):
        print("Ending the app")