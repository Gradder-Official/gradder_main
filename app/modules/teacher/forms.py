from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileRequired, FileAllowed
from wtforms import (
    DateTimeField,
    StringField,
    TextAreaField,
    SubmitField,
    SelectField,
    MultipleFileField,
)
from wtforms.validators import DataRequired

from bson import ObjectId


class NewAssignmentForm(FlaskForm):
    assigned_to = SelectField(u"Class", validators=[DataRequired()], coerce=ObjectId)
    due_by = StringField(
        "Due by", validators=[DataRequired()]
    )  # Not DateTime field because it is weird
    estimated_time = StringField(
        "Estimated time in minutes", validators=[DataRequired()]
    )
    title = StringField("Assignment title", validators=[DataRequired()])
    content = TextAreaField("The assignment description")

    files = MultipleFileField(
        "File upload",
        validators=[
            FileAllowed(
                ["pdf", "docx", "png", "jpg", "jpeg"],
                "Allowed formats: pdf, docx, png, jpeg",
            )
        ],
    )

    submit = SubmitField("Submit")


class NewSubmissionForm(FlaskForm):
    content = TextAreaField()

    files = MultipleFileField(
        "File upload",
        validators=[
            FileAllowed(
                ["pdf", "docx", "png", "jpg", "jpeg"],
                "Allowed formats: pdf, docx, png, jpeg",
            )
        ],
    )

    submit = SubmitField("Submit")


class EditClassForm(FlaskForm):
    description = TextAreaField("Description")
    syllabus = FileField("Update syllabus (current: empty)")

    submit = SubmitField("Submit")

