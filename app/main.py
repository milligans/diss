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
    form=ContactForm(request.form)
    return render_template("index.html")
