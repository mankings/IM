from helpers import *

import pyautogui as ag, pydirectinput as di
import time

di.pause = 0.5

#
# movement
#
def player_move(direction, steps):
	if game_state()	!= "overworld": 
		return (False, "Nao consigo mover o jogador de momento.")

	if direction not in [KEY_UP, KEY_DOWN, KEY_LEFT, KEY_RIGHT]:
		if direction == "cima": direction = KEY_UP
		elif direction == "baixo": direction = KEY_DOWN
		elif direction == "esquerda": direction = KEY_LEFT
		elif direction == "direita": direction = KEY_RIGHT
		else: return (False, "Nao consegui perceber a direcao.")

	print(steps)
	if steps == "um": steps = 1
	else: steps = int(steps)
		
	for n in range(steps):
		di.press(direction)
	return (True, "Cheguei ao destino!")

#
# battle
#
def battle_attack():
	# check if battle
    if game_state() != "battle":
        print("not in a battle!")
        return (False, "Nao estamos numa batalha!")
    
    # go to correct option
    navigate_menu('menu_pointer', 'fight_btn', navigation="horizontal")
    navigate_menu('menu_pointer', 'fight_btn', navigation="vertical")
    di.press(KEY_A)
    return (True, "Que ataque devo escolher?")

def battle_choose_attack(attack_number):
	if game_state() == "overworld":
		return (False, "Nao estamos numa batalha!")

	if game_state() == "battle":
		navigate_menu('menu_pointer', 'fight_btn', navigation="horizontal")
		navigate_menu('menu_pointer', 'fight_btn', navigation="vertical")
		di.press(KEY_A)

	attack_number = attack_number.lower()
	if attack_number in ['1', "um", "primeiro"]:
		di.press(KEY_UP)
		di.press(KEY_LEFT)
	elif attack_number in ['2', "segundo"]:
		di.press(KEY_RIGHT)
		di.press(KEY_UP)
	elif attack_number in ['3', "terceiro"]:
		di.press(KEY_DOWN)
		di.press(KEY_LEFT)
	elif attack_number in ['4', "quarto"]:
		di.press(KEY_RIGHT)
		di.press(KEY_DOWN)
		
	di.press(KEY_A)
	return (True, "Estourei-o todo.")
		
def battle_pokemon():
	if game_state() == "battle": 
		navigate_menu('menu_pointer', 'pkmn_btn', navigation="horizontal")
		navigate_menu('menu_pointer', 'pkmn_btn', navigation="vertical")
		di.press(KEY_A)
	elif game_state() == "overworld":
		di.press(KEY_START)
		navigate_menu('menu_pointer', 'pkmn_btn', navigation="vertical")
		di.press(KEY_A)
	return (True, "Que Pokemon devo escolher?")
		

def choose_pokemon(pokemon_number):
	msg = ""
	pokemon_number = pokemon_number.lower()

	if game_state() == "overworld":
		di.press(KEY_START)
		navigate_menu('menu_pointer', 'pkmn_btn', navigation="vertical")
		di.press(KEY_A)
	
	di.press(KEY_RIGHT)
	# Acoes comuns a battle e overworld
	if pokemon_number in ['2', "segundo"]:
		di.press(KEY_DOWN)
	if pokemon_number in ['3', "terceiro"]:
		di.press(KEY_DOWN)
		di.press(KEY_DOWN)
		
	
	
	di.press(KEY_A)
	wait_for('menu_pointer')
	
	# Acoes para overworld
	if find_on_screen('switch_btn'):
		msg = "Mudei o Pokemon que comeca as batalhas."
		navigate_menu('menu_pointer', 'switch_btn', navigation="vertical")
		di.press(KEY_A)
		di.press(KEY_LEFT)
		di.press(KEY_A)
		
		time.sleep(1.5)
		di.press(KEY_B)
		wait_for('start_menu')
		di.press(KEY_B)
		
	# Acao para battle
	else: 
		msg = "Isso! Vai!"
		di.press(KEY_A)
	
	return (True, msg)
	
	
def battle_throw_ball(ball_type: str):
	# check if battle
	print(game_state())
	if game_state() != "battle":
		return (False, "Nao estamos numa batalha!")
	
	# go to correct option
	navigate_menu('menu_pointer', 'bag_btn', navigation="horizontal")
	navigate_menu('menu_pointer', 'bag_btn', navigation="vertical")

	# open bag
	di.press(KEY_A)
	time.sleep(0.5)
	
	# go to correct pocket
	if not find_on_screen('bag_pokeballs'):
		di.press(KEY_RIGHT)
		di.press(KEY_RIGHT)
		
	time.sleep(1)

	# select correct pokeball type
	ball_type = ball_type.lower()
	if ball_type in ['pokeball', 'pokebola'] and find_on_screen('pokeball_label'):
		navigate_menu('menu_pointer', 'pokeball_label', navigation="vertical")
	elif ball_type in ['greatball', 'great bola', 'great'] and find_on_screen('greatball_label'):
		navigate_menu('menu_pointer', 'greatball_label', navigation="vertical")
	elif ball_type in ['ultraball', 'ultra bola', 'ultra'] and find_on_screen('ultraball_label'):
		navigate_menu('menu_pointer', 'ultraball_label', navigation="vertical")
	else:
		di.press(KEY_B)
		return (False, "Nao temos dessas pokebolas. Vai comprar seu roto!")

	# throw pokeball
	di.press(KEY_A)
	di.press(KEY_A)
	
	accept_all_dialogue()
	return (True, f'Lancei uma {ball_type}.')

def battle_run():
	# go to correct option
	navigate_menu('menu_pointer', 'run_btn', navigation="horizontal")
	navigate_menu('menu_pointer', 'run_btn', navigation="vertical")
		
	# TODO check if sucessful
	accept_all_dialogue()

#
# misc
#
def start_game():
	start_window()
	time.sleep(3)
	get_window()
	di.press('f1')
	
	return (True, 'Consegui abrir o jogo, agora podemos jogar!')

def save_game():
	# check if overworld
	if game_state() != "overworld":
		print("not in overworld!")
		return (False, "Nao consigo guardar o jogo de momento.")

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
	accept_all_dialogue()
	
	return (True, "O jogo foi guardado com sucesso.")

def direction(direction):
	direction = direction.lower()
	if direction == 'direita': di.press(KEY_RIGHT)
	elif direction == 'esquerda': di.press(KEY_LEFT)
	elif direction == 'cima': di.press(KEY_UP)
	elif direction == 'baixo': di.press(KEY_DOWN)
	
	return (True, "")

def accept():
	di.press(KEY_A)

def refuse():
	di.press(KEY_B)
	
def accept_all_dialogue():
	di.PAUSE = 1
	di.press(KEY_A)
	pointer = find_on_screen('speech_pointer') or find_on_screen('menu_pointer')
	while(pointer):
		di.press(KEY_A)
		pointer = find_on_screen('speech_pointer') or find_on_screen('menu_pointer')
	di.press(KEY_A)
	
	di.PAUSE = 0.25

def deny_all_dialogue():
	di.PAUSE = 1
	di.press(KEY_B)
	pointer = find_on_screen('speech_pointer') or find_on_screen('menu_pointer')
	while(pointer):
		di.press(KEY_B)
		pointer = find_on_screen('speech_pointer') or find_on_screen('menu_pointer')
	di.press(KEY_B)
	
	di.PAUSE = 0.25
		
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