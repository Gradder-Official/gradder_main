from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField
from wtforms.validators import DataRequired, Length, Email, Regexp, EqualTo


from api.tools.mixins import JSONForm

class LoginForm(FlaskForm, JSONForm):
    email = StringField("Email", validators=[DataRequired(), Email(), Length(1, 64)])
    password = PasswordField("Password", validators=[DataRequired()])
    remember_me = BooleanField("Keep me logged in")
    
    submit = SubmitField("Log in")


class ResetPasswordForm(FlaskForm, JSONForm):
    new_password = PasswordField("New password", validators=[DataRequired()])
    confirm_password = PasswordField(
        "Confirm new password",
        validators=[
            DataRequired(),
            EqualTo("new_password", message="New passwords must match."),
        ],
    )
    submit = SubmitField("Reset Password")


class PasswordChangeForm(FlaskForm):
    new_password = PasswordField(
        "New password",
        validators=[
            DataRequired(),
            EqualTo("new_password2", message="New passwords must match."),
        ],
    )
    new_password2 = PasswordField("Confirm new password", validators=[DataRequired()])

    submit = SubmitField("Change password")
