from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField, SelectField
from wtforms.validators import DataRequired, Length, Email, Regexp, EqualTo
from wtforms import ValidationError
from app import db
from bson.objectid import ObjectId


class NewStudentsTeachers(FlaskForm):
    first_name = StringField('First name', validators=[DataRequired(), Length(1, 64)])
    last_name = StringField('Last name', validators=[DataRequired(), Length(1, 64)])
    email = StringField('Email', validators=[DataRequired(), Email(), Length(1, 64)])
    password = PasswordField('Password', validators=[
        DataRequired(), EqualTo('password2', message='Passwords must match.')])
    password2 = PasswordField('Confirm password', validators=[DataRequired()])
    user_type = SelectField('User type', 
                            choices=[('Student', 'Student'),
                                     ('Teacher', 'Teacher')], validators=[DataRequired()])
    auth_token = StringField('Authorization token', validators=[DataRequired()])
    secret_question = StringField('Secret question', validators=[DataRequired()])
    secret_answer = StringField('Answer to the secret question', validators=[DataRequired()])

    submit = SubmitField('Register')

    def validate_email(self, field):
        from app import db

        if(
            db.students.find_one({"email": field.data.lower()}) or
            db.teachers.find_one({"email": field.data.lower()})):
            raise ValidationError("This email is already in use")
        else:
            return True
    

    def validate_auth_token(self, field):
        from app import db
        token = db.tokens.find_one({"_id": field.data})
        print(token)
        if token is not None:
            return True
        else:
            raise ValidationError("Invalid token")

class NewClasses(FlaskForm):
    department = StringField('Department', validators=[DataRequired(), Length(1, 64)])
    number = StringField('Class Number', validators=[DataRequired(), Length(1, 64)])
    name = StringField('Class Name', validators=[DataRequired(), Length(1, 64)])
    teacher = StringField('Teacher ID', validators=[DataRequired()])
    description = StringField('Description', validators=[DataRequired()])
    schedule_time = StringField('Time', validators=[DataRequired()])
    schedule_days = StringField('Days', validators=[DataRequired()])

    submit = SubmitField('Register')


class AddStudentClass(FlaskForm):
    class_id = StringField('ObjectId', validators=[DataRequired(), Length(1, 128)])
    email = StringField('Email', validators=[DataRequired(), Length(1, 128)])
    submit = SubmitField('Confirm')



class AddTeacherClass(FlaskForm):
    class_id = StringField('ObjectId', validators=[DataRequired(), Length(1, 128)])
    email = StringField('Email', validators=[DataRequired(), Length(1, 128)])
    submit = SubmitField('Confirm')

