from os import environ

class Config(object):
USERS = [int(i) for i in environ.get("USERS", "").split(" ")]

