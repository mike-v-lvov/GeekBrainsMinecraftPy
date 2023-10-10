from mcpi.minecraft import Minecraft

import time

mc = Minecraft.create()


def hipped_roof(x_roof, y_roof, z_roof, height_roof, block): # крыша  дома
    levels = range(height_roof) # [0, 1, 2, 3, 4], если height_roof = 5
    for level in levels:
        mc.setBlocks(
            x_roof - level,
            y_roof,
            z_roof - level,
            x_roof + level,
            y_roof,
            z_roof + level,
            block
        )
        y_roof -= 1


def window(x_window, y_window, z_window, block_window):
    mc.setBlocks(x_window, y_window + 2, z_window + 3, x_window + 10, y_window + 4, z_window + 4, block_window)



def base(x_base, y_base, z_base, height_base, block_base):
    air = 0
    mc.setBlocks(x_base, y_base, z_base, x_base + height_base, y_base + height_base, z_base + height_base, block_base)
    mc.setBlocks(x_base + 1, y_base + 1, z_base + 1, x_base + height_base - 1, y_base + height_base - 1, z_base + height_base - 1, air)
    mc.setBlock(x_base + 2, y_base, z_base + 2, 5)



def door(x_door, y_door, z_door, block_door=0):
    mc.setBlocks(x_door, y_door + 1, z_door + 5, x_door + 3, y_door + 4, z_door + 3, block_door)


def tree(x, y, z, trunk, crown):
    mc.setBlocks(x - 1, y, z - 1, x - 1, y + 7, z - 1, trunk)
    for j in range(3):
        mc.setBlocks(x - 3 + j, y + 8 + j, z - 3 + j, x + 3 - j, y + 8 - j, z + 3 - j, crown)


def house(x, y, z):
    time.sleep(2)
    hipped_roof(x + 3, y + 10, z + 3, 5, 5)
    base(x, y, z, 6, 1)
    door(x, y, z, 0)
    window(x, y, z, 0)
    tree(x - 5, y, z - 5, 17, 18)
    file = open("log.txt", "a")
    file.write("a house has been build at position "+ '\n' + str(x) + '\n' + str(y) + "\n" + str(z) + "\n" + "\n")
    file.close()

