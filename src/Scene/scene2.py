from src.Scene.scene import Scene
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
    
    def start(self, app):
        print("Scene2 started")
        self.scene_state = "UPDATE"
        
    def update(self, app):
        print("Scene2 updating")
        if True:
            self.scene_state = "END"
            
    def end(self, app):
        print("Scene2 ended")
        self.scene_state = "END"
        app.GameState = "SCENE3"
        app.AppState = "START"