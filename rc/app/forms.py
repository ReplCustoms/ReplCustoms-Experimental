from flask_wtf import FlaskForm
from wtforms.validators import DataRequired, InputRequired, Length, EqualTo
from wtforms import StringField, SubmitField, SelectField, PasswordField

class RegistrationForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired(), Length(min=2, max=20)])
    password = PasswordField('Password', validators=[DataRequired()])
    confirm_password = PasswordField('Confirm Password', validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField('Sign Up')

class LoginForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    submit = SubmitField('Login')

class SearchUser(FlaskForm):
    q = StringField(
        'Username', validators=[DataRequired(), Length(min=2, max=15)])
    s = SubmitField('Search')

class SearchPost(FlaskForm):
    q = StringField('Post', validators=[DataRequired(), Length(min=4, max=40)])
    o = SelectField(
        'Filter', choices=[('new', 'New'), ('hot', 'Hot'), ('top', 'Top')])
    s = SubmitField('Search')

class SearchDB(FlaskForm):
    q = StringField(
        'Search Database', validators=[InputRequired(), Length(min=4, max=30)])
    s = SubmitField('Go')
