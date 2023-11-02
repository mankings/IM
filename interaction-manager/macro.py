import pydirectinput as di
import pyautogui
import pygetwindow
import time

WINDOW_TITLE = "Pokemon - Leaf Green Version (U) (V1.1) - VisualBoyAdvance-M 2.1.7"

# KEYS
A = 'a'
B = 'b'
L = 's'
R = 'd'
UP = 'up'
DOWN = 'down'
LEFT = 'left'
RIGHT = 'right'
START = 'enter'
SELECT = 'backspace'

def getWindow():
	window = pygetwindow.getWindowsWithTitle(WINDOW_TITLE)[0]
	window.activate()
	return window

def save():
	di.press(START)
	# go to correct option
	di.press(A)
	di.press(A)
	

def main():
	getWindow()
	save()

if __name__ == '__main__':
	main()