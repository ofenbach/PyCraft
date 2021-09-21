from ursina import *

class InventoryBar(Entity):

    def __init__(self):
        super().__init__(
            parent=camera.ui,
            model='quad',
            texture=load_texture("assets/inventory.png"),
            scale=(0.5,0.05),
            position=Vec2(0,-0.45),
        )