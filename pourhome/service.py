import threading


class Service():

    def __init__(self):
        self._process = None

    def start(self):
        self._process = threading.Thread(target=self.event)
        self._process.start()

    def stop(self):
        pass

    def event(self):
        pass
