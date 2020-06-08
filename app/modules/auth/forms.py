from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField, SelectField
from wtforms.validators import DataRequired, Length, Email, Regexp, EqualTo
from wtforms import ValidationError


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
    secret_question = StringField('Secret question', validators=[DataRequired()])
    secret_answer = StringField('Answer to the secret question', validators=[DataRequired()])

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
        token = db.collection_tokens.document(field.data).get().to_dict()
        if token is not None:
            return True
        else:
            raise ValidationError("Invalid token")


class PasswordChangeForm(FlaskForm):
    new_password = PasswordField('New password', validators=[DataRequired(), EqualTo('new_password2', message='New passwords must match.')])
    new_password2 = PasswordField('Confirm new password', validators=[DataRequired()])

    secret_question = StringField('Answer to your secret question', validators=[DataRequired()])

    submit = SubmitField('Change password')


class SecretQuestionChangeForm(FlaskForm):
    password = PasswordField('Password', validators=[DataRequired()])

    new_secret_question = StringField('New secret question', validators=[DataRequired()])
    new_secret_answer = StringField('Answer to the new secret question', validators=[DataRequired()])

    submit = SubmitField('Change secret question')
