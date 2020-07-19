import os

class Config(object):
	DEBUG = True
	CACHE_TYPE = "simple"
	CACHE_DEFAULT_TIMEOUT = 300
	SECRET_KEY = os.getenv("SECRET_KEY")