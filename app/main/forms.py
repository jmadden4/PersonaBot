from flask_wtf import FlaskForm
from werkzeug.datastructures import MultiDict
from wtforms import StringField, TextAreaField, BooleanField, SelectField,\
    SubmitField
from wtforms.validators import Required, Length, Email, Regexp
from wtforms import ValidationError
from flask import Flask
app = Flask(__name__)

class SomeForm(FlaskForm):
	name = StringField('Enter a data point from a customer', validators=[Required()])
	#email = StringField('Email', [DataRequired(), Email()])
	submit = SubmitField('Submit')

	def reset(self):
	    #data = MultiDict([ ('csrf', self.generate_csrf_token() ) ])
	    #data = self.generate_csrf_token()
	    data = self.generate_csrf_token()
	    self.process(data)
	
	def generate_csrf_token():
	    if '_csrf_token' not in session:
		session['_csrf_token'] = some_random_string()
	    return session['_csrf_token']


	

	