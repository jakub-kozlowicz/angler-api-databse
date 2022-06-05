"""Flask website entrypoint"""

import json

import requests
from flask import Flask, render_template, request, url_for

from anglers_banking.forms.credit import (
    AddCreditForm,
    DeleteCreditForm,
    GetCreditForm,
    UpdateCreditCurrencyForm,
    UpdateCreditValueForm,
)
from anglers_banking.forms.user import (
    AddUserForm,
    DeleteUserForm,
    GetUserForm,
    UpdateUserNameForm,
)

app = Flask(__name__)
app.config.from_pyfile("config.py")

URL = ""


@app.route("/", methods=["GET", "POST"])
def index() -> str:
    global URL
    if request.method == "POST":
        if request.form.get("Python") == "Python":
            URL = "https://api.python.anglers-banking.online/"
        elif request.form.get("C#") == "C#":
            URL = "http://api.csharp.anglers-banking.online/api/"
        elif request.form.get("Reset") == "Reset":
            URL = ""

    return render_template("index.html", title="Anglers Credits Database", url=URL)


@app.route("/add-credit", methods=["GET", "POST"])
def add_credit():
    data = None
    global URL
    url = URL
    form = AddCreditForm()
    if form.validate_on_submit():
        response = requests.post(
            url
            + (
                f"credits?"
                f"user_id={form.user_id.data}"
                f"&value={form.value.data}"
                f"&currency={form.currency.data}"
                f"&bank_name={form.bank_name.data}"
            )
        )
        data = json.dumps(response.json(), indent=4, sort_keys=True)

    return render_template(
        "add-credit.html", title="Add credit to database", form=form, data=data
    )


@app.route("/delete-credit", methods=["GET", "POST"])
def delete_credit():
    data = None
    global URL
    url = URL
    form = DeleteCreditForm()
    if form.validate_on_submit():
        response = requests.delete(url + f"credits?credit_id={form.credit_id.data}")
        data = json.dumps(response.json(), indent=4, sort_keys=True)

    return render_template(
        "delete-credit.html", title="Delete credit from database", form=form, data=data
    )


@app.route("/get-credit", methods=["GET", "POST"])
def get_credit():
    data = None
    global URL
    url = URL
    form = GetCreditForm()
    if form.validate_on_submit():
        credit_id = form.credit_id.data
        user_id = form.user_id.data
        currency = form.currency.data
        endpoint = "credits?"
        if not any([credit_id, user_id, currency]):
            endpoint += ""
        elif all([credit_id, currency]) and user_id is None:
            endpoint += f"credit_id={credit_id}&currency={currency}"
        elif credit_id is not None and not any([user_id, currency]):
            endpoint += f"credit_id={credit_id}"
        elif user_id is not None and not any([credit_id, currency]):
            endpoint += f"user_id={user_id}"

        response = requests.get(url + endpoint)
        data = json.dumps(response.json(), indent=4, sort_keys=True)

    return render_template(
        "get-credit.html",
        title="Get credits information from database",
        form=form,
        data=data,
    )


@app.route("/update-credit-value", methods=["GET", "POST"])
def update_credit_value():
    data = None
    global URL
    url = URL
    form = UpdateCreditValueForm()
    if form.validate_on_submit():
        response = requests.put(
            url
            + (
                f"credits?"
                f"credit_id={form.credit_id.data}"
                f"&value={form.value.data}"
            )
        )
        data = json.dumps(response.json(), indent=4, sort_keys=True)

    return render_template(
        "update-credit-value.html",
        title="Update credit value in database",
        form=form,
        data=data,
    )


@app.route("/update-credit-currency", methods=["GET", "POST"])
def update_credit_currency():
    data = None
    global URL
    url = URL
    form = UpdateCreditCurrencyForm()
    if form.validate_on_submit():
        response = requests.patch(
            url
            + (
                f"credits?"
                f"credit_id={form.credit_id.data}"
                f"&currency={form.currency.data}"
            )
        )
        data = json.dumps(response.json(), indent=4, sort_keys=True)

    return render_template(
        "update-credit-currency.html",
        title="Update credit currency in database",
        form=form,
        data=data,
    )


@app.route("/add-user", methods=["GET", "POST"])
def add_user():
    data = None
    global URL
    url = URL
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
        data = json.dumps(response.json(), indent=4, sort_keys=True)

    return render_template(
        "add-user.html", title="Add user to database", form=form, data=data
    )


@app.route("/delete-user", methods=["GET", "POST"])
def delete_user():
    data = None
    global URL
    url = URL
    form = DeleteUserForm()
    if form.validate_on_submit():
        response = requests.delete(url + f"users?user_id={form.user_id.data}")
        data = json.dumps(response.json(), indent=4, sort_keys=True)

    return render_template(
        "delete-user.html", title="Delete user from database", form=form, data=data
    )


@app.route("/get-user", methods=["GET", "POST"])
def get_user():
    data = None
    global URL
    url = URL
    form = GetUserForm()
    if form.validate_on_submit():
        user_id = form.user_id.data
        full_name = form.full_name.data
        endpoint = "users?"
        if not any([full_name, user_id]):
            endpoint += ""
        elif all([full_name, user_id]):
            endpoint += f"user_id={user_id}&full_name={full_name}"
        elif user_id is not None:
            endpoint += f"user_id={user_id}"
        elif full_name is not None:
            endpoint += f"full_name={full_name}"

        response = requests.get(url + endpoint)
        data = json.dumps(response.json(), indent=4, sort_keys=True)

    return render_template(
        "get-user.html",
        title="Get users information from database",
        form=form,
        data=data,
    )


@app.route("/update-user-name", methods=["GET", "POST"])
def update_user_name():
    data = None
    global URL
    url = URL
    form = UpdateUserNameForm()
    if form.validate_on_submit():
        response = requests.put(
            url
            + (
                f"users?"
                f"user_id={form.user_id.data}"
                f"&full_name={form.full_name.data}"
            )
        )
        data = json.dumps(response.json(), indent=4, sort_keys=True)

    return render_template(
        "update-user-name.html",
        title="Update user name in database",
        form=form,
        data=data,
    )


if __name__ == "__main__":
    app.run()
