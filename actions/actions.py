# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/custom-actions

import logging
from typing import Text
from typing import Dict
from typing import List
from typing import Any

from rasa_sdk import Action
from rasa_sdk import Tracker
from rasa_sdk import FormValidationAction
from rasa_sdk.events import EventType
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.types import DomainDict

from utils.action_util import get_weather

logger = logging.getLogger(__name__)


class ActionWeatherForm(Action):
    def name(self) -> Text:
        return "action_weather_form"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict) -> List[EventType]:
        slots = tracker.current_slot_values()
        city = slots["city"]
        date = slots["date"]
        dispatcher.utter_message(text=get_weather(city, date))
        return []


class ValidateWeatherForm(FormValidationAction):
    def name(self) -> Text:
        return "validate_weather_form"

    @staticmethod
    def get_date_list() -> List[Text]:
        return ["今天", "明天", "后天"]

    def validate_date(self, slot_value: Any, dispatcher: CollectingDispatcher, tracker: Tracker, domain: DomainDict) \
            -> Dict[Text, Any]:
        if type(slot_value) == list:
            slot_value = slot_value[0]

        if slot_value in self.get_date_list():
            return {"date": slot_value}
        else:
            return {"date": None}

    @staticmethod
    def get_city_list() -> List[Text]:
        return ["杭州", "武汉", "上海"]

    def validate_city(self, slot_value: Any, dispatcher: CollectingDispatcher, tracker: Tracker, domain: DomainDict) \
            -> Dict[Text, Any]:
        if type(slot_value) == list:
            slot_value = slot_value[0]

        if slot_value in self.get_city_list():
            return {"city": slot_value}
        else:
            return {"city": None}


class ActionAskWeatherFormCity(Action):
    def name(self) -> Text:
        return "action_ask_weather_form_city"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict) -> List[EventType]:
        dispatcher.utter_message(text="你想询问哪个城市的？[杭州、武汉、上海]")
        return []


class ActionAskWeatherFormDate(Action):
    def name(self) -> Text:
        return "action_ask_weather_form_date"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict) -> List[EventType]:
        dispatcher.utter_message(text="你想询问哪个日期的？[今天、明天、后天]")
        return []
