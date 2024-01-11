/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */

import java.io.IOException;
import scxmlgen.Fusion.FusionGenerator;
//import FusionGenerator;

import Modalities.Output;
import Modalities.Speech;
import Modalities.Touch;

/**
 *
 * @author nunof
 */
public class GenFusionSCXML {

  /**
   * @param args the command line arguments
   */
  public static void main(String[] args) throws IOException {

    FusionGenerator fg = new FusionGenerator();

    fg.Complementary(Speech.CHOOSE_1, Touch.CHANGE_POKEMON, Output.CHANGE_POKEMON_1);
    fg.Complementary(Speech.CHOOSE_2, Touch.CHANGE_POKEMON, Output.CHANGE_POKEMON_2);
    fg.Complementary(Speech.CHOOSE_3, Touch.CHANGE_POKEMON, Output.CHANGE_POKEMON_3);
    fg.Complementary(Speech.CHOOSE_4, Touch.CHANGE_POKEMON, Output.CHANGE_POKEMON_4);
    fg.Complementary(Speech.CHOOSE_5, Touch.CHANGE_POKEMON, Output.CHANGE_POKEMON_5);

    fg.Complementary(Speech.CHOOSE_1, Touch.MOVE_UP, Output.MOVE_UP_1);
    fg.Complementary(Speech.CHOOSE_2, Touch.MOVE_UP, Output.MOVE_UP_2);
    fg.Complementary(Speech.CHOOSE_3, Touch.MOVE_UP, Output.MOVE_UP_3);
    fg.Complementary(Speech.CHOOSE_4, Touch.MOVE_UP, Output.MOVE_UP_4);
    fg.Complementary(Speech.CHOOSE_5, Touch.MOVE_UP, Output.MOVE_UP_5);
    fg.Complementary(Speech.CHOOSE_6, Touch.MOVE_UP, Output.MOVE_UP_6);
    fg.Complementary(Speech.CHOOSE_7, Touch.MOVE_UP, Output.MOVE_UP_7);
    fg.Complementary(Speech.CHOOSE_8, Touch.MOVE_UP, Output.MOVE_UP_8);
    fg.Complementary(Speech.CHOOSE_9, Touch.MOVE_UP, Output.MOVE_UP_9);
    fg.Complementary(Speech.CHOOSE_10, Touch.MOVE_UP, Output.MOVE_UP_10);

    fg.Complementary(Speech.CHOOSE_1, Touch.MOVE_RIGHT, Output.MOVE_RIGHT_1);
    fg.Complementary(Speech.CHOOSE_2, Touch.MOVE_RIGHT, Output.MOVE_RIGHT_2);
    fg.Complementary(Speech.CHOOSE_3, Touch.MOVE_RIGHT, Output.MOVE_RIGHT_3);
    fg.Complementary(Speech.CHOOSE_4, Touch.MOVE_RIGHT, Output.MOVE_RIGHT_4);
    fg.Complementary(Speech.CHOOSE_5, Touch.MOVE_RIGHT, Output.MOVE_RIGHT_5);
    fg.Complementary(Speech.CHOOSE_6, Touch.MOVE_RIGHT, Output.MOVE_RIGHT_6);
    fg.Complementary(Speech.CHOOSE_7, Touch.MOVE_RIGHT, Output.MOVE_RIGHT_7);
    fg.Complementary(Speech.CHOOSE_8, Touch.MOVE_RIGHT, Output.MOVE_RIGHT_8);
    fg.Complementary(Speech.CHOOSE_9, Touch.MOVE_RIGHT, Output.MOVE_RIGHT_9);
    fg.Complementary(Speech.CHOOSE_10, Touch.MOVE_RIGHT, Output.MOVE_RIGHT_10);

    fg.Complementary(Speech.CHOOSE_1, Touch.MOVE_LEFT, Output.MOVE_LEFT_1);
    fg.Complementary(Speech.CHOOSE_2, Touch.MOVE_LEFT, Output.MOVE_LEFT_2);
    fg.Complementary(Speech.CHOOSE_3, Touch.MOVE_LEFT, Output.MOVE_LEFT_3);
    fg.Complementary(Speech.CHOOSE_4, Touch.MOVE_LEFT, Output.MOVE_LEFT_4);
    fg.Complementary(Speech.CHOOSE_5, Touch.MOVE_LEFT, Output.MOVE_LEFT_5);
    fg.Complementary(Speech.CHOOSE_6, Touch.MOVE_LEFT, Output.MOVE_LEFT_6);
    fg.Complementary(Speech.CHOOSE_7, Touch.MOVE_LEFT, Output.MOVE_LEFT_7);
    fg.Complementary(Speech.CHOOSE_8, Touch.MOVE_LEFT, Output.MOVE_LEFT_8);
    fg.Complementary(Speech.CHOOSE_9, Touch.MOVE_LEFT, Output.MOVE_LEFT_9);
    fg.Complementary(Speech.CHOOSE_10, Touch.MOVE_LEFT, Output.MOVE_LEFT_10);

    fg.Complementary(Speech.CHOOSE_1, Touch.MOVE_DOWN, Output.MOVE_DOWN_1);
    fg.Complementary(Speech.CHOOSE_2, Touch.MOVE_DOWN, Output.MOVE_DOWN_2);
    fg.Complementary(Speech.CHOOSE_3, Touch.MOVE_DOWN, Output.MOVE_DOWN_3);
    fg.Complementary(Speech.CHOOSE_4, Touch.MOVE_DOWN, Output.MOVE_DOWN_4);
    fg.Complementary(Speech.CHOOSE_5, Touch.MOVE_DOWN, Output.MOVE_DOWN_5);
    fg.Complementary(Speech.CHOOSE_6, Touch.MOVE_DOWN, Output.MOVE_DOWN_6);
    fg.Complementary(Speech.CHOOSE_7, Touch.MOVE_DOWN, Output.MOVE_DOWN_7);
    fg.Complementary(Speech.CHOOSE_8, Touch.MOVE_DOWN, Output.MOVE_DOWN_8);
    fg.Complementary(Speech.CHOOSE_9, Touch.MOVE_DOWN, Output.MOVE_DOWN_9);
    fg.Complementary(Speech.CHOOSE_10, Touch.MOVE_DOWN, Output.MOVE_DOWN_10);

    fg.Redundancy(Speech.SAVE, Touch.SAVE, Output.SAVE);
    fg.Redundancy(Speech.STOP, Touch.STOP, Output.STOP);
    fg.Redundancy(Speech.LIKE, Touch.LIKE, Output.LIKE);

    fg.Build("fusion.scxml");
  }

}
