from flask import Flask
from jinja2 import Template
from flask import render_template, url_for, request, redirect, flash
from wtforms import Form, BooleanField, StringField, PasswordField, validators
from flask_bootstrap import Bootstrap
from app.forms import ContactForm

app= Flask(__name__)
Bootstrap(app)

@app.route('/', methods=['GET', 'POST'])
def index():
    form=ContactForm()
    # if form.validate_on_submit():
    #     print("here")
    return render_template("index.html", form=form)

@app.errorhandler(404)
def page_not_found(e):
    # note that we set the 404 status explicitly
    return render_template('404.html'), 404