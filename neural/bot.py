import time
import threading
from pynput.mouse import Button, Controller as mousecontrol
from pynput.keyboard import Key, Controller as keyboardcontrol

item = "test PLZ ignore"


mouse = mousecontrol()
keyboard = keyboardcontrol()
mouse.position = (100, 280)
mouse.press(Button.left)
mouse.release(Button.left)

counter = 0
while(counter < 3):
    keyboard.type(item)
    keyboard.press(Key.enter)
    keyboard.release(Key.enter)
    counter +=1
