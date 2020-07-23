# python rc/shell.py
# file for DB unit testing

from app import db
from app.models import User, Pin
from datetime import datetime

"""
test_user = User(
	id = 0,
	username = "IreTheKID",
	pfp = "https://example.com/picture.png",
	join_date = datetime.now()
)

test_user2 = User(
	id = 1,
	username = "IreTheALT",
	pfp = "https://example.com/picture.png",
	join_date = datetime.now()
)

test_pin = Pin(
	id = 1234,
	type = "post",
	content = "enigma",
	pin_date = datetime.now(),
	creator = test_user.id
)

db.create_all()
db.session.add(test_user)
db.session.add(test_user2)
db.session.add(test_pin)


db.session.rollback()
db.session.remove()
"""
