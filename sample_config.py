from os import environ

class Config(object):
 API_ID = int(environ.get("API_ID")
 API_HASH = int(environ.get("API_HASH", ""))
 BOT_TOKEN = int(environ.get("BOT_TOKEN", ""))
 BITLY_KEY = int(environ.get("BITLY_KEY, ""))
 OWNER = int(environ.get("OWNER", ""))
 USERS = [int(i) for i in environ.get("USERS", "").split(" ")]
