import pygetwindow
import subprocess
import time
from pygetwindow import PyGetWindowException

import cv2, PIL
import os

# KEYS
KEY_A = 'c'
KEY_B = 'x'
KEY_L = 's'
KEY_R = 'd'
KEY_UP = 'up'
KEY_DOWN = 'down'
KEY_LEFT = 'left'
KEY_RIGHT = 'right'
KEY_START = 'enter'
KEY_SELECT = 'backspace'
KEY_FASTFORWARD = 'space'

# GAME WINDOW INFO
WINDOW_TITLE = "leaf-green - VisualBoyAdvance-M 2.1.7"
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
        print("found", template_name, "treshold:", max_treshold)
        return top_left_coords
    else:
        return False
    
def wait_for(template_name, timeout=10):
    for i in range(timeout):
        if find_on_screen(template_name):
            return True
        else:
            print("waiting for", template_name)
            time.sleep(1)
    return False
    
def cv2_open_image_grayscale(img_path):
    image = cv2.imread(img_path, cv2.IMREAD_UNCHANGED)
    image_gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    
    return image_gray

def get_template_path(file_name):
    return os.path.join('templates', file_name + '.png')

def start_window():
    emulator_path = "pokemon/visualboyadvance-m.exe"  # Replace with the actual path to VisualBoyAdvance-M
    rom_path = "pokemon/leaf-green.gba"  # Replace with the actual path to your GBA ROM file

    try:
        subprocess.Popen([emulator_path, rom_path])
        return True

    except Exception as e:
        print(f"Error: {e}")