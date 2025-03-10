import threading


class Service():

    def start(self):
        self._process = threading.Thread(target=self.event)
        self._process.start()

    def stop(self):
        print("Stop")

    def event(self):
        print("event")
