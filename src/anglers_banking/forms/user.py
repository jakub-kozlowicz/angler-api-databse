"""Validation forms for users manipulation"""


from flask_wtf import FlaskForm
from wtforms import IntegerField, StringField, SubmitField
from wtforms.validators import DataRequired, Length


class GetUserForm(FlaskForm):
    """Getting user information form validation"""

    user_id = IntegerField("Client ID", validators=[])
    full_name = StringField("User full name", validators=[Length(max=255)])
    submit = SubmitField("Get user information")


class AddUserForm(FlaskForm):
    """Adding user form validation"""

    user_id = IntegerField("Client ID", validators=[DataRequired()])
    full_name = StringField(
        "User full name", validators=[DataRequired(), Length(max=255)]
    )
    submit = SubmitField("Get user information")


class UpdateUserNameForm(FlaskForm):
    """Updating user name form validation"""

    user_id = IntegerField("Client ID", validators=[DataRequired()])
    full_name = StringField(
        "User full name", validators=[DataRequired(), Length(max=255)]
    )
    submit = SubmitField("Get user information")


class DeleteUserForm(FlaskForm):
    """Deleting user form validation"""

    user_id = IntegerField("Client ID", validators=[DataRequired()])
    submit = SubmitField("Get user information")
