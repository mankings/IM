from helpers import *

import pyautogui as ag, pydirectinput as di
import time

#
# movement
#
def player_move(direction, steps):
	direc = direction
	print("1", direc, steps)
	if direction not in [KEY_UP, KEY_DOWN, KEY_LEFT, KEY_RIGHT]:
		if direction == "cima": direc = KEY_UP
		elif direction == "baixo": direc = KEY_DOWN
		elif direction == "esquerda": direc = KEY_LEFT
		elif direction == "direita": direc = KEY_RIGHT
		else: return (False, "Direcao invalida.")
		
	for n in range(steps):
		print("2", direc, steps)
		di.press(direc)
	return (True, "Movimento executado com sucesso.")

# def player_run(direction):
# 	di.keyDown(direction)
# 	# TODO discover why not runnig
# 	di.keyDown(KEY_B)

# def player_stop():
# 	# TODO discover why not stopping
# 	for key in [KEY_UP, KEY_DOWN, KEY_LEFT, KEY_RIGHT, KEY_B]:
# 		print(key)
# 		di.keyUp(key)

#
# battle
#
def battle_attack():
	# check if battle
    if game_state() != "battle":
        print("not in a battle!")
        return
    
    # go to correct option
    navigate_menu('menu_pointer', 'attack_btn', navigation="horizontal")
    navigate_menu('menu_pointer', 'attack_btn', navigation="vertical")
    di.press(KEY_A)

def battle_choose_attack(attack_number):
	# check if attacking
	if game_state() != "attacking":
		print("not attacking!")
		return # todo return value
	
	# TODO go to correct option

def battle_throw_ball(ball_type: str):
	# check if battle
	if game_state() != "battle":
		print("not in a battle!")
		return # todo return value
	
	# go to correct option
	navigate_menu('menu_pointer', 'bag_btn', navigation="horizontal")
	navigate_menu('menu_pointer', 'bag_btn', navigation="vertical")

	# open bag
	di.press(KEY_A)

	# go to correct pocket
	if not find_on_screen('bag_pokeballs'):
		di.press(KEY_RIGHT)
		di.press(KEY_RIGHT)

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
	di.press(KEY_A)
	di.press(KEY_A)
	
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
		return (False, "Nao e possivel guardar o jogo de momento.")

	# open start menu
	tries = 0
	while not find_on_screen('start_menu'):
			di.press('enter')
			tries += 1
			if tries > 3:
				print("can't open start menu")
				return (False, "Nao foi possivel abrir o menu.")
	
	# go to correct option
	navigate_menu('menu_pointer', 'save_btn', navigation="vertical")
	
	# accept all
	di.press(KEY_A)
	di.press(KEY_A)
	time.sleep(1)
	di.press(KEY_A)
	di.press(KEY_A)
	time.sleep(1)
	di.press(KEY_A)
	di.press(KEY_A)
	
	return (True, "O jogo foi guardado com sucesso.")

def accept():
	di.press(KEY_A)

def refuse():
	di.press(KEY_B)
	
def accept_all_dialogue():
	pointer = find_on_screen('speech_pointer')
	while(pointer):
		di.press(KEY_A)
		pointer = find_on_screen('speech_pointer')

def deny_all_dialogue():
	pointer = find_on_screen('speech_pointer')
	while(pointer):
		di.press(KEY_B)
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
			di.press(KEY_DOWN) if navigation == "vertical" else di.press(KEY_RIGHT)
		elif (pointer_coord - tolerance) > btn_coord:
			di.press(KEY_UP) if navigation == "vertical" else di.press(KEY_LEFT)
	
		pointer = find_on_screen(pointer_name)
		pointer_coord = pointer[1] if navigation == "vertical" else pointer[0]
		btn = find_on_screen(btn_name)
		btn_coord = btn[1] if navigation == "vertical" else btn[0]