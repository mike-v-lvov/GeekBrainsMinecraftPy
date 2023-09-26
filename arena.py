import threading
from mcpi.minecraft import Minecraft

import time
mc = Minecraft.create()

class object():
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

class Arena(Obgect):
    def __init__(self, x, y, z):
        Obgect.__init__(self, x, y, z)
        self.wigth = 10
        self.height = 3
        self.lenght = 20
        self.finish = self.z + self.lenght - 1

