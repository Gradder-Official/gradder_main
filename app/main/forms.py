from flask_wtf import FlaskForm, RecaptchaField
from flask_wtf.file import FileField, FileRequired, FileAllowed
from wtforms import DateTimeField, IntegerField, StringField, TextAreaField, SubmitField, SelectField
from wtforms.validators import DataRequired, Length, Email, Regexp, EqualTo
from wtforms import ValidationError


class ContactUsForm(FlaskForm):
    first_name = StringField('First name', validators=[
                             DataRequired(), Length(1, 64)])
    last_name = StringField('Last name', validators=[
                            DataRequired(), Length(1, 64)])

    email = StringField('Email', validators=[
                        DataRequired(), Email(), Length(1, 64)])
    subject = StringField('Subject', validators=[
                          DataRequired(), Length(1, 128)])

    message = TextAreaField('Message', validators=[
                            DataRequired(), Length(1, 512)])

    submit = SubmitField('Submit')


class CareersForm(FlaskForm):
    first_name = StringField('First name', validators=[
                             DataRequired('Please enter your first name.'), Length(1, 64, 'Should be between 1 and 64 symbols.')])
    last_name = StringField('Last name', validators=[
                            DataRequired('Please enter your last name.'), Length(1, 64, 'Should be between 1 and 64 symbols.')])

    email = StringField('Email', validators=[
                        DataRequired('Please enter your email.'), Email('This data is not a valid email.'), Length(1, 64, 'Should be between 1 and 64 symbols.')])

    job = SelectField('', choices=[('', 'I am applying for...'),
                                   ('Business development specialist',
                                    'Business development specialist'),
                                   ('Business analytics specialist',
                                    'Business analytics specialist'),
                                   ('Chatbot developer', 'Chatbot developer'),
                                   ('Copywriter & SMM Specialist',
                                    'Copywriter & SMM Specialist'),
                                   ('Graphic Designer', 'Graphic Designer'),
                                   ('Flask web developer', 'Flask web developer'),
                                   ('Front-end developer', 'Front-end developer'),
                                   ('Market research specialist',
                                    'Market research specialist'),
                                   ('Mobile developer for Android/iOS',
                                    'Mobile developer for Android/iOS'),
                                   ('Q&A/Testing specialist', 'Q&A/Testing specialist')],
                      validators=[DataRequired('Please select your application type.')])

    resume = FileField('CV Upload', validators=[FileAllowed(
        ['pdf', 'docx'], 'Only PDF or .docx formats allowed.')])

    comments = TextAreaField('Optional comments (max 500 symbols)',
                             validators=[Length(0, 500, 'The limit is 500 symbols.')])

    submit = SubmitField('Apply')


class NewAssignmentForm(FlaskForm):
    assigned_to = StringField('Class ID', validators=[DataRequired()])
    due_by = DateTimeField(
        'Due by', format="%m/%d/%y %H:%M", validators=[DataRequired()])
    subject = StringField('Your subject', validators=[DataRequired()])
    estimated_time = StringField('Estimated time in minutes', validators=[DataRequired()])
    content = TextAreaField('The assignment', validators=[DataRequired()])

    submit = SubmitField('Submit')
