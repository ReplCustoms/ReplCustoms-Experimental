from flask import Flask
from config import devConfig
from flask_caching import Cache
from flask_login import LoginManager
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config.from_object(devConfig)

cache = Cache(app)
db = SQLAlchemy(app)
loginM = LoginManager(app)

from app import routes, errors, models, login

rtc = routes
etc = errors
mtc = models
ltc = login