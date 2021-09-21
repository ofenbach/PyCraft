
from ursina.prefabs.first_person_controller import FirstPersonController

import night_sky
from arm import Arm
from context import Context
from heart import Heart
from inv_bar import *
from world import World

context = Context()

speed_timer = 0
rotation_timer = 0

def update():
    global speed_timer


    if held_keys["w"]:
        arm.walk_animation()
    if held_keys["1"]:
        context.block_pick = 1
    if held_keys["2"]:
        context.block_pick = 2
    if held_keys["3"]:
        context.block_pick = 3

    if held_keys["left shift"]:
        speed_timer+=0.25
        if speed_timer > 3.5:
            speed_timer = 3.5
    else:
        if speed_timer > 0:
            speed_timer -= 0.5

    steve.speed = 3.5 + speed_timer

    world.update_light(steve)



app = Ursina()
window.title = 'HorrorCraft'                # The window title
window.borderless = True               # Show a border
#window.fullscreen = True               # Do not go Fullscreen
window.exit_button.visible = False      # Do not show the in-game red X that loses the window
window.fps_counter.enabled = True

# generate world
sky = night_sky.NightSky()
world = World(context, (21,21))

inventory = InventoryBar()
heart = Heart()
arm = Arm()
steve = FirstPersonController()
forest = Audio("assets/forest.wav", loop = True, autoplay = True)
forest.play()

app.run()