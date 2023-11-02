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

# GAME WINDOW INFO
WINDOW_TITLE = "Pokemon - Leaf Green Version (U) (V1.1) - VisualBoyAdvance-M 2.1.7"

def cv2_open_image_grayscale(img_path):
    image = cv2.imread(img_path, cv2.IMREAD_UNCHANGED)
    image_gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    
    return image_gray

def find_on_screen(template_name):
    treshold = 0.8
    
    screenshot_path = screenshot_window()
    template_path = get_template_path(template_name)
    
    screenshot = cv2_open_image_grayscale(screenshot_path)
    template = cv2_open_image_grayscale(template_path)

    result = cv2.matchTemplate(screenshot, template, cv2.TM_CCOEFF_NORMED)
    _, max_treshold, _, max_loc = cv2.minMaxLoc(result)
    top_left_coords = max_loc
    print("Found " + template_name + " at " + str(top_left_coords) + ". " + str(max_treshold))
    
    if max_treshold > treshold:
        return top_left_coords
    else:
        return False
    
def screenshot_window():
    offset = 30
        
    window = get_window()
    screenshot = PIL.ImageGrab.grab(bbox=(window.left, window.top + offset * 2, window.left + window.width, window.top + window.height - offset))		
    img_path = os.path.join('interaction-manager', 'screenshot.png')
    screenshot.save(img_path)
    
    return img_path

def get_window():
    window = pygetwindow.getWindowsWithTitle(WINDOW_TITLE)[0]
    window.activate()
    
    return window

def get_template_path(file_name):
    return os.path.join('interaction-manager', 'templates', file_name + '.png')