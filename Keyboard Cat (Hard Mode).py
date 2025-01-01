# Keyboard Cat
# Hard Mode (Only press usable keys)
from pynput.keyboard import Key, Controller
import pyautogui
import random
import time
Keyboard = Controller()

pyautogui.screenshot("Test.png", region= [0, 0, 1920, 1080])

Keys = [] #Bias forwards, duh.
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
