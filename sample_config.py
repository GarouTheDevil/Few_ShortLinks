from os import environ

class Config(object):
 API_ID = environ.get("API_ID", 10293305))
 API_HASH = int(environ.get("API_HASH", "9b3bb6ac48fbbc1195e4657fe30858e9"))
 BOT_TOKEN = int(environ.get("BOT_TOKEN", "5519560955:AAHkEKKpNMIoptfSbk9vV5q-Wh5XTOmg8n4"))
 BITLY_KEY = int(environ.get("96bbcd78781ecd9018670be6c876452af049084a"))
 OWNER = int(environ.get("OWNER", "Stay007"))
 USERS = [int(i) for i in environ.get("USERS", "1802569102 1016768333").split(" ")]
