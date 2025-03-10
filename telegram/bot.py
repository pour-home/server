from peewee import *
from pourhome import Register

class TelegramBot(Model):
    name = CharField()
    token = CharField()  # From database

    class Meta:
        database = Register.db()

Register.db().create_tables([TelegramBot])