# Keyboard Cat
# Hard Mode (Only press usable keys)
from pynput.keyboard import Key, Controller
import random
import time
Keyboard = Controller()

Keys = []
convertstring = "w a s d t"
Keys = convertstring.split()
Keys.append(Key.space)

def PressKey(KeyCode, Time):
    Keyboard.press(KeyCode,)
    time.sleep(Time)
    Keyboard.release(KeyCode)

while True:
    time.sleep(0.5)
    PressKey(random.choice(Keys), 1)
