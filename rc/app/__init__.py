from flask import Flask
from config import Config
from flask_caching import Cache
from flask_misaka import Misaka

app = Flask(__name__)
app.config.from_object(Config)

cache = Cache(app)
Misaka(app)

from app import routes

rtc = routes