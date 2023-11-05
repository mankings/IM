import macros
from helpers import *

from fastapi import FastAPI
from pydantic import BaseModel


app = FastAPI()
@app.post("/")
def root():
	return {"message": "Hello World. Be prepared to play Pokémon Leaf Green!"}


class PlayerMoveBody(BaseModel):
    direction: str
    steps: int
@app.post("/movement/player_move")
def player_move(body: PlayerMoveBody):
	get_window()
	macros.player_move(body.direction, body.steps)
	
	return {"result": "yes"}


# @app.post("/movement/player_run")
# def player_run():
# 	get_window()
# 	macros.player_run('right')
	
# 	return {"result": "yes"}


# @app.post("/movement/player_stop")
# def player_stop():
# 	get_window()
# 	macros.player_stop()
	
# 	return {"result": "yes"}


@app.post("/battle/attack")
def battle_attack():
    get_window()
    macros.battle_attack()
    
    return {"result": "yes"}


class ChooseAttackBody(BaseModel):
    attack_number: int
@app.post("/battle/choose_attack")
def battle_choose_attack(body: ChooseAttackBody):
    get_window()
    macros.battle_choose_attack(body.attack_number)
    
    return {"result": "yes"}


class ThrowBallBody(BaseModel):
    ball_type: str
@app.post("/battle/throw_ball")
def battle_throw_ball(body: ThrowBallBody):
    get_window()
    macros.battle_throw_ball(body.ball_type)
    
    return {"result": "yes"}


@app.post("/battle/run")
def battle_run():
    get_window()
    macros.battle_run()
    
    return {"result": "yes"}


@app.post("/misc/confirm")
def confirm():
    get_window()
    result = macros.confirm()
    
    return {"result": result}


@app.post("/misc/deny")
def deny():
    get_window()
    result = macros.deny()
    
    return {"result": result}


@app.post("/misc/save_game")
def save_game():
    get_window()
    result = macros.save_game()
    
    return {"result": result}