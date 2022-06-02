"""Validation forms for credits manipulation"""


from flask_wtf import FlaskForm
from wtforms import IntegerField, StringField, SubmitField
from wtforms.validators import DataRequired, Length, NumberRange, Optional


class GetCreditForm(FlaskForm):
    """Getting credit information form validation"""

    credit_id = IntegerField("Credit ID", validators=[Optional(), NumberRange(min=0)])
    currency = StringField(
        "Credit currency", validators=[Optional(), Length(min=3, max=3)]
    )
    user_id = IntegerField("Client ID", validators=[Optional(), NumberRange(min=0)])
    submit = SubmitField("Get credit information")


class AddCreditForm(FlaskForm):
    """Adding credit form validation"""

    user_id = IntegerField("User ID", validators=[DataRequired(), NumberRange(min=0)])
    value = IntegerField(
        "Credit value", validators=[DataRequired(), NumberRange(min=0)]
    )
    currency = StringField(
        "Credit currency", validators=[DataRequired(), Length(min=3, max=3)]
    )
    bank_name = StringField("Bank name", validators=[DataRequired(), Length(max=255)])
    submit = SubmitField("Add credit")


class UpdateCreditValueForm(FlaskForm):
    """Updating credit value form validation"""

    credit_id = IntegerField(
        "Credit ID", validators=[DataRequired(), NumberRange(min=0)]
    )
    value = IntegerField(
        "Credit value", validators=[DataRequired(), NumberRange(min=0)]
    )
    submit = SubmitField("Update credit value")


class UpdateCreditCurrencyForm(FlaskForm):
    """Updating credit currency form validation"""

    credit_id = IntegerField(
        "Credit ID", validators=[DataRequired(), NumberRange(min=0)]
    )
    currency = StringField(
        "Credit currency", validators=[DataRequired(), Length(min=3, max=3)]
    )
    submit = SubmitField("Update credit currency")


class DeleteCreditForm(FlaskForm):
    """Deleting credit form validation"""

    credit_id = IntegerField(
        "Credit ID", validators=[DataRequired(), NumberRange(min=0)]
    )
    submit = SubmitField("Delete credit")
