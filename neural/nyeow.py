from pynput.mouse import Button, Controller, Listener
from PIL import ImageGrab
import time

mouse = Controller()


p1 = (90, 640)
p2 = (90, 710)
p3 = (90, 740)
p4 = (90, 775)
p5 = (90, 810)
p6 = (90, 845)
p7 = (90, 880)



q = 0

while(q < 30):
    mouse.position = p1
    mouse.press(Button.left)
    mouse.release(Button.left)
    mouse.press(Button.left)
    mouse.release(Button.left)
    time.sleep(0.3)
    mouse.position = p2
    mouse.press(Button.left)
    mouse.release(Button.left)
    mouse.press(Button.left)
    mouse.release(Button.left)
    time.sleep(0.3)
    mouse.position = p3
    mouse.press(Button.left)
    mouse.release(Button.left)
    mouse.press(Button.left)
    mouse.release(Button.left)
    time.sleep(0.3)
    mouse.position = p4
    mouse.press(Button.left)
    mouse.release(Button.left)
    mouse.press(Button.left)
    mouse.release(Button.left)
    time.sleep(0.3)
    mouse.position = p5
    mouse.press(Button.left)
    mouse.release(Button.left)
    mouse.press(Button.left)
    mouse.release(Button.left)
    time.sleep(0.3)
    mouse.position = p6
    mouse.press(Button.left)
    mouse.release(Button.left)
    mouse.press(Button.left)
    mouse.release(Button.left)
    time.sleep(0.3)
    mouse.position = p7
    mouse.press(Button.left)
    mouse.release(Button.left)
    mouse.press(Button.left)
    mouse.release(Button.left)
    time.sleep(0.3)
    q += 1
