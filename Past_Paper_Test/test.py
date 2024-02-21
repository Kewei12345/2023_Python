import pynput
from pynput.keyboard import Key, Controller
import time
import random

keyboard = Controller()

arr = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
timearr = [0.028, 0.039, 0.036, 0.033, 0.03]

time.sleep(3)

for item in arr:
    keyboard.press(item)
    time.sleep(random.choice(timearr))
