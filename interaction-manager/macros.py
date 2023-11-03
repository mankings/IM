from helpers import *

import pyautogui as ag, pydirectinput as di
import time

def save_game():
	# check if overworld
	if game_state() != "overworld":
		print("not in overworld!")
		return

	# open start menu
	if not find_on_screen('start_menu'):
		di.press(START)
	
	# go to correct option
	navigate_menu('menu_pointer', 'save_btn', navigation="vertical")
	
	# accept all
	di.press('c')
	di.press('c')
	time.sleep(1)
	di.press('c')
	di.press('c')

def battle_throwball(ball_type: str):
	# check if battle
	if game_state() != "battle":
		print("not in a battle!")
		return
	
	# go to correct option
	navigate_menu('menu_pointer', 'bag_btn', navigation="horizontal")
	navigate_menu('menu_pointer', 'bag_btn', navigation="vertical")
	
	# open bag
	di.press('c')

	# go to correct pocket
	if not find_on_screen('bag_pokeballs'):
		di.press(RIGHT)
		di.press(RIGHT)

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
	di.press('c')
	di.press('c')
	
	accept_all()
	
def battle_run():
	# go to correct option
	navigate_menu('menu_pointer', 'run_btn', navigation="horizontal")
	navigate_menu('menu_pointer', 'run_btn', navigation="vertical")
		
	accept_all()
	
def accept_all():
	pointer = find_on_screen('speech_pointer')
	while(pointer):
		di.press(A)
		pointer = find_on_screen('speech_pointer')

def deny_all():
	pointer = find_on_screen('speech_pointer')
	while(pointer):
		di.press(B)
		pointer = find_on_screen('speech_pointer')
		

	# accept all
	# di.press('k')
	# time.sleep(1)
	# di.press('k')
	
# check if battle, if bag, if pokemon screen, if overworld
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
			di.press(DOWN) if navigation == "vertical" else di.press(RIGHT)
		elif (pointer_coord - tolerance) > btn_coord:
			di.press(UP) if navigation == "vertical" else di.press(LEFT)
	
		pointer = find_on_screen(pointer_name)
		pointer_coord = pointer[1] if navigation == "vertical" else pointer[0]
		btn = find_on_screen(btn_name)
		btn_coord = btn[1] if navigation == "vertical" else btn[0]