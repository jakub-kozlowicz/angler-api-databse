"""Flask website entrypoint"""

import requests
from flask import Flask, flash, redirect, render_template, request, url_for

from anglers_banking.forms.credit import (AddCreditForm, DeleteCreditForm,
                                          GetCreditForm,
                                          UpdateCreditCurrencyForm,
                                          UpdateCreditValueForm)
from anglers_banking.forms.user import (AddUserForm, DeleteUserForm,
                                        GetUserForm, UpdateUserNameForm)

app = Flask(__name__)
app.config.from_pyfile("config.py")


@app.route("/", methods=["GET", "POST"])
def index() -> str:
    return render_template("index.html", title="Anglers Credits Database")


@app.route("/add-credit", methods=["GET", "POST"])
def add_credit():
    data = None
    url = "http://localhost:8000/"
    form = AddCreditForm()
    if form.validate_on_submit():
        response = requests.post(
            url
            + (
                f"credits?"
                f"user_id={form.user_id.data}"
                f"&value={form.value.data}"
                f"&currency={form.currnecy.data}"
                f"&bank_name={form.bank_name.data}"
            )
        )
        data = response.json()

    return render_template(
        "add-credit.html", title="Add credit to database", form=form, data=data
    )


@app.route("/delete-credit", methods=["GET", "POST"])
def delete_credit():
    data = None
    url = "http://localhost:8000/"
    form = DeleteCreditForm()
    if form.validate_on_submit():
        response = requests.delete(url + f"credits?credit_id={form.credit_id.data}")
        data = response.json()

    return render_template(
        "delete-credit.html", title="Delete credit from database", form=form, data=data
    )


@app.route("/get-credit", methods=["GET", "POST"])
def get_credit():
    data = None
    url = "http://localhost:8000/"
    form = GetCreditForm()
    if form.validate_on_submit():
        # TODO: Check which parameters was passed and construct proper request
        response = requests.get(url + "credits?")
        data = response.json()

    return render_template(
        "get-credit.html",
        title="Get credits information from database",
        form=form,
        data=data,
    )


@app.route("/update-credit-value", methods=["GET", "POST"])
def update_credit_value():
    data = None
    url = "http://localhost:8000/"
    form = UpdateCreditValueForm()
    if form.validate_on_submit():
        response = requests.put(
            url
            + (
                f"/credits?"
                f"credit_id={form.credit_id.data}"
                f"&value={form.value.data}"
            )
        )
        data = response.json()

    return render_template(
        "update-credit-value.html",
        title="Update credit value in database",
        form=form,
        data=data,
    )


@app.route("/update-credit-currency", methods=["GET", "POST"])
def update_credit_currency():
    data = None
    url = "http://localhost:8000/"
    form = UpdateCreditCurrencyForm()
    if form.validate_on_submit():
        response = requests.patch(
            url
            + (
                f"/credits?"
                f"credit_id={form.credit_id.data}"
                f"&currency={form.currency.data}"
            )
        )
        data = response.json()

    return render_template(
        "update-credit-currency.html",
        title="Update credit currency in database",
        form=form,
        data=data,
    )


@app.route("/add-user", methods=["GET", "POST"])
def add_user():
    data = None
    url = "http://localhost:8000/"
    form = AddUserForm()
    if form.validate_on_submit():
        response = requests.post(
            url
            + (
                f"users?"
                f"user_id={form.user_id.data}"
                f"&full_name={form.full_name.data}"
            )
        )
        data = response.json()

    return render_template(
        "add-user.html", title="Add user to database", form=form, data=data
    )


@app.route("/delete-user", methods=["GET", "POST"])
def delete_user():
    data = None
    url = "http://localhost:8000/"
    form = DeleteUserForm()
    if form.validate_on_submit():
        response = requests.delete(url + f"credits?user_id={form.user_id.data}")
        data = response.json()

    return render_template(
        "delete-user.html", title="Delete user from database", form=form, data=data
    )


@app.route("/get-user", methods=["GET", "POST"])
def get_user():
    data = None
    url = "http://localhost:8000/"
    form = GetUserForm()
    if form.validate_on_submit():
        # TODO: Check which parameters was passed and construct proper request
        response = requests.get(url + "users?")
        data = response.json()

    return render_template(
        "get-user.html",
        title="Get users information from database",
        form=form,
        data=data,
    )


@app.route("/update-user-name", methods=["GET", "POST"])
def update_user_name():
    data = None
    url = "http://localhost:8000/"
    form = UpdateUserNameForm()
    if form.validate_on_submit():
        response = requests.post(
            url
            + (
                f"users?"
                f"user_id={form.user_id.data}"
                f"&full_name={form.full_name.data}"
            )
        )
        data = response.json()

    return render_template(
        "update-user-name.html",
        title="Update user name in database",
        form=form,
        data=data,
    )


if __name__ == "__main__":
    app.run()
