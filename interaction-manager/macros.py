from helpers import *

import pyautogui as ag, pydirectinput as di
import time

#
# movement
#
def player_move(direction, steps):
	for n in range(steps):
		di.press(direction)

def player_run(direction):
	di.keyDown(direction)
	# TODO discover why not runnig
	di.keyDown(Keys.B)
	
def player_stop():
	# TODO discover why not stopping
	for key in [Keys.UP, Keys.DOWN, Keys.LEFT, Keys.RIGHT, Keys.B]:
		print(key)
		di.keyUp(key)

#
# battle
#
def battle_throwball(ball_type: str):
	# check if battle
	if game_state() != "battle":
		print("not in a battle!")
		return
	
	# go to correct option
	navigate_menu('menu_pointer', 'bag_btn', navigation="horizontal")
	navigate_menu('menu_pointer', 'bag_btn', navigation="vertical")
	
	# open bag
	di.press(Keys.A)

	# go to correct pocket
	if not find_on_screen('bag_pokeballs'):
		di.press(Keys.RIGHT)
		di.press(Keys.RIGHT)

	# select correct pokeball type
	if ball_type == 'pokeball':
		navigate_menu('menu_pointer', 'pokeball_label', navigation="vertical")
	elif ball_type == 'greatball':
		navigate_menu('menu_pointer', 'greatball_label', navigation="vertical")
	elif ball_type == 'ultraball':
		navigate_menu('menu_pointer', 'ultraball_label', navigation="vertical")
	else:
		print('Pokeball type not found.')
	
	# throw pokeball
	di.press(Keys.A)
	di.press(Keys.A)
	
	accept_all_dialogue()
	
def battle_run():
	# go to correct option
	navigate_menu('menu_pointer', 'run_btn', navigation="horizontal")
	navigate_menu('menu_pointer', 'run_btn', navigation="vertical")
		
	# TODO check if sucessful
	# accept_all()

#
# misc
#
def save_game():
	# check if overworld
	if game_state() != "overworld":
		print("not in overworld!")
		return False

	# open start menu
	if not find_on_screen('start_menu'):
		di.press(Keys.START)
	
	# go to correct option
	navigate_menu('menu_pointer', 'save_btn', navigation="vertical")
	
	# accept all
	di.press(Keys.A)
	di.press(Keys.A)
	time.sleep(1)
	di.press(Keys.A)
	di.press(Keys.A)
	
	return True
	
def accept_all_dialogue():
	pointer = find_on_screen('speech_pointer')
	while(pointer):
		di.press(Keys.A)
		pointer = find_on_screen('speech_pointer')

def deny_all_dialogue():
	pointer = find_on_screen('speech_pointer')
	while(pointer):
		di.press(Keys.B)
		pointer = find_on_screen('speech_pointer')
		
def game_state():
	# search for player; if player on screen, on overworld
	player = find_on_screen('player_up') or find_on_screen('player_down') or find_on_screen('player_left') or find_on_screen('player_right')
	if player:
		return "overworld"
	
	# search for battle menu; if on screen, ongoing battle
	battle = find_on_screen('battle_menu')
	if battle:
		return "battle"

	# search for bag;
	bag = find_on_screen('bag_items') or find_on_screen('bag_keyitems') or find_on_screen('bag_pokeballs')
	if bag:
		return "bag"
	
def navigate_menu(pointer_name, btn_name, navigation="vertical"):
	tolerance = 20
	
	pointer = find_on_screen(pointer_name)
	pointer_coord = pointer[1] if navigation == "vertical" else pointer[0]
	btn = find_on_screen(btn_name)
	btn_coord = btn[1] if navigation == "vertical" else btn[0]
	
	while abs(pointer_coord - btn_coord) > tolerance:
		print(abs(pointer_coord - btn_coord))

		if (pointer_coord + tolerance) < btn_coord:
			di.press(Keys.DOWN) if navigation == "vertical" else di.press(Keys.RIGHT)
		elif (pointer_coord - tolerance) > btn_coord:
			di.press(Keys.UP) if navigation == "vertical" else di.press(Keys.LEFT)
	
		pointer = find_on_screen(pointer_name)
		pointer_coord = pointer[1] if navigation == "vertical" else pointer[0]
		btn = find_on_screen(btn_name)
		btn_coord = btn[1] if navigation == "vertical" else btn[0]