import macros
from helpers import *

from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def root():
	return {"message": "Hello World"}

@app.get("/save_game")
def save_game():
	get_window()
	result = macros.save_game()

@app.get("/player_move")
def player_move():
	get_window()
	macros.player_move('up', steps=5)
	macros.player_move('right', steps=10)
	macros.player_move('down', steps=2)
	
	return {"result": "yes"}

@app.get("/player_run")
def player_run():
	get_window()
	macros.player_run('right')
	
	return {"result": "yes"}

@app.get("/player_stop")
def player_stop():
	get_window()
	macros.player_stop()
	
	return {"result": "yes"}