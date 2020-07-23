from app import db
from datetime import datetime
from flask_login import UserMixin

def check_user(username):
	u = User.query.filter_by(username=username).first()
	if u:
		return True
	else: return False

def new_user(uid, uname, upfp, ujd):
	newyou = User(
		id = uid,
		username = uname,
		pfp = upfp,
		join_date = ujd
	)
	db.session.add(newyou)
	db.session.commit()

	return True


class User(db.Model, UserMixin):
	id = db.Column(db.Integer, primary_key=True)
	username = db.Column(db.String(20), unique=True, nullable=False)
	pfp = db.Column(db.String, nullable=False)
	join_date = db.Column(db.DateTime, default=datetime.utcnow, nullable=False)
	pins = db.relationship('Pin', backref='creator', lazy=True)
	searches = db.relationship('Search', backref='creator', lazy=True)

	def __repr__(self):
		return f"User(Username:{self.username} | ID:{self.id})"


class Pin(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	type = db.Column(db.String, nullable=False)
	content = db.Column(db.String, nullable=False)
	pin_date = db.Column(db.DateTime, default=datetime.utcnow, nullable=False)
	user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)

	def __repr__(self):
		return f"Pin(Type:{self.type} | {self.content} | {self.id}>"


class Search(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	type = db.Column(db.String, nullable=False)
	content = db.Column(db.String, nullable=False)
	create_date =  db.Column(db.DateTime, default=datetime.now(), nullable=False)
	user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)

	def __repr__(self):
		return f"Search(Type:{self.type} | Content:{self.content} | ID:{self.id})"

