# from bottle import route, run, template

# @route('/hello/<name>')
# def index(name):
#     return template('<b>Hello {{name}}</b>!', name=name)

# run(host='localhost', port=8080)

from telegram import TelegramService
from tapo import TapoService

telegramService = TelegramService()
telegramService.start()
telegramService.notify("ciao")

tapoService = TapoService()
tapoService.start()
