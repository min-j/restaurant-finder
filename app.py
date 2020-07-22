from flask import Flask, render_template, request
import os

# -- Initialization section --
app = Flask(__name__)

# -- Routes section --
@app.route('/')
@app.route('/index')
def index():
    return render_template("index.html")