import os

class Config(object):
	DEBUG = False
	TESTING = False
	FLASK_DEBUG = 0
	CACHE_TYPE = "simple"
	CACHE_DEFAULT_TIMEOUT = 300
	SECRET_KEY = os.getenv("SECRET_KEY")

class devConfig(Config):
	DEBUG = True
	TESTING = True
	FLASK_DEBUG = 1
	CACHE_TYPE = "null"

class proConfig(Config):
	CACHE_DEFAULT_TIMEOUT = 120

class defConfig(Config):
	DEBUG = False
	FLASK_DEBUG = 0
	CACHE_TYPE = "null"