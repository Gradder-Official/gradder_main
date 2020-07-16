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


class SubmissionForm(FlaskForm):
    comment = TextAreaField("Send a private comment to your teacher")

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

