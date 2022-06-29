from os import environ

class Config(object):
API_ID = (environ.get('API_ID'))
API_HASH = environ.get('API_HASH')
BOT_TOKEN = environ.get('BOT_TOKEN')
BITLY_KEY = environ.get('BITLY_KEY')
OWNER = environ.get('OWNER','BotDunia')
USERS = [int(i) for i in environ.get("USERS", "").split(" ")]
