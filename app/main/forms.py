from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, BooleanField, SelectField,\
    SubmitField
from wtforms.validators import Required, Length, Email, Regexp
from wtforms import ValidationError


class SomeForm(FlaskForm):
    name = StringField('How is your dog acting right now?', validators=[Required()])
    submit = SubmitField('Submit')