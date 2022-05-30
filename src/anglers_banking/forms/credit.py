"""Validation forms for credits manipulation"""


from flask_wtf import FlaskForm
from wtforms import FloatField, IntegerField, StringField, SubmitField
from wtforms.validators import DataRequired, Length


class GetCreditForm(FlaskForm):
    """Getting credit information form validation"""

    credit_id = IntegerField("Credit ID", validators=[])
    currency = StringField("Credit currency", validators=[Length(min=3, max=3)])
    user_id = IntegerField("Client ID", validators=[])
    submit = SubmitField("Get credit information")


class AddCreditForm(FlaskForm):
    """Adding credit form validation"""

    user_id = IntegerField("User ID", validators=[DataRequired()])
    value = FloatField("Credit value", validators=[DataRequired()])
    currency = StringField(
        "Credit currency", validators=[DataRequired(), Length(min=3, max=3)]
    )
    bank_name = StringField("Bank name", validators=[DataRequired(), Length(max=255)])
    submit = SubmitField("Add credit")


class UpdateCreditValueForm(FlaskForm):
    """Updating credit value form validation"""

    credit_id = IntegerField("Credit ID", validators=[DataRequired()])
    value = FloatField("Credit value", validators=[DataRequired()])
    submit = SubmitField("Update credit value")


class UpdateCreditCurrencyForm(FlaskForm):
    """Updating credit currency form validation"""

    credit_id = IntegerField("Credit ID", validators=[DataRequired()])
    currency = StringField(
        "Credit currency", validators=[DataRequired(), Length(min=3, max=3)]
    )
    submit = SubmitField("Update credit currency")


class DeleteCreditForm(FlaskForm):
    """Deleting credit form validation"""

    credit_id = IntegerField("Credit ID", validators=[DataRequired()])
    submit = SubmitField("Delete credit")
