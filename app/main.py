from flask import Flask
from jinja2 import Template
from flask import render_template, url_for, request, redirect, flash

app= Flask(__name__)
@app.route('/')
def index():
    return render_template("index.html")
