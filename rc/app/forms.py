from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, SelectField
from wtforms.validators import DataRequired, InputRequired, Length

class SearchUser(FlaskForm):
	q = StringField(
		'Username', 
		validators=[DataRequired(), Length(min=2, max=15)]
	)
	s = SubmitField('Search')

class SearchPost(FlaskForm):
	q = StringField(
		'Post',
		validators=[DataRequired(), Length(min=4, max=40)]
	)
	o = SelectField(
		'Filter',
		choices = [
			('new', 'New'),
			('hot', 'Hot'),
			('top', 'Top')
		]
	)
	s = SubmitField('Search')

class SearchDB(FlaskForm):
	q = StringField(
		'Search Database',
		validators=[
			InputRequired(),
			Length(min=4, max=30)
		]
	)
	s = SubmitField('Go')
