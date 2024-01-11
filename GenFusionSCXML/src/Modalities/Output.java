package Modalities;

import scxmlgen.interfaces.IOutput;

public enum Output implements IOutput{


    CHANGE_POKEMON_1("[FUSION][SWAP][1]"),
    CHANGE_POKEMON_2("[FUSION][SWAP][2]"),
    CHANGE_POKEMON_3("[FUSION][SWAP][3]"),
    CHANGE_POKEMON_4("[FUSION][SWAP][4]"),
    CHANGE_POKEMON_5("[FUSION][SWAP][5]"),

    MOVE_UP_1("[FUSION][SWIPEUP][1]"),
    MOVE_UP_2("[FUSION][SWIPEUP][2]"),
    MOVE_UP_3("[FUSION][SWIPEUP][3]"),
    MOVE_UP_4("[FUSION][SWIPEUP][4]"),
    MOVE_UP_5("[FUSION][SWIPEUP][5]"),
    MOVE_UP_6("[FUSION][SWIPEUP][6]"),
    MOVE_UP_7("[FUSION][SWIPEUP][7]"),
    MOVE_UP_8("[FUSION][SWIPEUP][8]"),
    MOVE_UP_9("[FUSION][SWIPEUP][9]"),
    MOVE_UP_10("[FUSION][SWIPEUP][10]"),

    MOVE_DOWN_1("[FUSION][DOWN][1]"),
    MOVE_DOWN_2("[FUSION][DOWN][2]"),
    MOVE_DOWN_3("[FUSION][DOWN][3]"),
    MOVE_DOWN_4("[FUSION][DOWN][4]"),
    MOVE_DOWN_5("[FUSION][DOWN][5]"),
    MOVE_DOWN_6("[FUSION][DOWN][6]"),
    MOVE_DOWN_7("[FUSION][DOWN][7]"),
    MOVE_DOWN_8("[FUSION][DOWN][8]"),
    MOVE_DOWN_9("[FUSION][DOWN][9]"),
    MOVE_DOWN_10("[FUSION][DOWN][10]"),
    
    MOVE_RIGHT_1("[FUSION][RIGHT][1]"),
    MOVE_RIGHT_2("[FUSION][RIGHT][2]"),
    MOVE_RIGHT_3("[FUSION][RIGHT][3]"),
    MOVE_RIGHT_4("[FUSION][RIGHT][4]"),
    MOVE_RIGHT_5("[FUSION][RIGHT][5]"),
    MOVE_RIGHT_6("[FUSION][RIGHT][6]"),
    MOVE_RIGHT_7("[FUSION][RIGHT][7]"),
    MOVE_RIGHT_8("[FUSION][RIGHT][8]"),
    MOVE_RIGHT_9("[FUSION][RIGHT][9]"),
    MOVE_RIGHT_10("[FUSION][RIGHT][10]"),
    
    MOVE_LEFT_1("[FUSION][LEFT][1]"),
    MOVE_LEFT_2("[FUSION][LEFT][2]"),
    MOVE_LEFT_3("[FUSION][LEFT][3]"),
    MOVE_LEFT_4("[FUSION][LEFT][4]"),
    MOVE_LEFT_5("[FUSION][LEFT][5]"),
    MOVE_LEFT_6("[FUSION][LEFT][6]"),
    MOVE_LEFT_7("[FUSION][LEFT][7]"),
    MOVE_LEFT_8("[FUSION][LEFT][8]"),
    MOVE_LEFT_9("[FUSION][LEFT][9]"),
    MOVE_LEFT_10("[FUSION][LEFT][10]"),

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
