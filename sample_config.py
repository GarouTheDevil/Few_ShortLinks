from os import environ

class Config(object):
USERS = [int(i) for i in environ.get("USERS", "1802569102 1016768333").split(" ")]
