from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileRequired, FileAllowed
from wtforms import StringField, TextAreaField, SubmitField, SelectField
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
                             DataRequired(), Length(1, 64)])
    last_name = StringField('Last name', validators=[
                            DataRequired(), Length(1, 64)])

    email = StringField('Email', validators=[
                        DataRequired(), Email(), Length(1, 64)])

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
                      validators=[DataRequired()])

    resume = FileField('CV Upload', validators=[
                       FileAllowed(['pdf', 'docx'], 'PDF or .docx formats only')])

    comments = TextAreaField('Additional comments',
                             validators=[Length(0, 500)])

    submit = SubmitField('Apply')
