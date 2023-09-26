import threading
from mcpi.minecraft import Minecraft

import time
mc = Minecraft.create()

class Object():
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

class Arena(Object):
    def __init__(self, x, y, z):
        Object.__init__(self, x, y, z)
        self.width = 10
        self.height = 3
        self.length = 20
        self.finish = self.z + self.length - 1
        mc.setBlocks(self.x - 1, self.y, self.x - 1,
                self.x + self.width + 1, self.y - 3, self.z + self.length + 1, 2)

        mc.setBlocks(self.x - 1, self.y + 1, self.z - 1,
                self.x + self.width + 1, self.y + self.height, self.z + self.length + 1, 20)

        mc.setBlocks(self.x, self.y + 1, self.z,
                self.x + self.width, self.y + self.finish, 41)

        mc.setBlocks(self.x, self.y, self.finish,
                self.x + self.width, self.y, self.finish, 41)


x, y, z = mc.player.getTilePos()
arena = Arena(x, y, z)


