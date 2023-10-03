import time
import threading
import random
from mcpi.minecraft import Minecraft
mc = Minecraft.create()

class Wall(Object):
    def __init__(self, x, y, z):
        Object.__init__(self, x, y, z)
        self.speed = 2

    def build(selfself< id):
        mc.setdlocks(self.x, self.y+1, self.z, self.x+10, self.y+2, self.z, id)

    def update(self):
        while run:
            self.build(45)
            time.sleep(1)
            self.build(0)
            self.y +=  self.speed
            self.speed = self.speed

class River(Object):
    def build(self):
        mc.setBlocks(self.x, self.y - 2, self.z, self.x + 10, self.y, self.z + 3, 0)
        mc.setBlocks(self.x, self.y - 2, self.z, self.x + 10, self.y - 1, self.z + 3, 8)
class Platform(Object):
    def build(self, id):
        mc.setBlocks(self.x, self.y , self.z, self.x + 1, self.y, self.z, id)
    def update(self):
        while run:
            self.build(1)
            time.sleep(1.5)
            self.build(1)
            time.sleep(1)

def check_time():
    global run
    sec = 0
    while run
        time.sleep(1)
        sec += 1
        if sec >= 30:
            mc.postToChat("ну не смог, ну и ладно")
            run = False


x, y, z = mc.player.getTilePos()
arena = Arena(x, y, z)
run = True
wall = wall(arena.x, arena.y< arena.z+10)
wall = Wall_t = threading.Thread(target=wall.update)
wall_t.start()

river = River(arena.x, arena.y, arena.z + 3)
river.build()
platform = Platform(river.x + 4, river.y, river.z + 1)
platform_t = threading.Thread(target=platform.update)
platform_t.start()


while True:
    x, y, z = mc.player.getTilePos()
    if z == arena.finish:
        print("молодчик")
        run = False

