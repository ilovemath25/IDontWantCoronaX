from src.Scene.scene import Scene
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

    def start(self, app):
        print("Scene1 started")
        self.scene_state = "UPDATE"

    def update(self, app):
        print("Scene1 updating")
        if True:
            self.scene_state = "END"

    def end(self, app):
        print("Scene1 ended")
        self.scene_state = "END"
        app.GameState = "SCENE2"
        app.AppState = "START"