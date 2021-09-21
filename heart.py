from ursina import *

class Heart(Entity):

    def __init__(self):
        super().__init__(
            parent=camera.ui,
            model='quad',
            texture=load_texture("assets/heart.png"),
            scale=(0.025,0.025),
            position=Vec2(-0.24,-0.4),
        )