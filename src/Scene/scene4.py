from src.Scene.scene import Scene
"""
video (ending scene)
- the character wakes up from a dream
- the end
"""
class Scene4(Scene):
    def __init__(self):
        super().__init__()
        
    def start(self, app):
        print("Scene4 started")
        self.scene_state = "UPDATE"
        
    def update(self, app):
        print("Scene4 updating")
        if True:
            self.scene_state = "END"
            
    def end(self, app):
        print("Scene4 ended")
        self.scene_state = "END"
        app.AppState = "END"