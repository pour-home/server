from peewee import *
import threading

db = SqliteDatabase("pourhome.db")


class Service(Model):

    def start(self):
        self._process = threading.Thread(target=self.event)
        self._process.start()

    def stop(self):
        print("Stop")

    def event(self):
        print("event")

    class Meta:
        database = db
