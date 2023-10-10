from mcpi.minecraft import Minecraft

import time
from littlehouse import house

mc = Minecraft.create()

x, y, z = mc.player.getTilePos()

for j in range(6):
    house(x, y, z)
    z = z + 15