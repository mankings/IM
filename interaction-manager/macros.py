from helpers import *

def save():
	# open start menu
	di.press(START)
	
	# go to correct option
	navigate_vertical('menu_pointer', 'save_btn')
	
	# accept all
	di.press(FASTFORWARD)
	di.press('k')
	di.press(FASTFORWARD)
	di.press('k')


def navigate_vertical(pointer_name, btn_name):
	pointer = find_on_screen(pointer_name)
	btn = find_on_screen(btn_name)
	
	tolerance = 10
	while abs(pointer[1] - btn[1]) > tolerance:

		if pointer[1] + tolerance < btn[1]:
			di.press(DOWN)
		elif pointer[1] - tolerance > btn[1]:
			di.press(UP)
	
		pointer = find_on_screen(pointer_name)
		save_btn = find_on_screen(btn_name)
	
	