from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField


class TextForm(FlaskForm):
    text = StringField('Text')
    submit = SubmitField('submit')