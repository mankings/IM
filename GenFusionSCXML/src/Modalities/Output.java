package Modalities;

import scxmlgen.interfaces.IOutput;

public enum Output implements IOutput{


    CHANGE_POKEMON_1("[FUSION][SWAP][1]"),
    CHANGE_POKEMON_2("[FUSION][SWAP][2]"),
    CHANGE_POKEMON_3("[FUSION][SWAP][3]"),
    CHANGE_POKEMON_4("[FUSION][SWAP][4]"),
    CHANGE_POKEMON_5("[FUSION][SWAP][5]"),

    MOVE_UP_1("[FUSION][WALK][UP][1]"),
    MOVE_UP_2("[FUSION][WALK][UP][2]"),
    MOVE_UP_3("[FUSION][WALK][UP][3]"),
    MOVE_UP_4("[FUSION][WALK][UP][4]"),
    MOVE_UP_5("[FUSION][WALK][UP][5]"),
    MOVE_UP_6("[FUSION][WALK][UP][6]"),
    MOVE_UP_7("[FUSION][WALK][UP][7]"),
    MOVE_UP_8("[FUSION][WALK][UP][8]"),
    MOVE_UP_9("[FUSION][WALK][UP][9]"),
    MOVE_UP_10("[FUSION][WALK][UP][10]"),

    MOVE_DOWN_1("[FUSION][WALK][DOWN][1]"),
    MOVE_DOWN_2("[FUSION][WALK][DOWN][2]"),
    MOVE_DOWN_3("[FUSION][WALK][DOWN][3]"),
    MOVE_DOWN_4("[FUSION][WALK][DOWN][4]"),
    MOVE_DOWN_5("[FUSION][WALK][DOWN][5]"),
    MOVE_DOWN_6("[FUSION][WALK][DOWN][6]"),
    MOVE_DOWN_7("[FUSION][WALK][DOWN][7]"),
    MOVE_DOWN_8("[FUSION][WALK][DOWN][8]"),
    MOVE_DOWN_9("[FUSION][WALK][DOWN][9]"),
    MOVE_DOWN_10("[FUSION][WALK][DOWN][10]"),
    
    MOVE_RIGHT_1("[FUSION][WALK][RIGHT][1]"),
    MOVE_RIGHT_2("[FUSION][WALK][RIGHT][2]"),
    MOVE_RIGHT_3("[FUSION][WALK][RIGHT][3]"),
    MOVE_RIGHT_4("[FUSION][WALK][RIGHT][4]"),
    MOVE_RIGHT_5("[FUSION][WALK][RIGHT][5]"),
    MOVE_RIGHT_6("[FUSION][WALK][RIGHT][6]"),
    MOVE_RIGHT_7("[FUSION][WALK][RIGHT][7]"),
    MOVE_RIGHT_8("[FUSION][WALK][RIGHT][8]"),
    MOVE_RIGHT_9("[FUSION][WALK][RIGHT][9]"),
    MOVE_RIGHT_10("[FUSION][WALK][RIGHT][10]"),
    
    MOVE_LEFT_1("[FUSION][WALK][LEFT][1]"),
    MOVE_LEFT_2("[FUSION][WALK][LEFT][2]"),
    MOVE_LEFT_3("[FUSION][WALK][LEFT][3]"),
    MOVE_LEFT_4("[FUSION][WALK][LEFT][4]"),
    MOVE_LEFT_5("[FUSION][WALK][LEFT][5]"),
    MOVE_LEFT_6("[FUSION][WALK][LEFT][6]"),
    MOVE_LEFT_7("[FUSION][WALK][LEFT][7]"),
    MOVE_LEFT_8("[FUSION][WALK][LEFT][8]"),
    MOVE_LEFT_9("[FUSION][WALK][LEFT][9]"),
    MOVE_LEFT_10("[FUSION][WALK][LEFT][10]"),

    STOP("[FUSION][STOP]"),
    LIKE("[FUSION][LIKE]"),
    SAVE("[FUSION][SAVE]"),

    ;
    
    
    
    private String event;

    Output(String m) {
        event=m;
    }
    
    public String getEvent(){
        return this.toString();
    }

    public String getEventName(){
        return event;
    }
}
