from flask_wtf import FlaskForm
from app.mixins import JSONForm
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


class SubmissionForm(FlaskForm, JSONForm):
    comment = TextAreaField("Submit your work here")

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

