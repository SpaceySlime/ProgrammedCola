# Keyboard Cat
from pynput.keyboard import Key, Controller
import random
import time
Keyboard = Controller()

Keys = []
convertstring = "q w e r t y u i o p a s d f g h j k l z x c v b n m"
Keys = convertstring.split()

def PressKey(KeyCode, Time):
    Keyboard.press(KeyCode,)
    time.sleep(Time)
    Keyboard.release(KeyCode)

while True:
    time.sleep(0.5)
    PressKey(random.choice(Keys), 1)
