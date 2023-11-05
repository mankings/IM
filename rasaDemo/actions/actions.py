# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/custom-actions


# This is a simple example for a custom action which utters "Hello World!"

# from typing import Any, Text, Dict, List
#
# from rasa_sdk import Action, Tracker
# from rasa_sdk.executor import CollectingDispatcher
#
#
# class ActionHelloWorld(Action):
#
#     def name(self) -> Text:
#         return "action_hello_world"
#
#     def run(self, dispatcher: CollectingDispatcher,
#             tracker: Tracker,
#             domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
#
#         dispatcher.utter_message(text="Hello World!")
#
#         return []

from typing import Any, Text, Dict, List

from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.events import SlotSet, UserUtteranceReverted

import json
import requests


def write_log(text):
    with open("log.txt", "a") as log:
        log.write(text)

class ActionDefaultFallback(Action):
    """Executes the fallback action and goes back to the previous state
    of the dialogue"""

    def name(self) -> Text:
        return "action_default_fallback"

    async def run(
        self,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: Dict[Text, Any],
    ) -> List[Dict[Text, Any]]:
        write_log("Actions: " + "No_understand: " + "enter\n")
        
        print("Confiança: ", tracker.latest_message["intent"].get("confidence"))
        write_log("Confiança: " + str(tracker.latest_message["intent"].get("confidence")) + "\n")
        
        if tracker.latest_message["intent"].get("confidence") > 0.5:
            dispatcher.utter_message(response="utter_default")
        
        #publish.single(topic="comandos/voz/UI", payload=json.dumps({"comando": "no_understand"}), hostname="localhost")
        
        write_log("Actions: " + "No_understand: " + "exit\n")
        
        # Revert user message which led to fallback.
        return [UserUtteranceReverted()]
    
class ActionSaveGame(Action):
   def name(self) -> Text:
       return "action_save_game"
   
   async def run(
        self,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: Dict[Text, Any],
    ) -> List[Dict[Text, Any]]:
       write_log("Actions: " + "Save_game: " + "enter\n")
        
       api_url = "http://localhost:5000/misc/save_game"
       
       data = {}
       
       try:
           response = requests.post(api_url, json=data)
           response_data = response.json()
           dispatcher.utter_message(f"API response: {response_data}")
       except Exception as e:
           dispatcher.utter_message("An error occurred while connecting to the API.")

       return []
        

# class ActionAfirmar(Action):
    
#     def name(self) -> Text:
#         return "action_afirmar"
    
#     def run(self, dispatcher: CollectingDispatcher,
#             tracker: Tracker,
#             domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        
#         write_log("Actions: " + "Afirmar: " + "enter\n")
#         print("Confiança: ", tracker.latest_message["intent"].get("confidence"))
#         write_log("Confiança: " + str(tracker.latest_message["intent"].get("confidence")) + "\n")
        
#         msg = {"comando": "confirmar"}
#     #    publish.single(topic="comandos/voz/UI", payload=json.dumps(msg), hostname="localhost")
        
#         write_log("Actions: " + "Afirmar: " + "exit\n")
        
#         return []

# class ActionNegar(Action):
    
#     def name(self) -> Text:
#         return "action_negar"
    
#     def run(self, dispatcher: CollectingDispatcher,
#             tracker: Tracker,
#             domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        
#         write_log("Actions: " + "Negar: " + "enter\n")
#         print("Confiança: ", tracker.latest_message["intent"].get("confidence"))
#         write_log("Confiança: " + str(tracker.latest_message["intent"].get("confidence")) + "\n")
        
#         msg = {"comando": "negar"}
#         #publish.single(topic="comandos/voz/UI", payload=json.dumps(msg), hostname="localhost")
        
#         write_log("Actions: " + "Negar: " + "exit\n")
        
#         return []
    
# class ActionSearchAttack(Action):
    
#     def name(self) -> Text:
#         return "action_search_attack"
    
#     def run(self, dispatcher: CollectingDispatcher,
#             tracker: Tracker,
#             domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        
#         attack = tracker.get_slot("attack")
    