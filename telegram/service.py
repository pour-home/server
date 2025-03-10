import requests, time
from pourhome import Service
from peewee import *
from pourhome import Register


class TelegramService(Service):

    token = CharField(unique=True)  # From database
    chatid = CharField(
        null=True
    )  # Ask to setup with a message and then get from database
    offset = CharField(default="0")
    apiurl = ""
    name = "telegram"

    def then(self, action, parameters):
        if action == "notify":
            self.notify("ciao!")

    def notify(self, message):
        print(
            requests.get(
                f"{self._apiurl}/sendMessage?chat_id={self.chatid}&text={message}"
            ).json()
        )

    def event(self):
        while True:
            print("Telegram!")
            time.sleep(1)
        # self._apiurl = f"https://api.telegram.org/bot{self.token}"
        # print(requests.get(f"{self._apiurl}/getUpdates?offset={self.offset}").json())
