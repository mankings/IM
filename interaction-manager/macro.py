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

def getWindow():
	window = pygetwindow.getWindowsWithTitle(WINDOW_TITLE)[0]
	window.activate()
	return window

def save(window):
	di.PAUSE = 0.15
	ag.PAUSE = 0.15
	
	di.press(START)

	
	# go to correct option
	screenshot(window)
	findOnScreenshot('a', 'a')
	
	di.press(START)

	# di.press(FASTFORWARD) 
	# di.press(A)
	# di.press(A)
	# di.press(A)
	# di.press(FASTFORWARD)
	
def screenshot(window):


def findOnScreenshot(object, screenshot):
	# Load the screenshot and the image of the button
	screenshot = cv2.imread(os.path.join('screenshots', 'screenshot.png'), cv2.IMREAD_UNCHANGED)
	button = cv2.imread(os.path.join('Repo', 'interaction-manager', 'templates', 'menu_pointer.png'), cv2.IMREAD_UNCHANGED)

	# Convert the images to grayscale
	screenshot_gray = cv2.cvtColor(screenshot, cv2.COLOR_BGR2GRAY)
	button_gray = cv2.cvtColor(button, cv2.COLOR_BGR2GRAY)

	# Use template matching to find the button in the screenshot
	result = cv2.matchTemplate(screenshot_gray, button_gray, cv2.TM_CCOEFF_NORMED)
	_, _, _, max_loc = cv2.minMaxLoc(result)
	
	# Draw a rectangle around the matched area in the screenshot
	top_left = max_loc
	print(max_loc)
	
	# cv2.rectangle(screenshot, top_left, top_left, color=(0, 0, 255), thickness=4)
	# cv2.imshow('Detected Button', screenshot)
	# cv2.waitKey(0)
	# cv2.destroyAllWindows()


def main():
	window = getWindow()
	save(window)

if __name__ == '__main__':
	main()