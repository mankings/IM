import pygetwindow
from pygetwindow import PyGetWindowException

import cv2, PIL
import os

# KEYS
from enum import Enum
class Keys(Enum):
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

# GAME WINDOW INFO
WINDOW_TITLE = "Pokemon - Leaf Green Version (U) (V1.1) - VisualBoyAdvance-M 2.1.7"
def get_window():
    try:
        window = pygetwindow.getWindowsWithTitle(WINDOW_TITLE)[0]
        window.activate()
    except PyGetWindowException:
        pass
    
    return window

def screenshot_window():
    offset = 30
        
    window = get_window()
    screenshot = PIL.ImageGrab.grab(bbox=(window.left, window.top + offset * 2, window.left + window.width, window.top + window.height - offset))		
    screenshot.save('screenshot.png')
    
    return 'screenshot.png'

def find_on_screen(template_name):
    treshold = 0.82
    
    screenshot_path = screenshot_window()
    template_path = get_template_path(template_name)
    
    screenshot = cv2_open_image_grayscale(screenshot_path)
    template = cv2_open_image_grayscale(template_path)

    result = cv2.matchTemplate(screenshot, template, cv2.TM_CCOEFF_NORMED)
    _, max_treshold, _, max_loc = cv2.minMaxLoc(result)
    top_left_coords = max_loc
    print(template_name + " at " + str(top_left_coords) + " - " + str(max_treshold))
    
    if max_treshold > treshold:
        return top_left_coords
    else:
        return False
    
def cv2_open_image_grayscale(img_path):
    image = cv2.imread(img_path, cv2.IMREAD_UNCHANGED)
    image_gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    
    return image_gray

def get_template_path(file_name):
    return os.path.join('templates', file_name + '.png')




