from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileRequired, FileAllowed
from wtforms import DateTimeField, StringField, TextAreaField, SubmitField, SelectField, MultipleFileField
from wtforms.validators import DataRequired

class NewAssignmentForm(FlaskForm):
    assigned_to = StringField('Class ID', validators=[DataRequired()]) # TODO: add dropdown
    due_by = DateTimeField(
        'Due by', format="%m/%d/%y %H:%M", validators=[DataRequired()])
    subject = StringField('Your subject', validators=[DataRequired()])
    estimated_time = StringField('Estimated time in minutes', validators=[DataRequired()])
    content = TextAreaField('The assignment', validators=[DataRequired()])

    files = MultipleFileField('File upload', validators=[FileAllowed(
        ['pdf', 'docx'], 'Only PDF or .docx formats allowed.')])

    submit = SubmitField('Submit')
