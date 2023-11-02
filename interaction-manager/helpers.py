import pygetwindow, pyautogui as ag, pydirectinput as di
import cv2, PIL
import time, os

# KEYS
A = 'c'
B = 'x'
L = 's'
R = 'd'
UP = 'up'
DOWN = 'down'
LEFT = 'left'
RIGHT = 'right'
START = 'enter'
SELECT = 'backspace'
FASTFORWARD = 'space'

WINDOW_TITLE = "Pokemon - Leaf Green Version (U) (V1.1) - VisualBoyAdvance-M 2.1.7"

def getTemplate():
    pass

def screenshot(window):
    offset = 30
    print(window.left, window.top, window.width, window.height)
    screenshot = PIL.ImageGrab.grab(bbox=(window.left, window.top + offset * 2, window.left + window.width, window.top + window.height - offset))
		
    screenshot.save(os.path.join('interaction-manager', 'screenshot.png'))

def getWindow():
    window = pygetwindow.getWindowsWithTitle(WINDOW_TITLE)[0]
    window.activate()
    return window
