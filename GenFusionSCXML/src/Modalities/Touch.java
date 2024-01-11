/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package Modalities;

import scxmlgen.interfaces.IModality;

/**
 *
 * @author nunof
 */
public enum Touch implements IModality{

    CHANGE_POKEMON("[GESTURES][SWAP]", 1500),

    MOVE_UP("[GESTURES][SWIPEUP]", 1500),
    MOVE_DOWN("[GESTURES][DOWN]", 1500),
    MOVE_RIGHT("[GESTURES][SWIPERIGHTR]", 1500),
    MOVE_LEFT("[GESTURES][SWIPELEFTL]", 1500),

    STOP("[GESTURES][STOP]", 1500),
    LIKE("[GESTURES][LIKE]", 1500),
    SAVE("[GESTURES][SAVE]", 1500),

    ;
    
    private String event;
    private int timeout;


    Touch(String m, int time) {
        event=m;
        timeout=time;
    }

    @Override
    public int getTimeOut() {
        return timeout;
    }

    @Override
    public String getEventName() {
        //return getModalityName()+"."+event;
        return event;
    }

    @Override
    public String getEvName() {
        return getModalityName().toLowerCase()+event.toLowerCase();
    }
    
}