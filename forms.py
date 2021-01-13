from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, SubmitField
from wtforms.validators import DataRequired, Length


class ContactForm(FlaskForm):
    """Contact form"""
    name = StringField('Name', [DataRequired()])
    email = StringField('Email', [DataRequired()])
    body = TextAreaField('Message', [DataRequired(), Length(min=5, message='Your message is too short!')])
    submit = SubmitField('Send')
