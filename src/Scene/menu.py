from src.Scene.scene import Scene
"""
menu (start)
- title screen with options to start the game or exit
"""
class Menu(Scene):
    def __init__(self):
        super().__init__()

    def start(self, app):
        print("Menu started")
        self.scene_state = "UPDATE"

    def update(self, app):
        print("Menu updating")
        if True:
            self.scene_state = "END"

    def end(self, app):
        print("Menu ended")
        self.scene_state = "END"
        app.GameState = "SCENE1"
        app.AppState = "START"