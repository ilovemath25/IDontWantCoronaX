from src.Scene.scene import Scene
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
        
    def start(self, app):
        print("Scene3 started")
        self.scene_state = "UPDATE"
        
    def update(self, app):
        print("Scene3 updating")
        if True:
            self.scene_state = "END"
            
    def end(self, app):
        print("Scene3 ended")
        self.scene_state = "END"
        app.GameState = "SCENE4"
        app.AppState = "START"