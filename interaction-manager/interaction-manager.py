import macros
from helpers import *

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel


app = FastAPI()

origins = ["*"] 

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.post("/")
def root():
	return {"message": "Hello World. Be prepared to play Pokémon Leaf Green!"}


class PlayerMoveBody(BaseModel):
    direction: str
    unit: str
@app.post("/movement/player_move")
def player_move(body: PlayerMoveBody):
    get_window()
    result = macros.player_move(body.direction, body.unit)
	
    return {"result": result[0], "text": result[1]}


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
    attack_number: str
@app.post("/battle/choose_attack")
def battle_choose_attack(body: ChooseAttackBody):
    get_window()
    macros.battle_choose_attack(body.attack_number)
    
    return {"result": "yes"}

@app.post("/battle/pokemon")
def battle_pokemon():
    get_window()
    macros.battle_pokemon()
    
    return {"result": "yes"}

class ChoosePokemonBody(BaseModel):
    pokemon_number: str
@app.post("/battle/choose_pokemon")
def choose_pokemon(body: ChoosePokemonBody):
    get_window()
    macros.choose_pokemon(body.pokemon_number)
    
    return {"result": "yes"}


class ThrowBallBody(BaseModel):
    ball_type: str
@app.post("/battle/throw_ball")
def battle_throw_ball(body: ThrowBallBody):
    get_window()
    macros.battle_throw_ball(body.ball_type)
    
    return {"result": "yes"}


@app.post("/battle/run_away")
def battle_run():
    get_window()
    result = macros.battle_run()
    
    return {"result": result}


@app.post("/misc/confirm")
def confirm():
    get_window()
    result = macros.accept()
    
    return {"result": result}


@app.post("/misc/deny")
def deny():
    get_window()
    result = macros.refuse()
    
    return {"result": result}


@app.post("/misc/save_game")
def save_game():
    get_window()
    result = macros.save_game()
    
    return {"result": result[0], "text": result[1]}

@app.post("/misc/skip_dialogue")
def skip_dialogue():
    get_window()
    result = macros.deny_all_dialogue()
    
    return {"result": result[0], "text": result[1]}
