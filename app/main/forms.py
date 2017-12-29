from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, BooleanField, SelectField,\
    SubmitField
from wtforms.validators import Required, Length, Email, Regexp
from wtforms import ValidationError


class SomeForm(FlaskForm):
    name = StringField('Enter a data point from a customer', validators=[Required()])
    submit = SubmitField('Submit')