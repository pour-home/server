import requests


class TelegramService:

    _offset = 0
    _token = ""  # From database
    _chatid = ""  # Ask to setup with a message and then get from database
    _token = ""
    _apiurl = ""

    def _loadToken(self):
        self._token = "GET FROM DATABASE"
        self._apiurl = f"https://api.telegram.org/bot{self._token}"

    def notify(self, message):
        print(
            requests.get(
                f"{self._apiurl}/sendMessage?chat_id={self._chatid}&text={message}"
            ).json()
        )

    def start(self):
        self._loadToken()
        print(requests.get(f"{self._apiurl}/getUpdates?offset={self._offset}").json())
