from flask import Flask, render_template, request
from model import search
# import os

# -- Initialization section --
app = Flask(__name__)

# -- Routes section --
@app.route('/')
@app.route('/index')
def index():
    return render_template("index.html")

@app.route('/test', methods= ["GET", "POST"])
def test():
    if request.method == "GET":
        return render_template("results.html")
    else:
        print(request.form)
        t = request.form["Term"]
        loc = request.form["loc"]
        print(search(t, loc))
        return "POSTING..."
