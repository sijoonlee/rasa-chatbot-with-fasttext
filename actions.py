# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/core/actions/#custom-actions/


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
#         dispatcher.utter_message("Hello World!")
#
#         return []


# from __future__ import absolute_import
# from __future__ import division
# from __future__ import unicode_literals

from rasa_core_sdk import Action
from rasa_core_sdk.events import SlotSet
from pymongo import MongoClient
from bson import json_util, ObjectId
import json

# client = MongoClient('mongodb://127.0.0.1:27017')
config_file = open("./config/mongodb", "r+")
mongodb_address = config_file.read()
client = MongoClient(mongodb_address)

db = client.slc_db
collection = db.teachers

class ActionSearchOffice(Action):
    def name(self):
        return 'action_search_office'
    def run(self, dispatcher, tracker, domain):
        dispatcher.utter_message("search office called")
        name = tracker.get_slot("name")
        course = tracker.get_slot("course")
        course_code = tracker.get_slot("course_code")
        if name != "":
            key = "name"
            query = name
        elif course != "":
            key = "course"
            query = course
        elif course_code != "":
            key = "course_code"
            query = course_code
        else:
            return [SlotSet('is_false_call', 'True')]

        #response = json.loads(json_util.dumps(collection.find_one({key:query.lower()})))
        response = json.loads(json_util.dumps(collection.find_one({key:{'$regex':query.lower()}})))
        
        if response:
            office = response['office']
            dispatcher.utter_message(" office = " + office)
            
        else:
            dispatcher.utter_message("Sorry, couldn't find in my database: " + query)
        return [SlotSet('name', ''), SlotSet('course', ''), SlotSet('course_code', '')]



class ActionSearchOfficeHour(Action):
    def name(self):
        return 'action_search_office_hour'
    def run(self, dispatcher, tracker, domain):
        dispatcher.utter_message("search office hour called")
        name = tracker.get_slot("name")
        course = tracker.get_slot("course")
        course_code = tracker.get_slot("course_code")
        if name != "":
            key = "name"
            query = name
        elif course != "":
            key = "course"
            query = course
        elif course_code != "":
            key = "course_code"
            query = course_code
        else:
            dispatcher.utter_message("?")
            return [SlotSet('is_false_call', 'True')]

        #response = json.loads(json_util.dumps(collection.find_one({key:query.lower()})))
        response = json.loads(json_util.dumps(collection.find_one({key:{'$regex':query.lower()}})))
        
        if response:
            office_hour = response['office_hour']
            if len(office_hour) == 0:
                dispatcher.utter_message("No office hours")
            else:
                for key, value in office_hour.items():
                    dispatcher.utter_message(key + " : " + value)
        else:
            dispatcher.utter_message("Sorry, couldn't find in my database: " + query)
        return [SlotSet('name', ''), SlotSet('course', ''), SlotSet('course_code', '')]

class ActionSearchOfficeHour(Action):
    def name(self):
        return 'action_reset_search_state'
    
    def run(self, dispatcher, tracker, domain):
        return [SlotSet('name', ''), SlotSet('course', ''), SlotSet('course_code', '')]
        
