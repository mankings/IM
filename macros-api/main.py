from turtle import undobufferentries
import macros
import helpers

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from apscheduler.schedulers.background import BackgroundScheduler


app = FastAPI()

origins = ["*"] 
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

scheduler = BackgroundScheduler()
scheduler.start()

@app.post("/")
def root():
	return {"message": "Hello World. Be prepared to play Pokémon Leaf Green!"}

def setup():
    helpers.get_window()
    scheduler.remove_all_jobs()
    return True


class PlayerMoveBody(BaseModel):
    direction: str
    unit: str
@app.post("/movement/player_move")
def player_move(body: PlayerMoveBody):
    setup()
    result = macros.player_move(body.direction, body.unit)

    return {"result": result[0], "text": result[1]}

@app.post("/movement/player_start_moving")
def player_start_moving(body: PlayerMoveBody):
    setup()
    interval = 1
    scheduler.add_job(macros.player_move, 'interval', [body.direction, body.unit], seconds=interval, id="player_move")
    
    return {"result": True, "text": "Aqui vou eu!"}

@app.post("/movement/player_stop_moving")
def player_stop_moving():
    setup()
    
    return {"result": True, "text": "Parei de me mexer."}

@app.post("/battle/attack")
def battle_attack():
    setup()
    result = macros.battle_attack()
    
    return {"result": True, "text": result[1]}


class ChooseAttackBody(BaseModel):
    attack: str
@app.post("/battle/choose_attack")
def battle_choose_attack(body: ChooseAttackBody):
    setup()
    result = macros.battle_choose_attack(body.attack)
    
    return {"result": result[0], "text": result[1]}

@app.post("/battle/pokemon")
def battle_pokemon():
    setup()
    result = macros.battle_pokemon()
    
    return {"result": result[0], "text": result[1]}


class ChoosePokemonBody(BaseModel):
    pokemon: str
@app.post("/battle/choose_pokemon")
def choose_pokemon(body: ChoosePokemonBody):
    setup()
    result = macros.choose_pokemon(body.pokemon)
    
    return {"result": result[0], "text": result[1]}


class ThrowBallBody(BaseModel):
    pokeball: str
@app.post("/battle/throw_ball")
def battle_throw_ball(body: ThrowBallBody):
    setup()
    result = macros.battle_throw_ball(body.pokeball)
    
    return {"result": result[0], "text": result[1]}


@app.post("/battle/run_away")
def battle_run():
    setup()
    result = macros.battle_run()
    
    return {"result": result}


@app.post("/misc/confirm")
def confirm():
    setup()
    result = macros.accept()
    
    return {"result": result}


@app.post("/misc/deny")
def deny():
    setup()
    result = macros.refuse()
    
    return {"result": result}


@app.post("/misc/save_game")
def save_game():
    setup()
    result = macros.save_game()
    
    return {"result": result[0], "text": result[1]}

class DirectionBody(BaseModel): 
    direction: str
@app.post("/misc/direction")
def direction(body: DirectionBody):
    setup()
    result = macros.direction(body.direction)
    
    return {"result": result[0], "text": result[1]}

@app.post("/misc/skip_dialogue")
def skip_dialogue():
    setup()
    result = macros.deny_all_dialogue()
    
    return {"result": result[0], "text": result[1]}

@app.post("/misc/start_game")
def start_game():
    result = macros.start_game()
    
    return {"result": result[0], "text": result[1]}