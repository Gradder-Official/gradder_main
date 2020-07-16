from flask_wtf import FlaskForm, RecaptchaField
from flask_wtf.file import FileField, FileRequired, FileAllowed
from wtforms import (
    DateTimeField,
    IntegerField,
    StringField,
    TextAreaField,
    SubmitField,
    SelectField,
    MultipleFileField,
    BooleanField,
)
from wtforms.validators import DataRequired, Length, Email, Regexp, EqualTo
from wtforms import ValidationError


class ContactUsForm(FlaskForm):
    first_name = StringField("First name", validators=[DataRequired(), Length(1, 64)])
    last_name = StringField("Last name", validators=[DataRequired(), Length(1, 64)])

    email = StringField("Email", validators=[DataRequired(), Email(), Length(1, 64)])
    subject = StringField("Subject", validators=[DataRequired(), Length(1, 128)])

    message = TextAreaField("Message", validators=[DataRequired(), Length(1, 512)])

    submit = SubmitField("Submit")


class CareersForm(FlaskForm):
    first_name = StringField(
        "First name",
        validators=[
            DataRequired("Please enter your first name."),
            Length(1, 64, "Should be between 1 and 64 symbols."),
        ],
    )
    last_name = StringField(
        "Last name",
        validators=[
            DataRequired("Please enter your last name."),
            Length(1, 64, "Should be between 1 and 64 symbols."),
        ],
    )

    email = StringField(
        "Email",
        validators=[
            DataRequired("Please enter your email."),
            Email("This data is not a valid email."),
            Length(1, 64, "Should be between 1 and 64 symbols."),
        ],
    )

    job = SelectField(
        "",
        choices=[
            ("", "I am applying for..."),
            ("Business development specialist", "Business development specialist"),
            ("Business analytics specialist", "Business analytics specialist"),
            ("Chatbot developer", "Chatbot developer"),
            ("Copywriter & SMM Specialist", "Copywriter & SMM Specialist"),
            ("Graphic Designer", "Graphic Designer"),
            ("Flask web developer", "Flask web developer"),
            ("Front-end developer", "Front-end developer"),
            ("Market research specialist", "Market research specialist"),
            ("Mobile developer for Android/iOS", "Mobile developer for Android/iOS"),
            ("Q&A/Testing specialist", "Q&A/Testing specialist"),
        ],
        validators=[DataRequired("Please select your application type.")],
    )

    resume = FileField(
        "CV Upload",
        validators=[FileAllowed(["pdf", "docx"], "Only PDF or .docx formats allowed.")],
    )

    comments = TextAreaField(
        "Optional comments (max 500 symbols)",
        validators=[Length(0, 500, "The limit is 500 symbols.")],
    )

    submit = SubmitField("Apply")


class SubscriberForm(FlaskForm):
    email = StringField(
        "Email",
        validators=[DataRequired("Please enter your email"), Email("Invalid email")],
    )
    submit1 = SubmitField("Subscribe")


class InquiryForm(FlaskForm):
    name = StringField(
        "Full name",
        validators=[
            DataRequired("Please enter your name"),
            Length(1, 64, "Should be no longer than 64 characters"),
        ],
    )
    email = StringField(
        "Email",
        validators=[DataRequired("Please enter your email"), Email("Invalid email")],
    )
    subject = SelectField(
        "Subject",
        choices=[
            ("Bugs/suggestions", "Bugs/suggestions"),
            ("Investments", "Investing in us"),
            ("Partnership", "Partnership"),
            ("Questions", "Questions"),
            ("Beta-sign-up", "Sign up for early access"),
            ("Other", "Other"),
        ],
    )
    inquiry = TextAreaField(
        "Inquiry/additional comments",
        validators=[
            DataRequired("Please enter your message"),
            Length(1, 1000, "Should be no longer than 1000 symbols"),
        ],
    )
    submit2 = SubmitField("Submit")


class UnsubscribeForm(FlaskForm):
    checkbox = BooleanField(
        "I want to unsubscribe from Gradder updates.",
        validators=[DataRequired("Please check the box")],
    )
    submit = SubmitField("Unsubscribe")

