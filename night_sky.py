from ursina import Entity, load_texture, scene


class NightSky(Entity):

    def __init__(self):
        super().__init__(
            parent = scene,
            model = 'sphere',
            texture = load_texture("assets/night_sky.png"),
            scale=250,
            double_sided=True,
        )