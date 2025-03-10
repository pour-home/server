from .service import db


example_rules = [
    {
        "if": {
            "moment": {
                "time": "18:30"
            }
        },
        "then": {
            "telegram": {
                "sendmessage": {
                    "text": "Ciao! Sono le {{moment.time}}"
                }
            }
        },
    }
]


class Register:

    services = {}

    @staticmethod
    def start():
        # Create an instance from database for each service and start it
        for name, service_model in Register.services.items():
            for service in service_model.select():
                service.start()

    @staticmethod
    def stop():
        pass

    @staticmethod
    def new_service(service):
        Register.services[service.name] = service
        db.create_tables([service])

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
                    for service, parameters in example_rule["then"].items():
                        # Register.services[service]
                        print("Rule executed!")
            except KeyError:
                # not found
                pass
