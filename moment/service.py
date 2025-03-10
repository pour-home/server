import time

from pourhome import Service
from pourhome import Register


class MomentService(Service):

    name = "moment"

    def event(self):
        while True:
            print("Time!")
            Register.notify_event(self, "time", "18:30")
            time.sleep(5)
