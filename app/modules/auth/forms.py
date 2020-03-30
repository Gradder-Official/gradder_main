from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField, SelectField
from wtforms.validators import DataRequired, Length, Email, Regexp, EqualTo
from wtforms import ValidationError

from app.modules.db.classes import Student, Teacher, Parent

class LoginForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired(), Email(), Length(1, 64)])
    password = PasswordField('Password', validators=[DataRequired()])
    remember_me = BooleanField('Keep me logged in')
    submit = SubmitField('Log in')


class RegistrationForm(FlaskForm):
    first_name = StringField('First name', validators=[DataRequired(), Length(1, 64)])
    last_name = StringField('Last name', validators=[DataRequired(), Length(1, 64)])
    email = StringField('Email', validators=[DataRequired(), Email(), Length(1, 64)])
    password = PasswordField('Password', validators=[
        DataRequired(), EqualTo('password2', message='Passwords must match.')])
    password2 = PasswordField('Confirm password', validators=[DataRequired()])
    user_type = SelectField('User type', 
                            choices=[('Admin', 'Admin'), ('Student', 'Student'),
                                     ('Teacher', 'Teacher'), ('Parent', 'Parent')],
                            validators=[DataRequired()])
    auth_token = StringField('Authorization token', validators=[DataRequired()])
    submit = SubmitField('Register')


    def validate_email(self, field):
        from app import db
        checks = [
            list(db.collection_admins.where(u'email', u'==', field.data.lower()).stream()),
            list(db.collection_parents.where(u'email', u'==', field.data.lower()).stream()),
            list(db.collection_students.where(u'email', u'==', field.data.lower()).stream()),
            list(db.collection_teachers.where(u'email', u'==', field.data.lower()).stream())
        ]
        
        if any(checks):
            raise ValidationError("This email is already in use")
        else:
            return True
    

    def validate_auth_token(self, field):
        from app import db
        token = db.collection_tokens.document(field.data)
        if token:
            return True
        else:
            raise ValidationError("Invalid token")
