from ursina import *


class Block(Button):

    def __init__(self, context, texture = "gras", position = (0,0,0)):
        self.context = context
        self._position = position
        self.light_level = 15
        self.color = color.rgb(self.light_level, self.light_level / 2, self.light_level / 4)
        self.punch_sound = Audio("assets/assets_punch_sound.wav", loop = False, autoplay = False)

        self._texture = load_texture("assets/blocks/"+str(texture)+".png")
        super().__init__(
            parent = scene,
            position = self._position,
            model = "cube",
            origin_y = 0.5,
            texture=texture,
            color = color.rgb(self.light_level, self.light_level, self.light_level),
            scale=1,
        )

    def update_light(self, light_level):

        self.light_level = light_level
        self.color = color.rgb(self.light_level, self.light_level/2, self.light_level/4)
        """super().__init__(
            parent=scene,
            position=self._position,
            model="cube",
            origin_y=0.5,
            texture=self._texture,
            color=color.rgb(self._brightness, self._brightness, self._brightness),
            scale=1,
        )"""


    def input(self,key):
        if self.hovered:

            if key == "left mouse down":
                self.punch_sound.play()
                destroy(self)

            if key == "right mouse down":

                if self.context.block_pick == 1:
                    Block(self.context,"gras", position=self.position+mouse.normal)
                if self.context.block_pick == 2:
                    Block(self.context,"dirt",position=self.position+mouse.normal)
                if self.context.block_pick == 3:
                    Block(self.context,"stone",position=self.position+mouse.normal)

                self.punch_sound.play()