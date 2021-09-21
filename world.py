import random

import numpy
import numpy as np

from block import Block


class World:

    def __init__(self, context, size=(8,8)):
        self.size = size
        self.context = context
        self.blocks = []

        self.world_array = numpy.zeros((16,16,16))
        self.world_array_blocks = []
        self.world_array_blocks = [[[0 for k in range(16)] for j in range(16)] for i in range(16)]

        # generate world
        smoothing_time = 0
        y = 0
        for z in range(16):
            for x in range(16):
                smoothing_time += 1
                if smoothing_time > 4:
                    y = np.random.randint(0, 2)
                    smoothing_time = 0
                self.world_array[z][-y][x] = 1   # gras
                self.world_array_blocks[z][-y][x] = Block(context, "dirt", (z, y, x))

        for z in range(8):
            for y in range(1, 5):
                for x in range(16):
                    _random = random.randrange(0, 5)
                    if _random < 3:
                        self.world_array[z][x][y] = 2
                        self.world_array_blocks[z][y][x] = Block(context, "dirt", (z, -y, x))  # gras
                    if _random == 3:
                        self.world_array[z][x][y] = 3
                        self.world_array_blocks[z][y][x] = Block(context, "sand", (z, -y, x))  # gras
                    if _random == 4:
                        self.world_array[z][y][x] = 4
                        self.world_array_blocks[z][y][x] = Block(context, "gravel", (z, -y, x))  # gras

        for z in range(8):
            for y in range(6, 7):
                for x in range(16):
                    self.world_array[z][y][x] = 5  # gras
                    self.world_array_blocks[z][y][x] = Block(context, "stone", (z, -y, x))

        for z in range(8):
            for y in range(7, 8):
                for x in range(16):
                    self.world_array[z][y][x] = 6
                    self.world_array_blocks[z][y][x] = Block(context, "bedrock", (z, -y, x))

    def update_light(self, steve):
        steve_z = float(steve.position[0])
        steve_y = float(steve.position[1])
        steve_x = float(steve.position[2])

        for z in range(16):
            for y in range(16):
                for x in range(16):

                    # only tes on grass
                    if self.world_array[z][-y][x] == 1:
                        distance_steve_block = float(abs((((steve_z - z)**2 + (steve_y - y)**2 + (steve_x - x)**2))**0.5))

                        # SMOOTH LIGHTING
                        if -1 < distance_steve_block < 1:
                            self.world_array_blocks[z][-y][x].update_light(255-(distance_steve_block*20))
                        elif -2 < distance_steve_block < 2:
                            self.world_array_blocks[z][-y][x].update_light(255- (distance_steve_block*25))
                        elif -4 < distance_steve_block < 4:
                            self.world_array_blocks[z][-y][x].update_light(255- (distance_steve_block*30))
                        elif -6 < distance_steve_block < 6:
                            self.world_array_blocks[z][-y][x].update_light(255- (distance_steve_block*30))
                        elif -8 < distance_steve_block < 8:
                            self.world_array_blocks[z][-y][x].update_light(255- (distance_steve_block*30))
                        elif -10 < distance_steve_block < 10:
                            self.world_array_blocks[z][-y][x].update_light(255- (distance_steve_block*30))
                        else:
                            self.world_array_blocks[z][-y][x].update_light(15)


