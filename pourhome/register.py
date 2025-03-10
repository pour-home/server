example_rules = [
    {
        "if": {
            "moment": {
                "time": "18:30"
            }
        },
        "then": {
            "telegram": {
                "send_message": {
                    "bot_id" : "1",
                    "chat_id" : "437706966",
                    "message": "Ciao! Sono le {moment-time}"
                }
            }
        },
    }
]

import json
from peewee import *

db = SqliteDatabase("pourhome.db")


class Register:

    services = {}

    @staticmethod
    def db():
        return db

    @staticmethod
    def start():
        # Create an instance from database for each service and start it
        for _, service in Register.services.items():
            service.start()

    @staticmethod
    def stop():
        pass

    @staticmethod
    def new_service(service):
        Register.services[service.name] = service()

    @staticmethod
    def execute_rule():
        pass

    @staticmethod
    def notify_event(obj, event, event_value):
        service_name = obj.name
        for example_rule in example_rules:
            try:
                # check IF execute rule
                rule_value = example_rule["if"][service_name][event]
                if event_value == rule_value:
                    # THEN
                    extras = {
                        f"{service_name}-{event}" : f"{event_value}"
                    }
                    for service_name, action_bundle in example_rule["then"].items():
                        # Get the service
                        service = Register.services[service_name]
                        for action, parameters in action_bundle.items():
                            # Template substitution
                            for parameter, value in parameters.items():
                                parameters[parameter] = value.format_map(extras)
                        service.then(action, parameters)
            except KeyError:
                # not found
                pass
