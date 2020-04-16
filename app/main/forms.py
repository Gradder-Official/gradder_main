from flask_wtf import FlaskForm
from wtforms import StringField, TextField, SubmitField
from wtforms.validators import DataRequired, Length, Email, Regexp, EqualTo
from wtforms import ValidationError


class ContactUsForm(FlaskForm):
    first_name = StringField('First name', validators=[DataRequired(), Length(1, 64)])
    last_name = StringField('Last name', validators=[DataRequired(), Length(1, 64)])

    email = StringField('Email', validators=[DataRequired(), Email(), Length(1, 64)])
    subject = StringField('Subject', validators=[DataRequired(), Length(1, 128)])

    message = TextField('Message', validators=[DataRequired(), Length(1, 512)])

    submit = SubmitField('Submit')