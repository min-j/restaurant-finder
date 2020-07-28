from flask import Flask, render_template, request
import model as m
import os
from datetime import datetime
from dotenv import load_dotenv

# -- Initialization section --
app = Flask(__name__)
load_dotenv()
API_KEY = os.getenv("GOOGLE_KEY")


# -- Routes section --

@app.route('/index')
def index():
    return render_template("index.html", time=datetime.now())


@app.route('/', methods=["GET", "POST"])
@app.route('/result', methods=["GET", "POST"])
def result():
    # within a number of swipes see to user preference
    # the use of the restaurant finder twice is repetitive change it
    # by searching for it depending on something
    find = None
    res = None
    if request.method == "GET":
        find = m.search(m.getRandom(), 'NYC')
        res = m.getDetails(find['businesses'][0]['id'])
    elif request.method == "POST":
        t = request.form["term"]
        loc = request.form["loc"]
        find = m.search(t, loc)
        res = m.getDetails(find['businesses'][0]['id'])
    try:
        price = "(" + res["price"] + ")"
    except (KeyError, TypeError):
        price = ""
    params = {
        'name': res['name'],
        'price': price,
        'img1': res['photos'][0],
        'img2': res['photos'][1],
        'img3': res['photos'][2],
        'rating': m.getRating(res['rating']),
        'address': res['location']['display_address'][0] + ", " + res['location']['display_address'][1],
        'categories': res['categories'],
        'KEY': API_KEY
    }
    if request.method == "GET":
        return render_template("result.html", time=datetime.now(), **params)
    else:
        # when the user chooses more than choice throw it into a list
        # and then pop it for viewing
        print(request.form)
        if request.form["formType"] == "no":
            return "NO"
        elif request.form['formType'] == "yes":
            # provide the user with information about the restaruant
            return "YES"
        else:
            t = request.form["term"]
            loc = request.form["loc"]
            find = m.search(t, loc)  # Look for more than one business and adapt
            res = m.getDetails(find['businesses'][0]['id'])
            # print(res)
            try:
                price = "(" + res["price"] + ")"
            except (KeyError):
                price = ""
            params = {
                'name': res['name'],
                'price': price,
                'img1': res['photos'][0],
                'img2': res['photos'][1],
                'img3': res['photos'][2],
                'rating': m.getRating(res['rating']),
                'address': res['location']['display_address'][0] + ", " + res['location']['display_address'][1],
                'categories': res['categories'],
                'KEY': API_KEY
            }
            # print(params['categories'])
            return render_template("result.html", time=datetime.now(), **params)
