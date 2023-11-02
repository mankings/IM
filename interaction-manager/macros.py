from calendar import c
from helpers import *

def save_game():
	# open start menu
	if not find_on_screen('start_menu'):
		di.press(START)
	
	# go to correct option
	navigate('menu_pointer', 'save_btn', navigation="vertical")
	
	# accept all
	di.press(FASTFORWARD)
	di.press('k')
	di.press(FASTFORWARD)
	di.press('k')

def battle_run():
	# go to correct option
	navigate('menu_pointer', 'run_btn', navigation="vertical")
	navigate('menu_pointer', 'run_btn', navigation="horizontal")
		
	# accept all
	di.press(FASTFORWARD)
	di.press('k')
	di.press(FASTFORWARD)
	di.press('k')


def navigate(pointer_name, btn_name, navigation="vertical"):
	tolerance = 20
	
	pointer = find_on_screen(pointer_name)
	pointer_coord = pointer[1] if navigation == "vertical" else pointer[0]
	btn = find_on_screen(btn_name)
	btn_coord = btn[1] if navigation == "vertical" else btn[0]
	
	while abs(pointer_coord - btn_coord) > tolerance:
		print(abs(pointer_coord - btn_coord))

		if (pointer_coord + tolerance) < btn_coord:
			di.press(DOWN) if navigation == "vertical" else di.press(RIGHT)
		elif (pointer_coord - tolerance) > btn_coord:
			di.press(UP) if navigation == "vertical" else di.press(LEFT)
	
		pointer = find_on_screen(pointer_name)
		pointer_coord = pointer[1] if navigation == "vertical" else pointer[0]
		save_btn = find_on_screen(btn_name)
		btn_coord = btn[1] if navigation == "vertical" else btn[0]