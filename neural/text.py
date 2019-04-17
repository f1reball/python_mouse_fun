from pynput.mouse import Button, Controller, Listener
from PIL import ImageGrab
import time

mouse = Controller()

target = (72, 74, 78)
start = (90, 640)
end = (90, 740)


q = 0

p = ImageGrab.grab().load()[mouse.position]
while (q < 10):
    for x in range(250):
        z = x+640
        p = ImageGrab.grab().load()[(90, z)]
        if(p == target):
            mouse.position = (90, z)
            mouse.press(Button.left)
            mouse.release(Button.left)
            mouse.press(Button.left)
            mouse.release(Button.left)
    q += 1;
'''
while(x < 50):
    mouse.position = (152, 643)
    mouse.press(Button.left)
    mouse.release(Button.left)
    mouse.press(Button.left)
    mouse.release(Button.left)
    time.sleep(0.3)

    mouse.position = (125, 705)
    mouse.press(Button.left)
    mouse.release(Button.left)
    mouse.press(Button.left)
    mouse.release(Button.left)
    time.sleep(0.3)
    x +=1

mouse.position = (282, 964)
mouse.press(Button.left)
mouse.release(Button.left)
'''
