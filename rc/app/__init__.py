from flask import Flask
from config import devConfig
from flask_caching import Cache
from flask_misaka import Misaka

app = Flask(__name__)
app.config.from_object(devConfig)

cache = Cache(app)
Misaka(app)

from app import routes

rtc = routes

