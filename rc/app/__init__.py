from flask import Flask
from config import devConfig
from flask_caching import Cache
from flask_misaka import Misaka
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config.from_object(devConfig)

cache = Cache(app)
db = SQLAlchemy(app)
migrate = Migrate(app, db)
md = Misaka(app)

from app import routes, models, errors

rtc = routes
mtc = models
etc = errors
