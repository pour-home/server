import requests, time
from pourhome import Service
from .bot import TelegramBot

class TelegramService(Service):

    apiurl = ""
    name = "telegram"

    def _get_bot_from_id(self, bot_id):
        bots = TelegramBot.select().where(TelegramBot.id==bot_id)
        if bots:
            return bots[0]

    def then(self, action, parameters):
        if action == "send_message":
            self.send_message(**parameters)

    def send_message(self, bot_id, chat_id, message):
        bot = self._get_bot_from_id(bot_id)
        if bot:
            apiurl = f"https://api.telegram.org/bot{bot.token}"
            requests.get(
                f"{apiurl}/sendMessage?chat_id={chat_id}&text={message}"
            ).json()

    def event(self):
        while True:
            print("Telegram!")
            time.sleep(5)
            # bots = TelegramBot.select()
            # for bot in bots:
            #     apiurl = f"https://api.telegram.org/bot{bot.token}"
            #     print(requests.get(f"{apiurl}/getUpdates").json())
            #     time.sleep(5)
        # self._apiurl = f"https://api.telegram.org/bot{self.token}"
        # 
