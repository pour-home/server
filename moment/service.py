import time

from pourhome import Service
from peewee import *
from pourhome import Register


class MomentService(Service):

    name = "moment"

    def event(self):
        while True:
            print("Time!")
            time.sleep(1)
        # Register.notify_event(self, "time", "18.30")
