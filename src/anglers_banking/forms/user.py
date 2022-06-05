"""Validation forms for users manipulation"""


from flask_wtf import FlaskForm
from wtforms import IntegerField, StringField, SubmitField
from wtforms.validators import DataRequired, Length, NumberRange, Optional


class GetUserForm(FlaskForm):
    """Getting user information form validation"""

    user_id = IntegerField("Client ID", validators=[Optional(), NumberRange(min=0)])
    full_name = StringField("User full name", validators=[Optional(), Length(max=255)])
    submit = SubmitField("Get user information")


class AddUserForm(FlaskForm):
    """Adding user form validation"""

    full_name = StringField(
        "User full name", validators=[DataRequired(), Length(max=255)]
    )
    submit = SubmitField("Add user to database")


class UpdateUserNameForm(FlaskForm):
    """Updating user name form validation"""

    user_id = IntegerField("Client ID", validators=[DataRequired(), NumberRange(min=0)])
    full_name = StringField(
        "User full name", validators=[DataRequired(), Length(max=255)]
    )
    submit = SubmitField("Update user name")


class DeleteUserForm(FlaskForm):
    """Deleting user form validation"""

    user_id = IntegerField("Client ID", validators=[DataRequired(), NumberRange(min=0)])
    submit = SubmitField("Delete user from database")
