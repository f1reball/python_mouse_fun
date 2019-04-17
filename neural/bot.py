import time
import threading
from pynput.mouse import Button, Controller as mousecontrol
from pynput.keyboard import Key, Controller as keyboardcontrol

item = "test plz ignore"
counter = 0

mouse = mousecontrol()
keyboard = keyboardcontrol()
mouse.position = (100, 280)
mouse.press(Button.left)
mouse.release(Button.left)

while(counter < 3):
    keyboard.type(item)
    keyboard.press(Key.enter)
    keyboard.release(Key.enter)
    counter +=1
