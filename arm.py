from ursina import *


class Arm(Entity):


    def __init__(self):

        super().__init__(
            parent = camera.ui,
            model = 'sphere',
            texture = load_texture("assets/torch.png"),
            scale=0.2,
            rotation = Vec3(150,-10,0),
            position = Vec2(0.4,-0.5)
        )
        self.timer = 0

    def walk_animation(self):
        self.set_position(Vec3((10-sin(self.timer/6)*1, -10 + sin(self.timer/6)*1.8), 10))
        #self.position[1] = sin(self.timer)*5
        self.timer += 1