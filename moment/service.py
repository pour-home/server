from datetime import datetime

from pourhome import Service
from pourhome import Register


class MomentService(Service):

    name = "moment"
    
    def __init__(self):
        self._hour = None
        self._minute = None
        self._day = None

    def event(self):
        while True:
            if self._hour != datetime.hour:
                self._hour = datetime.hour
                Register.notify_event(self, "time", f"{self._hour}:{self._minute}")
            if self._day != datetime.day:
                self._day = datetime.day
                Register.notify_event(self, "day", f"{self._day}")
            time.sleep(5)
