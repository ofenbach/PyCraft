from ursina import *

class Button(Button):

    def __init__(self):
        super().__init__(
            parent = scene,
            model= "cube",
            texture = "brick",

            color = "#303030",
            highlight_color = color.red,
            pressed_color = color.red,
        )

    def input(self, key):
        if self.hovered:
            if key == "left mouse down":
                self.color = color.blue