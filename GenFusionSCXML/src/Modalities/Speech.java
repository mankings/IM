/* 
  *   Speech.java generated by speechmod 
 */   

package Modalities; 

import scxmlgen.interfaces.IModality; 

public enum Speech implements IModality{  


	CHOOSE_1("[SPEECH][UNITS][1]", 1500),
	CHOOSE_2("[SPEECH][UNITS][2]", 1500),
	CHOOSE_3("[SPEECH][UNITS][3]", 1500),
	CHOOSE_4("[SPEECH][UNITS][4]", 1500),
	CHOOSE_5("[SPEECH][UNITS][5]", 1500),
	CHOOSE_6("[SPEECH][UNITS][6]", 1500),
	CHOOSE_7("[SPEECH][UNITS][7]", 1500),
	CHOOSE_8("[SPEECH][UNITS][8]", 1500),
	CHOOSE_9("[SPEECH][UNITS][9]", 1500),
	CHOOSE_10("[SPEECH][UNITS][10]", 1500),
	


	SAVE("[SPEECH][SAVE_GAME]", 1500),
	STOP("[SPEECH][STOP_MOVING]", 1500),	
    LIKE("[SPEECH][SKIP_DIALOGUE]", 1500),
	
	;


private String event; 
private int timeout;
Speech(String m, int time) {
	event=m;
	timeout=time;
}
@Override
public int getTimeOut(){
	return timeout;
}
@Override
public String getEventName(){
	return event;
}
@Override
public String getEvName(){
	return getModalityName().toLowerCase() +event.toLowerCase();
}

}