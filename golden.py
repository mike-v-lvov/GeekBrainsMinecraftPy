import threading

from mcpi.minecraft import Minecraft

import time

mc = Minecraft.create()

def hello():
    while True:
        x, y, z = mc.player.getTilePos()
        mc.setBlock(x, y-1, z, 41)

def msg():
    while True:
        msg = input('сщобщение: ')
        mc.postToChat(msg)

hello_thread = threading.Thread(target = hello)
msg_thread = threading.Thread(target = msg)

hello_thread.start()
msg_thread.start()